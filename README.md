# Speech2Text on Raspberry Pi

**Step 0:** Install python3

`sudo apt install python3-pip`

## Dependencies
### SpeechRecognition
`pip3 install SpeechRecognition`

### PyAudio
**Step 1:** On the command line (Terminal) you need to first install the ALSA library using the following command:

`sudo apt-get install libasound-dev`

**Step 2:** Then you need to compile the PortAudio library:

`sudo apt-get install portaudio19-dev`

**Step 3:** Now you  can install PyAudio using the following command:

`pip3 install pyaudio --user`

**Step 4:** how ever I had an issue with calling it in Python 3 or Python hence i used the following command... and Shazam! 

`sudo apt-get install python3-pyaudio`

### gTTS

`pip3 install gTTS`

### PlaySound

`pip3 install playsound`
