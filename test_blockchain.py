from blockchain import create_genesis_block as simple_create_genesis_block
from blockchain import create_new_block as simple_create_new_block
from blockchain import is_chain_valid as simple_is_chain_valid
from quantum_blockchain import create_genesis_block as ql_create_genesis_block
from quantum_blockchain import create_new_block as ql_create_new_block
from quantum_blockchain import is_chain_valid as ql_is_chain_valid
from quantum_blockchain import bbm92_protocol
import time

def test_simple_blockchain():
    # Create a simple blockchain
    start_time = time.time()

    blockchain = [simple_create_genesis_block()]
    previous_block = blockchain[0]

    # Add blocks to the blockchain
    for i in range(1, 4):
        new_data = f"Block #{i}"
        new_block = simple_create_new_block(previous_block, new_data)
        blockchain.append(new_block)
        previous_block = new_block

    # Attempt double-spending attack
    malicious_block = simple_create_new_block(previous_block, "Malicious Transaction")
    blockchain.append(malicious_block)

    # Print the blockchain
    for block in blockchain:
        print(f"Index: {block.index}")
        print(f"Previous Hash: {block.previous_hash}")
        print(f"Timestamp: {block.timestamp}")
        print(f"Data: {block.data}")
        print(f"Hash: {block.hash}")
        print("\n")

    # Validate the blockchain
    print("Is the simple blockchain valid?", simple_is_chain_valid(blockchain))

    # Measure and print the time taken
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Time taken to compromise simple blockchain creation: {elapsed_time*1000} miliseconds\n")


def test_quantum_lattice_blockchain():
    start_time = time.time()
    # Create a quantum lattice blockchain
    blockchain = [ql_create_genesis_block()]
    previous_block = blockchain[0]

    # Add blocks to the blockchain
    for i in range(1, 4):
        new_data = f"Block #{i}"
        quantum_key = bbm92_protocol()

        # If the key exchange failed, exit the program
        if quantum_key is None:
            print("Quantum lattice blockchain creation aborted.")
            break

        new_block = ql_create_new_block(previous_block, new_data, quantum_key)
        blockchain.append(new_block)
        previous_block = new_block
    
    # Attempt double-spending attack
    malicious_block = ql_create_new_block(previous_block, "Malicious Transaction", "Quantum Key")
    blockchain.append(malicious_block)


    # Print the blockchain
    for block in blockchain:
        print(f"Index: {block.index}")
        print(f"Previous Hash: {block.previous_hash}")
        print(f"Timestamp: {block.timestamp}")
        print(f"Data: {block.data}")
        print(f"Quantum Key: {block.quantum_key}")
        print(f"Hash: {block.hash}")
        print("\n")

    # Validate the blockchain
    print("Is the quantum lattice blockchain valid?", ql_is_chain_valid(blockchain))

    # Measure and print the time taken
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Time taken to compromise quantum lattice blockchain creation: {elapsed_time*1000} miliseconds\n")

if __name__ == "__main__":
    # Test the simple blockchain
    print("\n" + "="*50 + "\n")
    print("Testing Simple Blockchain:")
    test_simple_blockchain()
    print("\n" + "="*50 + "\n")

    # Test the quantum lattice blockchain
    print("Testing Quantum Lattice Blockchain:")
    test_quantum_lattice_blockchain()

