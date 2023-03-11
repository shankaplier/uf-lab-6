# This is done by G Shashank
import sys

def encoder(unencodedString, numbertobeadded):
    # Variable to hold the final encoded string
    encodedstring = ""

    # for loop that loops through every number in the input
    for i in unencodedString:
        # Variable that holds the encoded number
        decodednumber = int(i) + numbertobeadded
        # If the decoded number exceeds 10 we use division to change it back to a single number
        if decodednumber >= 10:
            num1 = decodednumber%10
            num2 = decodednumber//10
            decodednumber = num1 + num2
        # We convert the final number into a string and add it to encodedstring
        encodedstring += str(decodednumber)

    return encodedstring

#This function was created by Adam Magoulas
def decoder(encodedString, decoderNum):
    encodedString = str(encodedString)
    enc_list = list(encodedString)
    index = 0
    for char in enc_list:
        char = int(char)
        char -= decoderNum
        enc_list[index] = char
        index+=1
    decoded = ''
    for i in enc_list:
        decoded += str(i)
    return (decoded)

if __name__ == "__main__":
    while True:
        option = input('''Do you want to encode or decode a number?:
1) encode
2) decode
3) exit\n''')

        if option == "3":
            sys.exit()
        elif option == "1":
            unencodedString = input("\nWhat do you want the encoding number to be: ")
            numbertobeadded = int(input("\nBy what value do you want to shift the input: "))
            encodedString = encoder(unencodedString, numbertobeadded)
            print(f"\nThe encoded value is: {encodedString}\n")
        elif option == "2":
            encodedString = input("What do you want the decoding number to be: ")
            decoderNum = int(input("\nBy what value do you want to decode the input: "))
            decoded = decoder(encodedString, decoderNum)
            print(f"\nThe decoded value is: {decoded}\n")

