import time
import traceback


class K8sOAuthApi():
    def __init__(self):
        self.oauth_mo = None

    def get_oauth_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.oauth_mo is not None:
                return self.oauth_mo

        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return None

        try:
            start_time = int(time.time() * 1000)
            response = api_handler.resources.get(
                api_version='config.openshift.io/v1',
                kind='OAuth'
            )
            self.oauth_mo = response.get().to_dict()['items']
            self.log.k8s(
                'get',
                'oauth',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('k8s.get_oauth_mo', traceback.format_exc())
            self.log.k8s(
                'get',
                'oauth',
                True,
                int(time.time() * 1000) - start_time
            )
            print(traceback.format_exc())
            return None

        self.log.k8s_mo(
            'oauth',
            self.oauth_mo
        )

        return self.oauth_mo

    def update_oauth_mo(self, crb):
        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return False

        try:
            start_time = int(time.time() * 1000)
            obj_list = api_handler.resources.get(api_version='config.openshift.io/v1', kind='OAuth')
            success = True
            response = obj_list.replace(
                body=crb,
                name=crb['metadata']['name'],
            )
        except BaseException:
            success = False
            self.log.error('k8s.update_oauth_mo', traceback.format_exc())

        self.log.k8s(
            'update',
            'oauth',
            success,
            int(time.time() * 1000) - start_time
        )

        return success
