# Twitch Spotlight

Currently 95% of streamers on Twitch have 5 viewers or less. As 5% of streamers have most of the audience, this project aims to change that by giving more exposure to small streamers!

Twitch Spotligh is a concept first created by superjp, on a web app called [petitstream.com](https://petitstream.com/) (for french streamers). The idea is simple:
- A random streamer that has 5 viewers or less is chosen and displayed on the website.
- Every 5 minutes a new stream starts, choosing a new random streamer!


This project provides a django server that allows you to setup such a web app for any language.

## Setup
-------------
### Twitch API
The first step is to setup the Twitch API app keys. You can do so by setting up the environment variables `TWITCH_SPOTLIGHT_APP_ID` and `TWITCH_SPOTLIGHT_APP_SECRET`. You can generate you keys on the [Twitch developper console](https://dev.twitch.tv/console/apps).

On Windows
```bash
set TWITCH_SPOTLIGHT_APP_ID=mykeyhere
set TWITCH_SPOTLIGHT_APP_SECRET=mysecretkeyhere
```

On Linux
```bash
export TWITCH_SPOTLIGHT_APP_ID=mykeyhere
export TWITCH_SPOTLIGHT_APP_SECRET=mysecretkeyhere
```

### Install requirements
```bash
pip install -r requirements.txt
```

### Migrate models
```bash
python manage.py migrate
```

## Running the server

```
python manage.py runserver
```

If using VSCode launch settings are available for making migrations, migrating and running the server.