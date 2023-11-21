from os import system as s
s("cls")
import pandas as pd
import numpy as np

file = pd.read_csv('train.csv')

y = file['10']
x = file.drop(['10'], axis=1)

x_traspose  = np.transpose(x)

z = x_traspose  @ x
z_inverse = np.linalg.inv(z)
w = z_inverse @ x_traspose @ y
print(w.shape)
print(w)
np.savetxt("output", w)