###### Simple video compressor for discord.

# Video-compressor

Compresses videos to under 10mb to allow them to be shared via discord.

## Prerequisite:
- Have python installed on your machine.

## Setup Guide:
1. Copy ```compressor.py``` to a folder containing videos to be compressed. 
2. In the same directory as  ```compressor.py```, run ```py -m pip install moviepy``` in the terminal

## Use Guide:
### Option 1:
In the same directory as ```compressor.py```, open the terminal and run ```py compressor.py```. Then follow instructions.
### Option 2:
In the same directory as ```compressor.py```, open the terminal. You can now run ```py compressor.py your_video.mp4```, where ```your_video.mp4``` is the video you are attempting to compress. 

## Notes:
- AI was used in the creation of this project but it was reviewed and tested
- Made and tested for "clip" length videos (30 sec - 1 min). Not reccomended for very long videos.
- Supported filetypes: .mp4, .mov, .mkv, .avi, .webm, .wmv

## Todo:
- [ ] Support for other filetypes (images?)
- [ ] Mass-converting (converting a whole folder)
- [ ] Move converted videos to a converted folder
- [x] Implement other video filetypes
- [x] Implement CLI interface for choosing video 
