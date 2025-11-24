# chris-ai-game-object-detection
Object Detection in the Timberman Game

conda create -n chris-obj-detect python=3.9

conda activate chris-obj-detect

Install Microsoft Visual C++ 14 or greater

cd vcpkg && bootstrap-vcpkg.bat && vcpkg --classic install libavif

pip install -r requirements.txt

git clone https://github.com/ultralytics/yolov5 && cd yolov5 && pip install -r requirements.txt