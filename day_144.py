from datetime import datetime

def format_date(date):
    """
    Format date using strftime().
    """
    return date.strftime('%Y-%m-%d %H:%M:%S')

# Example usage
current_date = datetime.now()
formatted_date = format_date(current_date)
print(formatted_date)