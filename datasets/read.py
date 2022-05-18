import scipy.io

dict = scipy.io.loadmat("cpsd_ch1.mat")
X = dict['X'] # Признаки 
Y = dict['Y'] # Индекс устройства