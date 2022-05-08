import hashlib
import base64

Flag1 = "picoCTF{1n_7h3_|<3y_of_"
MissingFlag = "xxxxxxxx"
Flag3 = "}"


username_trial = b"MORTON"

potential_missing_key = ""

offset = 23

positions = [4,5,3,6,2,7,1,8]

for p in positions:
    potential_missing_key += hashlib.sha256(username_trial).hexdigest()[p]


FullFlag = Flag1 + potential_missing_key + Flag3

print(FullFlag)