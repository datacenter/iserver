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
            output = '<b>Welcome to <a href="https://wwwin-github.cisco.com/emear-telcocloud/iserver">iserver-bot</a> for Vimercate lab</b><br><br>'
            output = '%sUseful Links<br>' % (output)
            output = '%s- <a href="https://cisco.sharepoint.com/sites/EMEA-SP-Innovation-Lab/SitePages/Vimercate-Innovation-Lab.aspx">Lab sharepoint</a><br>' % (output)
            output = '%s- <a href="https://cisco.sharepoint.com/sites/EMEA-SP-Innovation-Lab/Lists/testCalendar/EMEA%%20SP%%20Innovation%%20Lab%%20Calendar.aspx?isAscending=false&viewid=695e1785%%2D292e%%2D4cfd%%2D95cb%%2Dc56a141f0669">Lab calendar</a><br>' % (output)
            output = '%s- <a href="https://cisco.sharepoint.com/:p:/s/EMEA-SP-Innovation-Lab/EYD9xxmR1YxLiMV-pDuPe94BYuW6YGXlV5kVS7btIDVfCA?e=KeTAP9">Wiring diagrams</a><br>' % (output)
            output = '%s- <a href="https://netbox-eu-spn.cisco.com">Netbox</a><br>' % (output)
            output = '%s<br>Notes<br>' % (output)
            output = '%s- only for authorized users<br>' % (output)
            output = '%s- join iserver-bot space to provide feedback and send requests<br>' % (output)

        except BaseException:
            output = '<b>Command execution failed [%s]</b>\n\n%s' % (command_run_id, traceback.format_exc())

        return output
