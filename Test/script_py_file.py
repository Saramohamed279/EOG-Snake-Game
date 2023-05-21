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
from pylab import figure, clf, plot, xlabel, ylabel, title, grid, axes, show
from scipy.signal import find_peaks
import scipy.signal
import pickle
from scipy import signal
from scipy.signal import butter, filtfilt

import os

# Dataset Classes:
# ________________

script_dir = os.path.dirname(__file__)

# Yukari-->Up
# Asagi-->Down
# Sag-->Right
# Sol-->Left
# Kirp-->Blink
# Center ????
# what h and v reprenets ???


# Define the class labels
class_labels = {

    'yukarı': 0,
    'yukari': 0,
    'asagi': 1,
    'sag': 2,
    'sol': 3,
    'kirp': 4
}

class_names = {
    0: 'Up',
    1: 'Down',
    2: 'Right',
    3: 'Left',
    4: 'Blink'
}

h = []
classes = class_labels.keys()

test_data_2_dir = os.path.join(script_dir, '..', "Data", "test data 2.csv")
test_signals = os.path.join(script_dir, '..', "Data", "test signals2/*.txt")

# print(test_signals)

with open(test_data_2_dir, 'w') as csv_file:
    for filename in glob.glob(test_signals):
        # Get the class label from the filename

        # print(filename)
        h = filename.split('\\')[-1].split('.')[0]
        matches = re.split(r'(\d+)', h)
        # print(matches)

        if len(matches) == 5:
            # print(len(matches))
            if matches[2] in classes:
                if matches[4] == 'h':

                    # print(matches[2])

                    f = filename.replace('h', 'v')

                    try:
                        # print(f)
                        with open(f, 'r') as file:
                            # Read the contents of the file and split it into lines
                            lines_v = file.read()
                        lines_v = lines_v.replace('\n', ',')
                        for line in lines_v:
                            csv_file.write(line)
                        with open(filename, 'r') as file:
                            # Read the contents of the file and split it into lines
                            lines_h = file.read()
                        lines_h = lines_h.replace('\n', ',')
                        for line in lines_h:
                            csv_file.write(line)

                        label = class_labels[matches[2]]
                        csv_file.write(str(label) + '\n')
                    except FileNotFoundError:
                        pass

names = np.arange(0, 503)

test_data_dir = os.path.join(script_dir, '..', "Data", "test data.csv")
scalar_dir = os.path.join(script_dir, "scaler1.pkl")
svm_dir = os.path.join(script_dir, "svm.pkl")

# print(test_data_2_dir)

df = pd.read_csv(test_data_2_dir, names=names)
# print(df.head(10))
# define the desired order of the values
value_order = [1, 1, 3, 3, 1, 1, 3, 3, 1, 1, 4, 4, 1, 1, 2, 2, 1, 2, 2, 1, 4]

x = df.iloc[:, :-1]


def butter_bandpass_filter(Input_Signal, Low_Cutoff, High_Cutoff, Sampling_Rate, order):
    nyq = 0.5 * Sampling_Rate
    low = Low_Cutoff / nyq
    high = High_Cutoff / nyq
    Numerator, denominator = butter(order, [low, high], btype='band', output='ba', analog=False, fs=None)
    filtered = filtfilt(Numerator, denominator, Input_Signal)
    return filtered


def prepare(x):
    # Preprocessing
    filtered_signal = butter_bandpass_filter(x, Low_Cutoff=0.5, High_Cutoff=30.0, Sampling_Rate=176, order=2)
    resampled_Signal = []
    for i in filtered_signal:
        re_Sgnl = signal.resample(i, 60)
        resampled_Signal.append(re_Sgnl)
    Mean = [np.mean(resampled_Signal[i]) for i in range(len(resampled_Signal))]
    RemovedDC_signal = [(resampled_Signal[i] - Mean[i]) for i in range(len(resampled_Signal))]
    # Extract features
    coeffs = wavedec(RemovedDC_signal, 'db4', level=2)
    res = pywt.waverec([coeffs[0], coeffs[1]], 'db4')
    scaler = pickle.load(open(scalar_dir, 'rb'))
    X_test = scaler.transform(res)
    abc = pickle.load(open(svm_dir, 'rb'))
    ytest_pred_abc = abc.predict(X_test)
    return ytest_pred_abc


def get_predictions():
    return prepare(x)


print(get_predictions())
