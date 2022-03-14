import discord
import os 
import requests #The requests module allows code to make an HTTP request
                #to get data from the API, and the API returns JSON.
import json     #The json module bc it will be easier to access the data from the API
import random   #Random module used for random messages.
from replit import db #Replit's database
from keep_alive import keep_alive

#Creates an instance of a client
client = discord.Client()

#List of words that relate to being sad. Anytime a user uses one of 
#these words, the bot will return a response.
sad_words = ["sad", "depressed", "unhappy", "angry", "miserable", "depressing"]

#A list of encouraging statements
starter_encouragements = [
  "Cheer up",
  "Hang in there!",
  "You are a great person!"
]

if "responding" not in db.keys():
  db["responding"] = True

#Returns a random quote from the API
def get_quote():
    response = requests.get("https://zenquotes.io/api/random") #API url
    json_data = json.loads(response.text)
    #'q' - represents the quote
    #'a' - represents the author of the quote
    quote = json_data[0]['q'] + ' -' + json_data[0]['a']
    return(quote)

def update_encouragements(encouraging_message):
  if("encouragements" in db.keys()):
    #Creates a list called encouragements and sets it equal to the db[key]
    encouragements = db["encouragements"] # encouragements = "You cool"
    encouragements.append(encouraging_message) #You cool, You are smart
    db["encouragements"] = encouragements      #"You cool" = 
  else:
    db["encouragements"] = [encouraging_message]

def delete_encouragement(index):
  encouragements = db["encouragements"]
  if(len(encouragements) > index):
    del encouragements[index]
    db["encouragements"] = encouragements

#When the bot is on and ready to use, it will print a message
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


#on_message event triggers each time a message is received.
@client.event
async def on_message(message):
    msg = message.content
    if message.author == client.user:
        return
    if msg.startswith('$inspire'):
        quote = get_quote()
        await message.channel.send(quote)

    if db["responding"]:
      options = starter_encouragements
      if "encouragements" in db.keys():
        options = options + list(db["encouragements"])
  
      #Bot will go through every word in the list of sad words
      #and see if any sad words are in the message
      if any(word in msg for word in sad_words):
        await message.channel.send(random.choice(options))

    #User command to add new encouraging message to the messages database.
    if msg.startswith("$new"):
      #Since the command will be in the format "$new happy to see you"
      #we want the message to only include the words after the command $new,
      #so we split the message into an array of size 2. Then take the value,
      #at index 1 and use that as the encouraging message.
      encouraging_message = msg.split("$new ", 1)[1]
      update_encouragements(encouraging_message)
      await message.channel.send("New encouraging message added.") 

    #User command to deleter an encouraging message 
    #from the messages database using a number to indicate the index.
    if msg.startswith("$del"):
      encouragements = []
      if("encouragements" in db.keys()):
        index = int(msg.split("$del", 1)[1])
        delete_encouragement(index)
        encouragements = db["encouragements"]
      await message.channel.send(list(encouragements))

    if msg.startswith("$list"):
      encouragements = []
      if "encouragements" in db.keys():
        encouragements = db["encouragements"]
      await message.channel.send(list(encouragements))

    if msg.startswith("$responding"):
      value = msg.split("$responding ", 1)[1]

      if value.lower() == "true":
        db["responding"] = True
        await message.channel.send("Responding is on.")
      else:
        db["responding"] = False
        await message.channel.send("Responding is off.")
        


#Runs the bot.
#keep_alive()
client.run(os.environ['TOKEN'])

