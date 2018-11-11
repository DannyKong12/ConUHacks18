# AwesomeSports

AwesomeSports is a project we built for ConUHacks 2018

### About the project
Ever missed an soccer match but don't want to spend an hour re-watching it? AwesomeSports can help. Awesomesports is a tool that generates highlights from sports matches. 

### How we built it
We used python and flask as a backend with a server. This repo hosts the backend and some scripts we used to create our app. The program works by grabbing data from a large dataset provided by Astucemedia, and parsing the data to get an estimate of when we can clip the video. We generate a series of clips from the match, which we then grab using ffmpeg. Generally, the time in the game is not related to the time in the video, so we use computer vision to detect the time from the scoreboard, and clip the video. 

### What's next for AwesomeSports
The project as it stands is incomplete, largely due to time constraints. Some of the features we hoped to implement were not there, and many of the core functionality is hard-coded for proof of concept. We also want to more intelligently use the data to find highlights, but our simple approach was still able to generate great highlights, without missing any of the action.
