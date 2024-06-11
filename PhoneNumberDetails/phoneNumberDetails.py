import phonenumbers as ph
from phonenumbers import carrier
from phonenumbers import geocoder
from phonenumbers import timezone

number = "+84375235456"
number = ph.parse(number)

print(timezone.time_zones_for_number(number))
print(geocoder.description_for_number(number, 'en'))
print(carrier.name_for_number(number, 'en'))