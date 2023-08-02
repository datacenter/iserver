import time
from datetime import datetime

from lib import filter_helper


class ProtocolLldpEventInfo():
    def __init__(self):
        self.lldp_event = {}

    def get_protocol_lldp_event_info(self, managed_object):
        info = {}
        info['__Output'] = {}
        for key in managed_object:
            info[key] = managed_object[key]

        info['pod_node_name'] = '%s/%s' % (
            info['dn'].split('/')[1],
            self.get_node_name(
                info['dn'].split('/')[2].split('-')[1]
            )
        )

        # "affected": "topology/pod-1/node-2208/sys/lldp/inst/if-[eth1/4/3]/adj-1"
        info['interface_id'] = None
        if 'affected' in info:
            if 'sys/lldp/inst/if-' in info['affected']:
                info['interface_id'] = info['affected'].split('sys/lldp/inst/if-[')[1].split(']')[0]

        # "dn": "subj-[topology/pod-1/node-2208/sys/lldp/inst/if-[eth1/4/3]/adj-1]/rec-12886869434",
        if 'affected' not in info:
            if 'sys/lldp/inst/if-' in info['dn']:
                info['interface_id'] = info['dn'].split('sys/lldp/inst/if-[')[1].split(']')[0]

        info['descrT'] = filter_helper.get_string_chunks(
            filter_helper.sanitize_string(
                info['descr']
            ),
            40
        )

        info['dnT'] = filter_helper.get_string_chunks(
            info['dn'],
            40,
            separator='/'
        )

        info['affectedT'] = filter_helper.get_string_chunks(
            filter_helper.sanitize_string(
                info['affected']
            ),
            40,
            separator='/'
        )

        # "2022-04-29T13:32:45.167+02:00"
        info['timestamp'] = int(
            time.mktime(
                datetime.strptime(
                    info['created'],
                    '%Y-%m-%dT%H:%M:%S.%f%z'
                ).timetuple()
            )
        )

        info['severityT'] = self.system_fault_severity_name[info['severity']]
        info['__Output']['severityT'] = self.system_fault_severity_color[info['severity']]

        return info

    def get_protocol_lldp_event(self, pod_id, node_id):
        key = '%s.%s' % (pod_id, node_id)
        if key in self.lldp_event:
            return self.lldp_event[key]

        managed_objects = self.get_protocol_lldp_event_mo(pod_id, node_id)
        if managed_objects is None:
            return None

        self.lldp_event[key] = []
        for managed_object in managed_objects:
            self.lldp_event[key].append(
                self.get_protocol_lldp_event_info(
                    managed_object
                )
            )

        self.log.apic_mo(
            'lldpInst.eventRecord.info.%s' % (key),
            self.lldp_event[key]
        )

        return self.lldp_event[key]

    def get_protocol_lldp_adjacency_event(self, pod_id, node_id, interface_id, event_filter=None):
        events = []

        all_events = self.get_protocol_lldp_event(
            pod_id,
            node_id
        )
        if all_events is None:
            return events

        for event_info in all_events:
            if event_info['interface_id'] is not None:
                if event_info['interface_id'] == interface_id:
                    if not self.match_system_fault(event_info, event_filter):
                        continue

                    events.append(
                        event_info
                    )

        return events
