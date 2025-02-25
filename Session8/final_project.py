alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


#hello
def encrypt(original_text, decode_or_encode ):
    final_text = ""
    vowels = ['a', 'e', 'i', 'o', 'u']
    for letter in original_text:
        if decode_or_encode == "encode":
            if letter in vowels:
                shifted_position_wovel = alphabet.index(letter) + 1
                final_text += alphabet[shifted_position_wovel]
            else:
                shifted_position_consonant = alphabet.index(letter) - 1
                final_text += alphabet[shifted_position_consonant]
        else:
            if letter in vowels:
                shifted_position_wovel = alphabet.index(letter) -1
                final_text += alphabet[shifted_position_wovel]
            else:
                shifted_position_consonant = alphabet.index(letter) + 1
                final_text += alphabet[shifted_position_consonant]

    print(f"Here is the decoded text: {final_text}")


should_continue = True

while should_continue :
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    encrypt(text, direction)

    restart = input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n").lower()
    if restart == "no":
        should_continue = False





