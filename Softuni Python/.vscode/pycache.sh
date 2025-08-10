#! /usr/bin/bash -e

find "$PWD" -type f -iname "*.pyc" -exec rm -rfv "{}" + 2>/dev/null

find "$PWD" -type d -iname "__pycache__" -exec rm -rfv "{}" + 2>/dev/null