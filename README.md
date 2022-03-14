# Encouragement Bot

This Discord bot sends out encouraging messages whenever "sad" words are used or the users in the server explicitly want an inspiring quote.

Commands:
- $new (insert encouraging message here): User inserts a new encouraging message to the database.
     - Example: $new You are a great person!
- $del (to be deleted encouraging message): User inserts a new encouraging message to the database.
     - Example: $del You are a great person!
- $list: Lists all the possible inspiring messages in the database to the user.
     - Example: $list You are a great person! <br />
- $responding: 
- $inspire: 

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install discord
pip install flask
```

## Usage

```python
import foobar

# returns 'words'
foobar.pluralize('word')

# returns 'geese'
foobar.pluralize('goose')

# returns 'phenomenon'
foobar.singularize('phenomena')
```
