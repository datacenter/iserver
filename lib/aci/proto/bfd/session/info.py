from lib import filter_helper
from lib import ip_helper


class ProtocolBfdSessionInfo():
    def __init__(self):
        self.bfd_sessions = {}

    def get_protocol_bfd_sessions_up_count(self, sessions):
        sessions_up = 0
        for session in sessions:
            if session['up']:
                sessions_up = sessions_up + 1
        return sessions_up

    def get_protocol_bfd_session_info(self, managed_object):
        info = {}
        info['__Output'] = {}
        for key in managed_object:
            if key in ['healthInst']:
                continue

            info[key] = managed_object[key]

        info['pod_node_name'] = '%s/%s' % (
            info['dn'].split('/')[1],
            self.get_node_name(
                info['dn'].split('/')[2].split('-')[1]
            )
        )

        # "dn": "topology/pod-1/node-2208/sys/bfd/inst/session-1090519058"
        info['session_id'] = None
        if len(info['dn'].split('/')) == 7:
            if info['dn'].split('/')[6].startswith('session-'):
                info['session_id'] = info['dn'].split('/')[6].split('-')[1]

        info['__Output']['discr'] = 'Yellow'

        if info['operSt'] == 'up':
            info['__Output']['operSt'] = 'Green'
        else:
            info['__Output']['operSt'] = 'Red'

        if info['remoteOperSt'] == 'up':
            info['__Output']['remoteOperSt'] = 'Green'
        else:
            info['__Output']['remoteOperSt'] = 'Red'

        info['up'] = False
        if info['operSt'] == 'up' and info['remoteOperSt'] == 'up':
            info['up'] = True

        (info['__Output']['health'], info['health']) = self.get_health_info(
            managed_object['healthInst']['cur']
        )

        (info['__Output']['faults'], info['faults']) = self.get_faults_info(
            managed_object['faultCounts']
        )

        return info

    def get_protocol_bfd_sessions_info(self, pod_id, node_id):
        key = '%s.%s' % (pod_id, node_id)
        if key in self.bfd_sessions:
            return self.bfd_sessions[key]

        bfd_sessions_mo = self.get_protocol_bfd_sessions_mo(pod_id, node_id)
        if bfd_sessions_mo is not None:
            self.bfd_sessions[key] = []
            for bfd_session_mo in bfd_sessions_mo:
                self.bfd_sessions[key].append(
                    self.get_protocol_bfd_session_info(
                        bfd_session_mo
                    )
                )

        self.log.apic_mo(
            'bfd.sessions.info.%s' % (key),
            self.bfd_sessions[key]
        )

        return self.bfd_sessions[key]

    def match_protocol_bfd_session(self, bfd_session_info, bfd_session_filter):
        if bfd_session_filter is None or len(bfd_session_filter) == 0:
            return True

        for ap_rule in bfd_session_filter:
            key = ap_rule.split(':')[0]
            value = ':'.join(ap_rule.split(':')[1:])
            if key == 'session_id':
                if not filter_helper.match_string(value, bfd_session_info['discr']) and not filter_helper.match_string(value, bfd_session_info['remoteDiscr']):
                    return False

            if key == 'interface_id':
                if not filter_helper.match_string(value, bfd_session_info['ifId']):
                    return False

            if key == 'session_state':
                if value != 'any':
                    if not filter_helper.match_string(value, bfd_session_info['operSt']) and not filter_helper.match_string(value, bfd_session_info['remoteOperSt']):
                        return False

            if key == 'vrf':
                if not filter_helper.match_string(value, bfd_session_info['vrfName']):
                    return False

            if key == 'ip':
                if not filter_helper.match_string(value, bfd_session_info['destAddr']) and not filter_helper.match_string(value, bfd_session_info['srcAddr']):
                    return False

            if key == 'subnet':
                if not ip_helper.is_ipv4_in_cidr(bfd_session_info['destAddr'], value) and not ip_helper.is_ipv4_in_cidr(bfd_session_info['srcAddr'], value):
                    return False

        return True

    def get_protocol_bfd_sessions(self, pod_id, node_id, bfd_session_filter=None):
        all_bfd_sessions = self.get_protocol_bfd_sessions_info(pod_id, node_id)
        if all_bfd_sessions is None:
            return None

        bfd_sessions = []

        for bfd_session_info in all_bfd_sessions:
            if not self.match_protocol_bfd_session(bfd_session_info, bfd_session_filter):
                continue

            bfd_session_info['stats'] = self.get_protocol_bfd_session_stats(
                pod_id,
                node_id,
                bfd_session_info['discr']
            )

            bfd_session_info['peer'] = None
            if bfd_session_info['up']:
                bfd_session_info['peer'] = self.get_protocol_bfd_session_peer(
                    pod_id,
                    node_id,
                    bfd_session_info['discr']
                )

            bfd_sessions.append(
                bfd_session_info
            )

        bfd_sessions = sorted(
            bfd_sessions,
            key=lambda i: (
                i['srcAddr'].lower(),
                i['destAddr'].lower()
            )
        )

        return bfd_sessions
