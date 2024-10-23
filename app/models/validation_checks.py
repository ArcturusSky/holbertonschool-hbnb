"""
Module holding all the checks to alleviate others files.
"""

import re
from .PseudoDataBase import username_list, placename_list, places_adress_list

# Checks in User's Class
def name_lenght_validation50(name):
    """Check if name has a valid length (1 to 50 characters)."""

    if len(name) > 50 or len(name) <= 0:
        raise ValueError(f"{name}'s lenght is invalid. Must be between 1 and 50 characters.")
    else:
        return name

def username_validation(username):
    """Check if username already exist."""

    if username in username_list:
        raise ValueError(f"{username} already exist.")
    else:
        return username

def email_validation(email):
    """Validate if email format is correct using a regex."""

    # Correct format for an email
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    
    if not re.match(email_regex, email):
        raise ValueError("Invalid email format.")
    else:
        return email

def phone_validation(phone_number):
    """
    Validate phone number using regex.
    Accepts international and standard formats.
    """

    # Correct format for a phone number
    phone_regex = r'^(\+?\d{1,3})?[-.\s]?(\(?\d{3}\)?)[-.\s]?(\d{3})[-.\s]?(\d{4})$'
    
    if not re.match(phone_regex, phone_number):
        raise ValueError("Invalid phone number.")
    else:
        return phone_number

def password_validation(password):
    """Validate if password is strong enough using a regex."""

    password_regex = r'^(?=.*[A-Z])(?=.*\d)[a-zA-Z0-9_.+-]{6,}$'
    if not re.match(password_regex, password):
        raise ValueError("Password must be at least 6 characters long, contain at least one uppercase letter and one digit.")
    else:
        return password


# Checks in Place's Class
def owner_validation(username):
    """Check if the owner exist."""

    if username not in username_list:
        raise ValueError(f"{username} doesn't exist")
    else:
        return username

def adress_validation(latitude, longitude):
    """Validate if latitue and longitude are valids."""
    if not -90 < latitude < 90 or -180 < longitude < 180:
        raise ValueError("Coordinates are invalids.")
    else:
        adress = (latitude, longitude)
        return adress

def place_validation(placename, adress):
    """Check if the place doesn't already exist."""

    if placename in placename_list and adress in places_adress_list:
        raise ValueError(f"{placename} already exist at {adress}")
    else:
        return placename

def description_validation(description):
    """Check if the description is existing and not too long."""

    if len(description) <= 0 or len(description) > 5000:
        raise ValueError("Description must be between 1 and 5000 characters.")
    else:
        return description

def price_validation(price):
    """ Check if the price is a positive value"""
    if price <= 0:
        raise ValueError("Price must be valid")
    else:
        return price

# Checks in Review's Class

def title_validation(title):
    """Check if title is valid"""

    if 50 < len(title) < 0:
        raise ValueError("Title must be between 1 and 50 characters")
    else:
        return title

    # Check if text is valid (used description validation)

def rating_validation(rating):
    """Check if rating is valid"""

    if 5 < rating < 0:
        raise ValueError("Rating must be between 1 and 5")
    else:
        return rating

def existing_place_validation(placename):
    """Check if place exist"""

    if placename not in placename_list:
        raise ValueError("Place doesn't exist")
    else:
        return placename

    # Check if user exist (used owner validation)


# Checks in Amenity's Class