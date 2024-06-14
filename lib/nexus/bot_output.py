from lib import output_helper

from lib.nexus.lacp.bot_output import LacpBotOutput
from lib.nexus.lldp.bot_output import LldpBotOutput
from lib.nexus.mac.bot_output import MacBotOutput
from lib.nexus.version.bot_output import VersionBotOutput


class NexusBotOutput(
    LacpBotOutput,
    LldpBotOutput,
    MacBotOutput,
    VersionBotOutput
    ):
    def __init__(self, verbose=False, debug=False, log_id=None):
        self.my_output = output_helper.OutputHelper(
            log_id=log_id,
            verbose=verbose,
            debug=debug
        )
        LacpBotOutput.__init__(self)
        LldpBotOutput.__init__(self)
        MacBotOutput.__init__(self)
        VersionBotOutput.__init__(self)

    def print_devices(self, info, title=False):
        self.my_output.clear_output()

        if title:
            self.my_output.my_print(
                'Nexus Device [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.my_print('None')
            return self.my_output.get_output(), None

        order = [
            'name',
            'ip',
            'username',
            'domain',
            'cache_enabled',
            'cache_ttl',
            'cache_valid'
        ]

        headers = [
            'Name',
            'IP',
            'Username',
            'Domain',
            'Cache',
            'TTL',
            'Valid'
        ]

        self.my_output.my_table(
            info,
            order=order,
            headers=headers,
            underline=True,
            table=True,
            stream='output'
        )

        output = self.my_output.get_output()

        self.my_output.clear_output()

        self.my_output.my_table_html(
            info,
            order,
            headers,
            title='Nexus Device'
        )

        html_output = self.my_output.get_output()

        return output, html_output

    def print_devices_cache(self, info, title=False):
        self.my_output.clear_output()

        if title:
            self.my_output.my_print(
                'Nexus Cache [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.my_print('None')
            return self.my_output.get_output(), None

        order = [
            'name',
            'cache_enabled',
            'cache_ttl',
            'cache_valid',
            'cache_command.command',
            'cache_command.time',
            'cache_command.valid'
        ]

        headers = [
            'Name',
            'Cache',
            'TTL',
            'Valid',
            'Command',
            'Time',
            'Valid'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['cache_command']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            table=True,
            stream='output'
        )

        output = self.my_output.get_output()

        self.my_output.clear_output()

        self.my_output.my_table_html(
            info,
            order,
            headers,
            title='Nexus Cache'
        )

        html_output = self.my_output.get_output()

        return output, html_output
