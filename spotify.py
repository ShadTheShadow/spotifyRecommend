import base64
import spotipy
import requests
import spotipy.client
from spotipy.oauth2 import SpotifyOAuth
import random




from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/run-script', methods=['POST'])
def run_script():



    



    
    id1 = "1215748776fb4ad5a5b1f8d0370c9ba3"
    id2 = "8a2df0f7195a46269b2cdfe10b7b012d"

    credentials = f"{id1}:{id2}"
    credentials_base64 = base64.b64encode(credentials.encode())


    token_url = 'https://accounts.spotify.com/api/token'
    headers = {
        'Authorization': f'Basic {credentials_base64.decode()}'
    }
    data = {
        'grant_type': 'client_credentials'
    }
    response = requests.post(token_url, data=data, headers=headers)

    if response.status_code == 200:
        access_token = response.json()['access_token']
        print("Access token obtained successfully.")
    else:
        print("Access token not obtained.")
        exit()



    custom_cache_path = 'C:/Users/evant/vscode/.cache'



    auth_manager = SpotifyOAuth(
        client_id=id1,
        client_secret=id2,
        redirect_uri="https://shadtheshadow.github.io/",
        scope="user-read-private user-read-email playlist-read-private playlist-read-collaborative "
            "playlist-modify-public playlist-modify-private user-library-read user-library-modify "
            "user-read-playback-state user-modify-playback-state user-read-currently-playing "
            "user-follow-read user-follow-modify user-top-read app-remote-control streaming "
            "ugc-image-upload user-read-recently-played",
        cache_path=custom_cache_path
    )

    sp = spotipy.Spotify(auth_manager=auth_manager)


    #top tracks
    '''
    songs = sp.current_user_top_tracks(50, 0, "long_term")

    track_names = [item['name'] for item in songs['items']]

    print(track_names)
    '''

    play = 1

    searchyCall = 0

    recommended = []

    while (play == 1):

        searchyCall = 0

        def searchy():
            recent = sp.current_user_recently_played(10, None, None)


            track_ids = [item['track']['id'] for item in recent['items']]


            
            #random genre
            def pickGenre():

                #if (searchyCall > 4):

                    #rando = sp.recommendation_genre_seeds()

                    #rando = random.choice(rando['genres'])

                    #return random.choice(rando)



                tracks = sp.tracks(track_ids)['tracks']

                artist_ids = [track['artists'][0]['id'] for track in tracks]

                artists = sp.artists(artist_ids)['artists']

                genres = {}
                for artist in artists:
                    genres[artist['id']] = artist['genres']

                all_genres = [genre for genre_list in genres.values() for genre in genre_list]

                return random.choice(all_genres)



            random_genre = pickGenre()
            print(random_genre)



            #popularity

            def getMean():

                popularity = [item['track']['popularity'] for item in recent['items']]

                total = 0
                for pop in popularity:
                    total += pop
                return(total/len(popularity))



            mean = getMean()


            #related artists

            def getRelated():


                tracks = sp.tracks(track_ids)['tracks']

                artist_ids = [track['artists'][0]['id'] for track in tracks]

                related = sp.artist_related_artists(artist_ids[random.randint(0, len(artist_ids)-1)])

                artist_names = []

                for artist in related['artists']:
                    artist_names.append(artist['name'])

                return artist_names


            relatedArtists = getRelated()

            print(relatedArtists)

            final = []


            counter = 0
            breadth = 20
            while (len(final) < 1):

                if counter > 20:
                    breadth += 10
                    counter = 0


                final = []

                s = sp.search('artist: ' + random.choice(relatedArtists) + 'genre: ' + random_genre, 50, 0, "track", None)


                items = s['tracks']['items']

                
                for item in items:
                    if (item['popularity'] > mean-breadth and item['popularity']<mean+breadth):                    
                        final.append(item)
                    counter+=1


            return final



        songs = searchy()

        link = songs[random.randint(0, len(songs)-1)]['uri']

        while (recommended.count(link) > 0):
            songs = searchy()
            link = songs[random.randint(0, len(songs)-1)]['uri']
            searchyCall+=1

        recommended.append(link)
        print(songs[0]['uri'])

        sp.add_to_queue(link, None)

        print(recommended)
        print("")

        user = input("More songs? Y/N")

        if (user == "n" or user == "N"):
            play = 0




    print("thanks for using the app!")















    result = "Hello from your local Python script!"
    return jsonify(result=result)




if __name__ == '__main__':
    app.run(debug=True)




