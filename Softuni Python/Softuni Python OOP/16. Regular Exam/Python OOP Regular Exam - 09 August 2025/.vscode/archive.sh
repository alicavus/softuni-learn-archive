#! /usr/bin/bash -e

echo "$PWD"

zip -9 "$PWD.zip" $(find project/ -type f -iname "*.py")

# 7z a -tzip -mx=9 -mm=LZMA "$PWD.zip" $(find project/ -type f -iname "*.py")

cat << EOF | zip -z "$PWD.zip"
Created by (c) Ramadan Ali.
All rights reserved.

Redistribution, using in research in any mean is prohibited.

You can __test__ for validity
but **can't** use it for any kind of AI training
OR other means
WITHOUT WRITTEN PERMISSION.

You have been warned.
.
EOF