from datetime import datetime

def calculate_age(birth_date):
    """ Calculate age from birth date. """
    birth_date = datetime.strptime(birth_date, '%Y-%m-%d')
    today = datetime.today()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age

# Example usage:
# print(calculate_age('1990-05-15'))