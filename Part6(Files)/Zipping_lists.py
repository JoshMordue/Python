albums = [("Welcome to my Nightmare", "Alice Cooper", 1975),
          ("Bad Company", "Bad Company", 1974),
          ("Nightflight", "Budgie", 1981),
          ("More Mayhem", "Imelda May", 2011),
          ("Ride the Lightning", "Metallica", 1984),
          ]

keys = ['album', 'artist', 'year', 'Test']

for row in albums:
    zip_object = zip(keys, row)
    # print(zip_object)
    # for thing in zip(keys, row):
    #     print("\t", thing)
    albums_dict = dict(zip_object)
    print(albums_dict)