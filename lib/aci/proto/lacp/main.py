from lib import filter_helper

from lib.aci.proto.lacp.instance.main import ProtocolLacpInstance
from lib.aci.proto.lacp.interface.main import ProtocolLacpInterface
from lib.aci.proto.lacp.event.main import ProtocolLacpEvent


class ProtocolLacp(
        ProtocolLacpInstance,
        ProtocolLacpInterface,
        ProtocolLacpEvent
        ):
    def __init__(self):
        ProtocolLacpInstance.__init__(self)
        ProtocolLacpInterface.__init__(self)
        ProtocolLacpEvent.__init__(self)

    def match_protocol_lacp_interface(self, interface_info, interface_filter):
        if interface_filter is None or len(interface_filter) == 0:
            return True

        for ap_rule in interface_filter:
            key = ap_rule.split(':')[0]
            value = ':'.join(ap_rule.split(':')[1:])

            key_found = False

            if key == 'mac':
                key_found = True
                found = False
                for lacp_interface_info in interface_info['lacp']:
                    if 'adjacency' in lacp_interface_info and 'sysId' in lacp_interface_info['adjacency']:
                        for mac_address in value.split(','):
                            if filter_helper.match_mac(mac_address, lacp_interface_info['adjacency']['sysId']):
                                found = True
                                break

                if not found:
                    return False

            if not key_found:
                self.log.error(
                    'match_protocol_lacp_interface',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_protocol_lacp(
            self,
            pod_id,
            node_id,
            instance_info=False,
            interface_info=False,
            interface_filter=None,
            event_info=False,
            event_filter=None
            ):
        info = {}

        if instance_info:
            info['instance'] = self.get_protocol_lacp_instance(
                pod_id,
                node_id
            )

        if interface_info:
            interfaces_info = self.get_interface_port_channel(
                pod_id,
                node_id
            )

            lacp_interfaces = self.get_interface_lacp(
                pod_id,
                node_id,
                adjacency_info=True
            )

            for interface in interfaces_info:
                interface['lacp'] = []
                for lacp_interface in lacp_interfaces:
                    if lacp_interface['id'] in interface['state']['portId']:
                        interface['lacp'].append(
                            lacp_interface
                        )

            info['interfaces'] = []
            for interface in interfaces_info:
                if not self.match_protocol_lacp_interface(interface, interface_filter):
                    continue

                info['interfaces'].append(
                    interface
                )

            if instance_info:
                info['instance']['summary'] = self.get_interface_port_channel_summary(
                    pod_id,
                    node_id
                )
                for key in info['instance']['summary']['__Output']:
                    info['instance']['__Output']['summary.%s' % (key)] = info['instance']['summary']['__Output'][key]

        if event_info:
            all_events = self.get_protocol_lacp_event(
                pod_id,
                node_id
            )
            info['eventLog'] = []
            for event in all_events:
                if not self.match_system_fault(event, event_filter, exclude_cleared=False):
                    continue

                info['eventLog'].append(
                    event
                )

        return info
