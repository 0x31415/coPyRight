#!/usr/bin/env python3
import sys
from src.copyrighter import coPyRighter

def main(folder_path : str = ''):
    copyrighter = coPyRighter(folder_path)
    copyrighter.do()

if __name__ == "__main__":
    if (len(sys.argv) !=2):
        raise ValueError("Too much/few args. Usage: ./main.py folders/")
    else:
        main(sys.argv[1])
