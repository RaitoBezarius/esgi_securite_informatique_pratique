import ctypes
libc = ctypes.CDLL('/lib/libc.so.6')
print(libc.printf(b"depuis la Python mais bien de la libc: %d mais aussi %s", 5, b"Hello World!\n"))
