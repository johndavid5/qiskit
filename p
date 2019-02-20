set -x
# python single-qubit-measurement.py 2>&1 | tee p.out
python ghz-circuit.py 2>&1 | tee p.out
set +x
