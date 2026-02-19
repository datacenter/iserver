import time
import traceback
from kubernetes.dynamic.exceptions import ApiException


class K8sVirtualMachineApi():
    def __init__(self):
        self.virtual_machine_mo = None

    def get_virtual_machine_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.virtual_machine_mo is not None:
                return self.virtual_machine_mo

        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return None

        try:
            start_time = int(time.time() * 1000)
            response = api_handler.resources.get(
                api_version='kubevirt.io/v1',
                kind='VirtualMachine'
            )
            self.virtual_machine_mo = response.get().to_dict()['items']
            self.log.k8s(
                'get',
                'virtual_machine',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('k8s.get_virtual_machine_mo', traceback.format_exc())
            self.log.k8s(
                'get',
                'virtual_machine',
                True,
                int(time.time() * 1000) - start_time
            )
            print(traceback.format_exc())
            return None

        self.log.k8s_mo(
            'virtual_machine',
            self.virtual_machine_mo
        )

        return self.virtual_machine_mo

    def patch_virtual_machine_mo(self, body):
        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return False, 'No api handler'

        try:
            obj_list = api_handler.resources.get(api_version='kubevirt.io/v1', kind='VirtualMachine')
            obj_list.patch(
                namespace=body['metadata']['namespace'],
                body=body,
                content_type='application/merge-patch+json'
            )

        except ApiException as err:
            return False, self.get_api_exception_reason(err)
        
        except BaseException:
            self.log.error('k8s.patch_virtual_machine_mo', traceback.format_exc())
            return False, 'Base exception'

        return True, None
    
    def delete_virtual_machine_mo(self, namespace, name):
        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return False

        try:
            start_time = int(time.time() * 1000)
            obj_list = api_handler.resources.get(api_version='kubevirt.io/v1', kind='VirtualMachine')
            success = True
            response = obj_list.delete(
                namespace=namespace,
                name=name
            )
        except BaseException:
            success = False
            self.log.error('ocp.delete_virtual_machine_mo', traceback.format_exc())

        self.log.ocp(
            'delete',
            'virtual_machine',
            success,
            int(time.time() * 1000) - start_time
        )

        return success
