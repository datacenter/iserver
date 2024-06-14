import time
import traceback
import yaml


class OcpVmDeleteImage():
    def __init__(self):
        pass

    def delete_image(self):
        if self.user_input['deployment']['image']['enabled']:
            image_dv_filename = self.user_input['deployment']['image']['dv']
            if image_dv_filename is not None:
                yaml_content = self.user_input['files'][image_dv_filename]
                content = yaml.safe_load(yaml_content)

                namespace = content['metadata']['namespace']
                name = content['metadata']['name']

                if self.k8s_handler.is_data_volume(namespace, name, cache_enabled=False):
                    self.my_output.default(
                        'Image dv will be deleted: %s/%s' % (
                            namespace,
                            name
                        )
                    )
                    success = self.k8s_handler.delete_data_volume(
                        namespace,
                        name
                    )
                    return success

                if self.k8s_handler.is_pvc(namespace, name, cache=False):
                    self.my_output.default(
                        'Image pvc will be deleted: %s/%s' % (
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
                    'Image dv/pvc already deleted: %s/%s' % (
                        namespace,
                        name
                    )
                )

        return True

    def delete_ocp_dv_vm_image(self, label_special, cache=True):
        data_volumes = self.get_ocp_dv_vm_image(label_special, cache=cache)
        if len(data_volumes) == 0:
            return True

        delete_success = True

        for data_volume in data_volumes:
            try:
                start_time = int(time.time() * 1000)
                obj_list = self.api.resources.get(api_version='cdi.kubevirt.io/v1beta1', kind='DataVolume')
                success = obj_list.delete(
                    namespace=data_volume['metadata']['namespace'],
                    name=data_volume['metadata']['name']
                )
            except BaseException:
                success = False
                self.log.error('ocp.delete_ocp_dv_vm_image', traceback.format_exc())

            self.log.ocp(
                'delete',
                'dv',
                success,
                int(time.time() * 1000) - start_time
            )

            if success:
                self.my_output.default(
                    'Delete data volume: %s/%s' % (
                        data_volume['metadata']['namespace'],
                        data_volume['metadata']['name']
                    )
                )
            else:
                self.my_output.error(
                    'Delete data volume failed: %s/%s' % (
                        data_volume['metadata']['namespace'],
                        data_volume['metadata']['name']
                    )
                )
                delete_success = False

        return delete_success
