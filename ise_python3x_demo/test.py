# -*- coding: utf-8 -*-
from ise_python3x_demo import getResult
import sys
import argparse
import os
import sys
import time


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--text', help='input text')
    parser.add_argument('--wavpath', help='wav path')
    parser.add_argument('--output', help='output path')
    parser.add_argument('--lang', help='language')

    args=parser.parse_args()
	
    with open(args.text,"r",encoding='utf-8') as fr:
        lines=fr.readlines()

    #wavfile=glob.glob(os.path.join(args.wavpath,"*.wav"))
	
    result=os.path.join(args.output,"result.txt")
    if not os.path.exists(args.output):
        os.makedirs(args.output)

    if os.path.exists(result):
        os.remove(result)

		
    count=1
    log=""
    for line in lines:
        strcount = str(format(count)).zfill(10)
        wavfile=os.path.join(args.wavpath,strcount+".wav")
        log+=strcount+":"+getResult(line,wavfile,args.lang)
        count+=1
        time.sleep(2)

    with open(result,"w") as fw:
        fw.write(log)
	

if __name__ == '__main__':
    main()