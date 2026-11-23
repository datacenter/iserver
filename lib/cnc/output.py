from lib import output_helper
from lib.cnc.node.output import NodeOutput


class CncOutput(
        NodeOutput
    ):
    def __init__(self, verbose=False, debug=False, log_id=None):
        self.my_output = output_helper.OutputHelper(
            log_id=log_id,
            verbose=verbose,
            debug=debug
        )
        self.is_cnc = True

        NodeOutput.__init__(self)

    def set_cnc_off(self):
        self.is_cnc = False

    def print_cnc_controllers(self, controllers, show_password=False):
        controllers = sorted(
            controllers,
            key=lambda i: i['name']
        )

        for controller in controllers:
            controller['__Output'] = {}
            if not show_password:
                controller['password'] = '******'

        order = [
            'name',
            'ip',
            'port',
            'username',
            'password',
            'domain'
        ]

        headers = [
            'Name',
            'IP',
            'Port',
            'Username',
            'Password',
            'Domain'
        ]

        self.my_output.my_table(
            controllers,
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            table=True
        )
