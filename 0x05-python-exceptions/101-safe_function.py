#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        return fct(*args)
    except Exception as err:
        print('Exception:', err, file=sys.stderr)
        return
