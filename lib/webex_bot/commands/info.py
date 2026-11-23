import uuid
import traceback
import logging

from lib import log_helper
from lib.webex_bot.models.command import Command

logger = logging.getLogger(__name__)


class InfoCommand(Command):
    def __init__(self):
        super().__init__(
            command_keyword="info",
            help_message="info",
            card=None,
        )
        self.run_id = 'bot.%s' % (str(uuid.uuid4()).rsplit('-', maxsplit=1)[-1])
        self.log_handler = log_helper.Log(self.run_id)
        self.log_handler.initialize()
        logger.info('Command initialized: info [%s]', self.run_id[4:])

    def execute(self, message, attachment_actions, activity):
        command_run_id = 'bot.%s' % (str(uuid.uuid4()).rsplit('-', maxsplit=1)[-1])
        self.log_handler = log_helper.Log(command_run_id)
        self.log_handler.initialize()

        logger.info('Command execution: get info [%s]', command_run_id[4:])

        try:
            output = '<b>Welcome to iserver-bot</b><br><br>'
            output = '%s<br>Notes<br>' % (output)
            output = '%s- only for authorized users<br>' % (output)
            output = '%s- join iserver-bot space to provide feedback and send requests<br>' % (output)

        except BaseException:
            output = '<b>Command execution failed [%s]</b>\n\n%s' % (command_run_id, traceback.format_exc())

        return output
