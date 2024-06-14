from lib import output_helper

from lib.aci.endpoint.bot_output import EndpointBotOutput
from lib.aci.node.bot_output import NodeBotOutput
from lib.aci.proto.bot_output import ProtocolBotOutput


class ApicBotOutput(
    EndpointBotOutput,
    NodeBotOutput,
    ProtocolBotOutput
    ):
    def __init__(self, verbose=False, debug=False, log_id=None):
        self.my_output = output_helper.OutputHelper(
            log_id=log_id,
            verbose=verbose,
            debug=debug
        )
        self.is_apic = True

        EndpointBotOutput.__init__(self)
        NodeBotOutput.__init__(self)
        ProtocolBotOutput.__init__(self)

    def print_apic_controllers(self, controllers, title=False):
        self.my_output.clear_output()

        controllers = sorted(
            controllers,
            key=lambda i: i['name']
        )

        for controller in controllers:
            controller['__Output'] = {}

            if controller['online']:
                controller['onlineTick'] = '\u2713'
                controller['__Output']['onlineTick'] = 'Green'
            else:
                controller['onlineTick'] = '\u2717'
                controller['__Output']['onlineTick'] = 'Red'

            if controller['cache']['enabled']:
                controller['cache']['enabledTick'] = '\u2713'
                controller['__Output']['cache.enabledTick'] = 'Green'
            else:
                controller['cache']['enabledTick'] = '\u2717'
                controller['__Output']['cache.enabledTick'] = 'Red'

            if controller['cache']['enabled']:
                if len(controller['cache']['object']):
                    controller['cache']['objectTick'] = '\u2713'
                    controller['__Output']['cache.objectTick'] = 'Green'
                else:
                    controller['cache']['objectTick'] = '\u2717'
                    controller['__Output']['cache.objectTick'] = 'Red'

            if not controller['cache']['enabled']:
                controller['cache']['ttlT'] = '--'
                controller['cache']['objectTick'] = '--'

        if title:
            self.my_output.my_print(
                'APIC [#%s]' % (len(controllers)),
                underline=True,
                before_newline=True
            )

        order = [
            'name',
            'ip',
            'port',
            'username',
            'domain',
            'cache.enabledTick',
            'cache.ttlT'
        ]

        headers = [
            'Name',
            'IP',
            'Port',
            'Username',
            'Domain',
            'Cache',
            'TTL'
        ]

        self.my_output.my_table(
            controllers,
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            table=True,
            stream='output'
        )

        output = self.my_output.get_output()

        self.my_output.clear_output()

        self.my_output.my_table_html(
            controllers,
            order,
            headers,
            title='APIC'
        )

        html_output = self.my_output.get_output()

        return output, html_output
