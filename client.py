import requests

BASE_URL = "http://127.0.0.1:5500"

def get_artist_by_id(artist_id: int):
    response = requests.get(f"{BASE_URL}/artists/{artist_id}")
    if response.status_code == 200:
        return response.json()
    elif response.status_code == 404:
        print("Artist not found.")
    else:
        print("An error occurred.")

def search_artist_by_name(name: str):
    response = requests.get(f"{BASE_URL}/artists/search/{name}")
    if response.status_code == 200:
        artists = response.json()
        for artist in artists:
            print(f"Artist ID: {artist['ArtistId']}, Name: {artist['Name']}")
    elif response.status_code == 404:
        print("No artists found with the given name.")
    else:
        print("An error occurred.")

def get_albums_by_artist_id(artist_id: int):
    response = requests.get(f"{BASE_URL}/albums/artist/{artist_id}")
    if response.status_code == 200:
        albums = response.json()
        for album in albums:
            print(f"Album ID: {album['AlbumId']}, Title: {album['Title']}")
    elif response.status_code == 404:
        print("No albums found for the given artist ID.")
    else:
        print("An error occurred.")

def get_tracks_by_album_id(album_id: int):
    response = requests.get(f"{BASE_URL}/tracks/album/{album_id}")
    if response.status_code == 200:
        tracks = response.json()
        for track in tracks:
            print(f"Track ID: {track['TrackId']}, Name: {track['Name']}")
    elif response.status_code == 404:
        print("No tracks found for the given album ID.")
    else:
        print("An error occurred.")

def get_all_artists():
    response = requests.get(f"{BASE_URL}/artists/")
    if response.status_code == 200:
        return response.json()
    else:
        print("An error occurred.")

def main():
    while True:
        print("\nMenu:")
        print("1. Rechercher un artiste par nom")
        print("2. Afficher les albums d'un artiste par ID")
        print("3. Afficher les pistes d'un album par ID")
        print("4. Afficher tous les artistes")
        print("5. Afficher un artiste par son ID.")
        print("6. Quitter")

        choice = input("Entrez votre choix: ")

        if choice == "1":
            name = input("Entrez le nom de l'artiste: ")
            search_artist_by_name(name)
        elif choice == "2":
            artist_id = int(input("Entrez l'ID de l'artiste: "))
            get_albums_by_artist_id(artist_id)
        elif choice == "3":
            album_id = int(input("Entrez l'ID de l'album: "))
            get_tracks_by_album_id(album_id)
        elif choice == "4":
            artists = get_all_artists()
            for artist in artists:
                print(f"Artist ID: {artist['ArtistId']}, Name: {artist['Name']}")
        elif choice == "5":
            artist_id = int(input("Enter the artist ID: "))
            artist = get_artist_by_id(artist_id)
            if artist:
                print(f"Artist ID: {artist['ArtistId']}, Name: {artist['Name']}")
        elif choice == "6":
            break
        else:
            print("Choix non valide. Veuillez réessayer.")

if __name__ == "__main__":
    main()