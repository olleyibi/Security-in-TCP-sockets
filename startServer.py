# get ref csv
def get_csv(data):
    import csv
    global codon
    global a_acid
    codon=[]
    a_acid=[]
    with open(data) as csv_file:#this will open the txt doc and store the 2nd row elements.sice first row is just heading
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:#for column row. it just passes
            if line_count == 0:
                line_count += 1
            else:
                codon.append(row[0])
                a_acid.append(row[1])


def optimize(input):
    x = int(len(input) / 3)
    for i in range(x):
        x = i + 1
        if (input[i * 3:(x * 3)] not in codon):
            return "DISCONNECT"


    change=input[0:3]
    message = input[0:3]
    acid = ''
    for i in range(len(codon)):
        if (codon[i] == message):
            acid = a_acid[i]
    for i in range(len(a_acid)):
        if (a_acid[i]==acid and codon[i] != message):
            message = codon[i]
            break
    return input.replace(change,message)



# server
import socket
import threading
import rsa
import pickle
from cryptography.fernet import Fernet
import hashlib


PORT  =  6600
SERVER = ""
ADDR = (SERVER,PORT)
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)




def handle_client(conn,addr):
    publicKeyPK, pubKeySha256 = pickle.loads(conn.recv(2048))
    if hashlib.sha256(publicKeyPK).hexdigest() != pubKeySha256:
        print("The key has been tampered!")
    else:
        publicKey = pickle.loads(publicKeyPK)
        print("Accepted public key")

    sym_key = Fernet.generate_key()
    en_sym_key = rsa.encrypt(pickle.dumps(sym_key), publicKey)
    en_sym_key_sha256 = hashlib.sha256(en_sym_key).hexdigest()
    print("Encrypting Transfer Key")
    conn.send(pickle.dumps((en_sym_key,en_sym_key_sha256)))
    f = Fernet(sym_key)



    
    connected = True
    while  connected:
        msg = conn.recv(2048)
        msg = f.decrypt(msg).decode(FORMAT)
        if msg == DISCONNECT_MESSAGE:
            connected = False
            conn.close()
        else:
            get_csv("codon-aminoacid.csv")
            msg = optimize(msg)
            if msg == "DISCONNECT":
                conn.send("CODON NOT CONTAINED IN FILE".encode(FORMAT))
                conn.close()
            else:
                msg = f.encrypt(msg.encode(FORMAT))
                conn.send(msg)
                
            
            print(f"[{addr}] {msg}")
            
            

def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn,addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn,addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")

        
print("[STARTING] server is starting....")
start()
