import time
import traceback


class K8sVersionApi():
    def __init__(self):
        self.version_mo = None

    def get_version_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.version_mo is not None:
                return self.version_mo

        api_handler = self.get_api(api_type='version')
        if api_handler is None:
            return None

        ocp_handler = self.get_api(cluster_type='ocp')

        try:
            start_time = int(time.time() * 1000)
            k8s_version = api_handler.get_code().to_dict()

            ocp_version = None
            if ocp_handler is not None:
                response = ocp_handler.resources.get(
                    api_version='config.openshift.io/v1',
                    kind='ClusterVersion'
                )
                ocp_version = response.get().to_dict()['items'][0]

            version_mo = {}
            version_mo['k8s'] = k8s_version
            version_mo['ocp'] = ocp_version
            self.version_mo = [version_mo]

            self.log.k8s(
                'get',
                'version',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('k8s.get_version_mo', traceback.format_exc())
            self.log.k8s(
                'get',
                'version',
                False,
                int(time.time() * 1000) - start_time
            )
            return None

        self.log.k8s_mo(
            'version',
            self.version_mo
        )

        return self.version_mo
