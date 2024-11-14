#!/usr/bin/env python3

import sys

sys.stdout.buffer.write(b"pratl" + b"\x00" * 5 + b"A+")
