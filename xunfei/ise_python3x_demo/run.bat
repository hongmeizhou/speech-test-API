
set workdir=E:\Work\SpeechDXTest\Tencent\xunfei\ise_python3x_demo
set text=E:\Work\SpeechDXTest\Tencent\xunfei\ise_python3x_demo\lang\zhcn\0000000001-0000000500.txt
set wavpath=E:\Work\SpeechDXTest\Tencent\xunfei\ise_python3x_demo\lang\zhcn\wav
set output=E:\Work\SpeechDXTest\Tencent\xunfei\ise_python3x_demo\output
set lang=cn

python %workdir%\test.py --text=%text% --lang=%lang% --wavpath=%wavpath% --output=%output%