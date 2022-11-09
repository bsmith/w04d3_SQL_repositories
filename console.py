import pdb
from models.artist import Artist
from models.album import Album

import repositories.artist_repository as artist_repository
import repositories.album_repository as album_repository

#album_repository.delete_all()
#artist_repository.delete_all()

artist_1 = Artist('Oasis')
artist_repository.save(artist_1)
artist_2 = Artist('Oasis 2')
artist_repository.save(artist_2)

artist_2.name = "Coldplay"
artist_repository.update(artist_2)

for artist in artist_repository.select_all():
    print(artist.__dict__)

album_1 = Album("Roll With It", "Rock", artist_1)
album_repository.save(album_1)
album_2 = Album("Another Album", "Pop", artist_2)
album_repository.save(album_2)

album_2.genre = "Jazz"
album_repository.update(album_2)

for album in album_repository.select_all():
    print(album.__dict__)

album = album_repository.select(album_1.id)
print(album.__dict__)

for album in album_repository.select_by_artist(artist_1):
    print(album.__dict__)
    print(album.artist.__dict__)


album_repository.delete(album_1.id)
artist_repository.delete(artist_1.id)

pdb.set_trace()
