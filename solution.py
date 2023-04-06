import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 451121038 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 1 - p
    ci = np.percentile(x, [1-alpha, alpha])
    return ci
