# https://nbviewer.jupyter.org/github/Qiskit/qiskit-tutorial/blob/master/qiskit/basics/getting_started_with_qiskit.ipynb

# Create the state:
# |\Psi> = (|000>+|111>) / \sqrt{2}

import numpy as np
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit import execute
from qiskit import BasicAer
from qiskit.tools.visualization import plot_state_city

backend = BasicAer.get_backend('statevector_simulator')

# Create a Quantum Register (with optional name 'q')
# ...with 3 qubits...
q = QuantumRegister(3, 'q')

# Create a Quantum Circuit acting on the q register...
circ = QuantumCircuit(q)

# Add a Hadamard gate H on qubit 0, which puts
# it into a superposition state...
circ.h(q[0])

# Add a CX(CNOT) gate (i.e. Controlled-Not operation or C_{x}) on control qubit 0 and target qubit 1, putting the qubits in a Bell state...
circ.cx(q[0], q[1])

# Add a CX(CNOT) gate on control qubit 0 and target qubit 2, putting the qubits in a GHZ state...
circ.cx(q[0], q[2])

print("Drawing the GHZ circuit...")
circ.draw()

print("Executing the GHZ circuit...")
job = execute(circ, backend)

result = job.result()

outputState = result.get_statevector(circ, decimals=3)
print("outputState =", outputState )
# e.g.,
# outputState =
# [
#   0.707+0.j
#   0.+0.j
#   0.+0.j
#   0.+0.j
#   0.+0.j
#   0.+0.j
#   0.+0.j
#   0.707+0.j
#]

# raise ImportError('Must have Matplotlib installed.')
#print("Plotting outputState via plot_state_city()...")
#plot_state_city(outputState)

print("Let off some steam, Bennett!")
