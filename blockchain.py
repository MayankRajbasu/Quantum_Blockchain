import hashlib
import time

class Block:
    def __init__(self, index, previous_hash, timestamp, data, hash):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = hash



def calculate_hash(index, previous_hash, timestamp, data):
    value = str(index) + str(previous_hash) + str(timestamp) + str(data)
    return hashlib.sha256(value.encode()).hexdigest()

def create_genesis_block():
    return Block(0, "0", int(time.time()), "Genesis Block", calculate_hash(0, "0", int(time.time()), "Genesis Block"))

def create_new_block(previous_block, data):
    index = previous_block.index + 1
    timestamp = int(time.time())
    hash = calculate_hash(index, previous_block.hash, timestamp, data)
    return Block(index, previous_block.hash, timestamp, data, hash)

def is_chain_valid(chain):
    for i in range(1, len(chain)):
        current_block = chain[i]
        previous_block = chain[i - 1]

        if current_block.hash != calculate_hash(current_block.index, previous_block.hash, current_block.timestamp, current_block.data):
            return False

    return True

# Create a simple blockchain
blockchain = [create_genesis_block()]
previous_block = blockchain[0]

# Add blocks to the blockchain
for i in range(1, 4):
    new_data = f"Block #{i}"
    new_block = create_new_block(previous_block, new_data)
    blockchain.append(new_block)
    previous_block = new_block

# Print the blockchain
for block in blockchain:
    print(f"Index: {block.index}")
    print(f"Previous Hash: {block.previous_hash}")
    print(f"Timestamp: {block.timestamp}")
    print(f"Data: {block.data}")
    print(f"Hash: {block.hash}")
    print("\n")

# Validate the blockchain
print("Is the blockchain valid?", is_chain_valid(blockchain))
