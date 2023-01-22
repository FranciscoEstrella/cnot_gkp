# cnot_gkp
Simulation of a teleported Controlled-NOT gate between GKP (Gottesman-Kitaev-Preskill) qubits for a modular superconducting arquitecture (https://www.nature.com/articles/s41586-018-0470-y)

Required software:<br />
-Python3.7 (or greater)<br />
-Strawberry Fields (from Xanadu)<br />

1-trace_vs_cutoffs<br />
-finding minimum cutoff for which 1-trace of output density matrices is less than 1*10^-3<br /> 
-negative and large probabilities (greater than 1) are found when using a cutoff larger than 40 in Strawberry Fields<br />

wlcg_fidelity_1_varying_parameter<br />
-workflow to compute fidelity of output states between teleported CNOT circuit and ideal CNOT circuit<br />
-fidelity is based on inner products of weighted linear combination of gaussians (wlcg) <br />
-only one parameter varies in the computation of fidelity (two-mode squeezing parameter)<br />


wlcg_fidelity_2_varying_parameters<br />
-workflow to compute fidelity of output states between teleported CNOT circuit and ideal CNOT circuit<br />
-fidelity is based on inner products of weighted linear combination of gaussians (wlcg)<br />
-two parameter vary in the computation of fidelity (two-mode squeezing parameter, GKP epsilon)<br />


number_distribution_fidelity_1_varying_parameter<br />
-workflow to compute fidelity of output states between teleported CNOT circuit and ideal CNOT circuit<br />
-a cutoff of 40 is used, and only one varying parameter is used (two-mode squeezing parameter)<br />
-main_programs directory contains essential code<br />
-TACC is UT Austin's cluster computer<br /> 


deliverables<br />
-taccster poster was used in TACC high performance computing symposium (September 2022)<br />
-Teleported CNOT Gate between GKP Qubits-presentation was used to present an update of project to quantum-circuits research group<br />
-Teleported CNOT Gate between GKP Qubits-report was used to present an update of project<br />
