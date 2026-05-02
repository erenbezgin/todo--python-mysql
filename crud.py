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


def update_task_status(task_id, new_status="Completed"):
    conn, cursor = connect_db()

    if conn and cursor:
        try:
            # ıd ile görev güncelleme
            sql = "UPDATE tasks SET status = %s WHERE id = %s"
            val = (new_status, task_id)

            cursor.execute(sql, val)
            conn.commit()

            if cursor.rowcount > 0:
                print(f"ID {task_id} olan görev '{new_status}' olarak güncellendi.")
            else:
                print("Hata: Bu ID'ye sahip bir görev bulunamadı.")

        except Exception as err:
            print(f"Güncelleme hatası: {err}")
        finally:
            cursor.close()
            conn.close()


def delete_task(task_id):
    conn, cursor = connect_db()

    if conn and cursor:
        try:
            # ıd sahip görev sil
            sql = "DELETE FROM tasks WHERE id = %s"
            val = (task_id,)

            cursor.execute(sql, val)
            conn.commit()

            if cursor.rowcount > 0:
                print(f"ID {task_id} olan görev başarıyla silindi.")
            else:
                print("Hata: Silinmek istenen ID bulunamadı.")

        except Exception as err:
            print(f"Silme hatası: {err}")
        finally:
            cursor.close()
            conn.close()


def get_tasks():
    conn, cursor = connect_db()
    if conn and cursor:
        cursor.execute("SELECT * FROM tasks")
        results = cursor.fetchall()
        cursor.close()
        conn.close()
        return results
    return []


if __name__ == "__main__":

    print("--- MEVCUT LİSTE ---")
    show_tasks()

    secim = input("Silmek istediğin ID'yi gir: ")
    delete_task(secim)

    print("--- GÜNCEL LİSTE ---")
    show_tasks()
