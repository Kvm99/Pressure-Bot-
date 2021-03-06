import psycopg2
from settings import config


def create_tables():
    """
    create 2 tables:
    users: - username, sex, age, weight, work
    pressure: pressure_id, username, systolic, diastoic,
    timestamp, date, arm, foreign key to users
    """

    tables = (
        """
        CREATE TABLE IF NOT EXISTS users (
          username VARCHAR(50) PRIMARY KEY NOT NULL,
          sex VARCHAR(20),
          age VARCHAR(15),
          weight VARCHAR(15),
          work VARCHAR(15)
        );
        """,

        """
        CREATE TABLE IF NOT EXISTS pressure(
            pressure_id SERIAL PRIMARY KEY,
            username VARCHAR(50),
            systolic VARCHAR(3) NOT NULL,
            diastolic VARCHAR(3) NOT NULL,
            timestamp timestamptz NOT NULL,
            arm VARCHAR(50) NOT NULL,
            pulse VARCHAR(3),
            FOREIGN KEY (username) REFERENCES users
        );
        """
        )
    try:
        connection = config()
        cursor = connection.cursor()

        for table in tables:
            cursor.execute(table)

        cursor.close()
        connection.commit()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if connection is not None:
            connection.close()


if __name__ == "__main__":
    create_tables()
