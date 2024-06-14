#!usr/bin/env python

import os
import base64
import json
import time
import traceback

class K8sSecrets():
    def __init__(self):
        self.k8s_secrets = None

    def convert_secret_output_json(self, output):
        try:
            if output is None:
                return None

            output = str(output)

            if 'last-applied-configuration' in output:
                return None

            output = output.replace('\'', '\"')
            output = output.replace(': None', ': null')
            output = output.replace(': True', ': true')
            output = output.replace(': False', ': false')
            return json.loads(output)
        except:
            self.log.error('k8s_secrets.convert_secret_output_json', output)
            self.log.error('k8s_secrets.convert_secret_output_json', traceback.format_exc())
            return None

    def convert_secret_metadata_managed_fields(self, mfs):
        try:
            if mfs is None:
                return None

            n = []
            for mf in mfs:
                t = dict()
                t['api_version'] = mf.api_version
                t['fields'] = mf.fields_v1
                t['manager'] = mf.manager
                t['operation'] = mf.operation
                t['time'] = self.convert_timestamp(mf.time)
                n.append(t)

        except:
            self.log.error('k8s_secrets.convert_secret_metadata_managed_fields', traceback.format_exc())
            return None

        return n

    def convert_secret_metadata(self, metadata):
        try:
            n = dict()
            n['uid'] = metadata.uid
            n['self_link'] = metadata.self_link
            n['resource_version'] = metadata.resource_version
            if metadata.owner_references is None:
                n['owner_references'] = None
            else:
                n['owner_references'] = str(metadata.owner_references)
            n['name'] = metadata.name
            n['namespace'] = metadata.namespace
            n['annotations'] = self.convert_secret_output_json(metadata.annotations)
            n['labels'] = self.convert_secret_output_json(metadata.labels)
            n['managed_fields'] = self.convert_secret_metadata_managed_fields(metadata.managed_fields)
            n['creation_timestamp'] = self.convert_timestamp(metadata.creation_timestamp)

        except:
            self.log.error('k8s_secrets.convert_secret_metadata', traceback.format_exc())
            return None

        return n

    def convert_secret(self, secret, get_data_property_types=None):
        try:
            n = dict()
            if get_data_property_types is None or secret.type in get_data_property_types:
                n['data'] = secret.data
                n['string_data'] = secret.string_data

            n['kind'] = secret.kind
            n['type'] = secret.type
            n['metadata'] = self.convert_secret_metadata(secret.metadata)

            try:
                n['name'] = n['metadata']['name']
            except:
                n['name'] = None

            try:
                n['namespace'] = n['metadata']['namespace']
            except:
                n['namespace'] = None

            try:
                n['age'] = int(time.time()) - n['metadata']['creation_timestamp']
            except:
                n['age'] = None

            try:
                test = json.dumps(n)
            except:
                self.log.error('k8s_secrets.convert_secret', 'Secret is not JSON')
                self.log.error('k8s_secrets.convert_secret', n)
                return None

        except:
            self.log.error('k8s_secrets.convert_secret', traceback.format_exc())
            return None

        return n

    def get_secret_data(self, secret_id = None, namespace = None, name = None, name_pattern = None):
        self.get_secrets()
        if self.k8s_secrets is None:
            return None

        try:
            for secret in self.k8s_secrets:
                match = False
                if secret_id is not None and secret['metadata']['uid'] == secret_id:
                    match = True

                if namespace is not None and name is not None:
                    if secret['namespace'] == namespace and secret['name'] == name:
                        match = True

                if namespace is not None and name_pattern is not None:
                    if secret['namespace'] == namespace and secret['name'].startswith(name_pattern):
                        match = True

                if match:
                    secret['decoded'] = dict()
                    for key in secret['data']:
                        try:
                            secret['decoded'][key] = base64.decodestring(
                                secret['data'][key].encode('utf-8')
                            ).decode('utf-8')
                        except:
                            self.log.error('k8s_secrets.get_secret', traceback.format_exc())
                            secret['decoded'][key] = None

                    ret = dict()
                    ret['data'] = secret['data']
                    ret['decoded'] = secret['decoded']
                    return ret

        except:
            self.log.error('k8s_secrets.get_secret', traceback.format_exc())

        return None

    def get_secret(self, secret_id = None, namespace = None, name = None, name_pattern = None):
        self.get_secrets()
        if self.k8s_secrets is None:
            return None

        try:
            for secret in self.k8s_secrets:
                match = False
                if secret_id is not None and secret['metadata']['uid'] == secret_id:
                    match = True

                if namespace is not None and name is not None:
                    if secret['namespace'] == namespace and secret['name'] == name:
                        match = True

                if namespace is not None and name_pattern is not None:
                    if secret['namespace'] == namespace and secret['name'].startswith(name_pattern):
                        match = True

                if match:
                    return secret

        except:
            self.log.error('k8s_secrets.get_secret', traceback.format_exc())

        return None

    def get_secrets(self, get_data_property_types=None):
        if self.k8s_secrets is not None:
            return

        # https://github.com/kubernetes-client/python/blob/master/kubernetes/docs/CoreV1Api.md#list_secret_for_all_namespaces
        try:
            self.k8s_secrets = []

            start_time = int(time.time()*1000)
            response = self.api.list_secret_for_all_namespaces(timeout_seconds=self.api_timeout_seconds)
            self.api_statistics('list_secret_for_all_namespaces', int(time.time()*1000) - start_time)

            if response is not None:
                for i in response.items:
                    secret = self.convert_secret(i, get_data_property_types=get_data_property_types)
                    if secret is not None:
                        self.k8s_secrets.append(secret)

        except:
            self.log.error('k8s_secrets.get_secrets', traceback.format_exc())