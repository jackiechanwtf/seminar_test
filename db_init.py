from pymysql import connect

db_config = {"host": "127.0.0.1", "port": 3306, "user": "root", "password": "BlueKnight"}


def create_db():
    with connect(**db_config) as connection:
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS test_db")
        connection.commit()
        cursor.close()


def create_tables():
    with connect(**db_config) as connection:
        cursor = connection.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS test_db.items (
            item_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(80) NOT NULL,
            price INT NOT NULL
        )
        """)
        connection.commit()
        cursor.close()


def insert_data(n):
    with connect(**db_config) as connection:
        cursor = connection.cursor()

        for i in range(n):
            item_data = {
                "name": f"item_{i + 1}",
                "price": 200 + i,
            }

            cursor.execute(
                """
            INSERT INTO test_db.items (item_id, name, price) VALUES (NULL, '{name}', {price})
            """.format(**item_data)
            )

        connection.commit()
        cursor.close()


if __name__ == "__main__":
    create_db()
    create_tables()
    insert_data(100)
