import time
import traceback


class K8sPackageApi():
    def __init__(self):
        self.package_mo = None

    def get_package_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.package_mo is not None:
                return self.package_mo

        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return None

        try:
            start_time = int(time.time() * 1000)
            response = api_handler.resources.get(
                api_version='packages.operators.coreos.com/v1',
                kind='PackageManifest'
            )
            self.package_mo = response.get().to_dict()['items']
            self.log.k8s(
                'get',
                'package',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('k8s.get_package_mo', traceback.format_exc())
            self.log.k8s(
                'get',
                'package',
                True,
                int(time.time() * 1000) - start_time
            )
            print(traceback.format_exc())
            return None

        self.log.k8s_mo(
            'package',
            self.package_mo
        )

        return self.package_mo
