import pickle

import matplotlib.pyplot as plt

import numpy as np

file_path='/home/cnotgategkpstates/Desktop/bosonic_fidelity_1_variable/qgt_data/'
file_name='qgt_average_means_fidelity'
with open(file_path+file_name, 'rb') as f:
    average_means_fidelity=pickle.load(f)

file_path='/home/cnotgategkpstates/Desktop/bosonic_fidelity_1_variable/qgt_data/'
file_name='qgt_average_covariance_fidelity'
with open(file_path+file_name, 'rb') as f:
    average_covariance_fidelity=pickle.load(f)

last_squeezing_parameter=-0.2
squeezing_parameters=np.flip(np.arange(last_squeezing_parameter,0.1,0.1))

fig, axs = plt.subplots(2)
fig.suptitle('means and covariance fidelities')
axs[0].plot(squeezing_parameters,average_means_fidelity)
axs[0].set(xlabel='two-mode squeezing parameter', ylabel='mean fidelity',title='first plot')
axs[0].invert_xaxis()
axs[0].grid()
axs[1].plot(squeezing_parameters,average_covariance_fidelity)
axs[1].set(xlabel='two-mode squeezing parameter', ylabel='covariance fidelity',title='second plot')
axs[1].invert_xaxis()
axs[1].grid()
plt.tight_layout()
plt.show()
