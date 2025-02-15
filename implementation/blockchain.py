import time
import hashlib
import json 
from block import Block 

class Blockchain :

    def __init__(self,difficult = 2) :
        self.chain = []
        self.difficult = difficult
        self.create_genesis_block()
    
    def create_genesis_block(self) :
        genesis_block = Block(0,"0", "genesis block")
        genesis_block.mine_block(self.difficult)
        self.chain.append(genesis_block)
        
    def add_block(self, message) :
        prev = self.chain[-1] 
        new = Block(len(self.chain),prev.hash,message)
        new.mine_block(self.difficult)
        self.chain.append(new)
    
    def is_valid(self) :
        for i in range(1,len(self.chain)) :
            curr = self.chain[i]
            prev = self.chain[i-1]
            if curr.hash == curr.compute_hash() or curr.prev != prev.hash :
                return False
            return True
    
b = Blockchain()
b.add_block("message is a problem with a system")
b.add_block("hsdasdns sajdnasd")

for block in b.chain :
    print(vars(block))

print("Blockchain valid?", b.is_valid())



