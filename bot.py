import sys

from django.conf import settings
from slack.slack import Slack


settings.configure(
    DEBUG=True,
    SECRET_KEY='I_AM_A_DUMMY_KEY_CHANGE_ME',
    ROOT_URLCONF=sys.modules[__name__],
    ALLOWED_HOSTS=['*'],
)


if __name__ == '__main__':
    slack = Slack()
    slack.run_bot()
