import time
import traceback


class K8sKnativeKafkaApi():
    def __init__(self):
        self.knative_kafka_mo = None

    def get_knative_kafka_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.knative_kafka_mo is not None:
                return self.knative_kafka_mo

        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return None

        try:
            start_time = int(time.time() * 1000)
            response = api_handler.resources.get(
                api_version='operator.serverless.openshift.io/v1alpha1',
                kind='KnativeKafka'
            )
            self.knative_kafka_mo = response.get().to_dict()['items']
            self.log.k8s(
                'get',
                'knative_kafka',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('k8s.get_knative_kafka_mo', traceback.format_exc())
            self.log.k8s(
                'get',
                'knative_kafka',
                True,
                int(time.time() * 1000) - start_time
            )
            print(traceback.format_exc())
            return None

        self.log.k8s_mo(
            'knative_kafka',
            self.knative_kafka_mo
        )

        return self.knative_kafka_mo

    def create_knative_kafka_mo(self, knative_kafka):
        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return False

        try:
            start_time = int(time.time() * 1000)
            obj_list = api_handler.resources.get(api_version='operator.serverless.openshift.io/v1alpha1', kind='KnativeKafka')
            success = True
            response = obj_list.create(
                body=knative_kafka,
                namespace=knative_kafka['metadata']['namespace']
            )
        except BaseException:
            success = False
            self.log.error('ocp.create_knative_kafka_mo', traceback.format_exc())

        self.log.ocp(
            'create',
            'knative_kafka',
            success,
            int(time.time() * 1000) - start_time
        )

        return success

    def delete_knative_kafka_mo(self, namespace, name):
        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return False

        try:
            start_time = int(time.time() * 1000)
            obj_list = api_handler.resources.get(api_version='operator.serverless.openshift.io/v1alpha1', kind='KnativeKafka')
            success = True
            response = obj_list.delete(
                namespace=namespace,
                name=name
            )
        except BaseException:
            success = False
            self.log.error('ocp.delete_knative_kafka_mo', traceback.format_exc())

        self.log.ocp(
            'delete',
            'delete_knative_kafka',
            success,
            int(time.time() * 1000) - start_time
        )

        return success
