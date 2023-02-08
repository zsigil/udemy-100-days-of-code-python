alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.

def encrypt(text, shift):
    cipher_text = ""
    for letter in text:
        old_index = alphabet.index(letter)
        new_index = (old_index + shift)%(len(alphabet))
        cipher_text += alphabet[new_index]

    print(f"The encoded text is {cipher_text}")

def decrypt(text, shift):
    plain_text = ""
    for letter in text:
        old_index = alphabet.index(letter)
        new_index = (old_index - shift)
        plain_text += alphabet[new_index]

    print(f"The original text is {plain_text}")

    
while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    if direction != "encode" and direction != "decode":
        break

    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if direction == "encode":
        encrypt(text, shift)
    
    else:
        decrypt(text, shift)