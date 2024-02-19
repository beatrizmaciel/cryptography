def replace(i, key, start, end):
    n = end - start + 1
    k = (i + key)%(end+1) + ((i + key)//(end+1))*start

    if i + key < start:
        k = k + n

    return chr(k)

def encrypt(msg, key):
    # ord is a unicode character
    cA, cZ, ca, cz = ord('A'), ord('Z'), ord('a'), ord('z')
    encrypted = ""

    for character in msg:
        i = ord(character)
        new_character = character

        if cA <= i <= cZ:
            new_character = replace(i, key, cA, cZ)
        
        elif i in range(ca, cz + 1):
            new_character = replace(i, key, ca, cz)
        
        encrypted = encrypted + new_character
    
    return encrypted

def decrypt(msg, key):
    return encrypt(msg, -key)

key = int(input("Insert a number: "))
msg = input("Insert a text: ")

encrypted = encrypt(msg, key)
print(encrypted)
decrypted = decrypt(encrypted, key)
print(decrypted)