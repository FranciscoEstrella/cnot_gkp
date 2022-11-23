#import modules
import strawberryfields as sf
from strawberryfields.ops import *

import numpy as np

import sys

import pickle

#should define name of output txt file (with any possible issues or relevant notes) as well as name of pickle file with linear combinations of gaussians results 
##and can also define the folder(s) to save both files

#output txt file (maybe not necessary)
file_path = '/home/cnotgategkpstates/Desktop/bosonic_fidelity_2_variables/csum_data/'
file_name= 'csum_output'
sys.stdout = open(file_path+file_name, "w")

#circuit parameters in this order: , fixed parameters: input states (gkp and coherent), cutoff, csum parameter, squeezing gate, amplitude damping, , varying parameters: squeezing gate, number of runs and distributions to processes

th_control, ph_control=0.0,0.0
gkp_control=[th_control,ph_control]
epsilon_control=0.120

th_target,ph_target=0.0,0.0
gkp_target=[th_target,ph_target]
epsilon_target=0.120

control_alpha=0.0
r_control = np.abs(control_alpha)
phi_control = np.angle(control_alpha)

target_alpha=0.0
r_target = np.abs(target_alpha)
phi_target = np.angle(target_alpha)

s=1
sf.hbar=1

#directory with parameters to pass onto the circuits' functions


####below is what is not working yet####

'''
#the array below will collect normalized vectors of means (in the [0] list), normalized cov matrices (in the [1] list),
# and the real part of the weight (in the [2] list) (the imaginary part is always 0)
def normalize_gaussians(data): #it is assumed that data is a tuple
    number_of_gaussians=len(data[0])
    normalized_csum_data=[[],[],[]]
    for i in range(number_of_gaussians):
        normalization_factor=np.sqrt(np.dot(np.conjugate(data[0][i]),data[0][i]))
        if normalization_factor==0:
            normalization_factor=1
        normalized_csum_data[0].append(list([1/normalization_factor*i for i in data[0][i]]))

        normalization_factor=np.sqrt(np.dot(np.conjugate(data[1][i][0]),data[1][i][0])+np.dot(np.conjugate(data[1][i][1]),data[1][i][1])+np.dot(np.conjugate(data[1][i][2]),data[1][i][2])+np.dot(np.conjugate(data[1][i][3]),data[1][i][3]))
        data[1][i][0]=[1/normalization_factor*i for i in data[1][i][0]]
        data[1][i][1]=[1/normalization_factor*i for i in data[1][i][1]]
        data[1][i][2]=[1/normalization_factor*i for i in data[1][i][2]]
        data[1][i][3]=[1/normalization_factor*i for i in data[1][i][3]]
        normalized_csum_data[1].append(data[1][i].tolist())

        normalized_csum_data[2].append(np.real(data[2][i]))

        data=normalized_csum_data
        return data

def csum_circuit(): #function of parameters in a dictionary
    prog=sf.Program(2)
    with prog.context as q:
        GKP(gkp_control,epsilon_control) |q[0]
        GKP(gkp_target,gkp_target) |q[1]

        #Coherent(r1,phi1) | q[0]
        #Coherent(r2,phi2) | q[1]

        CXgate(s) | (q[0],q[1])

    #The string parameter inside sf.Engine selects the backend to run the circuit and the output state is stored in the variable "state".
    #data contains the full information about the state (all vectors of means, covariance matrices, and weights, of the gaussians making the linear combination)
    eng=sf.Engine("bosonic")
    result=eng.run(prog)
    state=result.state
    data=state.data

    normalized_csum_data=normalize_gaussians(data)

    return normalized_csum_data

results=csum_circuit()

'''
####below is what works now####

prog=sf.Program(2)
with prog.context as q:
    GKP(gkp_control,epsilon_control) |q[0]
    GKP(gkp_target,epsilon_target) |q[1]

    #Coherent(r_control,phi_control) | q[0]
    #Coherent(r_target,phi_target) | q[1]

    CXgate(s) | (q[0],q[1])

#The string parameter inside sf.Engine selects the backend to run the circuit and the output state is stored in the variable "state".
#data contains the full information about the state (all vectors of means, covariance matrices, and weights, of the gaussians making the linear combination)
eng=sf.Engine("bosonic")
result=eng.run(prog)
state=result.state
data=state.data

#the array below will collect normalized vectors of means (in the [0] list), normalized cov matrices (in the [1] list),
# and the real part of the weight (in the [2] list) (the imaginary part is always 0)

number_of_gaussians=len(data[0])
normalized_csum_data=[[],[],[]]
for i in range(number_of_gaussians):
    normalization_factor=np.sqrt(np.dot(np.conjugate(data[0][i]),data[0][i]))
    if normalization_factor==0:
        normalization_factor=1
    normalized_csum_data[0].append(list([1/normalization_factor*i for i in data[0][i]]))

    normalization_factor=np.sqrt(np.dot(np.conjugate(data[1][i][0]),data[1][i][0])+np.dot(np.conjugate(data[1][i][1]),data[1][i][1])+np.dot(np.conjugate(data[1][i][2]),data[1][i][2])+np.dot(np.conjugate(data[1][i][3]),data[1][i][3]))
    data[1][i][0]=[1/normalization_factor*i for i in data[1][i][0]]
    data[1][i][1]=[1/normalization_factor*i for i in data[1][i][1]]
    data[1][i][2]=[1/normalization_factor*i for i in data[1][i][2]]
    data[1][i][3]=[1/normalization_factor*i for i in data[1][i][3]]
    normalized_csum_data[1].append(data[1][i].tolist())

    normalized_csum_data[2].append(np.real(data[2][i]))

#export results
file_path = '/home/cnotgategkpstates/Desktop/bosonic_fidelity_2_variables/csum_data/'
file_name= 'csum_data_e=0.120' #maybe include a varying function to change name of output files depending on parameters
with open(file_path+file_name, 'wb') as f:
    pickle.dump(normalized_csum_data, f)
