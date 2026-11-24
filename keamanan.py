import hashlib
import hmac
import os

iterasiBaru = 600_000
iterasiLama = 100_000
iterasiMaks = 10_000_000


def hitungHash(password, garam, iterasi):
    return hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), garam, iterasi)


def hashPassword(password):
    garam = os.urandom(16)
    hasil = hitungHash(password, garam, iterasiBaru)
    return f"{iterasiBaru}:{garam.hex()}:{hasil.hex()}"


def bacaHash(teks):
    if not isinstance(teks, str):
        return None
    bagian = teks.split(":")
    if len(bagian) == 2:
        iterasi = iterasiLama
        garamHex, hashHex = bagian
    elif len(bagian) == 3 and bagian[0].isascii() and bagian[0].isdigit():
        iterasi = int(bagian[0])
        garamHex, hashHex = bagian[1], bagian[2]
        if not 0 < iterasi <= iterasiMaks:
            return None
    else:
        return None
    if len(garamHex) != 32 or len(hashHex) != 64:
        return None
    try:
        return iterasi, bytes.fromhex(garamHex), bytes.fromhex(hashHex)
    except ValueError:
        return None


def sudahDihash(teks):
    return bacaHash(teks) is not None


def verifikasiPassword(password, tersimpan):
    data = bacaHash(tersimpan)
    if data is None:
        hitungHash(password, bytes(16), iterasiBaru)
        return False
    iterasi, garam, hashTersimpan = data
    hasil = hitungHash(password, garam, iterasi)
    return hmac.compare_digest(hasil, hashTersimpan)