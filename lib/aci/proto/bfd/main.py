from lib.aci.proto.bfd.instance.main import ProtocolBfdInstance
from lib.aci.proto.bfd.interface.main import ProtocolBfdInterface
from lib.aci.proto.bfd.session.main import ProtocolBfdSession


class ProtocolBfd(ProtocolBfdInstance, ProtocolBfdInterface, ProtocolBfdSession):
    def __init__(self):
        ProtocolBfdInstance.__init__(self)
        ProtocolBfdInterface.__init__(self)
        ProtocolBfdSession.__init__(self)

    def get_protocol_bfd(self, pod_id, node_id, bfd_filter=None, session_info=False):
        info = {}

        info['instance'] = self.get_protocol_bfd_instance(
            pod_id=pod_id,
            node_id=node_id
        )

        info['sessions'] = self.get_protocol_bfd_sessions(
            pod_id,
            node_id,
            bfd_session_filter=bfd_filter,
            session_info=session_info
        )

        info['interfaces'] = self.get_protocol_bfd_interfaces(
            pod_id,
            node_id
        )

        info['interfaces'] = self.add_protocol_bfd_interface_session_info(
            info['interfaces'],
            info['sessions'],
            remove_no_sessions=True
        )

        sessions_up = self.get_protocol_bfd_sessions_up_count(info['sessions'])
        sessions_count = len(info['sessions'])
        info['instance']['sessionSummary'] = '%s/%s' % (
            sessions_up,
            sessions_count
        )

        if sessions_up == sessions_count:
            info['instance']['__Output']['sessionSummary'] = 'Green'
        else:
            info['instance']['__Output']['sessionSummary'] = 'Red'

        return info
