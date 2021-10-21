# Security-in-TCP-sockets
Adding Security to TCP sockets


Aim
- evelop a secure networked application using TCP socket
- Develop a protocol to allow secure transfer of data

Protocol
-	Provided the server is running and a client connects to the server, the client generates an asymmetric key from the RSA library which uses a publicly known key for encryption, but requires a different key, known only to the intended recipient, for decryption.
-	The public key is then serialized using pickle.dump() and then hashed using an internal block size of 32 bits and sent to the server.
-	The server receives the package and deserializes it, with the help of the hash function, the correctness of the public key is verified.
-	The server generates a key for symmetric encryption which is then serialized, hashed and sent to the clients to ensure its accuracy.
-	The clients receive the package, deserialize and verifies if the key has been tampered with.
-	Both client and server initializes an encryption object using the symmetric key (Fernet())
-	For every new connection, this same handshake process is started.
-	After the creation of the encryption object, all communications from either party is encrypted or decrypted as required.

Optimization rule
The rule used by the server in optimizing the codon is based on the description of reverse engineering where the modifications in the RNA vaccine are all synonymous. The vaccine RNA code is different, but the same amino acids and the same protein come out. This increases the amount of “G” or “C” nucleotide in the vaccine which helps enhance protein production.
