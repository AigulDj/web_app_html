from lib.album_repository import AlbumRepository
from lib.album import Album

"""
When I call #all
I get all the albums in the albums table
"""
def test_all(db_connection):
    db_connection.seed("seeds/record_store_html.sql")
    repository = AlbumRepository(db_connection)
    assert repository.all() == [
        Album(1, 'Doolittle', 1989, 1),
        Album(2, 'Surfer Rosa', 1988, 1),
        Album(3, 'Waterloo', 1974, 2),
        Album(4, 'Super Trouper', 1980, 2),
        Album(5, 'Bossanova', 1990, 1),
        Album(6, 'Lover', 2019, 3),
        Album(7, 'Folklore', 2020, 3),
        Album(8, 'I Put a Spell on You', 1965, 4),
        Album(9, 'Baltimore', 1978, 4),
        Album(10, 'Here Comes the Sun', 1971, 4),
        Album(11, 'Fodder on My Wings', 1982, 4),
        Album(12, 'Ring Ring', 1973, 2)
    ]

'''
when i call find
i get one album back
'''
def test_find(db_connection):
    db_connection.seed("seeds/record_store_html.sql")
    repository = AlbumRepository(db_connection)
    assert repository.find(1) == Album(1, 'Doolittle', 1989, 1)










# """
# When I call #create
# I create an album in the database
# And I can see it back in #all
# """
# def test_create(db_connection):
#     db_connection.seed("seeds/record_store_html.sql")
#     repository = AlbumRepository(db_connection)
#     album = Album(None, "Test Title", 2000, 2)
#     repository.create(album)
#     assert repository.all() == [
#         Album(1, 'Pop Album 2019', 2019, 2),
#         Album(2, 'Hip-Hop Album 2021', 2021, 3),
#         Album(3, 'Jazz Album 2018', 2018, 4),
#         Album(4, "Test Title", 2000, 2)
#     ]
