import os

from discord.ext import commands
from discord import Activity, ActivityType
from googletrans import Translator, LANGCODES

import utils

try:
    import config
    TOKEN = config.TOKEN
except:
    TOKEN = os.environ.get("TOKEN")
HELP_TEXT = utils.HELP_TEXT

client = commands.Bot(command_prefix='!')

translator = Translator()

def find_in_list(lis, char):
    try:
        char_ind = lis.index(char)
        return char_ind
    except ValueError:
        return -1
    
# https://stackoverflow.com/a/57023599/7856040
def get_chunks(s, maxlength):
    start = 0
    end = 0
    while start + maxlength  < len(s) and end != -1:
        end = s.rfind(" ", start, start + maxlength + 1)
        yield s[start:end]
        start = end +1
    yield s[start:]
    
async def background_translate(ctx, text, langs, times):
    translation = text
    for i in range(times):
        for lang in langs:
            translation = translator.translate(translation, dest=lang).text
        translation = translator.translate(translation, dest='en').text
    
    endtext = '[*] "{}" **but translated {} times!**'.format(text.strip(), times*len(langs)) + "\n\n" + translation
    print("S - Output ready: {}".format(endtext))
    
    chunks = get_chunks(endtext, 2000)
    for chunk in chunks:
        await ctx.send(chunk)

@client.command()
async def translate(ctx):
    message = ctx.message
    # do not want the bot to reply to itself so
    if message.author == client.user:
        return
    
    request = '{}'.format(message.content)

    try:
        request = request.split("!translate ")[1]
    except IndexError:
        print("E - No message provided to translate, please refer to the help command (-h) for more info: {}".format(request))
        return await ctx.send("Error - No message provided to translate, please refer to the help command (-h) for more info: {}".format(request))

    print("Request: {}".format(request))
    
    print("=" * 50)
    print("S - New request received")
    
    args = request.split(" ")
    
    l_ind = find_in_list(args, "-l")
    n_ind = find_in_list(args, "-n")
    t_ind = find_in_list(args, "-t")
    h_ind = find_in_list(args, "-h")
    
    if h_ind != -1:
        print("S - Help information requested")
        return await ctx.send(HELP_TEXT)
    
    await ctx.send("Translation request received (⌐■_■)")

    if max(t_ind, l_ind, n_ind) == -1:
        text = request

        n = 10
        langs = ['de', 'ko', 'la', 'ja', 'eo'] # default
    else:
        if t_ind == -1 or len(args[t_ind+1:]) == 0:
            print("E - No text provided (-t): {}".format(request))
            return await ctx.send("Error - No text provided (-t): {}".format(request))
        
        text = " ".join(args[t_ind+1:])
        
        if max(l_ind, n_ind, t_ind) != t_ind:
            print("E - Optional arguments (-l,-n) should be positioned before the text argument (-t), please refer to the help command (-h) for more info: {}".format(request))
            return await ctx.send("Error - Optional arguments (-l,-n) should be positioned before the text argument (-t), please refer to the help command (-h) for more info: {}".format(request))
        
        if n_ind == -1:
            n = 10
        else:
            try:
                n = int(args[n_ind+1])
            except ValueError:
                print("E - Invalid no. of translations (-n), please refer to the help command (-h) for more info: {}".format(request))
                return await ctx.send("Error - Invalid no. of translations (-n), please refer to the help command (-h) for more info: {}".format(request))
        
        if l_ind == -1:
            langs = ['de', 'ko', 'la', 'ja', 'eo'] # default
        else:
            ind = l_ind
            while not ind in (n_ind, t_ind, h_ind):
                ind += 1
            
            langs = args[l_ind+1:ind]
            
            if len(langs) == 0:
                print("E - No language codes provided (-l), please refer to the help command (-h) for valid codes : {}".format(request))
                return await ctx.send("Error - No language codes provided (-l), please refer to the help command (-h) for valid codes : {}".format(request))
            
            invalid = [lang for lang in langs if not lang in list(LANGCODES.values())]
            
            if len(invalid) != 0:
                print("E - Invalid language code(s) provided (-l): {}. Please refer to the help command (-h) for valid codes: {}".format(" ".join(invalid), request))
                return await ctx.send("Error - Invalid language code(s) provided (-l): {}. Please refer to the help command (-h) for valid codes: {}".format(" ".join(invalid), request))
    
    print("S - Languages: {}".format(langs))
    print("S - No. of iterations: {}".format(n))
    print("S - Text to be translated: {}".format(text))

    await background_translate(ctx, text, langs, n)
    
@client.event
async def on_ready():
    print('S - Logged in as')
    print(client.user.name)
    print(client.user.id)

    server_listing = ", ".join([server.name for server in client.guilds])
    print("S - Active in {} servers: {}".format(len(client.guilds), server_listing))
    print('------')

    await client.change_presence(activity=Activity(type=ActivityType.watching, name="for !translate -h"))
    
@client.event
async def on_error(event, *args, **kwargs):
    print("Internal Error :(")

if __name__ == "__main__":
    client.run(TOKEN)