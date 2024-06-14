import time

import concurrent.futures
from concurrent.futures import ProcessPoolExecutor


class InterfaceSummary():
    def __init__(self):
        self.interface_types = [
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

    def get_interface_summary_output(self, port_up, port_down, port_count):
        if port_up == 0 and port_down == 0 and port_count == 0:
            return ('0/0/0', '')

        output = ''
        color = ':'

        output = '%s%s/' % (output, port_up)
        port_color = ''.join(['G' * len(str(port_up))])
        color = '%s%s.' % (color, port_color)

        output = '%s%s/' % (output, port_down)
        if port_down == 0:
            port_color = '.'
            color = '%s%s.' % (color, port_color)
        else:
            port_color = ''.join(['R' * len(str(port_down))])
            color = '%s%s.' % (color, port_color)

        output = '%s%s' % (output, port_count)
        port_color = ''.join(['.' * len(str(port_up))])
        color = '%s%s' % (color, port_color)

        return (output, color)

    def get_interface_type_summary(self, pod_id, node_id, interface_type):
        if interface_type == 'cloudsec':
            interfaces = self.get_interface_cloudsec_summary(
                pod_id,
                node_id
            )

        if interface_type == 'fc':
            interfaces = self.get_interface_fc_summary(
                pod_id,
                node_id
            )

        if interface_type == 'fcpc':
            interfaces = self.get_interface_fcpc_summary(
                pod_id,
                node_id
            )

        if interface_type == 'l3e':
            interfaces = self.get_interface_encap_routed_summary(
                pod_id,
                node_id
            )

        if interface_type == 'lb':
            interfaces = self.get_interface_looback_summary(
                pod_id,
                node_id
            )

        if interface_type == 'macsec':
            interfaces = self.get_interface_macsec_summary(
                pod_id,
                node_id
            )

        if interface_type == 'mgmt':
            interfaces = self.get_interface_management_summary(
                pod_id,
                node_id
            )

        if interface_type == 'pc':
            interfaces = self.get_interface_port_channel_summary(
                pod_id,
                node_id
            )

        if interface_type == 'phy':
            interfaces = self.get_interfaces_phy_summary(
                pod_id,
                node_id
            )

        if interface_type == 'svi':
            interfaces = self.get_interface_svi_summary(
                pod_id,
                node_id
            )

        if interface_type == 'tun':
            interfaces = self.get_interface_tunnel_summary(
                pod_id,
                node_id
            )

        if interface_type == 'vfc':
            interfaces = self.get_interface_vfc_summary(
                pod_id,
                node_id
            )

        if interface_type == 'vpc':
            interfaces = self.get_interface_virtual_port_channel_summary(
                pod_id,
                node_id
            )

        self.log.apic_mo(
            'intf_%s_summary' % (interface_type),
            interfaces
        )

    def get_interface_summary(self, pod_id=None, node_id=None):
        start_time = int(time.time() * 1000)
        self.log.debug(
            'get_interface_summary',
            'Start summary collection preparation'
        )

        with ProcessPoolExecutor() as executor:
            pool = [executor.submit(self.get_interface_type_summary, pod_id, node_id, key) for key in self.interface_types]
            result = concurrent.futures.wait(
                pool,
                timeout=30,
                return_when=concurrent.futures.ALL_COMPLETED
            )
            self.log.debug(
                'get_interface_summary',
                'Not completed: %s' % (str(result[1]))
            )
            executor.shutdown(
                wait=False,
                cancel_futures=True
            )

        duration = int(time.time() * 1000) - start_time
        self.log.debug(
            'get_interface_summary',
            'Finished summary collection: %s ms' % (duration)
        )

        summary = {}
        summary['__Output'] = {}
        for key in self.interface_types:
            summary[key] = self.log.get_apic_mo('intf_%s_summary' % (key))
            if summary[key] is None:
                self.log.error(
                    'get_interface_summary',
                    'Failed with %s' % (key)
                )
                continue

            for item in summary[key]['__Output']:
                summary['__Output']['%s.%s' % (key, item)] = summary[key]['__Output'][item]

        return summary

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
