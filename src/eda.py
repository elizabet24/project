"""EDA-пайплайн для временного ряда кредитного риска.

Заполняется в лабораторных 4–6.
"""

import os
import pandas as pd

def load_data(path: str) -> pd.DataFrame:
    """Загрузка данных из CSV.
    
    Args:
        path (str): Путь к файлу.
    Returns:
        pd.DataFrame: Загруженный датасет.
    """
    if not os.path.exists(path):
        raise FileNotFoundError(f"Файл не найден: {path}")
    
    df = pd.read_csv(path)
    print(f"Данные загружены. Размер: {df.shape}")
    return df


def describe(df):
    """Описательная статистика."""
    pass


def plot_series(df, column: str):
    """Визуализация временного ряда."""
    pass
