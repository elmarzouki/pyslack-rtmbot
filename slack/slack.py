import logging
import configparser
from slackclient import SlackClient
from chattybot.chatty import *

BASE_DIR = os.path.join(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__))), 'slack')


logging.basicConfig(
    stream=logging.StreamHandler(),
    level=logging.DEBUG,
    format="%(asctime)s:%(levelname)s:%(message)s"
)


class Slack:
    def __init__(self):
        self.bot_token = None
        self.channel = None
        self.slack_client = None
        self.chatbot_id = None
        self.rtm_read_delay = 1

    def __configure__(self):
        # read slack configurations from config.override.ini
        config = configparser.ConfigParser()
        path = BASE_DIR + '/' + 'config.override.ini'
        config.read(path)
        # set configurations
        self.bot_token = config['SLACK']['access_token']
        self.channel = config['SLACK']['channel']
        # instantiate Slack client
        self.slack_client = SlackClient(self.bot_token)
        # constants
        self.rtm_read_delay = int(config['SLACK']['rtm_read_delay'])
        return self

    def __connect__(self):
        # Connect to slack
        if self.slack_client.rtm_connect(with_team_state=False):
            logging.debug("The chatty connected and running!")
            # Send a connection success message
            self.slack_client.api_call(
                "chat.postMessage",     # slack web API
                channel=self.channel,
                text="The chatty connected and running!"
            )
            # Read bot's user ID by calling Web API method `auth.test`
            self.chatbot_id = self.slack_client.api_call("auth.test")["user_id"]

            while True:
                # Read latest messages
                for slack_message in self.slack_client.rtm_read():
                    message = slack_message.get("text")
                    user = slack_message.get("user")
                    if not message or not user:
                        continue
                    # logging message received
                    logging.debug("New message send: '{}' from: {}".
                                  format(message, user))
                    message_replay = get_message_replay(user, message)
                    self.slack_client.api_call(
                        "chat.postMessage",
                        channel=self.channel,
                        text=message_replay
                    )
                    # logging message sent
                    logging.debug("New message send: '{}' to: {}".
                                  format(message_replay, self.channel))
                # a second delay between reading from RTM
                time.sleep(self.rtm_read_delay)
        else:
            logging.debug("Couldn't connect to slack!")

    def run_bot(self):
        self.__configure__().__connect__()
