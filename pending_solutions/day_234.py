""" Insert data into database. """

import sqlite3

def insert_data(database_name, table_name, data):
    """
    Insert data into a specified table in a SQLite database.

    :param database_name: str - the name of the database file.
    :param table_name: str - the name of the table to insert data into.
    :param data: tuple - the data to insert (e.g., (value1, value2, ...)).
    """
    # Connect to the SQLite database
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()

    # Create the table if it does not exist
    create_table_query = f"""
    CREATE TABLE IF NOT EXISTS {table_name} (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        value1 TEXT,
        value2 TEXT
    )
    """
    cursor.execute(create_table_query)

    # Insert data into the table
    insert_query = f"INSERT INTO {table_name} (value1, value2) VALUES (?, ?)"
    cursor.execute(insert_query, data)

    # Commit the transaction
    conn.commit()

    # Close the connection
    conn.close()

# Example usage
database_name = 'example.db'
table_name = 'my_table'
data = ('example1', 'example2')
insert_data(database_name, table_name, data)