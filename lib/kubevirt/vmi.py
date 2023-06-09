import time
import traceback

import kubevirt


class KubevirtVmi():
    def __init__(self):
        pass

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

    def list_virtual_machine_instance_for_all_namespaces(self):
        if not self.connect():
            return False

        if self.api is None:
            return None

        start_time = int(time.time() * 1000)

        try:
            api_response = self.api.list_virtual_machine_instance_for_all_namespaces()
        except BaseException:
            api_response = None
            self.log.error(
                'kubevirt.list_virtual_machine_instance_for_all_namespaces',
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
            'vmi',
            True,
            int(time.time() * 1000) - start_time
        )
        if items is not None:
            self.log.kubevirt_mo(
                'vmi',
                items
            )

        return items
