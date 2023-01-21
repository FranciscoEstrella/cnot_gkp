# cnot_gkp
Simulation of a teleported Controlled-NOT gate between GKP (Gottesman-Kitaev-Preskill) qubits for a modular arquitecture

Required software: 
-Strawberry Fields (from Xanadu)

folder name (last update)<br />
description<br />

1-trace_vs_cutoff (May 2022)<br />
-finding minimum cutoff for which 1-trace of output density matrices is less than 1*10^-3 . 
-negative and large probabilities (greater than 1) are found when using a cutoff larger than 40 in Strawberry Fields<br />


evaluate_in_TACC_cutoff=40 (Jul 2022)<br />
-workflow to compute the fidelity of output states from the teleported CNOT circuit and ideal CNOT circuit<br />
-TACC refers to UT Austin's supercomputer<br /> 
-a fixed cutoff of 40 is used, only one varying parameter (two-mode squeezing parameter) is explored<br />
-code is in main_programs folder<br />


evaluate_in_TACC_cutoff=40_AD (Jul 2022)<br />
-workflow to compute the fidelity of output states from the teleported CNOT circuit and ideal CNOT circuit<br />
-TACC refers to UT Austin's supercomputer <br />
-a fixed cutoff of 40 is used, only one varying parameter (two-mode squeezing parameter) is explored<br />
-only difference is that here amplitude damping (AD) is incorporated<br />
-code is in main_programs folder<br />


bosonic_fidelity_1_variable (Sep 2022)<br />
-workflow to compute the fidelity of output states from the teleported CNOT circuit and ideal CNOT circuit<br />
-fidelity is based on taking inner products of weighted linear combination of gaussians<br />
-only one varying parameter (squeezing parameter) is explored<br />


bosonic_fidelity_2_variables (Sep 2022)<br />
-workflow to compute the fidelity of output states from the teleported CNOT circuit and ideal CNOT circuit<br />
-fidelity is based on taking inner products of weighted linear combinations of gaussians<br />
-two varying parameters (squeezing parameter and epsilon) are explored<br />

report and presentation (December 2021)<br />
-report used as a deliverable for an experimental physics course<br />
-presentation targeted for quantum circuit research group at UT Austin<br />
