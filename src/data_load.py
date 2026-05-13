import pandas as pd
import os

def load_data():
    # Шлях до файлу відносно кореня проєкту
    file_path = 'data/raw/data.csv'
    
    if os.path.exists(file_path):
        try:
            # Спробуємо завантажити дані з автовизначенням розділювача
            df = pd.read_csv(file_path, encoding='utf-8', sep=None, engine='python')
        except:
            # Якщо utf-8 не підійшов (часто для укр. даних), пробуємо Windows-1251
            df = pd.read_csv(file_path, encoding='cp1251', sep=None, engine='python')
        
        print("--- Модуль завантаження: Успіх ---")
        print(f"Завантажено рядків: {len(df)}")
        print("Перші 5 рядків даних:")
        print(df.head())
        return df
    else:
        print(f"Помилка: Файл {file_path} не знайдено!")
        return None

if __name__ == "__main__":
    load_data()