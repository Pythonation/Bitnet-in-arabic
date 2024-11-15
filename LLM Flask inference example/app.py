from flask import Flask, request, jsonify, render_template
import subprocess
import os

app = Flask(__name__)

# تعديل المسار ليناسب مجلد المشروع الخاص بك
MODEL_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 
                       "models/Llama3-8B-1.58-100B-tokens/ggml-model-i2_s.gguf")

def generate_response(prompt):
  try:
      cmd = f'python run_inference.py -m "{MODEL_PATH}" -p "{prompt}"'
      result = subprocess.run(
          cmd,
          shell=True,
          capture_output=True,
          text=True,
          timeout=60
      )
      print(f"Command output: {result.stdout}")  # للتصحيح
      print(f"Command errors: {result.stderr}")  # للتصحيح
      
      if result.returncode == 0:
          return result.stdout.strip()
      else:
          return f"Error: {result.stderr}"
  except subprocess.TimeoutExpired:
      return "Error: Request timed out"
  except Exception as e:
      return f"Error: {str(e)}"

@app.route('/')
def home():
  return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
  data = request.json
  prompt = data.get('prompt', '')
  
  if not prompt:
      return jsonify({'error': 'No prompt provided'}), 400
  
  response = generate_response(prompt)
  return jsonify({'response': response})

if __name__ == '__main__':
  print(f"Using model at: {MODEL_PATH}")  # للتأكد من المسار
  app.run(debug=True, host='0.0.0.0', port=5000)

