# spotifyRecommend

ONLY RUNS LOCALY - INSTRUCTIONS TO RUN

1. Make sure you have the latest verison of Python, pip, and Flask
2. Download both the spotify.py and index.html files
3. On the Spotify API website create a new app called "Recommend Bot"
5. In spotify.py, replace the "ENTER ID" and "CLIENT SECRET" field with your Client ID and Client Secret
6. Replace the custom_cache_path with your custom path to the .cache file created
7. Make sure you have a live instance of Spotify running on your machine
8. In your command line type "python spotify.py" to run Flask app
9. Then in your file explorer, run the index.html application
10. Click "Run Script" and check your Spotify app and there will be a new reccomended song in your queue


HOW RECOMMEND BOT WORKS
- It takes a random interval of 10 songs out of the past 50 you've listened to
- It then takes all of those and calculates the average popularity score
- It then picks a random artist you've listened to in that interval and uses the Spotify API to get related artists
- Then it uses the search method to search for songs related to that artist and within a reasonable popularity interval
- Finally, it picks a random one and adds it to your queue
