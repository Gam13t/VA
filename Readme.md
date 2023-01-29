# Voice assistant with features

### Introduction
This Voice assistant may be useful for people who want a little automation in their daily tasks. What makes it even a little more futuristic - you have all processes controlled by your voice.


### Basic idea of realization
- As TTS engine I would use pyttsx3, the most advanced TTS engine I could find for this purpose.
- As Speech recognition framework I would use SpeechRecognition.
- To remove all the noises and get users output I would use fuzzywuzzy.
- Pytest for testing.


### What's new?
Release notes can be easily found here: [Release Notes](releaseNotes.md)


### How to setup?

**Create venv for this python project.**

After you clone repository this is mandatory to create a new virtual envinroment for this project. To do it - you can simply execute:
> python -m venv env

and access it. If you are using Windows - you can do it by executing this command from the project root folder:
> ./env/Scripts/activate

after that you should see '(env)' in your console.

**Install requirements**

After you have dealt with the virtual envinroment - you should install requirements. To do it - execute the command listed below:
> pip install -r requirements.txt

That should install all the requirements you may need for running this project.

**Setup .env**

Next, you should create .env file in the root folder of this project and fill it with some values. As the example:
> DEBUG=false # DEBUG CONFIG
>
>NETWORK_TESTS=true # UNIT TESTS CONFIG
>
>
>ENABLE_EWELINK_HARDWARE_PROVIDER=false # CREDENTIALS FOR THE EWELINK CONNECT DEVICES
>
>LOGIN = "placeholder"
>
>PASSWORD = "placeholder"
>
>EMAIL = "placeholder"
>
>API_KEY = "placeholder"
>
>VA_NAME = "Маша"  # VOICE ASSISTANT NAME


**Setup pre-commit**

After that, if you gonna to create any pull request into this project - make sure you have installed pre-commit.
Run:
> pre-commit install
>
> pre-commit run --all-files

Proceed with any code amendments only after this step

**Run tests**

To run tests, just execute:
> pytest -vv

While last test - say 'привет' to pass it.

**Setted up**

Now you are fully done to proceed with this project. GL, HF <3
