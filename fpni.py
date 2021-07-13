import pyfiglet
fpni = pyfiglet.figlet_format("FPNI")
print(fpni)
print("Find Phone Number Information.")
print("Developer/Programmer - Mohit Pandey.\nGitHub:- @mohit377")

import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
from phonenumbers import timezone
enter_phone_number = input("Enter target phone number with country code: ")
phone_number = phonenumbers.parse(enter_phone_number)
print("Country: ", geocoder.description_for_number(phone_number, "en"))
print("Company: ", carrier.name_for_number(phone_number, "en"))
timeZone = timezone.time_zones_for_number(phone_number)
print("Time Zone: ", timeZone)
# Validating a phone number
valid = phonenumbers.is_valid_number(phone_number)
# Checking possibility of a number
possible = phonenumbers.is_possible_number(phone_number)
print("Is valid number: ", valid)
print("Possibility of number: ", possible)
print("Number Type: ", geocoder.number_type(phone_number))
print("Safe Display Name: ", carrier.safe_display_name(phone_number, 'en'))
print("Region Code for Number: ", geocoder.region_code_for_number(phone_number))
print("National Significant Number: ", geocoder.national_significant_number(phone_number))
