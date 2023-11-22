from qiskit import Aer, QuantumCircuit, transpile, assemble, execute
from qiskit.visualization import plot_histogram
import hashlib
import time
from math import gcd

def lattice_based_hash(index, previous_hash, timestamp, data):
    # Enhanced lattice-based hash function (simplified for illustration)
    prime_modulus = 7919  # Replace with a larger prime modulus in a real-world scenario
    lattice_hash_input = f'{index}{previous_hash}{timestamp}{data}'.encode()

    # Create a hash using a strong cryptographic hash function 
    hashed_value = int(hashlib.shake_256(lattice_hash_input).hexdigest(256), 16)

    # Ensure that the result is coprime with the modulus
    while gcd(hashed_value, prime_modulus) != 1:
        hashed_value += 1

    # Take the result modulo the prime modulus
    return hashed_value % prime_modulus

class Block:
    def __init__(self, index, previous_hash, timestamp, data, quantum_key, hash):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.quantum_key = quantum_key
        self.hash = hash


def calculate_hash(index, previous_hash, timestamp, data, quantum_key):
    # Use lattice-based hash function instead of SHA-256
    return lattice_based_hash(index, previous_hash, timestamp, data + quantum_key)

def create_genesis_block():
    return Block(0, "0", int(time.time()), "Genesis Block", "0", calculate_hash(0, "0", int(time.time()), "Genesis Block", "0"))


def create_new_block(previous_block, data, quantum_key):
    index = previous_block.index + 1
    timestamp = int(time.time())
    hash = calculate_hash(index, previous_block.hash, timestamp, data, quantum_key)
    return Block(index, previous_block.hash, timestamp, data, quantum_key, hash)


def is_chain_valid(chain):
    for i in range(1, len(chain)):
        current_block = chain[i]
        previous_block = chain[i - 1]

        if current_block.hash != calculate_hash(current_block.index, previous_block.hash, current_block.timestamp, current_block.data, current_block.quantum_key):
            return False

    return True

def bbm92_protocol():
    # Step 1: Prepare the quantum circuit
    alice = QuantumCircuit(1, 1, name='Alice')
    bob = QuantumCircuit(1, 1, name='Bob')

    alice.h(0)  # Apply Hadamard gate
    alice.measure(0, 0)  # Measure qubit

    # Share the quantum circuit state
    bob.measure(0, 0)

    # Step 2: Simulate the circuit
    backend = Aer.get_backend('qasm_simulator')
    shots = 1024
    alice_job = execute(alice, backend=backend, shots=shots)
    bob_job = execute(bob, backend=backend, shots=shots)
    
    alice_result = alice_job.result()
    bob_result = bob_job.result()

    # Step 3: Analyze the results
    alice_counts = alice_result.get_counts(alice)
    bob_counts = bob_result.get_counts(bob)

    # Extract key
    alice_key = list(alice_counts.keys())[0]
    bob_key = list(bob_counts.keys())[0]

    print("Alice's key:", alice_key)
    print("Bob's key:", bob_key)

    # Step 4: Compare keys and establish a secure key
    if alice_key == bob_key:
        print("Keys match. Secure key exchange successful!")
        return alice_key
    else:
        print("Keys do not match. Key exchange failed.")
        return None

# Create a simple blockchain with quantum key distribution and lattice-based hash
blockchain = [create_genesis_block()]
previous_block = blockchain[0]

# Add blocks to the blockchain
for i in range(1, 4):
    new_data = f"Block #{i}"
    quantum_key = bbm92_protocol()
    
    # If the key exchange failed, exit the program
    if quantum_key is None:
        print("Blockchain creation aborted.")
        break
    
    new_block = create_new_block(previous_block, new_data, quantum_key)
    blockchain.append(new_block)
    previous_block = new_block

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
print("Is the blockchain valid?", is_chain_valid(blockchain))
