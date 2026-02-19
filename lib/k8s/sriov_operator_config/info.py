import time
import yaml
from menu.common import get_confirmation


class K8sSriovOperatorConfigInfo():
    def __init__(self):
        self.sriov_operator_config = None

    def get_sriov_operator_config_info(self, sriov_operator_config_mo):
        if sriov_operator_config_mo is None:
            return None

        info = {}
        info['__Output'] = {}

        metadata_info = self.get_metadata_info(
            sriov_operator_config_mo
        )
        info.update(metadata_info)

        info['spec'] = self.get(sriov_operator_config_mo, 'spec')
        return info

    def get_sriov_operator_configs_info(self, cache_enabled=True):
        if cache_enabled:
            if self.sriov_operator_config is not None:
                return self.sriov_operator_config

        managed_objects = self.get_sriov_operator_config_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.sriov_operator_config = []
        for managed_object in managed_objects:
            sriov_operator_config_info = {}
            sriov_operator_config_info['info'] = self.get_sriov_operator_config_info(
                managed_object
            )
            sriov_operator_config_info['mo'] = managed_object
            self.sriov_operator_config.append(
                sriov_operator_config_info
            )

        return self.sriov_operator_config

    def get_sriov_operator_configs(self, return_mo=False, cache_enabled=True):
        all_sriov_operator_configs = self.get_sriov_operator_configs_info(cache_enabled=cache_enabled)
        if all_sriov_operator_configs is None:
            return None

        sriov_operator_configs = []

        for sriov_operator_config_info in all_sriov_operator_configs:
            if return_mo:
                sriov_operator_configs.append(
                    sriov_operator_config_info['mo']
                )
                continue

            sriov_operator_configs.append(
                sriov_operator_config_info['info']
            )

        return sriov_operator_configs

    def get_sriov_operator_config(self, return_mo=False, cache_enabled=True):
        configs = self.get_sriov_operator_configs(return_mo=return_mo, cache_enabled=cache_enabled)
        if configs is None or len(configs) != 1:
            return None
        return configs[0]

    def is_sriov_operator_config(self, cache_enabled=True):
        if self.get_sriov_operator_config(cache_enabled=cache_enabled) is None:
            return False
        return True

    def get_sriov_operator_config_body(self, namespace, name, injector, webhook):
        body = {}
        body['apiVersion'] = 'sriovnetwork.openshift.io/v1'
        body['kind'] = 'SriovOperatorConfig'
        body['metadata'] = {}
        body['metadata']['namespace'] = namespace
        body['metadata']['name'] = name
        body['spec'] = {}
        body['spec']['enableInjector'] = injector
        body['spec']['enableOperatorWebhook'] = webhook
        body['spec']['logLevel'] = 2
        return body
    
    def create_sriov_operator_config(self, namespace, name, injector, webhook, confirmation=False, my_output=None, wait=True):
        if my_output is None:
            confirmation = False

        if my_output is not None:
            my_output.default('Create SRIOV Operator Config', before_newline=True, underline=True)
            my_output.default('- namespace: %s' % (namespace))
            my_output.default('- name: %s' % (name))
            my_output.default('- injector: %s' % (injector))
            my_output.default('- webhook: %s' % (webhook))

        if self.is_sriov_operator_config():
            if my_output is not None:
                my_output.default('- already exists')
            return True
        
        body = self.get_sriov_operator_config_body(
            namespace,
            name,
            injector,
            webhook
        )
        if my_output is not None:
            my_output.default(yaml.dump(body), before_newline=True, wrap='~~~')

        if confirmation:
            if not get_confirmation():
                return False

        if not self.create_sriov_operator_config_mo(body):
            if my_output is not None:
                my_output.error('REST API failed')
            return False
        
        if my_output is not None:
            my_output.default('SRIOV operator config created', before_newline=True, after_newline=True)

        if wait:
            if my_output is not None:
                my_output.default('Wait for operator config [timeout:60]...')

            if not self.wait_sriov_operator_config(max_time=60):
                if my_output is not None:
                    my_output.error('Timed out')
                
                return False

            if my_output is not None:
                my_output.default('Wait for operator config resources...')

            if not self.wait_subscription_sriov_ready(configured=True, my_output=my_output):
                if my_output is not None:
                    my_output.error('Timed out')
                
                return False

        return True    

    def delete_sriov_operator_config(self, my_output=None, wait=True):
        if my_output is not None:
            my_output.default('Delete SRIOV Operator Config', before_newline=True, underline=True)

        config = self.get_sriov_operator_config(cache_enabled=False)
        if config is None:
            if my_output is not None:
                my_output.default('- already deleted')
            return True
        
        if my_output is not None:
            my_output.default('- name: %s' % (config['name']))
        
        if not self.delete_sriov_operator_config_mo(config['namespace'], config['name']):
            if my_output is not None:
                my_output.error('REST API failed')
            return False
        
        if my_output is not None:
            my_output.default('SRIOV operator config deleted', before_newline=True, after_newline=True)

        if wait:
            if my_output is not None:
                my_output.default('Wait for no sriov operator config [timeout:60]...')

            if not self.wait_no_sriov_operator_config(max_time=60):
                if my_output is not None:
                    my_output.error('Timed out')
                
                return False

            if my_output is not None:
                my_output.default('Wait for no sriov operator config resources...')

            if not self.wait_no_subscription_sriov_configuration(my_output=my_output):
                if my_output is not None:
                    my_output.error('Timed out')
                
                return False

        return True    

    def wait_sriov_operator_config(self, max_time=60):
        start_time = int(time.time())
        while True:
            if self.is_sriov_operator_config(cache_enabled=False):
                return True

            duration = int(time.time()) - start_time
            if duration > max_time:
                self.log.error(
                    'k8s.wait_sriov_operator_config',
                    'Max time reached'
                )
                return False

            time.sleep(5)

    def wait_no_sriov_operator_config(self, max_time=60):
        start_time = int(time.time())
        while True:
            if not self.is_sriov_operator_config(cache_enabled=False):
                return True

            duration = int(time.time()) - start_time
            if duration > max_time:
                self.log.error(
                    'k8s.wait_sriov_operator_config',
                    'Max time reached'
                )
                return False

            time.sleep(5)