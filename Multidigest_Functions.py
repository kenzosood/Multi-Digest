import hashlib

def SHA1(str):
    result = hashlib.sha1(str.encode())
    print("The HexaDecimal Equivalent to SHA1 is : ")
    print(result.hexdigest())
    print("\r")

def SHA224(str):
    result = hashlib.sha224(str.encode())
    print("The HexaDecimal Equivalent to SHA224 is : ")
    print(result.hexdigest())
    print("\r")


def SHA256(str):
    result = hashlib.sha256(str.encode())
    print("The HexaDecimal Equivalent to SHA256 is : ")
    print(result.hexdigest())
    print("\r")


def SHA384(str):
    result = hashlib.sha384(str.encode())
    print("The HexaDecimal Equivalent to SHA385 is : ")
    print(result.hexdigest())
    print("\r")


def SHA512(str):
    result = hashlib.sha512(str.encode())
    print("The HexaDecimal Equivalent to SHA512 is : ")
    print(result.hexdigest())
    print("\r")


def SHA3_224(str):
    result = hashlib.sha3_224(str.encode())
    print("The HexaDecimal Equivalent to SHA3_224 is : ")
    print(result.hexdigest())
    print("\r")


def SHA3_256(str):
    result = hashlib.sha3_256(str.encode())
    print("The HexaDecimal Equivalent to SHA3_256 is : ")
    print(result.hexdigest())
    print("\r")


def SHA3_384(str):
    result = hashlib.sha3_384(str.encode())
    print("The HexaDecimal Equivalent to SHA3_384 is : ")
    print(result.hexdigest())
    print("\r")


def SHA3_512(str):
    result = hashlib.sha3_512(str.encode())
    print("The HexaDecimal Equivalent to SHA3_512 is : ")
    print(result.hexdigest())
    print("\r")



def Blake2b(str):
    result = hashlib.blake2b(str.encode())
    print("The HexaDecimal Equivalent to BLAKE2b is : ")
    print(result.hexdigest())
    print("\r")


def Blake2s(str):
    result = hashlib.blake2s(str.encode())
    print("The HexaDecimal Equivalent to Blake2s is : ")
    print(result.hexdigest())
    print("\r")


def SHAKE_128(str):
    result = hashlib.shake_128(str.encode())
    print("The HexaDecimal Equivalent to SHAKE_128 is : ")
    print(result.hexdigest(25))
    print("\r")


def SHAKE_256(str):
    result = hashlib.shake_256(str.encode())
    print("The HexaDecimal Equivalent to SHAKE_256 is : ")
    print(result.hexdigest(25))
    print("\r")


def MD5(str):
    result = hashlib.md5(str.encode())
    print("The HexaDecimal Equivalent to MD5 is : ")
    print(result.hexdigest())
    print("\r")
