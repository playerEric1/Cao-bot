# CaoBot


[![Python3](https://img.shields.io/badge/python-3.10-blue.svg)](https://github.com/Der-Eddy/discord_bot)
[![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/Der-Eddy/discord_bot/master/LICENSE)
[![Discord Server](https://img.shields.io/badge/Support-Discord%20Server-blue.svg)](https://discord.gg/qTT64Nq59W)
![AWS](https://img.shields.io/badge/AWS-%23FF9900.svg?style=for-the-badge&logo=amazon-aws&logoColor=white)

CaoBot is a discord bot that contains a number of features to help with mathematics and other common utilities.

It's primary features include:

- Querying Wikipedia and generate a thumbnail
- Generating random numbers
- Quick image search
- Querying Wolfram|Alpha
- LaTeX rendering
- A Turing complete calculator


[Add the bot to your own server](https://discord.com/oauth2/authorize?client_id=1038261014409519155&permissions=8&scope=bot)


## Setup for use

The bot is currently developed for python `3.10.8`.

```bash
git clone https://github.com/playerEric1/Cao-bot.git
cd mathbot
pipenv --python 3.10
```

[Get your own discord bot token](https://discord.com/developers/applications).


Then navigate into the `cao-bot` directory and add the tokens to the .env file and run the bot with `python3.10 bot.py`.


## Contributing guide

Relevent discussion takes place on the CaoBot [Discord server](https://discord.gg/qTT64Nq59W).

Feel free to fork the repo and make a pull request once you've made the changes. 


## Setting up Wolfram|Alpha

1. [Grab yourself an API key](https://products.wolframalpha.com/api/)
2. Open .env and change add a row: WFA_APPID=ABCDEF (The API key you just got)

This should only be used for development and personal use.

## Links
- [Official Discord Server](https://discord.gg/qTT64Nq59W)
