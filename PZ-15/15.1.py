
'''приложение грузовые перевозки ддя некоторой организации бд должна содержать таблицу перевозки со след структурой записи маршрут
фамилия даты отправки и прибытие масса груза'''


import sqlite3 as sq

with sq.connect('tv.db') as con:
    con.execute('PRAGMA foreign_keys = ON')
    cur = con.cursor()


    cur.execute('''CREATE TABLE Perevozki (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                route TEXT,
                driver TEXT,
                dep_date TEXT,
                arr_date TEXT,
                weight REAL)
                ''')
    def add_data():
        sample_data = [
            ("Москва - СПб", "Иванов", "2026-06-01", "2026-06-02", 15.5),
            ("Казань - Москва", "Петров", "2026-06-03", "2026-06-04", 8.2),
            ("Краснодар - Сочи", "Сидоров", "2026-06-05", "2026-06-05", 3.0),
            ("Екатеринбург - Тюмень", "Иванов", "2026-06-06", "2026-06-07", 12.0),
            ("Москва - Воронеж", "Козлов", "2026-06-08", "2026-06-09", 18.1),
            ("Самара - Саратов", "Смирнов", "2026-06-10", "2026-06-11", 5.5),
            ("Ростов - Волгоград", "Морозов", "2026-06-12", "2026-06-13", 9.0),
            ("Уфа - Челябинск", "Новиков", "2026-06-14", "2026-06-15", 14.2),
            ("Нижний Новгород - Владимир", "Петров", "2026-06-16", "2026-06-16", 4.5),
            ("Пермь - Ижевск", "Павлов", "2026-06-17", "2026-06-18", 11.0)
        ]
        cur.executemany('''
            INSERT INTO Perevozki (route, driver, dep_date, arr_date, weight)
            VALUES (?, ?, ?, ?, ?)
        ''', sample_data)
        con.commit()
        print("10 записей успешно добавлены в базу данных")


    def show_all_data():
        print("\nВСЕ ДАННЫЕ В БАЗЕ:")
        cur.execute("SELECT * FROM Perevozki")
        for row in cur.fetchall():
            print(row)


    # Ищем по фамилии водителя
    def search_by_driver(driver_name):
        cur.execute("SELECT * FROM Perevozki WHERE driver = ?", (driver_name,))
        print(f"\nНайденные рейсы для водителя '{driver_name}':")
        for row in cur.fetchall():
            print(row)


    # Ищем по массе груза, которая больше указанного значения
    def search_by_weight_greater(min_weight):
        cur.execute("SELECT * FROM Perevozki WHERE weight > ?", (min_weight,))
        print(f"\nНайденные рейсы с массой груза > {min_weight}т:")
        for row in cur.fetchall():
            print(row)


    # Ищем по диапазону дат отправления
    def search_by_departure_date_range(start_date, end_date):
        cur.execute("SELECT * FROM Perevozki WHERE dep_date BETWEEN ? AND ?", (start_date, end_date))
        print(f"\nНайденные рейсы с датой отправления с {start_date} по {end_date}:")
        for row in cur.fetchall():
            print(row)


    #  Функции изменения (3 разных запроса)
    # Изменение массы груза по ID
    def update_weight_by_id(trip_id, new_weight):
        cur.execute("UPDATE Perevozki SET weight = ? WHERE id = ?", (new_weight, trip_id))
        con.commit()
        print(f"\nМасса груза для ID {trip_id} изменена на {new_weight}т.")


    # Изменение фамилии водителя по маршруту
    def update_driver_by_route(route_name, new_driver_name):
        cur.execute("UPDATE Perevozki SET driver = ? WHERE route = ?", (new_driver_name, route_name))
        con.commit()
        print(f"\nВодитель для маршрута '{route_name}' изменен на '{new_driver_name}'.")


    # Изменение даты прибытия для всех однодневных рейсов
    def update_arrival_for_one_day_trips(new_arrival_date):
        cur.execute("UPDATE Perevozki SET arr_date = ? WHERE dep_date = arr_date", (new_arrival_date,))
        con.commit()
        print(f"\nДата прибытия для однодневных рейсов изменена на '{new_arrival_date}'.")


    #  Функции удаления (3 разных запроса)
    # Удаление по ID
    def delete_by_id(trip_id):
        cur.execute("DELETE FROM Perevozki WHERE id = ?", (trip_id,))
        con.commit()
        print(f"\nЗапись с ID {trip_id} удалена.")


    # Удаление всех рейсов конкретного водителя
    def delete_by_driver(driver_name):
        cur.execute("DELETE FROM Perevozki WHERE driver = ?", (driver_name,))
        con.commit()
        print(f"\nВсе рейсы водителя '{driver_name}' удалены.")


    # Удаление всех рейсов, где масса груза больше заданной
    def delete_trips_by_max_weight(max_weight):
        cur.execute("DELETE FROM Perevozki WHERE weight > ?", (max_weight,))
        con.commit()
        print(f"\nУдалены рейсы с грузом тяжелее {max_weight}т.")


add_data()
show_all_data()