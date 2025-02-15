import time
import hashlib
import json 
class Block :
    def __init__(self, index, previous_hash, transactions, timestamp=None):
        self.index = index
        self.previous_hash = previous_hash
        self.transactions = transactions
        self.timestamp = timestamp or time.time()
        self.nonce = 0
        self.hash = self.compute_hash()
    
    def compute_hash(self) :
        block_string = json.dumps({
            "index" : self.index,
            "previous_hash": self.previous_hash,
            "transactions": self.transactions,
            "timestamp": self.timestamp,
            "nonce": self.nonce
        }).encode()

        return hashlib.sha256(block_string).hexdigest()

    def mine_block(self,difficulty) :
        while self.hash[:difficulty] != "0" * difficulty :
            self.nonce += 1
            self.hash = self.compute_hash()
