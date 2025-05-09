import time
import traceback


class K8sOperatorGroupApi():
    def __init__(self):
        self.operator_group_mo = None

    def get_operator_group_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.operator_group_mo is not None:
                return self.operator_group_mo

        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return None

        try:
            start_time = int(time.time() * 1000)
            response = api_handler.resources.get(
                api_version='operators.coreos.com/v1',
                kind='OperatorGroup'
            )
            self.operator_group_mo = response.get().to_dict()['items']
            self.log.k8s(
                'get',
                'operator_group',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('k8s.get_operator_group_mo', traceback.format_exc())
            self.log.k8s(
                'get',
                'operator_group',
                True,
                int(time.time() * 1000) - start_time
            )
            print(traceback.format_exc())
            return None

        self.log.k8s_mo(
            'operator_group',
            self.operator_group_mo
        )

        return self.operator_group_mo
