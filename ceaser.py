clear_text=input("Enter the secret message:").lower()
valid_letters="abcdefghijklmnopqrstuvwxyz"
key          ="cdefghijklmnopqrstuvwxyzab"
new_string=""
cipher_text=[]
new_message=""
for char in clear_text:
    if char in valid_letters:
        new_string+=char
def encrypt():
    index_values=[valid_letters.index(char) for char in new_string]
    return "".join(key[indexkey]for indexkey in index_values)
encrepted_message=encrypt()
print(encrepted_message)
# decrept_text=input("Enter the message to decrypt:").lower()
# def decrypt():
#     index_values=[key.index(char) for char in new_message ]
#     return "".join(valid_letters[indexvalid_letter] for indexvalid_letter in index_values)
# decrypted_message=decrypt()
# print(decrypted_message)