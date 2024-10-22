"""
Module holding all the checks to alleviate others files
"""

import re
from PseudoDataBase import username_list, placename_list, places_adress_list

# Checks in User's Class
def name_lenght_validation50(name):
    """Check if name has a valid length (1 to 50 characters)."""

    if len(name) <= 50 and len(name) > 0:
        return name
    else:
        raise ValueError(f"{name}'s lenght is invalid. Must be between 1 and 50 characters")

def username_validation(username):
    """Check if username already exist"""

    if not username in username_list:
        return username
    else:
        raise ValueError(f"{username} already exist")

def email_validation(email):
    """Validate if email format is correct using a regex."""

    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None

def phone_validation(phone):
    """
    Validate phone number using regex.
    Accepts international and standard formats.
    """
    phone_regex = r'^(\+?\d{1,3})?[-.\s]?(\(?\d{3}\)?)[-.\s]?(\d{3})[-.\s]?(\d{4})$'
    return re.match(phone_regex, phone) is not None

def password_validation(password):
    """Validate if password is strong enough using a regex."""

    password_regex = r'^(?=.*[A-Z])(?=.*\d)[a-zA-Z0-9_.+-]{6,}$'
    return re.match(password_regex, password) is not None

# Checks in Place's Class
def owner_validation(username):
    if username in username_list:
        return True
    else:
        raise ValueError(f"{username} doesn't exist")

def place_validation(placename, adress):
    if not placename in placename_list and adress not in places_adress_list:
        return True
    else:
        raise ValueError(f"{placename} already exist at {adress}")

# Checks in Review's Class

# Checks in Amenity's Class