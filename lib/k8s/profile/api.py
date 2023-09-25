import time
import traceback


class K8sProfileApi():
    def __init__(self):
        self.profile_mo = None

    def get_profile_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.profile_mo is not None:
                return self.profile_mo

        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return None

        try:
            start_time = int(time.time() * 1000)
            response = api_handler.resources.get(
                api_version='tuned.openshift.io/v1',
                kind='Profile'
            )
            self.profile_mo = response.get().to_dict()['items']
            self.log.k8s(
                'get',
                'profile',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('k8s.get_profile_mo', traceback.format_exc())
            self.log.k8s(
                'get',
                'profile',
                True,
                int(time.time() * 1000) - start_time
            )
            print(traceback.format_exc())
            return None

        self.log.k8s_mo(
            'profile',
            self.profile_mo
        )

        return self.profile_mo
