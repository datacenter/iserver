import time
from datetime import datetime

from lib import filter_helper


class ProtocolBfdEventInfo():
    def __init__(self):
        self.bfd_event = {}

    def get_protocol_bfd_event_info(self, managed_object):
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

        # "affected": "topology/pod-1/node-2208/sys/bfd/inst/session-1090519092"
        info['session_id'] = None
        if len(info['affected'].split('/')) == 7:
            if info['affected'].split('/')[6].startswith('session-'):
                info['session_id'] = info['affected'].split('/')[6].split('-')[1]

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
            info['affected'],
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

    def get_protocol_bfd_event(self, pod_id, node_id):
        key = '%s.%s' % (pod_id, node_id)
        if key in self.bfd_event:
            return self.bfd_event[key]

        managed_objects = self.get_protocol_bfd_event_mo(pod_id, node_id)
        if managed_objects is None:
            return None

        self.bfd_event[key] = []
        for managed_object in managed_objects:
            self.bfd_event[key].append(
                self.get_protocol_bfd_event_info(
                    managed_object
                )
            )

        self.log.apic_mo(
            'bfdInst.eventRecord.info.%s' % (key),
            self.bfd_event[key]
        )

        return self.bfd_event[key]

    def get_protocol_bfd_session_event(self, pod_id, node_id, session_id, event_filter=None):
        events = []

        all_events = self.get_protocol_bfd_event(
            pod_id,
            node_id
        )
        if all_events is None:
            return events

        for event_info in all_events:
            if event_info['session_id'] is not None:
                if event_info['session_id'] == session_id:
                    if not self.match_system_fault(event_info, event_filter):
                        continue

                    events.append(
                        event_info
                    )

        return events
