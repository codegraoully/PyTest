import hashlib

convert = input("Phrase? ")

converted = hashlib.sha512(str(convert).encode("utf-8")).hexdigest()

print(converted)
