#!/usr/bin/python
from subprocess import call
def file_lister(str):
        ret=call(['ls','-l',str])
        if (ret!=0):
                print("Please give valid file path")

if __name__=='__main__':
        str=raw_input("Enter the directory to search with complete path:")
        file_lister(str)
