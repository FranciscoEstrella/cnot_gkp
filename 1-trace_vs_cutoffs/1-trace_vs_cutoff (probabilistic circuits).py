import strawberryfields as sf
from strawberryfields.ops import *
import numpy as np
import time
import sys

t1=time.perf_counter()

#creates txt file with output
txt_file_title=input("(probabilistic circuits) enter the name of the file (input state) ")
file_path = '/home/cnotgategkpstates/Desktop/1-trace_vs_cutoffs/data/probabilistic_circuits_{}'.format(txt_file_title)
sys.stdout = open(file_path, "w")

#input gkp states parameters
gkpstate1=[0.0,0.0]
epsilon1=0.125
gkpstate2=[0.0,0.0]
epsilon2=0.125

#input coherent states parameters
alpha1 = 10
r1 = np.abs(alpha1)
phi1 = np.angle(alpha1)
alpha2 = -10
r2 = np.abs(alpha2)
phi2 = np.angle(alpha2)

#QGT circuit parameters
s=1
R2,PH2=-2.4,0.0

#AD parameters
Td_coherence= 100e-6 #coherence time data modes
Tc_coherence= 100e-6 #coherence time communication modes

time1=1e-6 #time to determine parameter on data qubits before any gate
time_CSUM=1e-6 #time to implement CSUM gate
time_2MSG=1e-6 #time to implement 2 mode squeezing gate
time_measurement=1e-6 #time to implement measurements

Td_1=np.exp(-time1/Td_coherence) #data qubits before CSUM
Td_2=np.exp(-time_CSUM/Td_coherence) #data qubits after CSUM
Td_3=np.exp(-time_measurement/Td_coherence) #data qubits after the measurements (on communication qubits) and before displacements

Tc_1=np.exp(-time_2MSG/Tc_coherence)#communication qubits after 2mode squeezing gate and before CSUM
Tc_2=np.exp(-time_CSUM/Tc_coherence) #communication qubits after CSUM

#cutoffs and runs in each cutoff
cutoffs=[30,40,50,60,70,80,90,100]
runs=30

#arrays to collect infidelity ("infidelity" = 1 - trace)
infidelities3_control=[]
infidelities3_target=[]
infidelities4_control=[]
infidelities4_target=[]

#QGT circuit
def circuit3(cutoff):
    prog=sf.Program(4)
    with prog.context as q:

        Coherent(r1,phi1) | q[0]
        Coherent(r2,phi2) | q[3]

        #GKP(gkpstate1,epsilon1) |q[0]
        #GKP(gkpstate2,epsilon2) |q[3]

        S2gate(R2,PH2) | (q[1],q[2])

        CXgate(s) | (q[0],q[1])
        CXgate(s) | (q[2],q[3])

        MeasureX | q[1]
        MeasureP | q[2]

        Xgate(s*q[1].par) | q[3]
        Zgate(s*q[2].par) | q[0]

    eng=sf.Engine("bosonic")
    result=eng.run(prog)
    state=result.state
    control_dm=state.reduced_dm(0,cutoff=cutoff)
    target_dm=state.reduced_dm(3,cutoff=cutoff)
    infidelities3_control.append(1-np.real_if_close(np.trace(control_dm)))
    infidelities3_target.append(1-np.real_if_close(np.trace(target_dm)))

#QGT citcuit AD
def circuit4(cutoff):
    prog=sf.Program(4)
    with prog.context as q:
        Coherent(r1,phi1) | q[0]
        Coherent(r2,phi2) | q[3]

        #GKP(gkpstate1,epsilon1) |q[0]
        #GKP(gkpstate2,epsilon2) |q[3]

        LossChannel(Td_1)|q[0]
        LossChannel(Td_1)|q[3]

        S2gate(R2,PH2) | (q[1],q[2])

        LossChannel(Tc_1)|q[1]
        LossChannel(Tc_1)|q[2]

        CXgate(s) | (q[0],q[1])
        CXgate(s) | (q[2],q[3])

        LossChannel(Td_2) | q[0]
        LossChannel(Td_2) | q[3]

        LossChannel(Tc_2) | q[1]
        LossChannel(Tc_2) | q[2]

        MeasureX | q[1]
        MeasureP | q[2]

        LossChannel(Td_3)|q[0]
        LossChannel(Td_3)|q[3]

        Xgate(s*q[1].par) | q[3]
        Zgate(s*q[2].par) | q[0]

    eng=sf.Engine("bosonic")
    result=eng.run(prog)
    state=result.state
    control_dm=state.reduced_dm(0,cutoff=cutoff)
    target_dm=state.reduced_dm(3,cutoff=cutoff)
    infidelities4_control.append(1-np.real_if_close(np.trace(control_dm)))
    infidelities4_target.append(1-np.real_if_close(np.trace(target_dm)))

for cutoff in cutoffs:
    cutoff=cutoff
    for i in range(runs):
        t3_1=time.perf_counter()
        circuit3(cutoff)
        t3_2=time.perf_counter()
        t4_1=time.perf_counter()
        circuit4(cutoff)
        t4_2=time.perf_counter()
        print("cutoff={}".format(cutoff))
        print("time for QGT circuit with cutoff={} is {}".format(cutoff,t3_2-t3_1))
        print("time for QGT AD circuit with cutoff={} is {}".format(cutoff,t4_2-t4_1))

print("QGT_control_infidelities=",infidelities3_control)
print("QGT_target_infidelities=",infidelities3_target)
print("QGT_AD_control_infidelities=",infidelities4_control)
print("QGT_AD_target_infidelities=",infidelities4_target)

t2=time.perf_counter()
print("time it took for the whole script in seconds is:",t2-t1)