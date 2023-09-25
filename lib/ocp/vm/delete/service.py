import yaml


class OcpVmDeleteService():
    def __init__(self):
        pass

    def delete_ocp_vm_services(self, label_special):
        services_info = self.k8s_handler.get_services_with_special_label(
            label_special
        )

        if services_info is not None and len(services_info) > 0:
            for service_info in services_info:
                if not self.k8s_handler.delete_namespaced_service(service_info['namespace'], service_info['name']):
                    self.log.error(
                        'delete_ocp_vm_service',
                        'Service delete failed: %s/%s' % (service_info['namespace'], service_info['name'])
                    )
                    return False

                self.log.debug(
                    'delete_ocp_vm_service',
                    'Service deleted: %s/%s' % (service_info['namespace'], service_info['name'])
                )

                self.my_output.default(
                    'Service %s/%s deleted' % (service_info['namespace'], service_info['name'])
                )

        return True

    def delete_service(self):
        vm_filename = self.user_input['deployment']['vm']
        yaml_content = self.user_input['files'][vm_filename]
        content = yaml.safe_load(yaml_content)

        label_special = None
        if 'spec' in content:
            if 'special' in content['spec']['template']['metadata']['labels']:
                label_special = content['spec']['template']['metadata']['labels']['special']
                is_service = self.k8s_handler.is_service_with_special_label(
                    label_special
                )

                if not is_service:
                    self.my_output.default('No virtual machine service found with label: %s' % (label_special))

                if is_service:
                    self.my_output.default('Deleting virtual machine services...')
                    success = self.delete_ocp_vm_services(label_special)

                    if not success:
                        self.my_output.error('Virtual machine services delete failed')
                        return False

                    self.my_output.default('Virtual machine services deleted')

        return True
