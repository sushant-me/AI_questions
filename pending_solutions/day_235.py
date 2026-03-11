"""
Update database records.
"""

import sqlite3

def update_records(database_path, updates):
    """
    Update records in the database.
    
    :param database_path: Path to the SQLite database.
    :param updates: Dictionary of updates where keys are table names and values are lists of tuples (condition, new_values).
    """
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()
    
    for table, update_data in updates.items():
        for condition, new_values in update_data:
            set_clause = ', '.join([f"{key} = ?" for key in new_values.keys()])
            where_clause = f"WHERE {condition}"
            update_query = f"UPDATE {table} SET {set_clause} {where_clause}"
            cursor.execute(update_query, list(new_values.values()))
    
    conn.commit()
    conn.close()

# Example usage:
# updates = {
#     'users': [
#         ('id = 1', {'name': 'John Doe', 'email': 'john.doe@example.com'}),
#         ('id = 2', {'name': 'Jane Smith', 'email': 'jane.smith@example.com'})
#     ]
# }
# update_records('https://example.com/database.db', updates)