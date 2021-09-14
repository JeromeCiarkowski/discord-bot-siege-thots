# discord-bot-siege-thots
## Description

`Discord Bot Siege Thots` is a simple Discord bot Python script integrated with the Nanoleaf open API. The simple program allows for simple text commands from a Discord client to control a configured Nanoleaf.

## Purpose

Prototype for [Nanoleaf Integrations](https://github.com/JeromeCiarkowski/nanoleaf-integrations). Simplicity and iteration are keys for success! By limiting the scope, I was able to focus my efforts on integrating Discord with Nanoleaf--demonstrating a base case integration. Nanoleaf Integrations will reiterate on the base case to abstract common integration functionality for a more intuitive program.

# Getting Started
### Clone Discord Bot Siege Thots

```
> git clone git@github.com:JeromeCiarkowski/discord-bot-siege-thots.git
> cd discord-bot-siege-thots
```
### Create, Initialize Virtual Environment

```
> virtualenv -p python3 venv
> pip install -r requirements.txt
```

### Create an Environment File, Populate Variables

```
> touch .env
```

* `DISCORD_GUILD`, `DISCORD_TOKEN`, `NANOLEAF_AUTH_TOKEN`, and `NANOLEAF_IP_ADDRESS` are required variables.
    * [RealPython's How to Make a Discord Bot in Python](https://realpython.com/how-to-make-a-discord-bot-python/)
    * [nanoleafapi GitHub repository](https://github.com/MylesMor/nanoleafapi)


### Execute Bot.py

```
> python bot.py
```

### TODO
* Everything