# pyslack-rtmbot

Slack-Bot interacting with events from [Slack's RTM API](https://api.slack.com/rtm) integrated with [ChatterBot](https://chatterbot.readthedocs.io/en/stable/).

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

1. Clone this repository: `git clone git@github.com:iSuperMostafa/pyslack-rtmbot.git`
2. Navigate to the project directory: `cd slack-bot-skeleton`
3. If you don't have virtualenv Installed, Install it: `pip install virtualenv`
4. Create virtualenv: `virtualenv env`
5. Activate env:
    ```bash
    source env/bin/activate         # if you're using linux :')
    env\Scripts\activate            # if you're using windows -_-
    ```
6. Install requirements: `pip install -r requirements.txt`
7. export secret tokens as environment variables:
    ```bash
    export SLACK_BOT_TOKEN='REPLACE_WITH_YOUR_BOT_USER_ACCESS_TOKEN'    # if you're using linux :')
    SET SLACK_BOT_TOKEN='REPLACE_WITH_YOUR_BOT_USER_ACCESS_TOKEN'       # if you're using windows -_-
    ```
8. Add your channel name to **channel** at bot/chatbot.py line 7
    ```python
    channel = "REPLACE_WITH_YOUR_CHANNEL_NAME"
    ```

## Run the application

Run the bot: `python bot/chatbot.py`

## Add Some NLP Magic to the bot

1. Add your chatbot name to **brain** at bot/chatbot.py line 13
    ```python
    brain = Brain('REPLACE_WITH_YOUR_CHATBOT_NAME')
    ```

2. Return the smart_replay at bot/chatbot.py - get_message_replay method
    ```python
    def get_message_replay(user, meesage):
        dummy_replay = get_dummy_message_replay(user, message)
        smart_replay = get_smart_message_replay(user, message)
        return smart_replay
    ```
