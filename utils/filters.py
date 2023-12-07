from scipy.signal import butter, iirnotch, filtfilt
import numpy as np
import numpy.fft as fft



def butter_bandpass(lowcut,highcut,fs,order=5): 
    nyq = 0.5*fs 
    b,a = butter(order,[lowcut/nyq,highcut/nyq],btype='band',analog=False) 
    return b,a 

def butter_bandpass_filter(data,lowcut,highcut,fs,order=5): 
    b,a = butter_bandpass(lowcut,highcut,fs,order=order) 
    y = filtfilt(b,a,data) 
    return y 

def notch(notch_freq,samp_freq,quality_factor=30): 
    b,a = iirnotch(notch_freq,quality_factor,samp_freq) 
    return b,a 

def notch_filter(data,notch_fs,fs,q=30): 
    b,a = notch(notch_fs,fs,q) 
    y = filtfilt(b,a,data) 
    return y 

def filt_GRID(data,lowcut=20,highcut=500,fs=4000,order=3,notch_fs=50,notch_q=30): 
    filt_out = np.zeros_like(data) 
    for i in range(data.shape[0]): 
        filt_out[i,:] = notch_filter(butter_bandpass_filter(data[i,:],lowcut,highcut,fs, order=order),notch_fs,fs,notch_q) 
        return filt_out
    
def highpass(data, f_0=4000, f_stop=100):
    f_nyq = f_0 / 2
    n = data.shape[1]
    f_all = np.linspace(-f_nyq, f_nyq, n)
    x = fft.fft(data, axis=1)
    desired_response = np.ones(n)
    desired_response[abs(f_all)<=f_stop] = 0
    x_filtered = np.abs(fft.ifft(x * fft.fftshift(desired_response)));

    return x_filtered

