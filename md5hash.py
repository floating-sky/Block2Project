import hashlib

input_string = input("Please give the text you would like to be encrypted using it's MD5 hash: ")

input_hash = hashlib.md5(input_string.encode()).hexdigest()

print("original text: " + input_string)
print("encrypted text: " + input_hash)
