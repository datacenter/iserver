import time
import traceback


class K8sSubscriptionApi():
    def __init__(self):
        self.subscription_mo = None

    def get_subscription_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.subscription_mo is not None:
                return self.subscription_mo

        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return None

        try:
            start_time = int(time.time() * 1000)
            response = api_handler.resources.get(
                api_version='operators.coreos.com/v1alpha1',
                kind='Subscription'
            )
            self.subscription_mo = response.get().to_dict()['items']
            self.log.k8s(
                'get',
                'subscription',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('k8s.get_subscription_mo', traceback.format_exc())
            self.log.k8s(
                'get',
                'subscription',
                True,
                int(time.time() * 1000) - start_time
            )
            print(traceback.format_exc())
            return None

        self.log.k8s_mo(
            'subscription',
            self.subscription_mo
        )

        return self.subscription_mo

    def create_subscription_mo(self, subscription):
        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return False

        try:
            start_time = int(time.time() * 1000)
            obj_list = api_handler.resources.get(api_version='operators.coreos.com/v1alpha1', kind='Subscription')
            success = True
            response = obj_list.create(
                body=subscription,
                namespace=subscription['metadata']['namespace'],
            )
        except BaseException:
            success = False
            self.log.error('ocp.create_subscription', traceback.format_exc())

        self.log.ocp(
            'create',
            'subscription',
            success,
            int(time.time() * 1000) - start_time
        )

        return success

    def delete_subscription_mo(self, namespace, name):
        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return False

        try:
            start_time = int(time.time() * 1000)
            obj_list = api_handler.resources.get(api_version='operators.coreos.com/v1alpha1', kind='Subscription')
            success = True
            response = obj_list.delete(
                namespace=namespace,
                name=name
            )
        except BaseException:
            success = False
            self.log.error('ocp.delete_subscription', traceback.format_exc())

        self.log.ocp(
            'delete',
            'subscription',
            success,
            int(time.time() * 1000) - start_time
        )

        return success
