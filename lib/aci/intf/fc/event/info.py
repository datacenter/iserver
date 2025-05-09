import time
from datetime import datetime

from lib import filter_helper


class InterfaceFcEventInfo():
    def __init__(self):
        self.interface_fc_event = {}

    def get_interface_fc_event_info(self, managed_object):
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

        # "affected": "topology/pod-1/node-2208/sys/inst-overlay-1/fc-[lo0]"
        info['interfaceId'] = None
        if '/fc-[' in info['affected']:
            info['interfaceId'] = info['affected'].split('/fc-[')[1].split(']')[0]

        info['descrT'] = filter_helper.get_string_chunks(
            filter_helper.sanitize_string(
                info['descr']
            ),
            80
        )

        info['changeSetT'] = filter_helper.get_string_chunks(
            filter_helper.sanitize_string(
                info['changeSet']
            ),
            80
        )

        info['dnT'] = filter_helper.get_string_chunks(
            info['dn'],
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

    def get_interface_fc_event(self, pod_id, node_id, deduplicate=True):
        key = '%s.%s' % (pod_id, node_id)
        if key in self.interface_fc_event:
            return self.interface_fc_event[key]

        managed_objects = self.get_interface_fc_event_mo(pod_id, node_id)
        if managed_objects is None:
            return None

        self.interface_fc_event[key] = []
        transaction_ids = []
        for managed_object in managed_objects:
            event_info = self.get_interface_fc_event_info(
                managed_object
            )
            if not deduplicate or event_info['txId'] not in transaction_ids:
                self.interface_fc_event[key].append(
                    event_info
                )
                transaction_ids.append(
                    event_info['txId']
                )

        self.log.apic_mo(
            'l1FcPhysIf.eventLog.info.%s' % (key),
            self.interface_fc_event[key]
        )

        return self.interface_fc_event[key]

    def get_interface_fc_id_event(self, pod_id, node_id, interface_id, event_filter=None):
        events = []

        all_events = self.get_interface_fc_event(
            pod_id,
            node_id
        )
        if all_events is None:
            return events

        for event_info in all_events:
            if event_info['interfaceId'] is not None:
                if event_info['interfaceId'] == interface_id:
                    if not self.match_system_fault(event_info, event_filter):
                        continue

                    events.append(
                        event_info
                    )

        return events
