import pandas as pd
import sqlite3
import os
import glob

# === 1. Визначаємо наші шляхи ===
# __file__ - зміна, яка зберігає шлях до цього файлу.
# os.path.abspath() - функція, яка перетворює шлях на абсолютний, тобто від диска аж до файлу (повний шлях).
# os.path.dirname - функція, яка виокремлює лише шлях до папки, де знаходиться файл. 
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(BASE_DIR)

# Шлях до папки з "сирими" CSV файлами
RAW_DATA_PATH = os.path.join(PROJECT_ROOT, 'data', 'raw')

# Шлях + ім'я для нашої НОВОЇ бази даних
DB_PATH = os.path.join(PROJECT_ROOT, 'data', 'interim', 'olist_database.db')

def create_database():
    """
    Знаходить всі .csv файли в папці data/raw
    і завантажує кожен у окрему таблицю в olist_database.db.
    """
    
    print(f"Starting database creation at: {DB_PATH}")
    
    # Створюємо з'єднання (connection) з нашою базою даних
    conn = sqlite3.connect(DB_PATH)
    
    # Знаходимо всі файли, які закінчуються на .csv у нашій папці
    csv_files = glob.glob(os.path.join(RAW_DATA_PATH, '*.csv'))
    
    if not csv_files:
        print(f"Error: No CSV files found in {RAW_DATA_PATH}")
        return

    print(f"Found {len(csv_files)} CSV files to load...")
    
    # Проходимося циклом по кожному CSV файлу
    for csv_file in csv_files:
        # Читаємо CSV у DataFrame
        df = pd.read_csv(csv_file)
        
        # Визначаємо ім'я для SQL-таблиці
        table_name = os.path.basename(csv_file).replace('.csv', '')
        
        # Записуємо дані з DataFrame прямо в нашу SQL базу даних
        df.to_sql(table_name, conn, if_exists='replace', index=False)
         
        print(f"Successfully loaded '{table_name}'")

    # Закриваємо з'єднання з базою даних
    conn.close()
    
    print("\nAll files loaded successfully into SQLite database.")

# Цей блок коду виконується ТІЛЬКИ якщо ти запускаєш цей файл напряму
if __name__ == "__main__":
    create_database()