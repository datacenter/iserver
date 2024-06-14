import uuid
import traceback
import logging

from lib.webex_bot.models.command import Command
from lib import log_helper

logger = logging.getLogger(__name__)


class GetXxxCommand(Command):
    def __init__(self):
        super().__init__(
            command_keyword="get xxx",
            help_message="Get xxx state",
            card=None,
        )
        self.run_id = 'bot.%s' % (str(uuid.uuid4()).rsplit('-', maxsplit=1)[-1])
        self.log_handler = log_helper.Log(self.run_id)
        self.log_handler.initialize()
        self.link = 'https://wwwin-github.cisco.com/emear-telcocloud/iserver'
        logger.info('Command initialized: get xxx [%s]', self.run_id[4:])

    def help(self):
        output = 'Get state of xxx'
        return output

    def parse(self, message):
        parse = {}
        parse['success'] = True
        parse['error'] = ''

        return parse

    def execute(self, message, attachment_actions, activity):
        command_run_id = 'bot.%s' % (str(uuid.uuid4()).rsplit('-', maxsplit=1)[-1])
        self.log_handler = log_helper.Log(command_run_id)
        self.log_handler.initialize()

        logger.info('Command execution: get nx [%s]', command_run_id[4:])

        if message.strip().lower() in ['help', '?', '--help']:
            return self.help()

        parsed = self.parse(message)
        if not parsed['success']:
            logger.info(parsed['error'])
            return parsed['error']

        try:
            output = 'command response'

        except BaseException:
            output = 'Command execution failed [%s]\n\n%s' % (command_run_id, traceback.format_exc())

        return output
