# slack-bot-skeleton

simple slack bot skeleton.

## Start with Slack-apps

1. Create a Slack account and workspace or join an existing workspace [here](https://slack.com/create).

    ![slack-1.png](assets/slack-1.png?raw=true "screenshot #1: create a Slack workspace")

2. Create a Slack app [here](https://api.slack.com/apps).

    ![slack-2.png](assets/slack-2.png?raw=true "screenshot #2: create a Slack app")

3. Add a Bot User.

    ![slack-3.png](assets/slack-3.png?raw=true "screenshot #3: Add a Bot User")

4. Install App.

    ![slack-4.png](assets/slack-4.png?raw=true "screenshot #4: Install App")

5. Integrate your bot with Slack channel.

    ![slack-5.png](assets/slack-5.png?raw=true "screenshot #5: Integrate your bot with Slack channel")

## Setup the environment

1. Clone this repository: `https://github.com/iSuperMostafa/slack-bot-skeleton.git`
2. Navigate to the project directory: `cd slack-bot-skeleton`
3. Create virtualenv: `virtualenv env`
4. Activate env: `source env/bin/activate`
5. Install pipenv: `pip install slackclient`
6. export secret tokens as environment variables: `export SLACK_BOT_TOKEN='REPLACE_WITH_YOUR_BOT_USER_ACCESS_TOKEN'`
7. Add your channel name to "channel" at bot/chatbot.py line 7

## Run the application

Run the bot: `python bot/chatbot.py`