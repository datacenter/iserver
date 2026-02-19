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

    def create_operator_group_mo(self, body):
        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return False

        try:
            start_time = int(time.time() * 1000)
            body['apiVersion'] = 'operators.coreos.com/v1'
            obj_list = api_handler.resources.get(api_version='operators.coreos.com/v1', kind='OperatorGroup')
            success = True
            response = obj_list.create(
                body=body,
                namespace=body['metadata']['namespace'],
            )
        except BaseException:
            success = False
            self.log.error('ocp.create_subscreate_operator_groupcription', traceback.format_exc())

        self.log.ocp(
            'create',
            'operator_group',
            success,
            int(time.time() * 1000) - start_time
        )

        return success

    def delete_operator_group_mo(self, namespace, name):
        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return False

        try:
            start_time = int(time.time() * 1000)
            obj_list = api_handler.resources.get(api_version='operators.coreos.com/v1', kind='OperatorGroup')
            success = True
            response = obj_list.delete(
                namespace=namespace,
                name=name
            )
        except BaseException:
            success = False
            self.log.error('ocp.delete_operator_group', traceback.format_exc())

        self.log.ocp(
            'delete',
            'operator_group',
            success,
            int(time.time() * 1000) - start_time
        )

        return success
