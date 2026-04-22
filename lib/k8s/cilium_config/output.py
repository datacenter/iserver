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

    def print_cilium_private_network_state(self, info, before_newline=True):
        if before_newline:
            self.my_output.default('')

        if info['enabled']:
            self.my_output.default('Private network %s' % (self.my_output.add_color('enabled', 'Green')))
            self.my_output.default('Cilium configuration', before_newline=True)
            self.my_output.default(yaml.dump(info['configuration']), wrap='~~~')
            self.print_cilium_private_network_webhook(info)
        else:
            self.my_output.default('Private network %s' % (self.my_output.add_color('disabled', 'Red')))

    def print_cilium_private_network_webhook(self, info):
        self.my_output.default('Private network webhook', before_newline=True)
        if info['webhook']['enabled']:
            self.my_output.default('- %s' % (self.my_output.add_color('enabled', 'Green')))
            if info['webhook']['configured']:
                self.my_output.default('- mutating webhook %s %s' % (info['webhook']['name'], self.my_output.add_color('found', 'Green')))
            else:
                self.my_output.default('- mutating webhook %s %s' % (info['webhook']['name'], self.my_output.add_color('not found', 'Red')))

            if info['webhook']['service_found']:
                self.my_output.default('- service %s %s' % (info['webhook']['service_name'], self.my_output.add_color('found', 'Green')))
            else:
                self.my_output.default('- service %s %s' % (info['webhook']['service_name'], self.my_output.add_color('not found', 'Red')))

            if len(info['webhook']['service_endpoints']) > 0:
                self.my_output.default('- service endpoints: %s' % (', '.join(info['webhook']['service_endpoints'])))
            else:
                self.my_output.default('- service endpoints %s' % (self.my_output.add_color('not found', 'Red')))
        else:
            self.my_output.default('- %s' % (self.my_output.add_color('disabled', 'Red')))
            if info['webhook']['configured']:
                self.my_output.default('- mutating webhook %s %s' % (info['webhook']['name'], self.my_output.add_color('found', 'Red')))
            if info['webhook']['service_found']:
                self.my_output.default('- service %s %s' % (info['webhook']['service_name'], self.my_output.add_color('found', 'Red')))