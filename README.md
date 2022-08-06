# Simple-Speech-To-Text
A simple raw python program to efficiently transcribe speech to text(only supports English language).

No external dependencies required. Uses AssemblyAI's transcription tool and Python to transcribe audio to text. Requires AssemblyAI's user API key. Go ahead and first create an account on [AssemblyAI](https://www.assemblyai.com) and get your API key.

Make sure to have the media file in the same folder as main.py. Clone the repo and run the file from cmd or terminal by

```
python main.py your-media-file-name
```
Wait for a few seconds until the AssemblyAI servers respond and the transcribed txt file should automatically be created in your project folder. Play your file and read the transcribed file along :) 

The longer the media file, the longer it'd take to transcribe. In case of any error, check your media file or try again.
