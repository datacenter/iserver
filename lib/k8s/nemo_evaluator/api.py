import time
import traceback


class K8sNemoEvaluatorApi():
    def __init__(self):
        self.nemo_evaluator_mo = None

    def get_nemo_evaluator_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.nemo_evaluator_mo is not None:
                return self.nemo_evaluator_mo

        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return None

        try:
            start_time = int(time.time() * 1000)
            response = api_handler.resources.get(
                api_version='apps.nvidia.com/v1alpha1',
                kind='NemoEvaluator'
            )
            self.nemo_evaluator_mo = response.get().to_dict()['items']
            self.log.k8s(
                'get',
                'nemo_evaluator',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('k8s.get_nemo_evaluator_mo', traceback.format_exc())
            self.log.k8s(
                'get',
                'nemo_evaluator',
                True,
                int(time.time() * 1000) - start_time
            )
            print(traceback.format_exc())
            return None

        self.log.k8s_mo(
            'nemo_evaluator',
            self.nemo_evaluator_mo
        )

        return self.nemo_evaluator_mo

    def create_nemo_evaluator_mo(self, nemo_evaluator):
        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return False

        try:
            start_time = int(time.time() * 1000)
            obj_list = api_handler.resources.get(api_version='apps.nvidia.com/v1alpha1', kind='NemoEvaluator')
            success = True
            response = obj_list.create(
                body=nemo_evaluator,
                namespace=nemo_evaluator['metadata']['namespace']
            )
        except BaseException:
            success = False
            self.log.error('ocp.create_nemo_evaluator_mo', traceback.format_exc())

        self.log.ocp(
            'create',
            'nemo_evaluator',
            success,
            int(time.time() * 1000) - start_time
        )

        return success

    def delete_nemo_evaluator_mo(self, namespace, name):
        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return False

        try:
            start_time = int(time.time() * 1000)
            obj_list = api_handler.resources.get(api_version='apps.nvidia.com/v1alpha1', kind='NemoEvaluator')
            success = True
            response = obj_list.delete(
                namespace=namespace,
                name=name
            )
        except BaseException:
            success = False
            self.log.error('ocp.delete_nemo_evaluator_mo', traceback.format_exc())

        self.log.ocp(
            'delete',
            'delete_nemo_evaluator',
            success,
            int(time.time() * 1000) - start_time
        )

        return success
