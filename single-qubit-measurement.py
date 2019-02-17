# https://nbviewer.jupyter.org/github/Qiskit/qiskit-tutorial/blob/master/qiskit/basics/getting_started_with_qiskit.ipynb
# Single Qubit Measurement
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, execute, Aer

# Define the Quantum and Classical Registers
q = QuantumRegister(1)
c = ClassicalRegister(1)

# Build the circuit
single_q_measurement = QuantumCircuit(q, c)
single_q_measurement.measure(q, c)

# Execute the circuit
job = execute(sinqle_q_measurement, backend = Aer.get_backend('qasm_simulator'), shots=1024)
result = job.result()

# Print the result
print(result.get_counts(single_q_measurement))
