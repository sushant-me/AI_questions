import sqlite3

def fetch_data_from_database():
    """
    Fetch data from database.
    """
    # Connect to the SQLite database
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    
    # SQL query to fetch data
    query = "SELECT * FROM example_table"
    
    try:
        # Execute the query
        cursor.execute(query)
        
        # Fetch all rows
        rows = cursor.fetchall()
        
        # Process rows
        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        # Close the connection
        if conn:
            conn.close()

# Call the function to fetch data
fetch_data_from_database()