import os
import time
import traceback
import yaml

from kubernetes import config
from kubernetes import client
from kubernetes.config import kube_config

from openshift.dynamic import DynamicClient
from urllib3.exceptions import MaxRetryError


class K8sApi():
    def __init__(self, kubeconfig_filename, cluster_type='standard'):
        self.kubeconfig_filename = kubeconfig_filename
        self.cluster_type = cluster_type
        self.api = {}
        self.api_timeout_seconds = 3
        self.connect_timeout_seconds = 3
        self.api_retries = 1

    def get_api(self, cluster_type='standard', api_type='v1'):
        if cluster_type not in ['standard', 'ocp']:
            self.log.error(
                'get_api',
                'Unsupported cluster type: %s' % (cluster_type)
            )
            return None

        if cluster_type == 'standard':
            if api_type == 'v1':
                return self.get_api_standard()

            if api_type == 'version':
                return self.get_api_version()

        if cluster_type == 'ocp':
            return self.get_api_ocp()

        return None

    def get_api_standard(self):
        if 'standard' in self.api and self.api['standard'] is not None:
            return self.api['standard']

        if not os.path.isfile(self.kubeconfig_filename):
            self.log.error(
                'k8s.get_api_standard',
                'Kubeconfig file not found: %s' % (self.kubeconfig_filename)
            )
            return None

        try:
            start_time = int(time.time() * 1000)

            my_config = client.Configuration()
            my_config.verify_ssl = False
            my_config.retries = self.api_retries

            with open(self.kubeconfig_filename, 'r', encoding='utf-8') as file_handler:
                configuration_yaml = yaml.safe_load(file_handler.read())

            k8_loader = kube_config.KubeConfigLoader(
                configuration_yaml
            )
            k8_loader.load_and_set(my_config)

            my_client = client.ApiClient(
                configuration=my_config
            )
            self.api['standard'] = client.CoreV1Api(
                api_client=my_client
            )

            response = self.api['standard'].list_namespace(
                timeout_seconds=self.api_timeout_seconds,
                _request_timeout=self.connect_timeout_seconds
            )

            self.log.k8s(
                'connect.standard',
                '-',
                True,
                int(time.time() * 1000) - start_time
            )

        except MaxRetryError:
            self.log.error(
                'k8s.get_api_standard',
                'Connection timed out'
            )
            return None

        except BaseException:
            self.log.error(
                'k8s.get_api_standard',
                'Kubeconfig file failed: %s' % (self.kubeconfig_filename)
            )
            self.log.error('k8s.get_api_standard', traceback.format_exc())
            return None

        return self.api['standard']

    def get_api_version(self):
        if 'version' in self.api and self.api['version'] is not None:
            return self.api['version']

        if not os.path.isfile(self.kubeconfig_filename):
            self.log.error(
                'k8s.get_api_version',
                'Kubeconfig file not found: %s' % (self.kubeconfig_filename)
            )
            return None

        try:
            start_time = int(time.time() * 1000)

            config.load_kube_config(self.kubeconfig_filename)
            self.api['version'] = client.VersionApi()

            self.log.k8s(
                'connect.version',
                '-',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error(
                'k8s.get_api_version',
                'Kubeconfig file failed: %s' % (self.kubeconfig_filename)
            )
            self.log.error('k8s.get_api_version', traceback.format_exc())
            return None

        return self.api['version']

    def get_api_ocp(self):
        if 'ocp' in self.api and self.api['ocp'] is not None:
            return self.api['ocp']

        if not os.path.isfile(self.kubeconfig_filename):
            self.log.error(
                'k8s.get_api_ocp',
                'Kubeconfig file not found: %s' % (self.kubeconfig_filename)
            )
            return None

        try:
            start_time = int(time.time() * 1000)

            my_config = client.Configuration()
            my_config.retries = self.api_retries

            with open(self.kubeconfig_filename, 'r', encoding='utf-8') as file_handler:
                configuration_yaml = yaml.safe_load(file_handler.read())

            k8_loader = kube_config.KubeConfigLoader(
                configuration_yaml
            )
            k8_loader.load_and_set(my_config)

            my_client = client.ApiClient(
                configuration=my_config
            )
            self.api['ocp'] = DynamicClient(my_client)

            # response = self.api['ocp'].resources.get(
            #     api_version='v1',
            #     kind='Namespace'
            # )

            self.log.k8s(
                'connect.ocp',
                '-',
                True,
                int(time.time() * 1000) - start_time
            )

        except MaxRetryError:
            self.log.error(
                'k8s.get_api_standard',
                'Connection timed out'
            )
            return None

        except BaseException:
            self.log.error(
                'k8s.get_api_ocp',
                'Kubeconfig file failed: %s' % (self.kubeconfig_filename)
            )
            self.log.error('k8s.get_api_standard', traceback.format_exc())
            return None

        return self.api['ocp']
