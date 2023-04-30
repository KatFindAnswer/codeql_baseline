from sympy import randprime

class RSA:
    def __init__(self,bits=2048) -> None:
        self.public_key= tuple()
        self.private_key= tuple()
        self.generate(bits)

    def generate(self,bits=2048):
        p = randprime(2**(bits//2)//2,2**(bits//2))
        q = randprime(2**(bits//2)//2,2**(bits//2))
        while q == p:
            q = randprime(2**(bits//2)//2,2**(bits//2))
        n = p * q

        PhiN = (p-1)*(q-1)
        #  Generate E
        e = randprime(100,100000)
        # Caculate module inverse
        d = pow(e,-1,PhiN)
        
        self.public_key = (e,n)
        self.private_key = (d,n)

        #Encrypt message
    def encrypt(self, msg):
        key, n = self.public_key
        m = int.from_bytes(msg.encode(),byteorder="big")
        c = pow(m,key,n)
        return c
        
    def decrypt(self, msg):
        key, n = self.private_key
        MPowE = pow(msg,key,n)
        m = MPowE.to_bytes(((MPowE.bit_length() + 7) // 8), byteorder="big").decode()
        return m
    def key(self):
        e, n = self.public_key
        d, n = self.private_key
        print(f"e: \n{e}")
        print(f"d: \n{d}")
        print(f"n: \n{n}")

if __name__ == '__main__':
    rsa = RSA(2048)
    msg_input = "I am B20DCAT049"
    rsa.key()
    print(f"Plain text: \n{msg_input}")

    enctext = rsa.encrypt(msg_input)

    print(f"Encrypt message: \n{enctext}")
    print(f"Decrypt message: \n{rsa.decrypt(enctext)}")
        