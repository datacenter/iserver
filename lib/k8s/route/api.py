import time
import traceback


class K8sRouteApi():
    def __init__(self):
        self.route_mo = None

    def get_route_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.route_mo is not None:
                return self.route_mo

        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return None

        try:
            start_time = int(time.time() * 1000)
            response = api_handler.resources.get(
                api_version='route.openshift.io/v1',
                kind='Route'
            )
            self.route_mo = response.get().to_dict()['items']
            self.log.k8s(
                'get',
                'route',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('k8s.get_route_mo', traceback.format_exc())
            self.log.k8s(
                'get',
                'route',
                True,
                int(time.time() * 1000) - start_time
            )
            print(traceback.format_exc())
            return None

        self.log.k8s_mo(
            'route',
            self.route_mo
        )

        return self.route_mo

    def create_route_mo(self, body):
        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return False

        try:
            start_time = int(time.time() * 1000)
            obj_list = api_handler.resources.get(api_version='route.openshift.io/v1', kind='Route')
            success = True
            response = obj_list.create(
                body=body
            )
        except BaseException:
            success = False
            self.log.error('ocp.route', traceback.format_exc())

        self.log.ocp(
            'create',
            'route',
            success,
            int(time.time() * 1000) - start_time
        )

        return success

    def delete_route_mo(self, namespace, name):
        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return False

        try:
            start_time = int(time.time() * 1000)
            obj_list = api_handler.resources.get(api_version='route.openshift.io/v1', kind='Route')
            success = True
            response = obj_list.delete(
                namespace=namespace,
                name=name
            )
        except BaseException:
            success = False
            self.log.error('ocp.route', traceback.format_exc())

        self.log.ocp(
            'create',
            'route',
            success,
            int(time.time() * 1000) - start_time
        )

        return success
    