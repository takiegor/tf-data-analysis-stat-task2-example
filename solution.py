import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 123456 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    n = len(x)
    t = np.abs (np.random.standard_t(df = n-1, size = 100000))
    std_error = np.std (x, ddof = 1) / np.sqrt(n)
    margin_of_error = t[np.searchsorted(np.sort(t), 1-(1-p)/2)] * std_error
    return (np.mean(x) - margin_of_error, np.mean(x) + margin_of_error)
