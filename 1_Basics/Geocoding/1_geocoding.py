# -*- coding: utf-8 -*-
"""
Created on Fri Jul 20 16:40:01 2018

@author: SilverDoe
"""

import requests
url = 'https://maps.googleapis.com/maps/api/geocode/json'
params = {'sensor': 'false', 'address': 'Mountain View, CA'}
r = requests.get(url, params=params)
results = r.json()['results']
location = results[0]['geometry']['location']
location['lat'], location['lng']


'''
Using geocoder library

============ Forward Geocoding ============================================='''

import geocoder
g = geocoder.google('Mountain View, CA')
g.geojson
g.json
g.wkt
g.osm

'''============ Reverse Geocoding ============================================='''
import geocoder
g = geocoder.google([45.15, -75.14], method='reverse')
g.city
g.state
g.state_long
g.country
g.country_long