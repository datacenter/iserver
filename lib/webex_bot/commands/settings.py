import uuid
import traceback
import logging

from lib import log_helper
from lib import output_helper
from lib import iaccount_helper
from lib.intersight import settings as intersight_settings
from lib.nexus import settings as nexus_settings
from lib.nexus import bot_output as nexus_bot_output
from lib.aci import settings as aci_settings
from lib.aci import bot_output as aci_bot_output
from lib.webex_bot.models.command import Command

logger = logging.getLogger(__name__)


class SettingsCommand(Command):
    def __init__(self, url):
        super().__init__(
            command_keyword="settings",
            help_message="settings",
            card=None,
        )
        self.run_id = 'bot.%s' % (str(uuid.uuid4()).rsplit('-', maxsplit=1)[-1])
        self.log_handler = log_helper.Log(self.run_id)
        self.log_handler.initialize()
        self.url = url
        logger.info('Command initialized: settings [%s]', self.run_id[4:])

    def print_intersight_settings(self, command_run_id):
        my_output = output_helper.OutputHelper(
            log_id=command_run_id
        )

        output = ''
        output_html = ''

        intersight_settings_handler = intersight_settings.IntersightSettings(log_id=command_run_id)
        settings = intersight_settings_handler.get_intersight_settings()
        logger.info(settings)

        iaccount_handler = iaccount_helper.IntersightAccount()
        accounts = iaccount_handler.get_iaccounts()

        if len(accounts) == 0:
            return output, output_html

        for account in accounts:
            account['cache_enabled'] = settings['CacheEnabled']
            account['ttl'] = settings['CacheTtl']

        my_output.clear_output()

        my_output.my_print(
            'Intersight',
            underline=True,
            before_newline=True
        )

        order = [
            'name',
            'account',
            'role',
            'cache_enabled',
            'ttl'
        ]

        headers = [
            'Name',
            'Account',
            'Role',
            'Cache',
            'TTL'
        ]

        my_output.my_table(
            accounts,
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            table=True,
            stream='output'
        )

        output = my_output.get_output()

        return output, None

    def execute(self, message, attachment_actions, activity):
        command_run_id = 'bot.%s' % (str(uuid.uuid4()).rsplit('-', maxsplit=1)[-1])
        self.log_handler = log_helper.Log(command_run_id)
        self.log_handler.initialize()

        logger.info('Command execution: get settings [%s]', command_run_id[4:])

        try:
            nexus_settings_handler = nexus_settings.NexusSettings(log_id=command_run_id)
            nexus_bot_output_handler = nexus_bot_output.NexusBotOutput(log_id=command_run_id)

            aci_settings_handler = aci_settings.ApicSettings(log_id=command_run_id)
            aci_bot_output_handler = aci_bot_output.ApicBotOutput(log_id=command_run_id)

            output = ''
            output_html = ''

            view_output, view_output_html = self.print_intersight_settings(
                command_run_id
            )
            output = output + view_output

            view_output, view_output_html = aci_bot_output_handler.print_apic_controllers(
                aci_settings_handler.get_apic_controllers(),
                title=True
            )
            output = output + view_output

            view_output, view_output_html = nexus_bot_output_handler.print_devices(
                nexus_settings_handler.get_nexus_devices(),
                title=True
            )
            output = output + view_output

            output = aci_bot_output_handler.my_output.sanitize_bot_output(
                output,
                output_html,
                self.url
            )

            logger.info('Output prepared')

        except BaseException:
            output = '<b>Command execution failed [%s]</b>\n\n%s' % (command_run_id, traceback.format_exc())

        return output
