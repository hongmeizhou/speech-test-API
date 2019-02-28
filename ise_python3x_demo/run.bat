
set workdir=E:\Work\SpeechDXTest\Tencent\ise_python3x_demo
set text=E:\Work\SpeechDXTest\Tencent\ise_python3x_demo\lang\enus\0000000001-0000000500.txt
set wavpath=E:\Work\SpeechDXTest\Tencent\ise_python3x_demo\lang\enus\wav
set output=E:\Work\SpeechDXTest\Tencent\ise_python3x_demo\output
set lang=en_us

python %workdir%\test.py --text=%text% --lang=%lang% --wavpath=%wavpath% --output=%output%