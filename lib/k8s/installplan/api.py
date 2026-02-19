import time
import traceback


class K8sInstallplanApi():
    def __init__(self):
        self.installplan_mo = None

    def get_installplan_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.installplan_mo is not None:
                return self.installplan_mo

        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return None

        try:
            start_time = int(time.time() * 1000)
            response = api_handler.resources.get(
                api_version='operators.coreos.com/v1alpha1',
                kind='InstallPlan'
            )
            self.installplan_mo = response.get().to_dict()['items']
            self.log.k8s(
                'get',
                'installplan',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('k8s.get_installplan_mo', traceback.format_exc())
            self.log.k8s(
                'get',
                'installplan',
                True,
                int(time.time() * 1000) - start_time
            )
            print(traceback.format_exc())
            return None

        self.log.k8s_mo(
            'installplan',
            self.installplan_mo
        )

        return self.installplan_mo

    def patch_installplan_mo(self, body):
        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return None

        try:
            obj_list = api_handler.resources.get(api_version='operators.coreos.com/v1alpha1', kind='InstallPlan')
            obj_list.patch(
                body=body,
                namespace=body['metadata']['namespace'],
                content_type='application/merge-patch+json'
            )

        except BaseException:
            self.log.error('k8s.patch_installplan_mo', traceback.format_exc())
            print(traceback.format_exc())
            return False

        return True