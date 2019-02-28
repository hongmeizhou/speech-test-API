
set workdir=C:\Users\v-honzho\Desktop\TencentTest
set text="I love how I taste, and I love how I smell."
set wavpath=\\tts\shanhai\ttsdata\ttsdata\en-us\Voices\Zo\Speech\Wave16kNormalized\0000000001-0000000500\0000000002.wav
set output=C:\Users\v-honzho\Desktop\TencentTest

python %workdir%\test.py --text=%text% --wavpath=%wavpath% --output=%output%