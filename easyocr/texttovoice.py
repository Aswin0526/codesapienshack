import pyttsx3
from imagetotext import imagetotext

# Initialize the pyttsx3 engine
engine = pyttsx3.init()

# Set properties before adding anything to speak
engine.setProperty('rate', 100)  # Speed of speech
engine.setProperty('volume', 1)  # Volume (0.0 to 1.0)

# Define the text you want to convert to speech
text = imagetotext()

# Pass the text to the engine
engine.say(text)

# Run the speech engine
engine.runAndWait()
