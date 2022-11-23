##original code got erased, but this would be analogous to the case with no amplitude damping

import pickle
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

cutoffs=[40]

avgcontrolfidelities={}
avgtargetfidelities={}
sdcontrolfidelities={}
sdtargetfidelities={}
for j in range(len(cutoffs)):
    file_path1='/home/cnotgategkpstates/Desktop/evaluate_in_TACC_cutoff=40/analyzed_data_and_results/average_control_fidelity_results_{}'.format(cutoffs[j])
    with open(file_path1, 'rb') as f:
        avgcontrolfidelities[j]=pickle.load(f)
    file_path1='/home/cnotgategkpstates/Desktop/evaluate_in_TACC_cutoff=40/analyzed_data_and_results/sd_control_fidelity_results_{}'.format(cutoffs[j])
    with open(file_path1, 'rb') as f:
        sdcontrolfidelities[j]=pickle.load(f)
    file_path2='/home/cnotgategkpstates/Desktop/evaluate_in_TACC_cutoff=40/analyzed_data_and_results/average_target_fidelity_results_{}'.format(cutoffs[j])
    with open(file_path2, 'rb') as f:
        avgtargetfidelities[j]=pickle.load(f)
    file_path2='/home/cnotgategkpstates/Desktop/evaluate_in_TACC_cutoff=40/analyzed_data_and_results/sd_target_fidelity_results_{}'.format(cutoffs[j])
    with open(file_path2, 'rb') as f:
        sdtargetfidelities[j]=pickle.load(f)

#Below are average fidelity plots vs two mode squeezing parameter (control mode)
nparameters=25
lastparameter=-2.4
parametersrange=np.flip(np.arange(lastparameter,0.1,0.1))

fig, axs = plt.subplots(3)
fig.suptitle('Fidelity in Control Mode for 00 GKP input state  \n vs Two-mode squeezing gate parameter')
for l in range(len(cutoffs)):
    axs[l].plot(parametersrange,avgcontrolfidelities[l])
    axs[l].set_title('Cutoff = {}'.format(cutoffs[l]))
    axs[l].invert_xaxis()
plt.tight_layout()
plt.show()

#Below are average fidelity plots vs two mode squeezing parameter (target mode)
fig, axs = plt.subplots(3)
fig.suptitle('Fidelity in Target Mode for 00 GKP input state  \n vs Two-mode squeezing gate parameter')
for l in range(len(cutoffs)):
    axs[l].plot(parametersrange,avgtargetfidelities[l])
    axs[l].set_title('Cutoff = {}'.format(cutoffs[l]))
    axs[l].invert_xaxis()
plt.tight_layout()
plt.show()

#below are log_10(infidelity) plots (control mode)
fig, axs = plt.subplots(3)
fig.suptitle('Log(1-fidelity) in Control Mode for 00 GKP input state  \n vs. Two-mode squeezing gate parameter')
for l in range(len(cutoffs)):
        yvalues=[]
        for value in avgcontrolfidelities[l]:
            yvalues.append(np.log10(1-value))
        axs[l].plot(parametersrange,yvalues)
        axs[l].set_title('Cutoff = {}'.format(cutoffs[l]))
        axs[l].invert_xaxis()
plt.tight_layout()
plt.show()

#below are log_10(infidelity) plots (target mode)
fig, axs = plt.subplots(3)
fig.suptitle('Log(1-fidelity) in Target Mode for 00 GKP input state \n vs. Two-mode squeezing gate parameter')
for l in range(len(cutoffs)):
        yvalues=[]
        for value in avgtargetfidelities[l]:
            yvalues.append(np.log10(1-value))
        axs[l].plot(parametersrange,yvalues)
        axs[l].set_title('Cutoff = {}'.format(cutoffs[l]))
        axs[l].invert_xaxis()
plt.tight_layout()
plt.show()
