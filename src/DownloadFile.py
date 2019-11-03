import sys
import urllib

print('What would you like to download?')
user_request=input("Insert url with uppercommas ")
requested_url=user_request
requested_location=input("Set download location ")


if user_request and requested_location:
	urllib.urlretrieve(requested_url, requested_location) 
else: 
    print('No input given')
