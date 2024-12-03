import sqlite3
import pandas as pd


def createTable():
    conn = sqlite3.connect('../database/mydatabase.db')
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS bron_stolik(
        people_name TEXT,
        day TEXT,
        time TEXT,
        people INTEGER,
        window TEXT,
        people_id INTEGER
    )
    """)
    conn.commit()
    conn.close()


def insertIntoToTable(people_name, day, time, people, window, people_id):
    conn = sqlite3.connect('../database/mydatabase.db')
    cur = conn.cursor()
    cur.execute("""
    INSERT INTO bron_stolik(people_name, day, time, people, window, people_id) VALUES (?, ?, ?, ?, ?, ?)
    """, (people_name, day, time, people, window, people_id))
    conn.commit()
    conn.close()


def activeBronSelect():
    conn = sqlite3.connect('../database/mydatabase.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM bron_stolik")
    rows = cur.fetchall()
    conn.close()

    # Убедитесь, что порядок колонок соответствует структуре таблицы в базе данных
    df = pd.DataFrame(rows, columns=['People Name', 'Day', 'Time', 'People', 'Wishes', 'Player ID'])
    return df

    # Получаем все строки результата
    # rows = cur.fetchall()
    #
    # # Список для хранения результатов
    # results = []
    #
    # # Проходим по каждой строке и выводим данные
    # for row in rows:
    #     day = row[0]
    #     time = row[1]
    #     people = row[2]
    #     wishes = row[3]
    #
    #     # Добавляем данные в список
    #     results.append({
    #         'day': day,
    #         'time': time,
    #         'people': people,
    #         'wishes': wishes
    #     })

    # Закрываем соединение с базой данных
    # Возвращаем все результаты
