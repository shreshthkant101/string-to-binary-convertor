text = str(input("Enter Text To Be Converted: \n\n")).lstrip().rstrip()

if len(text) > 0:
    x = ([ord(c) for c in text])
    string = ''
    for i in x:
        string += str(i)

    string = int(string)

    binaryText = bin(string)

    print("Binary Output \n")
    print(binaryText)
else:
    print("Please input a valid string")
