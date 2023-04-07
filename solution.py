import pandas as pd
import numpy as np

from scipy.stats import uniform


chat_id = 451121038 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    loc = x.mean()
    b = 2 * loc - 0.083
    
    scale = np.sqrt(((b - a)**2) / 12) / np.sqrt(len(x))
    return b - scale * uniform.ppf(1 - alpha / 2), \
           b - scale * uniform.ppf(alpha / 2)
