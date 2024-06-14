import uuid
import traceback
import logging

from lib import log_helper
from lib.webex_bot.models.command import Command

logger = logging.getLogger(__name__)


class WhoamiCommand(Command):
    def __init__(self, approved_users):
        super().__init__(
            command_keyword="whoami",
            help_message="whoami",
            card=None,
        )
        self.approved_users = approved_users
        self.run_id = 'bot.%s' % (str(uuid.uuid4()).rsplit('-', maxsplit=1)[-1])
        self.log_handler = log_helper.Log(self.run_id)
        self.log_handler.initialize()
        logger.info('Command initialized: whoami [%s]', self.run_id[4:])

    def execute(self, message, attachment_actions, activity):
        command_run_id = 'bot.%s' % (str(uuid.uuid4()).rsplit('-', maxsplit=1)[-1])
        self.log_handler = log_helper.Log(command_run_id)
        self.log_handler.initialize()

        logger.info('Command execution: whoami [%s]', command_run_id[4:])

        try:
            output = ''

            output = '%s<u>Webex</u><br>' % (output)
            output = '%s- id: %s<br>' % (output, activity['actor']['id'])
            output = '%s- name: %s<br>' % (output, activity['actor']['displayName'])
            output = '%s- email: %s<br>' % (output, activity['actor']['emailAddress'])

            for user in self.approved_users:
                if user['username'] == activity['actor']['emailAddress']:
                    output = '%s<br><u>Bot</u><br>' % (output)
                    output = '%s- role: %s<br>' % (output, user['role'])

        except BaseException:
            output = '<b>Command execution failed [%s]</b>\n\n%s' % (command_run_id, traceback.format_exc())

        return output
