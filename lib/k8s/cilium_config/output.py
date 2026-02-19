import yaml


class K8sCiliumConfigOutput():
    def __init__(self):
        pass

    def print_cilium_config(self, info):
        self.my_output.default(
            yaml.safe_dump(info['spec']), 
            before_newline=True, 
            wrap='~~~'
        )

    def print_cilium_config_state(self, info):
        self.my_output.default('Cilium config state', underline=False, before_newline=True)
        if info['processing_error']:
            self.my_output.default(
                '- processing error: %s [reason:%s]' % (
                    self.my_output.add_color(info['processing_error'], 'Red'),
                    info['info']['processing_error_reason']
                )
            )
            self.my_output.default(
                info['info']['processing_error_message'],
                wrap='~~~'
            )
        else:
            self.my_output.default(
                '- processing error: %s' % (
                    self.my_output.add_color(info['processing_error'], 'Green')
                )
            )
            
        if info['values_error']:
            self.my_output.default(
                '- values error: %s [reason:%s]' % (
                    self.my_output.add_color(info['values_error'], 'Red'),
                    info['info']['values_error_reason']
                )
            )
            self.my_output.default(
                info['info']['values_error_message'],
                wrap='~~~'
            )
        else:
            self.my_output.default(
                '- values error: %s' % (
                    self.my_output.add_color(info['values_error'], 'Green')
                )
            )

    def print_cilium_mesh_status(self, info):
        self.my_output.my_table_ng(
            info,
            [
                ['Cluster Name', 'cluster_name'],
                ['Cluster ID', 'cluster_id'],
                ['Cluster IP', 'ips'],
                ['Cluster Port', 'port'],
                ['Summary', 'agent_summary'],
                ['Cilium Agent', 'agent.metadata.pod'],
                ['Node', 'agent.metadata.node'],
                ['Node IP', 'agent.metadata.ip'],
                ['Ready', 'agent.readyTick']
            ]
        )