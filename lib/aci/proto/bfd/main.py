from lib.aci.proto.bfd.event.main import ProtocolBfdEvent
from lib.aci.proto.bfd.fault.main import ProtocolBfdFault
from lib.aci.proto.bfd.instance.main import ProtocolBfdInstance
from lib.aci.proto.bfd.interface.main import ProtocolBfdInterface
from lib.aci.proto.bfd.session.main import ProtocolBfdSession


class ProtocolBfd(ProtocolBfdEvent, ProtocolBfdFault, ProtocolBfdInstance, ProtocolBfdInterface, ProtocolBfdSession):
    def __init__(self):
        ProtocolBfdEvent.__init__(self)
        ProtocolBfdFault.__init__(self)
        ProtocolBfdInstance.__init__(self)
        ProtocolBfdInterface.__init__(self)
        ProtocolBfdSession.__init__(self)

    def get_protocol_bfd(
            self,
            pod_id,
            node_id,
            bfd_filter=None,
            instance_info=False,
            session_info=False,
            interface_info=False,
            fault_info=False,
            hfault_info=False,
            hfault_filter=None,
            event_info=False,
            event_filter=None
            ):
        info = {}

        info['node'] = self.get_node(
            pod_id=pod_id,
            node_id=node_id
        )

        if instance_info:
            info['instance'] = self.get_protocol_bfd_instance(
                pod_id=pod_id,
                node_id=node_id
            )

        if session_info:
            info['sessions'] = self.get_protocol_bfd_sessions(
                pod_id,
                node_id,
                bfd_session_filter=bfd_filter
            )

            if instance_info:
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

        if interface_info:
            info['interfaces'] = self.get_protocol_bfd_interfaces(
                pod_id,
                node_id
            )

            if session_info:
                info['interfaces'] = self.add_protocol_bfd_interface_session_info(
                    info['interfaces'],
                    info['sessions'],
                    remove_no_sessions=True
                )

        if fault_info:
            info['faultInst'] = self.get_protocol_bfd_fault(
                pod_id,
                node_id
            )
            for session in info['sessions']:
                session['faultInst'] = self.get_protocol_bfd_session_fault(
                    pod_id,
                    node_id,
                    session['session_id'],
                    'faultInst'
                )

        if hfault_info:
            info['faultRecord'] = self.get_protocol_bfd_fault_record(
                pod_id,
                node_id
            )
            for session in info['sessions']:
                session['faultRecord'] = self.get_protocol_bfd_session_fault(
                    pod_id,
                    node_id,
                    session['session_id'],
                    'faultRecord',
                    fault_filter=hfault_filter
                )

        if event_info:
            info['eventLog'] = self.get_protocol_bfd_event(
                pod_id,
                node_id
            )
            for session in info['sessions']:
                session['eventLog'] = self.get_protocol_bfd_session_event(
                    pod_id,
                    node_id,
                    session['session_id'],
                    event_filter=event_filter
                )

        return info
