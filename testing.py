import re
import sys

def ex():
    sys.exit()

request = '!translate -l de ko ja -n 50 -t kee-po'
request = '{}'.format(request)

request = request.split('!translate')[1].strip()

t_ind = request.find("-t")
text = request[t_ind+2:].strip()
options_str = request[:t_ind].strip()
    
args = options_str.split('-')[1:]
args = [arg.strip() for arg in args]

langs = []
n = -1

print("=" * 50)
print("New request received")

for arg in args:
    if arg.startswith('h'):
        print("Help information requested")
        
        # return await ctx.send(HELP_TEXT)
    if arg.startswith('l'):
        langs = arg.split(' ')[1:]
        if len(langs) == 0:
        #   return await ctx.send("Invalid language codes (-l): {}".format(message.content))
            print("Invalid language codes (-l): {}".format(request))
        
    if arg.startswith('n'):
        try:
            n = int(arg.split(' ')[1])
        except ValueError:
            # return await ctx.send("Invalid no. of translations (-n): {}".format(message.content))
            print("Invalid no. of translations (-n): {}".format(request))
            
print("*" * 20)
print("Languages: {}".format(langs))
print("No. of iterations: {}".format(n))
print("Text to be translated: {}".format(text))
