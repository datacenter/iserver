from lib import output_helper

from lib.psirt.advisory.output import PsirtAdvisoryOutput


class PsirtOutput(
    PsirtAdvisoryOutput
    ):
    def __init__(self, verbose=False, debug=False, log_id=None):
        self.my_output = output_helper.OutputHelper(
            log_id=log_id,
            verbose=verbose,
            debug=debug
        )

        PsirtAdvisoryOutput.__init__(self)

    def print_psirt_settings(self, psirt_settings, show_password=False):
        if not show_password:
            psirt_settings['key'] = '***'
            psirt_settings['secret'] = '***'

        order = [
            'enabled',
            'key',
            'secret',
            'cache',
            'directory',
            'ttl'
        ]

        headers = [
            'Enabled',
            'Key',
            'Secret',
            'Cache',
            'Directory',
            'TTL'
        ]
        self.my_output.dictionary(
            psirt_settings,
            keys=order,
            title_keys=headers,
            title='Psirt API settings'
        )
