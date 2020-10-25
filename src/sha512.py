import hashlib

convert = input("Phrase to encrypt? ")

converted = hashlib.sha512(str(convert).encode("utf-8")).hexdigest()

print(converted)
