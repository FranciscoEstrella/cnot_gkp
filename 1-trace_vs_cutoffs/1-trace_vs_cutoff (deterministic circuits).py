import strawberryfields as sf
from strawberryfields.ops import *
import numpy as np
import time
import sys

t1=time.perf_counter()

#creates txt file with output
txt_file_title=input("(deterministic circuits) enter the name of the file (input state) ")
file_path = '/home/cnotgategkpstates/Desktop/1-trace_vs_cutoffs/data/deterministic_circuits_{}'.format(txt_file_title)
sys.stdout = open(file_path, "w")

#input gkp states parameters
gkpstate1=[0.0,0.0]
epsilon1=0.125
gkpstate2=[0.0,0.0]
epsilon2=0.125

#input coherent states parameters
alpha1 = 100
r1 = np.abs(alpha1)
phi1 = np.angle(alpha1)
alpha2 = 0.0
r2 = np.abs(alpha2)
phi2 = np.angle(alpha2)


#QGT circuit parameters
s=1
R2,PH2=-2.4,0.0

#cutoffs
cutoffs=[30,40,50,60,70,80,90,100]

#arrays to collect infidelity ("infidelity = 1 - trace")
infidelities_control=[]
infidelities_target=[]
infidelities2_control=[]
infidelities2_target=[]

#only states,no gates circuit
def circuit(cutoff):
    prog=sf.Program(2)
    with prog.context as q:

        #Coherent(r1,phi1)|q[0]
        #Coherent(r2,phi2)|q[1]

        GKP(gkpstate1,epsilon1) |q[0]
        GKP(gkpstate2,epsilon2) |q[1]

    eng=sf.Engine("bosonic")
    result=eng.run(prog)
    state=result.state
    control_dm=state.reduced_dm(0,cutoff=cutoff)
    target_dm=state.reduced_dm(1,cutoff=cutoff)
    infidelities_control.append(1-np.real_if_close(np.trace(control_dm)))
    infidelities_target.append(1-np.real_if_close(np.trace(target_dm)))

#CSUM circuit
def circuit2(cutoff):
    prog=sf.Program(2)
    with prog.context as q:

        #Coherent(r1,phi1)|q[0]
        #Coherent(r2,phi2)|q[1]

        GKP(gkpstate1,epsilon1) |q[0]
        GKP(gkpstate2,epsilon2) |q[1]

        #Rgate(np.pi/2)|q[0]
        #Rgate(np.pi/2)|q[1]

        #Pgate(1)|q[0]
        #Pgate(1)|q[1]

        CXgate(s) | (q[0],q[1])

    eng=sf.Engine("bosonic")
    result=eng.run(prog)
    state=result.state
    control_dm=state.reduced_dm(0,cutoff=cutoff)
    target_dm=state.reduced_dm(1,cutoff=cutoff)
    infidelities2_control.append(1-np.real_if_close(np.trace(control_dm)))
    infidelities2_target.append(1-np.real_if_close(np.trace(target_dm)))

for cutoff in cutoffs:
    cutoff=cutoff
    t3_1=time.perf_counter()
    circuit(cutoff)
    t3_2=time.perf_counter()
    t4_1=time.perf_counter()
    circuit2(cutoff)
    t4_2=time.perf_counter()
    print("cutoff={}".format(cutoff))
    print("time for only_states circuit with cutoff={} is {}".format(cutoff,t3_2-t3_1))
    print("time for CSUM circuit with cutoff={} is {}".format(cutoff,t4_2-t4_1))

print("only_states_no_gates_control_infidelities=",infidelities_control)
print("only_states_no_gates_target_infidelities=",infidelities_target)
print("CSUM_control_infidelities=",infidelities2_control)
print("CSUM_target_infidelities=",infidelities2_target)

t2=time.perf_counter()
print("time it took for the whole script in seconds is:",t2-t1)
