import time
import traceback


class K8sPodApi():
    def __init__(self):
        self.pods = None

    def get_pods(self, cache=True):
        if not self.connect():
            return False

        if self.pods is not None and cache:
            return True

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
            return False

        self.pods = []
        for item in response.items:
            pod = self.convert_pod(item)
            if pod is not None:
                self.pods.append(pod)

        self.log.k8s_mo(
            'pod',
            self.pods
        )

        return True
