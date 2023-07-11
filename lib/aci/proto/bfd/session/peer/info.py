class ProtocolBfdSessionPeerInfo():
    def __init__(self):
        pass

    def get_protocol_bfd_session_peer_info(self, managed_object):
        info = {}
        info['__Output'] = {}
        for key in managed_object:
            info[key] = managed_object[key]

        if info['operSt'] == 'up':
            info['__Output']['operSt'] = 'Green'
        else:
            info['__Output']['operSt'] = 'Red'

        return info

    def get_protocol_bfd_session_peer(self, pod_id, node_id, session_id):
        managed_object = self.get_protocol_bfd_session_peer_mo(pod_id, node_id, session_id)
        if managed_object is None:
            return None

        return self.get_protocol_bfd_session_peer_info(managed_object)
