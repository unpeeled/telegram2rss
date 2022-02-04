#!/usr/bin/python3

import argparse
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'../lib')))

import Telegram2RSS

arg_parser = argparse.ArgumentParser(description='Telegram2RSS Converter')
arg_parser.add_argument('channel', help='Name of Telegram Channel')
arg_parser.add_argument('--url', help='Base URL of Telegram Channels',
                    default='https://t.me/s/')

args = arg_parser.parse_args()
