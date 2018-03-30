# slack-bot-skeleton

simple slack bot skeleton.

## Getting Started

Clone this repository: `https://github.com/iSuperMostafa/slack-bot-skeleton.git`

## Setup the environment

1. Create virtualenv: `virtualenv env`
2. Activate env: `source env/bin/activate`
3. Install pipenv: `pip install slackclient`

## Start with Slack-apps

1. create a Slack app [here](https://api.slack.com/apps).

    ![slack#1.png](assets/slack-1.png?raw=true "screenshot #1: create slack app")

2. Add a Bot User.

    ![slack#2.png](assets/slack-2.png?raw=true "screenshot #1: Add a Bot User")

3. Install App.

    ![slack#3.png](assets/slack-3.png?raw=true "screenshot #1: Install App")

4. export secret tokens as environment variables: `export SLACK_BOT_TOKEN='REPLACE_WITH_YOUR_BOT_USER_ACCESS_TOKEN'`

## Run the application

Run the bot: `python bot/chatbot.py`