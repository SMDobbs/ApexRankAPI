import sys
import requests
import json

#The two lines below this seek user input to find out what user they want to lookup and on what console
account = input('What user would you like to look up? ')
console = input('Do they play on PS4 PC or X1? ')

#Using the two variables above we now call the API function and convert our output to a JSON object
string = 'https://api.mozambiquehe.re/bridge?version=5&platform=' + console + '&player=' + account + '&auth=4fNjzJl9h3pReB5XjVCj'
r = requests.get(string)
obj = r.json()

#We now comb through the output from the API Call to locate the variables we want. Below we are parsing them out
name = obj["global"]["name"]
rank = obj['global']['rank']['rankName']
div = obj['global']['rank']['rankDiv']

#Using our variables we print out the resposne to our user
print(name + " is currently ranked " + rank  + " " + str(div))