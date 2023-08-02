import time
from datetime import datetime

from lib import filter_helper


class ProtocolBgpEventInfo():
    def __init__(self):
        self.proto_bgp_event = {}

    def get_protocol_bgp_event_info(self, managed_object):
        info = {}
        info['__Output'] = {}
        for key in managed_object:
            info[key] = managed_object[key]

        # topology/pod-1/node-2205/sys/bgp/inst
        info['podId'] = info['affected'].split('/')[1].split('-')[1]
        info['nodeId'] = info['affected'].split('/')[2].split('-')[1]
        info['pod_node_name'] = 'pod-%s/%s' % (
            info['podId'],
            self.get_node_name(
                info['nodeId']
            )
        )

        info['domainName'] = None
        info['nei'] = None

        if 'sys/bgp/inst/dom-' in info['affected']:
            info['domainName'] = info['affected'].split('sys/bgp/inst/dom-')[1].split('/')[0]

        if '/peer-[' in info['affected']:
            info['nei'] = info['affected'].split('/peer-[')[1].split(']')[0]

        info['domainNameT'] = info['domainName']
        if info['domainNameT'] is None:
            info['domainNameT'] = '--'

        info['neiT'] = info['nei']
        if info['neiT'] is None:
            info['neiT'] = '--'

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

    def get_protocol_bgp_event(self, pod_id, node_id):
        key = '%s.%s' % (pod_id, node_id)
        if key in self.proto_bgp_event:
            return self.proto_bgp_event[key]

        managed_objects = self.get_protocol_bgp_event_mo(pod_id, node_id)
        if managed_objects is None:
            return None

        self.proto_bgp_event[key] = []
        for managed_object in managed_objects:
            self.proto_bgp_event[key].append(
                self.get_protocol_bgp_event_info(
                    managed_object
                )
            )

        self.log.apic_mo(
            'bgpDom.eventLog.info.%s' % (key),
            self.proto_bgp_event[key]
        )

        return self.proto_bgp_event[key]
