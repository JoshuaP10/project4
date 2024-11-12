#!/usr/bin/env python3

import sys

sys.stdout.buffer.write(b'\x70\x72\x61\x74\x6c' + b'\x00' * 5 + b'\x41\x2b')
