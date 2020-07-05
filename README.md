# translator-bot
A discord bot that translates a given text repeatedly using Google Translate. For the keks and memes. Originally a Python script by SkullTech, made into a Python Discord bot by BKModding

## What is this and how is this useful?!
This script uses the advanced mind of Google Translate to figure out the hidden meanings behind ordinary english text.
Inspired by the following _meme_-videos.

- [Gucci Gang but it's been Google translated over 500 times](https://youtu.be/HMReGXCtTiM)
- [Pumped Up Kicks but it's been Google translated](https://youtu.be/ZMR395zmT1k)

## Usage

```
Translate text repeatedly using Google Translate. For the keks and memes. 
Originally by SkullTech. Made into a Discord bot by BK Modding

usage: !translate [-h] (-t TEXT) [-n NUM] [-l LANGS [LANGS ...]]

required arguments:
-t TEXT, Input text (in quotations)

optional arguments:
-h HELP, Show this help message and exit
-n NUM,  Number of time to go through the languages.
-l LANGS [LANGS ...], ISO 639-1 codes of the languages to use.

The default values of the optional arguments are
    * NUM 10
    * LANGS ['de', 'ko', 'la', 'ja', 'eo']
```

A simple use-case can be as follows
```Discord:
!translate -t "There's vomit on his sweater already, mom's spaghetti"

Output:
[*] "There's vo..." but translated 50 times!

Nikel-spaghete water (water spaghetti nickel) is solved.
```

A more involved use-case which uses all the available CLI arguments.
```Discord
!translate -t "There's vomit on his sweater already, mom's spaghetti" -n 10 -l de ko hi

Output:
[*] "There's vo..." but translated 30 times!

Your sweater is already spaghetti to celebrate your mother.
```

## Requirements for development 
```
Python 3.8.3
discord.py
googletrans
```