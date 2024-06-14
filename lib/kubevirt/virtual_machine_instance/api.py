import time
import traceback

import kubevirt


class KubevirtVirtualMachineInstanceApi():
    def __init__(self):
        self.virtual_machine_instance_mo = None

    def delete_namespaced_virtual_machine_instance(self, namespace, name):
        if not self.connect():
            return None

        if self.api is None:
            return None

        start_time = int(time.time() * 1000)

        body = kubevirt.K8sIoApimachineryPkgApisMetaV1DeleteOptions()

        try:
            api_response = self.api.delete_namespaced_virtual_machine_instance(
                name,
                namespace,
                body
            )
        except BaseException:
            api_response = None
            self.log.error(
                'kubevirt.delete_namespaced_virtual_machine_instance',
                traceback.format_exc()
            )

        self.log.kubevirt(
            'delete',
            'vmi',
            True,
            int(time.time() * 1000) - start_time
        )

        if api_response is None:
            return False

        return True

    def create_namespaced_virtual_machine_instance(self, vmi_definition):
        if not self.connect():
            return False

        if self.api is None:
            return False

        start_time = int(time.time() * 1000)

        namespace = vmi_definition['metadata']['namespace']
        body = kubevirt.V1VirtualMachineInstance(
            api_version=vmi_definition['apiVersion'],
            kind='VirtualMachineInstance',
            metadata=vmi_definition['metadata'],
            spec=vmi_definition['spec']
        )

        try:
            api_response = self.api.create_namespaced_virtual_machine_instance(
                body,
                namespace
            )
        except BaseException:
            api_response = None
            self.log.error(
                'kubevirt.create_namespaced_virtual_machine_instance',
                traceback.format_exc()
            )

        if api_response is None:
            self.log.kubevirt(
                'create',
                'vmi',
                False,
                int(time.time() * 1000) - start_time
            )
            return False

        self.log.kubevirt(
            'create',
            'vmi',
            True,
            int(time.time() * 1000) - start_time
        )

        return True

    def get_virtual_machine_instance_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.virtual_machine_instance_mo is not None:
                return self.virtual_machine_instance_mo

        if not self.connect():
            return None

        if self.api is None:
            return None

        try:
            start_time = int(time.time() * 1000)
            api_response = self.api.list_virtual_machine_instance_for_all_namespaces()
            if api_response is not None:
                self.virtual_machine_instance_mo = []
                for obj in api_response.items:
                    self.virtual_machine_instance_mo.append(
                        obj.to_dict()
                    )

            self.log.kubevirt(
                'get',
                'virtual_machine_instance',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error(
                'kubevirt.virtual_machine_instance_mo',
                traceback.format_exc()
            )
            self.log.kubevirt(
                'get',
                'virtual_machine_instance',
                True,
                int(time.time() * 1000) - start_time
            )

        self.log.kubevirt_mo(
            'vmi',
            self.virtual_machine_instance_mo
        )

        return self.virtual_machine_instance_mo
