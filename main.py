from wavelet_transform import *
from tratamento_dados import *
import tkinter as tk

txt_file_name = 'REP0101.TXT'

A3e, A3d, CA1e, CA1d=tratamento_dados(txt_file_name)

A3e_wavelet = wavelet_tranf(A3e)
A3d_wavelet = wavelet_tranf(A3d)
CA1e_wavelet = wavelet_tranf(CA1e)
CA1d_wavelet = wavelet_tranf(CA1d)

print(A3e_wavelet)