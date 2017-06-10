from dbconnect import dbconnect
from pymongo import GEO2D

db = dbconnect()
loc = [26.9124, 75.7873]

try:
    # change limit() to change maximum number of results
    found_cursor_gps = db.states.find({'gps': {'$near': loc}}, {'_id': False}).limit(1)
    if found_cursor_gps.count() is not 0:
        for i in found_cursor_gps:
            print(i)
    else:
        print('Sorry! no result found')

except Exception as e:
    if 'unable to find index for $geoNear query' in str(e):
        print('Unable to find any geospatial index...')
        print('Building index please wait...')
        db.states.create_index([("gps", GEO2D)])
        print('Done! Please restart the script.')
    else:
        print('Exception:', e)
