import re
import sys
import shlex

def ex():
    sys.exit()

def find_in_list(lis, char):
    try:
        char_ind = lis.index(char)
        return char_ind
    except ValueError:
        return -1

request = '!translate -l de ko ja -n 50 kee-po'
request = '{}'.format(request)

args = shlex.split(request)

l_ind = find_in_list(args, "-l")
n_ind = find_in_list(args, "-n")
t_ind = find_in_list(args, "-t")
h_ind = find_in_list(args, "-h")

if h_ind != -1:
    print("Help information requested")
    


print(args)

ex()

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
