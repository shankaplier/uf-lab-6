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



if __name__ == "__main__":
    x = encoder("12345555", 6)
    print(x)
