import yaml


class OcpVmDeleteDay0():
    def __init__(self):
        pass

    def delete_day0(self):
        if self.user_input['deployment']['day0']['enabled']:
            day0_dv_filename = self.user_input['deployment']['day0']['dv']
            if day0_dv_filename is not None:
                yaml_content = self.user_input['files'][day0_dv_filename]
                content = yaml.safe_load(yaml_content)

                namespace = content['metadata']['namespace']
                name = content['metadata']['name']

                if self.k8s_handler.is_data_volume(namespace, name, cache_enabled=False):
                    self.my_output.default(
                        'Day0 dv will be deleted: %s/%s' % (
                            namespace,
                            name
                        )
                    )
                    success = self.k8s_handler.delete_data_volume(
                        namespace,
                        name
                    )
                    return success

                if self.k8s_handler.is_pvc(namespace, name, cache_enabled=False):
                    self.my_output.default(
                        'Day0 pvc will be deleted: %s/%s' % (
                            namespace,
                            name
                        )
                    )
                    success = self.k8s_handler.delete_namespaced_pvc(
                        namespace,
                        name
                    )
                    return success

                self.my_output.default(
                    'Day0 dv/pvc already deleted: %s/%s' % (
                        namespace,
                        name
                    )
                )

        return True
