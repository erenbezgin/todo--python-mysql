import mysql.connector


def connect_db():
    try:
        # sql bağlantı isteği oluşturuyoruz
        conn = mysql.connector.connect(
            host="localhost",
            user="root",  # kullanıcı adınız neyse onu girin
            password="",  # şifrenizi girin
        )
        cursor = conn.cursor()

        # db olustur
        cursor.execute("CREATE DATABASE IF NOT EXISTS todo_db")

        # 2. olusturulan vdb yi seç
        cursor.execute("USE todo_db")

        # 3. tablo olustur varsa olanı kullan
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id INT AUTO_INCREMENT PRIMARY KEY,
                task_name VARCHAR(255) NOT NULL,
                status VARCHAR(50) DEFAULT 'Pending'
            )
        """)

        print("Database is ready and connected!")
        return conn, cursor

    except mysql.connector.Error as err:
        print(f"Hata: {err}")
        return None, None


if __name__ == "__main__":
    connect_db()
