# JOMD
JOMD is a Discord bot for [Dmoj](https://dmoj.ca/) Inspired by [TLE](https://github.com/cheran-senthil/TLE)

**Add the bot [here](https://discord.com/api/oauth2/authorize?client_id=725004198466551880&permissions=0&scope=bot)!**

## Previews
Point history

<img src="images/plot_points.png" width=500>

Rating history

<img src="images/plot_rating.png" width=500>

Point prediction

<img src="images/predict.png" width=500>

# Features
The features of JOMD are split up into seperate cogs each handling their related commands.

### User Cog
```
  cache      Caches the submissions of a user, will speed up other commands
  gimme      Recommend a problem
  predict    Predict total points after solving N pointer problem(s)
  user       Show user profile and latest submissions
  vc         Suggest a contest
```

### Plot Cog
```
  points Plot point progression
  rating Plot rating progression
  type   Graph problems solved by popular problem types
```

### Handles Cog

```
  link       Links your discord account to your dmoj account
  set        Manually link two accounts together
  unlink     Unlink your discord account with your dmoj account
  whois      Shows the discord account linked to the relevant dmoj account
```

# Setup

To setup the bot first clone the repository and cd into it

```
git clone https://github.com/JoshuaTianYangLiu/JOMD.git
cd JOMD
```


Make sure you have python3.7 installed.

```
apt-get install python3.7
```

Install relevant packages

```
pip3.7 install -r requirements.txt
```

Add your discord bot token with

```
export JOMD_BOT_TOKEN="INSERT BOT TOKEN HERE"
```

If you also want to add your DMOJ api token use

```
export JOMD_TOKEN="INSERT DMOJ API TOKEN HERE"
```

Run the bot with

```
python3.7 Main.py
```

# Usage
To use the bot, use the `+` prefix

# Contributing
Pull requests are welcomed and encouraged.
