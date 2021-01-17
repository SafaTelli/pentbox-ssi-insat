import hashlib
import base64

def mainMenu():
    print("******* OUTILS SSI_INSAT POUR LA CRYPTOGRAPHIE *******")
    print("")
    print("1: Codage et decodage d'un message")
    print("2: Hashage d'un message")
    print("3: Craquage d'un message hashe")
    print("4: Chiffrement et dechiffrement symetrique d'un message")
    print("5: Chiffrement et dechiffrement symetrique d'un message")
    print("6: Quitter")
    select=int(input("Saisir votre choix "))
    if select==1:
        codDecodeMessage()
    elif select==2:
        hashMessage()
    elif select==3:
        print("3")
    elif select==4:
        print("4")
    elif select==5:
        print("5")
    elif select==6:
        exit
    else:
        print("choix invalid")
        mainMenu()

def codDecodeMessage():
    txtMsg=input("Saisir un text pour codage: ")
    base64_bytes = base64.b64encode(txtMsg.encode('ascii'))
    print("le message code est: ",base64_bytes)
    txtForDecode=input("Saisir un text pour decodage: ")
    sample_string_bytes =base64.b64decode(txtForDecode.encode('ascii'))
    sample_string = sample_string_bytes.decode("ascii") 
    print("Le message original est: ",sample_string)

def hashMessage():
    print("liste des fonctions de hashage ")
    algorithms = hashlib.algorithms_guaranteed
    i=1
    for algo in algorithms:
        print(i,": ",algo)
        i=i+1
    txtForhash=input("saisir un message ")
    selectAlgo=int(input("saisir votre choix "))
    txtHashed="Le text hashe est: "
    if selectAlgo==10:
        txtHashed+=hashlib.md5(txtForhash.encode()).hexdigest()
    elif selectAlgo==14:
        txtHashed+=hashlib.sha256(txtForhash.encode()).hexdigest()
    print(txtHashed)













def crackMessage():
    txtMsg=input("Saisir un text pour codage: ")
    print("le message est: ",txtMsg)

def chiffreMessage():
    txtMsg=input("Saisir un text pour codage: ")
    print("le message est: ",txtMsg)

def dechiffreMessage():
    txtMsg=input("Saisir un text pour codage: ")
    print("le message est: ",txtMsg)

### main 
mainMenu()


