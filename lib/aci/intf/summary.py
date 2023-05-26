import time

import concurrent.futures
from concurrent.futures import ProcessPoolExecutor

from lib import log_helper


class InterfaceSummary():
    def __init__(self, log_id=None):
        self.log = log_helper.Log(log_id=log_id)

    def get_interface_type_summary(self, pod_id, node_id, interface_type):
        if interface_type == 'cloudsec':
            self.initialize_interface_cloudsec(
                pod_id=pod_id,
                node_id=node_id
            )

            interfaces = self.get_interface_cloudsec_summary(
                pod_id,
                node_id
            )

        if interface_type == 'fc':
            self.initialize_interface_fc(
                pod_id=pod_id,
                node_id=node_id
            )

            interfaces = self.get_interface_fc_summary(
                pod_id,
                node_id
            )

        if interface_type == 'fcpc':
            self.initialize_interface_fcpc(
                pod_id=pod_id,
                node_id=node_id
            )

            interfaces = self.get_interface_fcpc_summary(
                pod_id,
                node_id
            )

        if interface_type == 'l3e':
            self.initialize_interface_encap_routed(
                pod_id=pod_id,
                node_id=node_id
            )

            interfaces = self.get_interface_encap_routed_summary(
                pod_id,
                node_id
            )

        if interface_type == 'lb':
            self.initialize_interface_loopback(
                pod_id=pod_id,
                node_id=node_id
            )

            interfaces = self.get_interface_looback_summary(
                pod_id,
                node_id
            )

        if interface_type == 'macsec':
            self.initialize_interface_macsec(
                pod_id=pod_id,
                node_id=node_id
            )

            interfaces = self.get_interface_macsec_summary(
                pod_id,
                node_id
            )

        if interface_type == 'mgmt':
            self.initialize_interface_management(
                pod_id=pod_id,
                node_id=node_id
            )

            interfaces = self.get_interface_management_summary(
                pod_id,
                node_id
            )

        if interface_type == 'pc':
            self.initialize_interface_port_channels(
                pod_id=pod_id,
                node_id=node_id
            )

            interfaces = self.get_interface_port_channel_summary(
                pod_id,
                node_id
            )

        if interface_type == 'phy':
            interfaces = self.get_ports_summary(
                pod_id,
                node_id
            )

        if interface_type == 'svi':
            self.initialize_interface_svi(
                pod_id=pod_id,
                node_id=node_id
            )

            interfaces = self.get_interface_svi_summary(
                pod_id,
                node_id
            )

        if interface_type == 'tun':
            self.initialize_interface_tunnel(
                pod_id=pod_id,
                node_id=node_id
            )

            interfaces = self.get_interface_tunnel_summary(
                pod_id,
                node_id
            )

        if interface_type == 'vfc':
            self.initialize_interface_vfc(
                pod_id=pod_id,
                node_id=node_id
            )

            interfaces = self.get_interface_vfc_summary(
                pod_id,
                node_id
            )

        if interface_type == 'vpc':
            self.initialize_interface_virtual_port_channels(
                pod_id=pod_id,
                node_id=node_id
            )

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
                timeout=5,
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
