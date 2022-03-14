# Encouragement Bot

This Discord bot sends out encouraging messages whenever "sad" words are used or the users in the server explicitly want an inspiring quote.

Commands:
- $new (insert encouraging message here): User inserts a new encouraging message to the database.
     - Example: $new You are a great person!
     - Returns:  New encouraging message added.
- $del (to be deleted encouraging message): User inserts a new encouraging message to the database.
     - Example: $del You are a great person!
     - Returns: [('You are a great person!',), ('You are very cool!',), ('nice!',)] -----> [('You are very cool!',), ('nice!',)]
- $list: Lists all the possible inspiring messages in the database to the user.
     - Example: $list 
     - Returns: [('You are pretty cool!',), ('You are very cool!',), ('nice!',)]
- $responding: Returns true or false if the bot will respond to all "sad" words in all text messages or not.
     - Example: $responding false
     - Returns: Responding is off.

     - Example: $responding true
     - Returns: Responding is on.
- $inspire: Returns a random inspirational quote. 
    - Example: $inspire
    - Returns: When you are able to employ your will always for constructive purposes, you become the controller of your destiny. -Paramahansa Yogananda

## Installation

### For VS Code Version:
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the following before running:

```bash
pip install requests
pip install discord.py
pip install Flask
```

### For Repl.it Version:
`Link to the Repl.it Repository` : &nbsp;&nbsp;&nbsp;&nbsp; <https://replit.com/@KiranAziz/Encourage-Bot#main.py>

## Demo
