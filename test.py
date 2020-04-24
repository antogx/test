#!/usr/bin/python3.6
import argparse

def read_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("number1", help="First Number", type=int)
    parser.add_argument("number2", help="Second Number", type=int)
    parser.add_argument("-o", "--operation", help="Type of operation", choices=['add', 'subtract', 'multiply'])
    return parser.parse_args()

def ops():
    args = read_args()
    return args.operation

print(ops())