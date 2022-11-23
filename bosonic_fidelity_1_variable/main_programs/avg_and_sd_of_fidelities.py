import pickle

import numpy as np

import statistics

#variables i would have to know in advance
##number of circuit runs
##number of parameters of each varying parameter
#for this case i have
total_epsilon_parameters=3
total_R2_parameters=4
total_processes=6
total_runs=18
runs = np.arange(0,total_runs,1)

file_path='/home/cnotgategkpstates/Desktop/bosonic_fidelity_1_variable/qgt_data/'
file_name='qgt_means_fidelity'
with open(file_path+file_name, 'rb') as f:
    means_fidelity=pickle.load(f)
print(means_fidelity)
print(len(means_fidelity))
print(len(means_fidelity[0]))

'''file_path='/home/cnotgategkpstates/Desktop/bosonic_fidelity_2_variable/qgt_data/'
file_name='qgt_covariance_fidelity'
with open(file_path+file_name, 'rb') as f:
    covariance_fidelity=pickle.load(f)
#print(covariance_fidelity)'''


#the following is needed to know which runs to gather from each processor 
ave, res = divmod(runs.size, total_processes)
counts = [ave + 1 if p < res else ave for p in range(total_processes)]

print(counts)

#the following is used to create a different array that collects all circuit runs' results for each parameter
updated_means_fidelity=[]
updated_covariance_fidelity=[]
for k in range(total_R2_parameters):
    updated_means_fidelity.append([])
    updated_covariance_fidelity.append([])


#i don't fully understand this part but it's working
for i in range(total_R2_parameters):
    for j in range(total_processes):
        print(means_fidelity[j][counts[j]*i:counts[j]*i+counts[j]])
        updated_means_fidelity[i]+=means_fidelity[j][counts[j]*i:counts[j]*i+counts[j]]
        #updated_covariance_fidelity[i]+=covariance_fidelity[j][counts[j]*i:counts[j]*i+counts[j]]

#print(counts)
#print(means_fidelity)
#print(updated_means_fidelity)

average_means_fidelity=[]
average_covariance_fidelity=[]
for list in updated_means_fidelity:
    average_means_fidelity.append(statistics.mean(list))
#for list in updated_covariance_fidelity:
    #average_covariance_fidelity.append(statistics.mean(list))
##i'd then do the same thing to compute standard deviation


print(len(average_means_fidelity))
print(average_means_fidelity)


'''file_path='/home/cnotgategkpstates/Desktop/fidelity_2+_variables/qgt_data/'
file_name='qgt_average_means_fidelity'
with open(file_path+file_name, 'wb') as f:
    pickle.dump(average_means_fidelity, f)
file_path='/home/cnotgategkpstates/Desktop/fidelity_2+_variables/qgt_data/'
file_name='qgt_average_covariance_fidelity'
with open(file_path+file_name, 'wb') as f:
    pickle.dump(average_covariance_fidelity, f)
'''

#missing standard deviations