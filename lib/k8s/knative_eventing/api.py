import time
import traceback


class K8sKnativeEventingApi():
    def __init__(self):
        self.knative_eventing_mo = None

    def get_knative_eventing_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.knative_eventing_mo is not None:
                return self.knative_eventing_mo

        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return None

        try:
            start_time = int(time.time() * 1000)
            response = api_handler.resources.get(
                api_version='operator.knative.dev/v1beta1',
                kind='KnativeEventing'
            )
            self.knative_eventing_mo = response.get().to_dict()['items']
            self.log.k8s(
                'get',
                'knative_eventing',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('k8s.get_knative_eventing_mo', traceback.format_exc())
            self.log.k8s(
                'get',
                'knative_eventing',
                True,
                int(time.time() * 1000) - start_time
            )
            print(traceback.format_exc())
            return None

        self.log.k8s_mo(
            'knative_eventing',
            self.knative_eventing_mo
        )

        return self.knative_eventing_mo

    def create_knative_eventing_mo(self, knative_eventing):
        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return False

        try:
            start_time = int(time.time() * 1000)
            obj_list = api_handler.resources.get(api_version='operator.knative.dev/v1beta1', kind='KnativeEventing')
            success = True
            response = obj_list.create(
                body=knative_eventing,
                namespace=knative_eventing['metadata']['namespace']
            )
        except BaseException:
            success = False
            self.log.error('ocp.create_knative_eventing_mo', traceback.format_exc())

        self.log.ocp(
            'create',
            'knative_eventing',
            success,
            int(time.time() * 1000) - start_time
        )

        return success

    def delete_knative_eventing_mo(self, namespace, name):
        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return False

        try:
            start_time = int(time.time() * 1000)
            obj_list = api_handler.resources.get(api_version='operator.knative.dev/v1beta1', kind='KnativeEventing')
            success = True
            response = obj_list.delete(
                namespace=namespace,
                name=name
            )
        except BaseException:
            success = False
            self.log.error('ocp.delete_knative_eventing_mo', traceback.format_exc())

        self.log.ocp(
            'delete',
            'delete_knative_eventing',
            success,
            int(time.time() * 1000) - start_time
        )

        return success
