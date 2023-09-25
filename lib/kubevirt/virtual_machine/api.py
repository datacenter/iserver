import time
import traceback
import kubevirt


class KubevirtVirtualMachineApi():
    def __init__(self):
        self.virtual_machine_mo = None

    def patch_namespaced_virtual_machine(self, namespace, name, body):
        if not self.connect():
            return False

        if self.api is None:
            return False

        start_time = int(time.time() * 1000)

        try:
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
            return False

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
            return False

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

    def start_virtual_machine(self, namespace, name):
        body = {}
        body['spec'] = {}
        body['spec']['running'] = True
        return self.patch_namespaced_virtual_machine(namespace, name, body)

    def stop_virtual_machine(self, namespace, name):
        body = {}
        body['spec'] = {}
        body['spec']['running'] = False
        return self.patch_namespaced_virtual_machine(namespace, name, body)

    def get_virtual_machine_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.virtual_machine_mo is not None:
                return self.virtual_machine_mo

        if not self.connect():
            return None

        if self.api is None:
            return None

        try:
            start_time = int(time.time() * 1000)
            api_response = self.api.list_virtual_machine_for_all_namespaces()
            if api_response is not None:
                self.virtual_machine_mo = []
                for obj in api_response.items:
                    self.virtual_machine_mo.append(
                        obj.to_dict()
                    )

            self.log.kubevirt(
                'get',
                'virtual_machine',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error(
                'kubevirt.get_virtual_machine_mo',
                traceback.format_exc()
            )
            self.log.kubevirt(
                'get',
                'virtual_machine',
                True,
                int(time.time() * 1000) - start_time
            )

        self.log.kubevirt_mo(
            'vm',
            self.virtual_machine_mo
        )

        return self.virtual_machine_mo
