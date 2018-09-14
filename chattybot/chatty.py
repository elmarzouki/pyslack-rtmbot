import os
import time
from chattybot.brain import Brain


# brain = Brain('chatty')


def __get_dummy_message_replay__(user, message):
    # echo the message
    return "New echo <@{}>: {}".format(user, message)


def __get_smart_message_replay__(user, message):
    # call the NLP lib to get a proper response
    # return brain.get_reponse(message)
    pass


def get_message_replay(user, message):
    dummy_replay = __get_dummy_message_replay__(user, message)
    smart_replay = __get_smart_message_replay__(user, message)
    return dummy_replay