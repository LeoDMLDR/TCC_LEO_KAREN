import pywt

wavelet = 'bior1.1'
level = 2

def wavelet_tranf(signal):
    coeffs = pywt.wavedec(signal, wavelet, level=level)
    return coeffs