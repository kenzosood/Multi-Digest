import hashlib
import Multidigest_Functions as md
import time

print("This program will create an encryption for your Message in Multiple Encrypting Algorithms ( Digest )")

print("Data would be Encrypted in following Algorithms")
encryptions = ['[1] blake2s', '[2] sha3_256', '[3] sha3_224', '[4] sha3_384', '[5] sha224', '[6] sha3_512', '[7] blake2b', '[8] sha512', '[9] shake_256', '[10] shake_128', '[11] md5', '[12] sha256', '[13] sha1', '[14] sha384', '[00] All']

# print(*encryptions, sep="\n")

str = input("Enter a String You Want to Encrypt: ")

print ("Now choose which encryptions you want to use: ")
print(*encryptions, sep="\n")

opt = input("Enter any Option: ")

if opt == "1":
    md.Blake2s(str)
    
elif opt == "2":
    md.SHA3_256(str)

elif opt == "3":
    md.SHA3_224(str)

elif opt == "4":
    md.SHA3_384(str)

elif opt == "5":
    md.SHA224(str)

elif opt == "6":
    md.SHA3_512(str)

elif opt == "7":
    md.Blake2b(str)

elif opt == "8":
    md.SHA512(str)

elif opt == "9":
    md.SHAKE_256(str)

elif opt == "10":
    md.SHAKE_128(str)

elif opt == "11":
    md.MD5(str)

elif opt == "12":
    md.SHA256(str)

elif opt == "13":
    md.SHA1(str)

elif opt == "14":
    md.SHA384(str)

elif opt == "00":
    
    md.SHA384(str)
    time.sleep(1)
    md.SHA1(str)
    time.sleep(1)
    md.SHA256(str)
    time.sleep(1)
    md.SHA3_224(str)
    time.sleep(1)
    md.MD5(str)
    time.sleep(1)
    md.SHAKE_128(str)
    time.sleep(1)
    md.SHAKE_256(str)
    time.sleep(1)
    md.SHA512(str)
    time.sleep(1)
    md.Blake2b(str)
    time.sleep(1)
    md.SHA3_512(str)
    time.sleep(1)
    md.SHA224(str)
    time.sleep(1)
    md.SHA3_384(str)
    time.sleep(1)
    md.SHA3_256(str)
    time.sleep(1)
    md.Blake2s(str)

else:
    print("wrong output")
