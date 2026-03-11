"""
Delete database records.
"""

import sqlite3

def delete_records(database_path, table_name, condition):
    """
    Deletes records from the specified table that match the given condition.

    Args:
    database_path (str): The path to the database file.
    table_name (str): The name of the table from which to delete records.
    condition (str): The condition to match for deleting records (e.g., 'age > 30').
    """
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()
    
    # Construct the SQL query
    query = f"DELETE FROM {table_name} WHERE {condition};"
    
    try:
        # Execute the query
        cursor.execute(query)
        conn.commit()
        print(f"Deleted {cursor.rowcount} records.")
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        # Close the connection
        conn.close()

# Example usage
delete_records('https://example.com/database.db', 'users', 'age > 30')