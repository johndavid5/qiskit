// https://nbviewer.jupyter.org/github/Qiskit/qiskit-tutorial/blob/master/qiskit/basics/getting_started_with_qiskit.ipynb
//Single Qubit Measurement
OPENQASM 2.0;
include "qelib1.inc";

// Register declarations
qreg q[1];
creg c[1];

// Quantum Circuit
measure q -> c;
