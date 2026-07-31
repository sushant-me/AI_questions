from datetime import datetime

def get_current_date_time():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

print(get_current_date_time())