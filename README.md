# kirisund
A python script that plays audio when there is silence. 

<img src="https://github.com/ArmoryFou/kirisund/blob/main/kirisund.png" width="400" height="400" />

## Requirements

- Python
- pycaw
- pygame

## Usage

install the requirements
```
pip install pycaw pygame
```

change the audio folder path for your own (the folder where you have the audio).
```
AUDIO_FOLDER = "audio//folder"
```

(optional) change the amount of seconds before playing audio after a pause.
```
AUDIO_PLAY_DELAY = 2
```


> [!NOTE]
> Only reproduces .mp3 and .ogg.


## TO DO

- [ ] Add a personalizable shortcut to pause and resume.
- [ ] support for more formats .flac, .wav, etc.
- [ ] change playlist order ascendent, descendent or random.
- [ ] better interface.
