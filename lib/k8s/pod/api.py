import time
import traceback


class K8sPodApi():
    def __init__(self):
        self.pod_mo = None

    def get_pods_mo(self, cache=True):
        if not self.connect():
            return None

        if self.pod_mo is not None and cache:
            return self.pod_mo

        try:
            start_time = int(time.time() * 1000)
            response = self.api.list_pod_for_all_namespaces(
                timeout_seconds=self.api_timeout_seconds
            )
            self.log.k8s(
                'get',
                'pods',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('k8s.get_pods', traceback.format_exc())
            self.log.k8s(
                'get',
                'pods',
                False,
                int(time.time() * 1000) - start_time
            )
            return None

        self.pod_mo = []
        for item in response.items:
            pod = self.convert_pod(item)
            if pod is not None:
                self.pod_mo.append(pod)

        self.log.k8s_mo(
            'pod',
            self.pod_mo
        )

        return self.pod_mo
