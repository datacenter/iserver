import json
import yaml
import time
from lib import filter_helper
from menu.common import get_confirmation


class K8sKnativeKafkaInfo():
    def __init__(self):
        self.knative_kafka = None

    def get_knative_kafka_info(self, knative_kafka_mo):
        if knative_kafka_mo is None:
            return None

        info = {}
        info['__Output'] = {}

        metadata_info = self.get_metadata_info(
            knative_kafka_mo
        )
        info.update(metadata_info)

        info['spec'] = self.get(knative_kafka_mo, 'spec')
        return info

    def get_knative_kafkas_info(self, cache_enabled=True):
        if cache_enabled:
            if self.knative_kafka is not None:
                return self.knative_kafka

        managed_objects = self.get_knative_kafka_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.knative_kafka = []
        for managed_object in managed_objects:
            knative_kafka_info = {}
            knative_kafka_info['info'] = self.get_knative_kafka_info(
                managed_object
            )
            knative_kafka_info['mo'] = managed_object
            self.knative_kafka.append(
                knative_kafka_info
            )

        return self.knative_kafka

    def match_knative_kafka(self, knative_kafka_info, object_filter):
        if object_filter is None or len(object_filter) == 0:
            return True

        for rule in object_filter:
            (key, value) = rule.split(':')

            key_found = False

            if key == 'namespace':
                key_found = True
                if not filter_helper.match_string(value, knative_kafka_info['namespace']):
                    return False

            if key == 'name':
                key_found = True
                if not filter_helper.match_string(value, knative_kafka_info['name']):
                    return False

            if not key_found:
                self.log.error(
                    'match_knative_kafka',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_knative_kafkas(self, object_filter=None, return_mo=False, cache_enabled=True):
        all_knative_kafkas = self.get_knative_kafkas_info(cache_enabled=cache_enabled)
        if all_knative_kafkas is None:
            return None

        knative_kafkas = []

        for knative_kafka_info in all_knative_kafkas:
            if not self.match_knative_kafka(knative_kafka_info['info'], object_filter):
                continue

            if return_mo:
                knative_kafkas.append(
                    knative_kafka_info['mo']
                )
                continue

            knative_kafkas.append(
                knative_kafka_info['info']
            )

        return knative_kafkas

    def is_knative_kafka(self, namespace, name, cache_enabled=True):
        if self.get_knative_kafka(namespace, name, cache_enabled=cache_enabled) is None:
            return False
        return True

    def is_any_knative_kafka(self, cache_enabled=True):
        policies = self.get_knative_kafkas(cache_enabled=cache_enabled)
        if policies is None or len(policies) == 0:
            return False
        return True

    def get_knative_kafka(self, namespace, name, return_mo=False, cache_enabled=True):
        object_filter = []
        object_filter.append(
            'namespace:%s' % (namespace)
        )
        object_filter.append(
            'name:%s' % (name)
        )
        knative_kafkas = self.get_knative_kafkas(
            object_filter=object_filter,
            return_mo=return_mo,
            cache_enabled=cache_enabled
        )
        if knative_kafkas is None:
            return None

        if len(knative_kafkas) == 1:
            return knative_kafkas[0]

        return None

    def delete_knative_kafkas(self, my_output=None, wait=True):
        if my_output is not None:
            my_output.default('Delete Knative Kafka', before_newline=True, underline=True)

        nfds = self.get_knative_kafkas(
            cache_enabled=False
        )
        if nfds is None:
            if my_output is not None:
                my_output.error('Failed to get knative kafka')
            return False

        if len(nfds) == 0:
            if my_output is not None:
                my_output.default('- no knative kafka found')
            return True
        
        for nfd in nfds:
            if my_output is not None:
                my_output.default('- %s' % (nfd['namespace_name']))

            success = self.delete_knative_kafka_mo(
                nfd['namespace'],
                nfd['name']
            )
            if not success:
                if my_output is not None:
                    my_output.error('knative kafka delete failed')

                return False

            if wait:
                if my_output is not None:
                    my_output.default('- wait for no knative kafka')

                if not self.wait_no_knative_kafka(nfd['namespace'], nfd['name']):
                    if my_output is not None:
                        my_output.error('Time out')
                    return False
            
        return True
    
    def wait_knative_kafka(self, namespace, name, max_time=60):
        start_time = int(time.time())
        while True:
            info = self.get_knative_kafka(
                namespace,
                name,
                cache_enabled=False
            )
            if info is not None:
                return True

            duration = int(time.time()) - start_time
            if duration > max_time:
                self.log.error(
                    'k8s.wait_no_knative_kafka',
                    'Max time reached: %s/%s' % (namespace, name)
                )
                return False

            time.sleep(5)

    def wait_no_knative_kafka(self, namespace, name, max_time=60):
        start_time = int(time.time())
        while True:
            info = self.get_knative_kafka(
                namespace,
                name,
                cache_enabled=False
            )
            if info is None:
                return True

            duration = int(time.time()) - start_time
            if duration > max_time:
                self.log.error(
                    'k8s.wait_no_knative_kafka',
                    'Max time reached: %s/%s' % (namespace, name)
                )
                return False

            time.sleep(5)

    def create_knative_kafka(self, body, my_output=None, confirmation=False, wait=True):
        if my_output is None:
            confirmation = False

        namespace = body['metadata']['namespace']
        name = body['metadata']['name']
        if my_output is not None:
            my_output.default('Create knative kafka', before_newline=True, underline=True)
            my_output.default('- namespace: %s' % (namespace))
            my_output.default('- name: %s' % (name))

        if self.is_knative_kafka(namespace, name, cache_enabled=False):
            if my_output is not None:
                my_output.default('- already exists')
                return True
        
        if my_output is not None:
            my_output.default(yaml.dump(body), before_newline=True, wrap='~~~')

        if confirmation:
            if not get_confirmation():
                return False

        if not self.create_knative_kafka_mo(body):
            if my_output is not None:
                my_output.error('Knative kafka create failed')
            return False

        if my_output is not None:
            my_output.default('knative kafka created', before_newline=True, after_newline=True)

        if not wait:
            return True
        
        if my_output is not None:
            my_output.default('Wait for knative kafka...')

        if not self.wait_knative_kafka(namespace, name, max_time=30):
            if my_output is not None:
                my_output.error('Timed out')
            
            return False

        return True    