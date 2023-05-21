import glob
import re
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pywt import wavedec
import pywt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
from sklearn import metrics
from sklearn.metrics import confusion_matrix
from mlxtend.plotting import plot_confusion_matrix
import scipy.integrate as integrate
from statsmodels.tsa.ar_model import AutoReg
from pylab import figure,clf,plot,xlabel,ylabel,title,grid,axes,show
from scipy.signal import find_peaks
import scipy.signal
import pickle
from scipy import signal
from scipy.signal import butter, filtfilt

import os
# Dataset Classes:
# ________________

# Yukari-->Up
# Asagi-->Down
# Sag-->Right
# Sol-->Left
# Kirp-->Blink
# Center ????
# what h and v reprenets ???
class_names = {
    0: 'Up',
    1: 'Down',
    2: 'Right',
    3: 'Left',
    4: 'Blink'
}

names= np.arange(0,503)

script_dir = os.path.dirname( __file__ )
test_data_dir = os.path.join( script_dir, '..', "Data", "test data.csv")
scalar_dir = os.path.join( script_dir, "scaler1.pkl")
svm_dir = os.path.join( script_dir, "svm.pkl")

print(test_data_dir)

df = pd.read_csv(test_data_dir, names=names)

x=df.iloc[:,:-1]

def butter_bandpass_filter(Input_Signal, Low_Cutoff, High_Cutoff,Sampling_Rate, order):
    nyq = 0.5*Sampling_Rate
    low=Low_Cutoff/nyq
    high =High_Cutoff/nyq
    Numerator, denominator = butter(order,[low,high],btype='band', output='ba',analog=False, fs=None)
    filtered = filtfilt(Numerator,denominator,Input_Signal)
    return filtered

def prepare(x):
    # Preprocessing
    filtered_signal = butter_bandpass_filter(x,Low_Cutoff=0.5,High_Cutoff=30.0,Sampling_Rate=176,order=2)
    resampled_Signal = []
    for i in filtered_signal:
        re_Sgnl = signal.resample(i,60)
        resampled_Signal.append(re_Sgnl)
    Mean=[np.mean(resampled_Signal[i]) for i in range(len(resampled_Signal))]
    RemovedDC_signal=[(resampled_Signal[i]-Mean[i]) for i in range (len(resampled_Signal))]
    # Extract features
    coeffs = wavedec(RemovedDC_signal , 'db4', level = 2)
    res = pywt.waverec([coeffs[0],coeffs[1]],'db4')
    scaler=pickle.load(open(scalar_dir, 'rb'))
    X_test=scaler.transform(res)
    abc = pickle.load(open(svm_dir, 'rb'))
    ytest_pred_abc=abc.predict(X_test)
    return ytest_pred_abc


def get_predictions():
    return prepare(x)


# print(get_predictions())