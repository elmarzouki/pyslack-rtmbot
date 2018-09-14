# pyslack-rtmbot

Slack-Bot interacting with events from [Slack's RTM API](https://api.slack.com/rtm) integrated with [ChatterBot](https://chatterbot.readthedocs.io/en/stable/).

## Setup the environment

1. Setup [slack app](slack/README.md).
2. Clone this repository: `git clone git@github.com:iSuperMostafa/pyslack-rtmbot.git`
3. Navigate to the project directory: `cd pyslack-rtmbot`
4. If you don't have virtualenv Installed, Install it: `pip install virtualenv`
5. Create virtualenv: `virtualenv env -p python3`
6. Activate env:
    ```bash
    source env/bin/activate         # if you're using linux :')
    env\Scripts\activate            # if you're using windows -_-
    ```
7. Install requirements: `pip install -r requirements.txt`
8. configure your tokens and settings:
    ```bash
    cp slack/config.ini slack/config.override.ini
    nano slack/config.override.ini   # or open the file and edit the variables manually
    ```
    
## Run the application

Run the bot: `python app.py`

## Add Some NLP Magic to the bot
`
Return the smart_replay at bot/chatbot.py - get_message_replay method
```python
def get_message_replay(user, meesage):
    # dummy_replay = __get_dummy_message_replay__(user, message)
    smart_replay = __get_smart_message_replay__(user, message)
    return smart_replay
```
