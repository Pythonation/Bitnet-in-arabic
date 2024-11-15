## إعداد وتشغيل BitNet على WSL2 
## شاهد الشرح الكامل على يوتيوب!

لمشاهدة شرح مفصل وعملي لكافة الخطوات، تفضل بزيارة قناتنا على يوتيوب:

[![شاهد الفيديو](https://img.youtube.com/vi/4-HJOt53LMw/0.jpg)](https://youtu.be/4-HJOt53LMw)

لا تنسَ الاشتراك في القناة وتفعيل جرس التنبيهات ليصلك كل جديد! ❤️

### الخطوة 1: تثبيت WSL2

- تفعيل ميزات Windows:
```powershell
dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
```
- إعادة تشغيل الجهاز.
- تثبيت WSL2 Linux kernel: [تحميل من موقع مايكروسوفت](https://docs.microsoft.com/en-us/windows/wsl/install-manual#step-4---download-the-linux-kernel-update-package)
- تعيين WSL2 كإصدار افتراضي:
```powershell
wsl --set-default-version 2
```
- تثبيت توزيعة Linux (Ubuntu) من Microsoft Store.
- التحقق من التثبيت:
```powershell
wsl --version
wsl --list --verbose
```
- إعداد Ubuntu: إنشاء اسم مستخدم وكلمة مرور.


### الخطوة 2: إعداد الذاكرة

- إنشاء `.wslconfig` في `C:\Users\YourUsername\.wslconfig`:
```
[wsl2]
memory=12GB
swap=16GB
processors=4
```
- إعداد SWAP في Ubuntu:
```bash
free -h
sudo fallocate -l 16G /swapfile
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile
```
- جعل SWAP دائمة: إضافة ` /swapfile  none  swap  sw  0  0`  لـ `/etc/fstab`.


### الخطوة 3: تثبيت الأدوات

```bash
sudo apt update
sudo apt upgrade -y
sudo apt install build-essential pkg-config cmake git python3 python3-pip ninja-build -y
wget https://apt.llvm.org/llvm.sh
chmod +x llvm.sh
sudo ./llvm.sh 18 -- --install-dir /usr/lib/llvm-18
echo 'export PATH="/usr/lib/llvm-18/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
clang --version
```


### الخطوة 4: إعداد Conda

```bash
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
chmod +x Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh -b -p $HOME/miniconda3
echo 'export PATH="$HOME/miniconda3/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
conda init bash
# إعادة فتح Terminal
conda create -n bitnet-cpp python=3.9 -y
conda activate bitnet-cpp
```


### الخطوة 5: تثبيت BitNet

```bash
git clone --recursive https://github.com/microsoft/BitNet.git
cd BitNet
pip install -r requirements.txt
```


### الخطوة 6: بناء وتشغيل BitNet

- نموذج صغير:
```bash
python setup_env.py --hf-repo 1bitLLM/bitnet_b1_58-large -q i2_s
python run_inference.py -m models/bitnet_b1_58-large/ggml-model-i2_s.gguf -p "What is the capital of France?"
```

- نموذج 3B:
```bash
python setup_env.py --hf-repo 1bitLLM/bitnet_b1_58-3B -q i2_s
python run_inference.py -m models/bitnet_b1_58-3B/ggml-model-i2_s.gguf -p "What is the capital of France?"
```

- نموذج Llama3-8B:
```bash
sudo sync && sudo echo 3 | sudo tee /proc/sys/vm/drop_caches
free -h
# تعديل .wslconfig إذا لزم الأمر
python setup_env.py --hf-repo HF1BitLLM/Llama3-8B-1.58-100B-tokens -q i2_s
python run_inference.py -m models/Llama3-8B-1.58-100B-tokens/ggml-model-i2_s.gguf -p "Name three types of pets that people commonly keep at home:\nAnswer:"
```
- تفعيل بيئة Conda قبل التشغيل: `conda activate bitnet-cpp`
-  التأكد من المسار: `cd BitNet`

## شاهد الشرح الكامل على يوتيوب!

لمشاهدة شرح مفصل وعملي لكافة الخطوات، تفضل بزيارة قناتنا على يوتيوب:

[![شاهد الفيديو](https://img.youtube.com/vi/4-HJOt53LMw/0.jpg)](https://youtu.be/4-HJOt53LMw)

لا تنسَ الاشتراك في القناة وتفعيل جرس التنبيهات ليصلك كل جديد! ❤️

