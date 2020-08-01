# translator-bot
<img align="left" src="https://i.imgur.com/yo0W0R8.png"> A discord bot that translates a given text repeatedly using Google Translate. For the keks and memes. Originally a Python script by SkullTech, made into a Python Discord bot by BKModding

# [Invite on Discord!](https://discord.com/api/oauth2/authorize?client_id=445572978772541461&permissions=75776&scope=bot)

## What is this and how is this useful?!
This bot uses the **bIG BrAiN** of Google Translate to figure out the hidden meanings behind ordinary english text.
Inspired by the following _meme_-videos.

- [Gucci Gang but it's been Google translated over 500 times](https://youtu.be/HMReGXCtTiM)
- [Pumped Up Kicks but it's been Google translated](https://youtu.be/ZMR395zmT1k)

## Usage

<img src="https://i.imgur.com/9vbaJTu.png">
<img src="https://i.imgur.com/8Rm86rX.png">
<img src="https://i.imgur.com/99ZJij5.png">
<img src="https://i.imgur.com/75KA3cp.png">

```
Translate text repeatedly using Google Translate. For the keks and memes. 
Originally by SkullTech. Made into a Discord bot by BK Modding

Usage: !translate [-h] [-n NUM] [-l LANGS [LANGS ...]] [-t] TEXT

Required arguments:
TEXT, Input text. Must be specified with -t if including optional arguments. Can be omitted otherwise.

Optional arguments:
-h HELP, Show this help message and exit
-n NUM,  Number of times to go through the languages.
-l LANGS [LANGS ...], ISO 639-1 codes of the languages to use.

NOTE: All optional arguments must come before the TEXT argument (-t)

The default values of the optional arguments are
    * NUM 10
    * LANGS de ko la ja eo
    
NOTE: total number of translations is NUM * LANGS

Here's a short listing of all the ISO 639-1 language codes available:
af sq am ar hy az eu be bn bs bg ca ceb ny zh-cn zh-tw co hr cs da nl en eo et 
tl fi fr fy gl ka de el gu ht ha haw he hi hmn hu is ig id ga it ja jw kn kk 
km ko ku ky lo la lv lt lb mk mg ms ml mt mi mr mn my ne no or ps fa pl pt pa 
ro ru sm gd sr st sn sd si sk sl so es su sw sv tg ta te th tr 
uk ur ug uz vi cy xh yi yo zu

A more detailed listing which includes the corresponding language names can be found here:
https://gist.github.com/BK-Modding/25e5a787486baaabec434bc6a1a96670
```

A detailed listing of the language names and codes can also be found via the googletrans module:
```Python
import googletrans
googletrans.LANGCODES
```

### Examples:

The simplest use-case is one without any arguments:
```Discord:
!translate There's vomit on his sweater already, mom's spaghetti

Output:
[*] "There's vomit on his sweater already, mom's spaghetti" but translated 50 times!


Nikel-spaghete water (water spaghetti nickel) is solved.
```

You can also specify the text argument `-t` here, although it is unnecessary for such a basic use-case.
```Discord:
!translate -t There's vomit on his sweater already, mom's spaghetti

Output:
[*] "There's vomit on his sweater already, mom's spaghetti" but translated 50 times!


Nikel-spaghete water (water spaghetti nickel) is solved.
```

A more involved use-case which uses some or all the available arguments, however, requires you to specify the text argument `-t`:
```Discord
!translate -n 50 -t There's vomit on his sweater already, mom's spaghetti

Output:
[*] "There's vomit on his sweater already, mom's spaghetti" but translated 250 times!


Spaghetti and vomit in mom's sweater
```

```Discord
!translate -n 10 -l de ko hi -t There's vomit on his sweater already, mom's spaghetti

Output:
[*] "There's vomit on his sweater already, mom's spaghetti" but translated 30 times!


Your sweater is already spaghetti to celebrate your mother.
```

## Improvements and Changes

- Translation workflow is much faster after: 
   - Changing the argument parsing to take on a priority-based conditional check instead of an equivalent iterative loop-based check.
   - Fixed the translation function call to be correctly asynchronous.
- Help text updated to include more information.
- No need to enclose text in quotations anymore.
- Bot doesn't break if you include quotations (",') or hiphens (-) in the text now.
- Optional arguments must come before the text argument now.
- Accounted for the Bot's reply being longer than Discord's character limit (2000).
- Added functionality for a simpler use-case that doesn't require any arguments to be specified.

## Requirements for development 
```
Python 3
discord.py v1.0+
googletrans 
```

## Running the bot
1. Create a `config.py` and add a discord bot token via a `TOKEN` variable
    ```
    TOKEN = "*token goes here*"
    ```
2. Start the bot by running `botscript.py`
    ```
    python3 botscript.py
    ```