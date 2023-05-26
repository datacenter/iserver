from lib import log_helper


class InterfaceVirtualPortChannelSummary():
    def __init__(self, log_id=None):
        self.log = log_helper.Log(log_id=log_id)

    def get_interface_virtual_port_channel_summary(self, pod_id, node_id):
        ports = self.get_interface_virtual_port_channel(
            pod_id,
            node_id
        )

        if ports is None:
            return None

        summary = {}
        summary['__Output'] = {}
        summary['portUp'] = 0
        summary['portDown'] = 0
        summary['portCount'] = 0

        for port in ports:
            summary['portUp'] = summary['portUp'] + port['localMemberUp']
            summary['portDown'] = summary['portDown'] + port['localMemberDown']

        summary['portCount'] = summary['portUp'] + summary['portDown']

        (summary['portSummary'], summary['__Output']['portSummary']) = self.get_interface_summary_output(
            summary['portUp'],
            summary['portDown'],
            summary['portCount']
        )

        return summary
