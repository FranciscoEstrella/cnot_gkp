import pickle
import statistics
import numpy as np

cutoffs=[40]
nprocs=32
totalruns=500
runs = np.arange(0,totalruns,1)
nparameters=25

#each key-pair in the following dictionaries contains the fidelity results for the corresponding cutoff. the fidelity results contain lists of the output of each rank
controlfidelities={}
targetfidelities={}

for j in range(len(cutoffs)):
    #file_path1='/home/cnotgategkpstates/Desktop/qgt_laptop/doublevacuum_AD/control_fidelity_results_{}'.format(cutoffs[j])
    file_path1='/home/cnotgategkpstates/Desktop/evaluate_in_TACC_cutoff=40_AD/received_from_TACC/control_fidelity_results_{}'.format(cutoffs[j])
    with open(file_path1, 'rb') as f:
        controlfidelities[j]=pickle.load(f)
    #file_path2='/home/cnotgategkpstates/Desktop/qgt_laptop/doublevacuum_AD/target_fidelity_results_{}'.format(cutoffs[j])
    file_path2='/home/cnotgategkpstates/Desktop/evaluate_in_TACC_cutoff=40_AD/received_from_TACC/target_fidelity_results_{}'.format(cutoffs[j])
    with open(file_path2, 'rb') as f:
        targetfidelities[j]=pickle.load(f)

# determine the size of each sub-task
ave, res = divmod(runs.size, nprocs)
counts = [ave + 1 if p < res else ave for p in range(nprocs)]

#this is where i combine the results from several ranks into a single list for each cutoff
combined_control_fidelities={}
for l in range(len(cutoffs)):
    combined_control_fidelities[l]=[]
    for j in range(nparameters):
            for k in range(nprocs):
                combined_control_fidelities[l]+=controlfidelities[l][k][counts[k]*j:counts[k]*j+counts[k]]

combined_target_fidelities={}
for l in range(len(cutoffs)):
    combined_target_fidelities[l]=[]
    for j in range(nparameters):
        for k in range(nprocs):
            combined_target_fidelities[l]+=targetfidelities[l][k][counts[k]*j:counts[k]*j+counts[k]]

avgfidelitiescontrol={}
sdfidelitiescontrol={}
for l in range(len(cutoffs)):
    avgfidelitiescontrol[l]=[]
    sdfidelitiescontrol[l]=[]
    for i in range(nparameters):
        avgfidelitiescontrol[l].append(statistics.mean(combined_control_fidelities[l][totalruns*i:totalruns*i+totalruns]))
        sdfidelitiescontrol[l].append(statistics.pstdev(combined_control_fidelities[l][totalruns*i:totalruns*i+totalruns]))

avgfidelitiestarget={}
sdfidelitiestarget={}
for l in range(len(cutoffs)):
    avgfidelitiestarget[l]=[]
    sdfidelitiestarget[l]=[]
    for i in range(nparameters):
        avgfidelitiestarget[l].append(statistics.mean(combined_target_fidelities[l][totalruns*i:totalruns*i+totalruns]))
        sdfidelitiestarget[l].append(statistics.pstdev(combined_target_fidelities[l][totalruns*i:totalruns*i+totalruns]))

for l in range(len(cutoffs)):
    #file_path1='/home/cnotgategkpstates/Desktop/qgt_laptop/doublevacuum_AD/average_control_fidelity_results_{}'.format(cutoffs[l])
    file_path1='/home/cnotgategkpstates/Desktop/evaluate_in_TACC_cutoff=40_AD/analyzed_data_and_results/average_control_fidelity_results_{}'.format(cutoffs[l])
    with open(file_path1, 'wb') as f:
        pickle.dump(avgfidelitiescontrol[l], f)
    #file_path1='/home/cnotgategkpstates/Desktop/qgt_laptop/doublevacuum_AD/sd_control_fidelity_results_{}'.format(cutoffs[l])
    file_path1='/home/cnotgategkpstates/Desktop/evaluate_in_TACC_cutoff=40_AD/analyzed_data_and_results/sd_control_fidelity_results_{}'.format(cutoffs[l])
    with open(file_path1, 'wb') as f:
        pickle.dump(sdfidelitiescontrol[l], f)
    #file_path2='/home/cnotgategkpstates/Desktop/qgt_laptop/doublevacuum_AD/average_target_fidelity_results_{}'.format(cutoffs[l])
    file_path2='/home/cnotgategkpstates/Desktop/evaluate_in_TACC_cutoff=40_AD/analyzed_data_and_results/average_target_fidelity_results_{}'.format(cutoffs[l])
    with open(file_path2, 'wb') as f:
        pickle.dump(avgfidelitiestarget[l], f)
    #file_path2='/home/cnotgategkpstates/Desktop/qgt_laptop/doublevacuum_AD/sd_target_fidelity_results_{}'.format(cutoffs[l])
    file_path2='/home/cnotgategkpstates/Desktop/evaluate_in_TACC_cutoff=40_AD/analyzed_data_and_results/sd_target_fidelity_results_{}'.format(cutoffs[l])
    with open(file_path2, 'wb') as f:
        pickle.dump(sdfidelitiestarget[l], f)
