class K8sVirtualMachineCreateC8kv():
    def __init__(self):
        pass

    def get_virtual_machine_c8kv_body(
            self, 
            namespace,
            name,
            variables
        ):
        if 'size' not in variables:
            variables['size'] = '10Gi'

        if 'day0' not in variables:
            return None, 'day0 attribute required'

        if 'interface' not in variables:
            variables['interface'] = [dict(name='default', type='masquerade')]

        if 'cores' not in variables:
            variables['cores'] = 1

        if 'threads' not in variables:
            variables['threads'] = 1

        if 'sockets' not in variables:
            variables['sockets'] = 1

        if 'memory' not in variables:
            variables['memory'] = '4Gi'

        if 'node' not in variables:
            variables['node'] = None

        body = self.get_virtual_machine_body_main(namespace, name)
        if 'url' in variables and 'pvc' in variables:
            if variables['clone']:
                body['spec']['dataVolumeTemplates'] = [
                    self.get_virtual_machine_data_volume_pvc_template_body(
                        namespace, 
                        name, 
                        self.increase_virtual_machine_disk_size(variables['size'], 1.2), 
                        variables['pvc'],
                        storage_class=variables['sc']['name']
                    )
                ]
            else:
                body['spec']['dataVolumeTemplates'] = [
                    self.get_virtual_machine_data_volume_url_template_body(
                        namespace, 
                        name, 
                        variables['size'], 
                        variables['url'],
                        storage_class=variables['sc']['name']
                    )
                ]

        if 'url' in variables and 'pvc' not in variables:
            body['spec']['dataVolumeTemplates'] = [
                self.get_virtual_machine_data_volume_url_template_body(
                    namespace, 
                    name, 
                    variables['size'], 
                    variables['url'],
                    storage_class=variables['sc']['name']
                )
            ]

        if 'pvc' in variables and 'url' not in variables:
            body['spec']['dataVolumeTemplates'] = [
                self.get_virtual_machine_data_volume_pvc_template_body(
                    namespace, 
                    name, 
                    self.increase_virtual_machine_disk_size(variables['size'], 1.2), 
                    variables['pvc'],
                    storage_class=variables['sc']['name']
                )
            ]

        body['spec']['runStrategy'] = 'Always'
        body['spec']['template'] = self.get_virtual_machine_template_body(
            namespace, 
            name, 
            variables['cores'], 
            variables['threads'], 
            variables['sockets'], 
            variables['memory'], 
            interface=variables['interface'], 
            day0=variables['day0'],
            node=variables['node']
        )
        return body, None
