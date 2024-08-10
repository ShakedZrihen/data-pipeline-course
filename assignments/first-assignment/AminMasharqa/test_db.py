import psycopg2
from psycopg2 import OperationalError

def check_users_table():
    try:
        # Connect to PostgreSQL
        connection = psycopg2.connect(
            dbname="amin_db",
            user="amin",
            password="amin1234",
            host="localhost",
            port="5432"
        )
        
        cursor = connection.cursor()
        
        # Execute SQL query to check for the users table
        cursor.execute("SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name='users');")
        exists = cursor.fetchone()[0]

        if exists:
            print("The 'users' table exists in the database.")
        else:
            print("The 'users' table does not exist in the database.")
    
    except OperationalError as e:
        print(f"Error connecting to PostgreSQL: {e}")
    
    finally:
        # Close database connection
        if connection:
            cursor.close()
            connection.close()

if __name__ == "__main__":
    check_users_table()
