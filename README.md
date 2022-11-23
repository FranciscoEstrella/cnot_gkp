# cnot_gkp
simulating a CNOT gate between GKP qubits in a modular arquitecture

folder name (last update)
description


1-trace_vs_cutoff (May 2022)
-finding minimum cutoff for which 1-trace of output density matrices is less than 1*10^-3 . this is where the negative and huge probabilities were found after cutoff=40 


evaluate_in_TACC_cutoff=40 (Jul 2022)
-workflow to compute the fidelity of output states from the teleported CNOT circuit and ideal CNOT circuit
- TACC refers to UT Austin's supercomputer 
-a fixed cutoff of 40 is used, only one varying parameter (squeezing parameter) is explored
-code is in main_programs folder


evaluate_in_TACC_cutoff=40_AD (Jul 2022)
-workflow to compute the fidelity of output states from the teleported CNOT circuit and ideal CNOT circuit
- TACC refers to UT Austin's supercomputer 
-a fixed cutoff of 40 is used, only one varying parameter (squeezing parameter) is explored
-only difference is that here amplitude damping (AD) is incorporated
-code is in main_programs folder


bosonic_fidelity_1_variable (Sep 2022)
-workflow to compute the fidelity of output states from the teleported CNOT circuit and ideal CNOT circuit
-fidelity is based on taking inner products of weighted linear combination of gaussians
-only one varying parameter (squeezing parameter) is explored


bosonic_fidelity_2_variables (Sep 2022)
-workflow to compute the fidelity of output states from the teleported CNOT circuit and ideal CNOT circuit
-fidelity is based on taking inner products of weighted linear combinations of gaussians
-two varying parameters (squeezing parameter and epsilon) are explored

report and presentation (December 2021)
-report used as a deliverable for an experimental physics course
-presentation targeted for quantum circuit research group at UT Austin
