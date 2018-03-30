import os
import time
from slackclient import SlackClient
from brain import Brain

bot_token = os.environ.get('SLACK_BOT_TOKEN')
channel = "REPLACE_WITH_YOUR_CHANNEL_NAME"
# instantiate Slack client
slack_client = SlackClient(bot_token)
chatbot_id = None
# constants
rtm_read_delay = 1
brain = Brain('REPLACE_WITH_YOUR_CHATBOT_NAME')


def get_dummy_message_replay(user, message):
    # echo the message
    return "New echo <@{}>: {}".format(user, message)


def get_smart_message_replay(user, message):
    # call the NLP lib to get a proper response
    return brain.get_reponse(message)


def get_message_replay(user, message):
    dummy_replay = get_dummy_message_replay(user, message)
    smart_replay = get_smart_message_replay(user, message)
    return dummy_replay


def connect_slack():
    # Connect to slack
    if slack_client.rtm_connect(with_team_state=False):
        print("The Chatbot connected and running!")
        # Send a connection success message
        slack_client.api_call(
            "chat.postMessage",     # slack web API
            channel=channel,
            text="The Chatbot connected and running!"
        )
        # Read bot's user ID by calling Web API method `auth.test`
        chatbot_id = slack_client.api_call("auth.test")["user_id"]

        while True:
            # Read latest messages
            for slack_message in slack_client.rtm_read():
                message = slack_message.get("text")
                user = slack_message.get("user")
                if not message or not user:
                    continue
                message_replay = get_message_replay(user, message)
                slack_client.api_call(
                    "chat.postMessage",
                    channel=channel,
                    text=message_replay
                )
            # a second delay between reading from RTM
            time.sleep(rtm_read_delay)
    else:
        print("Couldn't connect to slack!")


if __name__ == '__main__':
    connect_slack()
