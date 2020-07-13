HELP_TEXT = '''
Translate text repeatedly using Google Translate. For the keks and memes. 
Originally by SkullTech. Made into a Discord bot by BK Modding

Usage: !translate [-h] [-n NUM] [-l LANGS [LANGS ...]] (-t TEXT)

Required arguments:
-t TEXT, Input text

Optional arguments:
-h HELP, Show this help message and exit
-n NUM,  Number of times to go through the languages.
-l LANGS [LANGS ...], ISO 639-1 codes of the languages to use.

NOTE: All optional arguments must come before the TEXT argument (-t)

The default values of the optional arguments are
    * NUM 10
    * LANGS de ko la ja eo
    
NOTE: total number of translations is NUM * LANGS

Here's a short listing of all the ISO 639-1 codes available:
af sq am ar hy az eu be bn bs bg ca ceb ny zh-cn zh-tw co hr cs da nl en eo et 
tl fi fr fy gl ka de el gu ht ha haw he hi hmn hu is ig id ga it ja jw kn kk 
km ko ku ky lo la lv lt lb mk mg ms ml mt mi mr mn my ne no or ps fa pl pt pa 
ro ru sm gd sr st sn sd si sk sl so es su sw sv tg ta te th tr 
uk ur ug uz vi cy xh yi yo zu

A more detailed listing which includes the corresponding language names can be found here:
https://gist.github.com/BK-Modding/25e5a787486baaabec434bc6a1a96670
'''