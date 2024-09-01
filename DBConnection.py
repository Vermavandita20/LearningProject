import psycopg2


def connect_to_postgres():
    try:
        # Establish a connection to the PostgreSQL database
        conn = psycopg2.connect(
            dbname="postgres",  # Replace with your database name
            user="postgres",         # Replace with your username
            password="root",     # Replace with your password
            host="localhost",             # Replace with your host, e.g., "localhost" or your database server IP
            port="5432"                   # Replace with your port number if different from default
        )

        # Create a cursor object using the connection
        cur = conn.cursor()

        # Execute a simple query
        cur.execute("SELECT version();")

        # Fetch and print the result of the query
        db_version = cur.fetchone()
        print(f"Connected to PostgreSQL database. Version: {db_version[0]}")

        # Close the cursor and connection
        cur.close()
        conn.close()

    except Exception as e:
        print(f"An error occurred while connecting to PostgreSQL: {e}")

if __name__ == "__main__":
    connect_to_postgres()
