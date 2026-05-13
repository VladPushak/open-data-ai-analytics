import pandas as pd
import os

def run_eda():
    # Шлях до твого файлу з даними
    file_path = 'data/raw/data.csv'
    
    if not os.path.exists(file_path):
        print(f"Помилка: Файл {file_path} не знайдено!")
        return

    # Завантажуємо дані (використовуємо кодування cp1251 для української мови)
    try:
        df = pd.read_csv(file_path, encoding='cp1251', sep=None, engine='python')
    except:
        df = pd.read_csv(file_path, encoding='utf-8', sep=None, engine='python')

    print("="*30)
    print("РОЗВІДУВАЛЬНИЙ АНАЛІЗ (EDA)")
    print("="*30)
    
    # 1. Скільки всього записів
    print(f"Усього навчальних закладів у базі: {len(df)}")

    # 2. Перевірка колонок
    print("\nДоступні дані (колонки):")
    print(df.columns.tolist())

    # 3. Перевірка Гіпотези №1 (Типи закладів)
    # Шукаємо колонку, яка схожа на "Тип" або "Форма власності"
    possible_cols = ['Тип', 'Форма власності', 'Назва'] 
    for col in df.columns:
        if any(word in col for word in possible_cols):
            print(f"\nРозподіл за колонкою '{col}':")
            print(df[col].value_counts().head(10))
            break
    
    # 4. Перевірка Гіпотези №3 (Пропуски в контактах)
    print("\nАналіз пропущених значень (NaN):")
    print(df.isnull().sum().head(10))

if __name__ == "__main__":
    run_eda()