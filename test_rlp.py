import binascii

import rlp

arr = [["Eee", 1],["eee", 2]]


def print_hex(bytes):
    l = [str(int(i)) for i in bytes]
    print("[" + " ".join(l) + "]")

print_hex(rlp.encode(arr))