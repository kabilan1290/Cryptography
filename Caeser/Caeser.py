print("Welcome To Caeser Cipher\n")
print("1.Caeser Encryption")
print("2.Caeser Decryption")
print("Enter......\n")
try:
    selection2 = int(input(""))
   
except ValueError:
    selection2=3000000000000000
   
if(selection2==1):
    #alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    out=[]
    a = 0
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    user1 =input("Enter your text to encrypt with caeser cipher\n")
    user = user1.lower()
    print("Your Text is :" + user)
    shift =""
    try:
        shift = int(input("Enter the number of Shift to perform\n"))
    except ValueError:
        print("Please enter Numbers only")
        exit(1)
    if (a==1):
        exit()


    length = len(user)
    for i in range(length):
        character = alpha.find(user[i])
        try:
            character = (character + shift) % 26
            output2=""
            output =alpha[character]
            out.append(output)
        except TypeError:
            exit(1)
        #ouput3 = output2.join(output)
    out1=''.join([str(j) for j in out])
    print("Your encrypted text :",out1)
elif(selection2==2):
    #alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    out=[]
    a = 0
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    user1 =input("Enter your text to decrypt with caeser cipher\n")
    user = user1.lower()
    print("Your Text is :" + user)
    shift =""
    try:
        shift = int(input("Enter the number of Shift to perform\n"))
    except ValueError:
        print("I said Numbers only!!!!!!!Just Die :p")
        exit(1)
    if (a==1):
        exit()


    length = len(user)
    for i in range(length):
        character = alpha.find(user[i])
        try:
            character = (character - shift) % 26
            output2=""
            output =alpha[character]
            out.append(output)
        except TypeError:
            exit(1)
        #ouput3 = output2.join(output)
    out1=''.join([str(j) for j in out])
    print("Your Decrypted text :",out1)
elif(selection2==3000000000000000):
    print("Why the heck you'r entering alphabets..!!")
else:
    print("Sorry you belong to another planet :(")

