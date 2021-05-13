#!/usr/bin/python3
"""Script which reads stdin line by line and computes metrics"""
import sys

size = 0
codes = {200: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
i = 0

try:
    for line in sys.stdin:
        tmp = line.split()
        size += int(tmp[-1])
        try:
            codes[int(tmp[-2])] += 1
        except:
            pass
        i += 1
        if i == 10:
            print('File size:', size)
            for k, v in sorted(codes.items()):
                print("{}: {}".format(k, v))
            i = 0
    else:
        print('File size:', size)
        for k, v in sorted(codes.items()):
            print("{}: {}".format(k, v))
except KeyboardInterrupt:
    print('File size:', size)
    for k, v in codes.items():
        print("{}: {}".format(k, v))
