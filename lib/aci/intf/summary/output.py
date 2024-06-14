import time

import concurrent.futures
from concurrent.futures import ProcessPoolExecutor


class InterfaceSummaryOutput():
    def __init__(self):
        pass

    def print_interface_summary(self, summary):
        order = [
            'cloudsec.portSummary',
            'fc.portSummary',
            'fcpc.portSummary',
            'l3e.portSummary',
            'lb.portSummary',
            'macsec.portSummary',
            'mgmt.portSummary',
            'pc.portSummary',
            'phy.portSummary',
            'svi.portSummary',
            'tun.portSummary',
            'vfc.portSummary',
            'vpc.portSummary'
        ]

        headers = [
            'cloudsec',
            'fc',
            'fcpc',
            'l3e',
            'lb',
            'macsec',
            'mgmt',
            'pc',
            'phy',
            'svi',
            'tun',
            'vfc',
            'vpc'
        ]

        self.my_output.dictionary(
            summary,
            title='Interface State Summary',
            underline=True,
            prefix="- ",
            justify=True,
            keys=order,
            title_keys=headers
        )

        order = [
            'uplinkSummary',
            'downlinkSummary',
            '100MSummary',
            '1GSummary',
            '10GSummary',
            '25GSummary',
            '40GSummary',
            '100GSummary',
            '400GSummary'
        ]

        headers = [
            'Uplink',
            'Downlink',
            '100M',
            '1G',
            '10G',
            '25G',
            '40G',
            '100G',
            '400G'
        ]

        self.my_output.dictionary(
            summary['phy'],
            title='Physical Interfaces',
            underline=True,
            prefix="- ",
            justify=True,
            keys=order,
            title_keys=headers
        )
