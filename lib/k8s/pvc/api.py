import time
import traceback


class K8sPvcApi():
    def __init__(self):
        self.pvcs = None

    def is_pvc(self, namespace, name, cache=True):
        if self.get_pvc(namespace, name, cache=cache) is None:
            return False
        return True

    def get_pvc(self, namespace, name, cache=True):
        pvcs = self.get_pvcs(cache=cache)
        if pvcs is None:
            return None

        for pvc in pvcs:
            if pvc['metadata']['namespace'] == namespace and pvc['metadata']['name'] == name:
                return pvc

        return None

    def get_pvcs(self, cache=True):
        if not self.connect():
            return None

        if self.pvcs is not None and cache:
            return self.pvcs

        try:
            start_time = int(time.time() * 1000)
            response = self.api.list_persistent_volume_claim_for_all_namespaces(
                timeout_seconds=self.api_timeout_seconds
            )
            self.log.k8s(
                'get',
                'pvcs',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('k8s.get_pvcs', traceback.format_exc())
            self.log.k8s(
                'get',
                'pvcs',
                True,
                int(time.time() * 1000) - start_time
            )
            return None

        self.pvcs = []
        for item in response.items:
            pvc = self.convert_object(item.to_dict())
            self.pvcs.append(
                pvc
            )

        self.log.k8s_mo(
            'pvc',
            self.pvcs
        )

        return self.pvcs

    def delete_namespaced_pvc(self, namespace, name):
        if not self.connect():
            return False

        if self.api is None:
            return None

        start_time = int(time.time() * 1000)
        try:
            api_response = self.api.delete_namespaced_persistent_volume_claim(
                name,
                namespace
            )
        except BaseException:
            api_response = None
            self.log.error(
                'k8s.delete_namespaced_pvc',
                traceback.format_exc()
            )

        if api_response is None:
            self.log.k8s(
                'delete',
                'pvc',
                False,
                int(time.time() * 1000) - start_time
            )
            return False

        self.log.k8s(
            'delete',
            'pvc',
            True,
            int(time.time() * 1000) - start_time
        )

        return True
