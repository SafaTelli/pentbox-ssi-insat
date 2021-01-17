import hashlib

def hash():
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
