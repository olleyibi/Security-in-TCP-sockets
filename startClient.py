# check length of the RNA String
def check_len(message):
    if len(message)%3 != 0:
        message = "DISCONNECT"
        print("INVALID RNA LENGTH")
        return message
    else:
        return message

    
# check each nucleotide in RNA String
def check_item(message):
    if message != "DISCONNECT":
        for i in message:
            if i not in ("G","A","C","T"):
                message = "DISCONNECT"
                print("INVALID RNA")
                break
        return message
    else:
        return message
    
    
# Request START RNA message
def start_rna():
    global msg
    msg = "empty"
    begin = "START RNA"
    while True:
            print("ENTER <START RNA> TO BEGIN")
            msg = input("Client: ").upper()
            if msg == begin:
                break
            else:
                print("INCORRECT INPUT, ENTER <START RNA> TO BEGIN")







# Ensure proper message is sent
begin = "START RNA"
message = ""





def get_message():
    print("PRESS <ENTER> IN ABSENCE OF A FILE") # get the file or input RNA
    filename = input("ENTER FILENAME: ")
    global message


    if filename:
        with open (filename,"r") as file:
            message = file.readline # read first line of the file
    else:
        print("'Y' to enter RNA \n'N' to exit")
        while True:
            answer = input("Enter (Y/N): ")
            if answer.upper() == 'Y':
                start_rna()
                print("Enter RNA")
                message = input("Client: ").upper() # Ensure uppercase is used for RNA string input
                message = check_len(message)
                message = check_item(message)
                break
            elif answer.upper() == 'N':
                message = "DISCONNECT"
                break
            else:
                print("INCORRECT ENTRY\n'Y' to enter RNA \n'N' to exit")

import socket
import rsa
import pickle
from cryptography.fernet import Fernet
import hashlib




import socket
HEADER = 64
PORT  =  6600
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER,PORT)
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "DISCONNECT"
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


# Generate an asymmetric key
asyKey = rsa.newkeys(2048)
#public key and private key
global publicKey
global privateKey
publicKey = asyKey[0]
privateKey = asyKey[1]

sendKey = pickle.dumps(publicKey)
sendKeySha256 = hashlib.sha256(sendKey).hexdigest()
client.send(pickle.dumps((sendKey, sendKeySha256)))
symKey, symKeySha256 = pickle.loads(client.recv(2048))
if hashlib.sha256(symKey).hexdigest() != symKeySha256:
    print("The key has been tampered!")
else:
    symKey = pickle.loads(rsa.decrypt(symKey, privateKey))
    print("Key exchange completed")

f = Fernet(symKey)


def send(msg):
    message = f.encrypt(msg.encode(FORMAT))
    client.send(message)

    rcv = client.recv(2048)
    rcv = f.decrypt(rcv).decode(FORMAT)
    print(rcv)
    
    
    
while True:
    if message != "DISCONNECT":
        get_message()
        send(message)
    else:
        send(message)
        input("<ENTER> TO EXIT")
        break
