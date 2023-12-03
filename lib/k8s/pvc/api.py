import time
import json
import traceback


class K8sPvcApi():
    def __init__(self):
        self.pvc_mo = None

    def get_pvc_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.pvc_mo is not None:
                return self.pvc_mo

        api_handler = self.get_api()
        if api_handler is None:
            return None

        try:
            start_time = int(time.time() * 1000)
            response = api_handler.list_persistent_volume_claim_for_all_namespaces(
                timeout_seconds=self.api_timeout_seconds
            )
            self.log.k8s(
                'get',
                'pvc',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('k8s.get_pvc', traceback.format_exc())
            self.log.k8s(
                'get',
                'pvc',
                True,
                int(time.time() * 1000) - start_time
            )
            return None

        self.pvc_mo = []
        for item in response.items:
            pvc = self.convert_object(item.to_dict())
            self.pvc_mo.append(
                pvc
            )

        self.log.k8s_mo(
            'pvc',
            self.pvc_mo
        )

        return self.pvc_mo

    def create_namespaced_pvc(self, pvc_definition):
        api_handler = self.get_api()
        if api_handler is None:
            return None

        start_time = int(time.time() * 1000)
        namespace = pvc_definition['metadata']['namespace']

        try:
            api_response = api_handler.create_namespaced_persistent_volume_claim(
                namespace,
                pvc_definition
            )
        except BaseException:
            api_response = None
            self.log.error(
                'k8s.create_namespaced_pvc',
                'PVC create failed: %s' % (json.dumps(pvc_definition, indent=4))
            )
            self.log.error(
                'k8s.create_namespaced_pvc',
                traceback.format_exc()
            )

        if api_response is None:
            self.log.k8s(
                'create',
                'pvc',
                False,
                int(time.time() * 1000) - start_time
            )
            return False

        self.log.k8s(
            'create',
            'pvc',
            True,
            int(time.time() * 1000) - start_time
        )

        return True

    def delete_namespaced_pvc(self, namespace, name):
        api_handler = self.get_api()
        if api_handler is None:
            return None

        start_time = int(time.time() * 1000)
        try:
            api_response = api_handler.delete_namespaced_persistent_volume_claim(
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
