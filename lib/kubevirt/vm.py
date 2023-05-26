import time
import traceback

import kubevirt


class KubevirtVm():
    def __init__(self):
        pass

    def patch_namespaced_virtual_machine(self, namespace, name, body):
        if not self.connect():
            return False

        if self.api is None:
            return None

        start_time = int(time.time() * 1000)

        try:
            # Note: rest.py of client library has been modified
            # def PATCH(self, url, headers=None, query_params=None, post_params=None, body=None, _preload_content=True,
            #         _request_timeout=None):
            #     if headers['Content-Type'] == 'application/json-patch+json':
            #         headers['Content-Type'] = 'application/merge-patch+json'
            api_response = self.api.patch_namespaced_virtual_machine(
                name,
                namespace,
                body
            )
        except BaseException:
            api_response = None
            self.log.error(
                'kubevirt.patch_namespaced_virtual_machine',
                traceback.format_exc()
            )

        self.log.kubevirt(
            'patch',
            'vm',
            True,
            int(time.time() * 1000) - start_time
        )

        if api_response is None:
            return False

        return True

    def create_namespaced_virtual_machine(self, vm_definition):
        if not self.connect():
            return False

        if self.api is None:
            return None

        start_time = int(time.time() * 1000)

        namespace = vm_definition['metadata']['namespace']
        body = kubevirt.V1VirtualMachine(
            api_version=vm_definition['apiVersion'],
            kind='VirtualMachine',
            metadata=vm_definition['metadata'],
            spec=vm_definition['spec']
        )

        try:
            api_response = self.api.create_namespaced_virtual_machine(
                body,
                namespace
            )
        except BaseException:
            api_response = None
            self.log.error(
                'kubevirt.create_namespaced_virtual_machine',
                traceback.format_exc()
            )

        if api_response is None:
            self.log.kubevirt(
                'create',
                'vm',
                False,
                int(time.time() * 1000) - start_time
            )
            return False

        self.log.kubevirt(
            'create',
            'vm',
            True,
            int(time.time() * 1000) - start_time
        )

        return True

    def delete_namespaced_virtual_machine(self, namespace, name):
        if not self.connect():
            return False

        if self.api is None:
            return None

        start_time = int(time.time() * 1000)

        body = kubevirt.K8sIoApimachineryPkgApisMetaV1DeleteOptions()

        try:
            api_response = self.api.delete_namespaced_virtual_machine(
                name,
                namespace,
                body
            )
        except BaseException:
            api_response = None
            self.log.error(
                'kubevirt.delete_namespaced_virtual_machine',
                traceback.format_exc()
            )

        self.log.kubevirt(
            'delete',
            'vm',
            True,
            int(time.time() * 1000) - start_time
        )

        if api_response is None:
            return False

        return True

    def list_virtual_machine_for_all_namespaces(self):
        if not self.connect():
            return None

        if self.api is None:
            return None

        start_time = int(time.time() * 1000)

        try:
            api_response = self.api.list_virtual_machine_for_all_namespaces()
        except BaseException:
            api_response = None
            self.log.error(
                'kubevirt.list_virtual_machine_for_all_namespaces',
                traceback.format_exc()
            )

        items = None
        if api_response is not None:
            items = []
            for obj in api_response.items:
                items.append(
                    obj.to_dict()
                )

        self.log.kubevirt(
            'get',
            'vm',
            True,
            int(time.time() * 1000) - start_time
        )
        if items is not None:
            self.log.kubevirt_mo(
                'vm',
                items
            )

        return items
