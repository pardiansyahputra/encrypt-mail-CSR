
#mail annonimous text from PYPHANTOMCRYPT



def encrypt(plaintext,shift):
    
    encrypted_text=""

    for char in plaintext:
        #this is for alphabet
        if char.isalpha():
            shift_amount=shift%26
            if char.islower():
                shifted_char=chr((ord(char)-ord("a")+shift_amount) %26 + ord ("a"))
            else:
                shifted_char=chr((ord(char)-ord("A")+shift_amount)%26 + ord ("A"))
            encrypted_text+=shifted_char
        #this is for numeric
        elif char.isdecimal():
            shift_amount=shift%10
            shifted_char=chr((ord)(char)-ord("0")+shift_amount%10 + ord("0"))
            encrypted_text+=shifted_char
        else:
            encrypted_text+=char
    return encrypted_text.replace(" ","")    


def decrypt(chipertext,shift):


    decrypt_text=""

    for char in chipertext:
        #this is for alphabet
        if char.isalpha():
            shift_amount=shift%26
            if char.islower():
                shifted_char=chr((ord(char)-ord("a")-shift_amount) %26 + ord ("a"))
            else:
                shifted_char=chr((ord(char)-ord("A")-shift_amount)%26 + ord ("A"))
            decrypt_text+=shifted_char
        #this is for numeric
        elif char.isdecimal():
            shift_amount=shift%10
            shifted_char=chr((ord)(char)-ord("0")-shift_amount%10 + ord("0"))
            decrypt_text+=shifted_char
        else:
            decrypt_text+=char
    return decrypt_text.replace(" ","")
    

       #variable selection code
while True:
    print("=======================================================================================================")
    print("=====================================.WELCOM TO PYPHANTOMCRYPT.========================================")
    print("#from phantom to securty===============================================================================")
    print("***")
    choice = input("Do you want to encrypt (e) or decrypt (d) or quit (q)? ")
    print("=======================================================================================================")


    if choice.lower() == 'e':
        plaintext = input("Enter the text to encrypt: ")
        print("***")
        try:

            shift = int(input("Enter the keyword : "))
            print("***")
            ciphertext = encrypt(plaintext,shift)
            print("***")
            print("Ciphertext:", ciphertext)
            print("***")

            #selected URL selection code
            import webbrowser
            url=str(input("input URL  www.exampel.com :"))
            webbrowser.open(url)

        except ValueError:
            print("Invalid shift value. Please enter an integer.")

    elif choice.lower() == 'd':
        ciphertext = input("Enter the text to decrypt: ")
        print("***")
        try:

            shift = int(input("Enter the keyword : "))
            print("***")
            decrypted_text = decrypt(ciphertext,shift)
            print("***")
            print("Decrypted text:", decrypted_text)
            print("***")

            #selected URL selection code
            import webbrowser
            url=str(input("input URL www.exampel.com :"))
            webbrowser.open(url)

        except ValueError:
            print("Invalid shift value. Please enter an integer.")

    elif choice.lower() == 'q':
        break

    else:
        print("Invalid choice. Please enter 'e', 'd', or 'q'.")

