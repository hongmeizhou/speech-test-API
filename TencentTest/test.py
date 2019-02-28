from init_oral_process import InitOral
from transmit_oral_process import TransmitOral
import json
import sys
import argparse


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--text', help='input text')
    parser.add_argument('--wavpath', help='wav path')
    parser.add_argument('--output', help='output path')

    args=parser.parse_args()

    InitOral(args.text)
    TransmitOral(args.wavpath,args.output)


if __name__ == '__main__':
    main()