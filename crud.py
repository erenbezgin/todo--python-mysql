from database import connect_db


def add_task(task_name):
    conn, cursor = connect_db()

    if conn and cursor:
        try:
            #  Görev ekleme
            sql = "INSERT INTO tasks (task_name) VALUES (%s)"
            val = (task_name,)  # tuple olarak gönder

            cursor.execute(sql, val)
            #  kayıt
            conn.commit()

            print(f"Başarıyla eklendi: {task_name}")

        except Exception as err:
            print(f"Ekleme hatası: {err}")
        finally:
            # close connet
            cursor.close()
            conn.close()


def show_tasks():
    conn, cursor = connect_db()

    if conn and cursor:
        try:
            # görevleri çek
            cursor.execute("SELECT * FROM tasks")

            # sonuçları al
            results = cursor.fetchall()

            print("\n--- TO DO ---")
            for row in results:
                # id ,görev adı, durum
                print(f"ID: {row[0]} | Görev: {row[1]} | Durum: {row[2]}")
            print("---------------------------\n")

        except Exception as err:
            print(f"Okuma hatası: {err}")
        finally:
            cursor.close()
            conn.close()


if __name__ == "__main__":

    gorev = input("Yeni görev girin: ")
    add_task(gorev)
    show_tasks()
