import numpy as np
import mat73
import os
import matplotlib.pyplot as plt
from utils.filters import *


data_root = './raw_data/'

filename = 'steady force 1.mat'

data = mat73.loadmat(os.path.join(data_root, filename))
data_mat = data['out_mat']
data_bandpass = np.abs(filt_GRID(data_mat))
# data_highpass = highpass(data_mat)

fig, ax = plt.subplots(1, 2, tight_layout=True, figsize=(20, 5))
ax = ax.flatten()
ax[0].plot(data_mat[0])
ax[0].set_title('Orginal data')
# plt.ylim((-50, 100))
ax[1].plot(data_bandpass[0])
ax[1].set_title('Filtered data')
plt.savefig('preprocess.png')
plt.show()
print(data_mat.shape)
print(data_filtered.shape)
