# Encouragement Bot

This Discord bot sends out encouraging messages whenever "sad" words are used or the users in the server explicitly want an inspiring quote.
![](https://github.com/kiranaziz/Encourage-Bot/blob/main/Discord%20Demo%20Photos/Sad%20Words.png)

### Commands:
- $new (insert encouraging message here): User inserts a new encouraging message to the database.
![](https://github.com/kiranaziz/Encourage-Bot/blob/main/Discord%20Demo%20Photos/New%20Message.png)
     - Example: $new nice!
     - Returns:  New encouraging message added.
- $del (to be deleted encouraging message): User deletes an encouraging message and returns list of remaining messages in the database.
![](https://github.com/kiranaziz/Encourage-Bot/blob/main/Discord%20Demo%20Photos/Delete%20Message.png)
     - Example: $del You are pretty cool!
     - Returns: [('You are pretty cool!',), ('You are very cool!',), ('nice!',)] -----> [('You are very cool!',), ('nice!',)]
- $list: Lists all the possible inspiring messages in the database to the user.
![](https://github.com/kiranaziz/Encourage-Bot/blob/main/Discord%20Demo%20Photos/List.png)
     - Example: $list 
     - Returns: [('You are very cool!',), ('nice!',)]
- $responding: Returns true or false if the bot will respond to all "sad" words in all text messages or not.
![](https://github.com/kiranaziz/Encourage-Bot/blob/main/Discord%20Demo%20Photos/Responding%20False.png)
     - Example: $responding false
     - Returns: Responding is off.
![](https://github.com/kiranaziz/Encourage-Bot/blob/main/Discord%20Demo%20Photos/Responding%20True.png)
     - Example: $responding true
     - Returns: Responding is on.
- $inspire: Returns a random inspirational quote.
![](https://github.com/kiranaziz/Encourage-Bot/blob/main/Discord%20Demo%20Photos/Inspirational%20Quote.png) 
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
