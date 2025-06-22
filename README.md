## DiscordBot
This application is a simple bot, live on Discord and deployed through Heroku, with features like Google search and checking past search history related to paricular keyword.

### Features
- Implemented Google Search API: command -> !google {type search_keyword u want to search} 
- Stores user search history on sqlite3: command -> !recent {type search_history_keyword u want to check}

### Implementation
It is divided in 3 parts:
- bot.py : Implemented bot commands
- google.py : Implemented google search api
- db.py :Implemented db connection to sqlite3, insert and query functions to store and retrive past history

