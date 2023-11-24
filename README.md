# Quantum_Blockchain

## Quantum-lattice BlockChain Structure
* Index
* Timestamp
* Data
* Quantum Key
* hash (lattice-based)


## Quantum Key Distribution ( based on BB92 protocol)
* Simulate BBM92 quantum key distribution protocol
* Creation of two quantum circuits named Alice and Bob
* Apply Hadamard gate on Alice's qubit, measure it, and share the circuit state with Bob
* Simulate circuits, compare results, and establish a secure key


## Latice Based Hash
* Take index, previous_hash, timestamp, data, quantum_key as input
* Calculate hash using lattice-based hash function 
* lattice-based hash function employs SHAKE-256 algorithm and large prime modulus for message digest and producing lattice-based hash using previous_hash


# Team Members
* Mayank Raj
* Susan Shilbi
* Shreyash Kumar S
* Shaswat Kaushik
* Vaidik Chhirolya

# Prposed Model Arhitecture:
![image](https://github.com/Mayank-902/Quantum_Blockchain/assets/76254590/fc64e23e-57aa-4ad0-b0c2-ae02ba14c0e3)

## The Test:

* We are implemting Double-Spending Attack on a simple blockchaina nd our proposed quantum blockchain and comparing the complexity of both the codes by looking at he outputs.
* The output clearly showcases that the more complex nature of the quantum blockcahin makes it harder for such an attack to be successful.
* This ensures the future safety of blockchain applications from the more sophisticated and fast Quantum Computers by utilizing quantum safe algorithms.
 
## OUTPUTS
# OUTPUT OF blockchain.py:
![image](https://github.com/Mayank-902/Quantum_Blockchain/assets/76254590/df8949f5-7929-4040-91bf-56e72810b6fb)

# OUTPUT OF quantum_blockchain.py:
![image](https://github.com/Mayank-902/Quantum_Blockchain/assets/76254590/6d3764b6-580b-445f-84cd-55d338848f35)

# OUTPUT OF test_blockchain.py:

* Testing Simple blockchain:
  ![image](https://github.com/Mayank-902/Quantum_Blockchain/assets/76254590/9cb596c1-47e0-494c-95b2-89143c82473c)
  
* Testing Quantum blockchain:
  ![image](https://github.com/Mayank-902/Quantum_Blockchain/assets/76254590/1afdf03d-a55f-43a8-ac07-62aa6541e1a9)
