import time
from datetime import datetime

from lib import filter_helper


class PoolVlanEventInfo():
    def __init__(self):
        self.pool_vlan_event = None

    def get_pool_vlan_event_info(self, managed_object):
        info = {}
        info['__Output'] = {}
        for key in managed_object:
            info[key] = managed_object[key]

        info['poolName'] = None

        if 'affected' in info:
            if 'uni/infra/vlanns-[' in info['affected']:
                info['poolName'] = info['affected'].split('uni/infra/vlanns-[')[1].split(']')[0]

        if 'affected' not in info and 'dn' in info:
            if 'uni/infra/vlanns-[' in info['dn']:
                info['poolName'] = info['dn'].split('uni/infra/vlanns-[')[1].split(']')[0]

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

    def get_pool_vlan_event(self, deduplicate=True):
        if self.pool_vlan_event is not None:
            return self.pool_vlan_event

        managed_objects = self.get_pool_vlan_event_mo()
        if managed_objects is None:
            return None

        self.pool_vlan_event = []
        transaction_ids = []
        for managed_object in managed_objects:
            event_info = self.get_pool_vlan_event_info(
                managed_object
            )
            if not deduplicate or event_info['txId'] not in transaction_ids:
                self.pool_vlan_event.append(
                    event_info
                )
                transaction_ids.append(
                    event_info['txId']
                )

        self.log.apic_mo(
            'fvnsVlanInstP.eventLog.info',
            self.pool_vlan_event
        )

        return self.pool_vlan_event

    def get_pool_vlan_id_event(self, pool_name, event_filter=None):
        events = []

        all_events = self.get_pool_vlan_event()
        if all_events is None:
            return events

        for event_info in all_events:
            if event_info['poolName'] is not None:
                if event_info['poolName'] == pool_name:
                    if not self.match_system_fault(event_info, event_filter):
                        continue

                    events.append(
                        event_info
                    )

        return events
