

from set_of_coinflips_pb2 import CoinFlip, SetOfCoinFlips, SetOfCoinFlipsPacked

def print_info(p):
    print("p.heads: " + str(p.heads))
    print("p.hasField(\"heads\"): " + str(p.HasField("heads")))
    print("p.SerializeToString(): " + str([ch for ch in p.SerializeToString()]))

def char_by_char(l):
    return str([ch for ch in l])

# Before we start:
# $ brew install protobuf
# $ pip install protobuf
# $ protoc set_of_coinflips.proto --python_out=. --java_out=.

# Create an extremely basic protobuf object:
p = CoinFlip()
print_info(p)

# If we set fields, things look different:
p.heads = True
print_info(p)

# But false is distinct from null:
p.heads = False
print_info(p)

# And we can get back there, too:
p.ClearField("heads")
print_info(p)

# some Python-ish things are not legal:
try:
    p.heads = "yep, I got heads!"
except TypeError as te:
    print("Raised a type error!")
    print("stack trace:")
    print("  " + te.message)
    print("/stack trace")

p.heads = True
p_serialized = p.SerializeToString()
with open('single_head', 'w') as f:
    f.write(p_serialized)

# Now run
# $ hexdump single_head
# 0000000 08 01
# 0000002

# Pretty cool!!

# But also a bit boring.
import random
python_headflips = [random.random() > .5 for i in range(10)]
set_of_coin_flips = SetOfCoinFlips()

print("Before setting any protobuf head flips:")
print(python_headflips)
print(" begin set_of_coin_flips")
print(set_of_coin_flips)
print(" end set_of_coin_flips")

for flip in python_headflips:
    cur_pb_flip = set_of_coin_flips.coinflips.add()
    cur_pb_flip.heads = flip

print("After setting any protobuf head flips:")
print(python_headflips)
print(" begin set_of_coin_flips")
print(set_of_coin_flips)
print(" end set_of_coin_flips")

# Similar type-safe behavior:
try:
    set_of_coin_flips.coinflips = "abc"
except AttributeError as ae:
    print("Raised an attribute error!")
    print("stack trace:")
    print("  " + ae.message)
    print("/stack trace")

# Can get the length of the repeated field:
print("Length: " + str(len(set_of_coin_flips.coinflips)))

# Can serialize the set_of_coin_flips object
set_of_coinflips_serialized = set_of_coin_flips.SerializeToString()
set_of_coinflips_char_by_char = char_by_char(set_of_coinflips_serialized)
print(format("Serialization of a SetOfCoinFlips object: (len={})".format(len(set_of_coinflips_serialized))))
print(set_of_coinflips_char_by_char)

# But they are longer than the concatenation of the same objects.
concatenation_of_coin_flips = ""
for flip in python_headflips:
    p = CoinFlip()
    p.heads = flip
    p_serialized = p.SerializeToString()
    concatenation_of_coin_flips += p_serialized
concat_char_by_char = char_by_char(concatenation_of_coin_flips)
print(format("Concatenation of 10 CoinFlip objects: {}".format(len(concatenation_of_coin_flips))))
print(concat_char_by_char)

# And those are even longer than if we had used a "packed" flag in the proto!
dense = SetOfCoinFlipsPacked()
for flip in python_headflips:
    dense.coinflips.append(flip)
dense_serialized = dense.SerializeToString()
dense_char_by_char = char_by_char(dense_serialized)
print(format("SetOfCoinFlipsPacked (dense) serialization: {}".format(len(dense_serialized))))
print(dense_char_by_char)

# But any of these options are much much better than using JSON:
import json
json_serialized = json.dumps(python_headflips)
json_char_by_char = char_by_char(json_serialized)
print("JSON character-by-character serialization: (len = {})".format(len(json_serialized)))
print(json_char_by_char)

# Write the dense object to disk for now:
filename = "packed_obj"
import sys
if len(sys.argv) > 1:
    filename = sys.argv[1]
with open(filename, 'w') as f:
    f.write(dense.SerializeToString())

# That's it!
# (but it is cool to run 
# $ hexdump packed_obj
# 0000000 0a 0a 00 00 01 01 01 01 01 01 01 00
# 000000c
# once more for good measure :-) )
