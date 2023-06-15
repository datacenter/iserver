import yaml


class OcpVmCreateService():
    def __init__(self):
        pass

    def create_deployment_services(self, deployment):
        if deployment['deployment']['service'] is not None:
            for key in deployment['deployment']['service']:
                service_filename = deployment['deployment']['service'][key]
                if service_filename is not None:
                    yaml_content = self.user_input['files'][service_filename]
                    content = yaml.safe_load(yaml_content)

                    namespace = content['metadata']['namespace']
                    name = content['metadata']['name']
                    self.my_output.default(
                        'Preparing %s service: %s/%s...' % (
                            key,
                            namespace,
                            name
                        )
                    )

                    service_mo = self.k8s_handler.get_service(
                        namespace,
                        name,
                        cache=False
                    )
                    if service_mo is not None:
                        self.my_output.default('Service already exists')
                        continue

                    if not self.k8s_handler.create_namespaced_service(content):
                        self.my_output.error('Service create failed')
                        return False

        return True
