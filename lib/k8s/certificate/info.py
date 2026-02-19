import time
import yaml
from lib import filter_helper
from menu.common import get_confirmation


class K8sCertificateInfo():
    def __init__(self):
        self.certificate = None

    def get_certificate_info(self, certificate_mo):
        if certificate_mo is None:
            return None

        info = {}
        info['__Output'] = {}

        metadata_info = self.get_metadata_info(
            certificate_mo
        )
        info.update(metadata_info)

        info['spec'] = self.get(certificate_mo, 'spec')
        info['status'] = self.get(certificate_mo, 'status')
        return info

    def get_certificates_info(self, cache_enabled=True):
        if cache_enabled:
            if self.certificate is not None:
                return self.certificate

        managed_objects = self.get_certificate_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.certificate = []
        for managed_object in managed_objects:
            certificate_info = {}
            certificate_info['info'] = self.get_certificate_info(
                managed_object
            )
            certificate_info['mo'] = managed_object
            self.certificate.append(
                certificate_info
            )

        return self.certificate

    def match_certificate(self, certificate_info, object_filter):
        if object_filter is None or len(object_filter) == 0:
            return True

        for rule in object_filter:
            (key, value) = rule.split(':')

            key_found = False

            if key == 'namespace':
                key_found = True
                if not filter_helper.match_string(value, certificate_info['namespace']):
                    return False
                
            if key == 'name':
                key_found = True
                if not filter_helper.match_string(value, certificate_info['name']):
                    return False

            if not key_found:
                self.log.error(
                    'match_certificate',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_certificates(self, object_filter=None, return_mo=False, cache_enabled=True):
        all_certificates = self.get_certificates_info(cache_enabled=cache_enabled)
        if all_certificates is None:
            return None

        certificates = []

        for certificate_info in all_certificates:
            if not self.match_certificate(certificate_info['info'], object_filter):
                continue

            if return_mo:
                certificates.append(
                    certificate_info['mo']
                )
                continue

            certificates.append(
                certificate_info['info']
            )

        return certificates

    def is_certificate(self, namespace, name, cache_enabled=True):
        if self.get_certificate(namespace, name, cache_enabled=cache_enabled) is None:
            return False
        return True

    def get_certificate(self, namespace, name, return_mo=False, cache_enabled=True):
        object_filter = []
        object_filter.append(
            'namespace:%s' % (namespace)
        )
        object_filter.append(
            'name:%s' % (name)
        )
        certificates = self.get_certificates(
            object_filter=object_filter,
            return_mo=return_mo,
            cache_enabled=cache_enabled
        )
        if certificates is None:
            return None

        if len(certificates) == 1:
            return certificates[0]

        return None

    def get_certificate_body(self, namespace, name, issuer):
        body = {}
        body['apiVersion'] = 'cert-manager.io/v1'
        body['kind'] = 'Certificate'
        body['metadata'] = {}
        body['metadata']['namespace'] = namespace
        body['metadata']['name'] = name
        body['spec'] = {}
        body['spec']['commonName'] = name
        body['spec']['isCA'] = True
        body['spec']['issuerRef'] = {}
        body['spec']['issuerRef']['group'] = 'cert-manager.io'
        body['spec']['issuerRef']['kind'] = 'Issuer'
        body['spec']['issuerRef']['name'] = issuer
        body['spec']['secretName'] = name
        return body

    def create_certificate(self, namespace, name, issuer, confirmation=False, my_output=None, wait=True):
        if my_output is None:
            confirmation = False

        if my_output is not None:
            my_output.default('Create Certificate', before_newline=True, underline=True)
            my_output.default('- namespace: %s' % (namespace))
            my_output.default('- name: %s' % (name))

        if self.is_certificate(namespace, name, cache_enabled=False):
            if my_output is not None:
                my_output.default('- already created')
            return True
        
        body = self.get_certificate_body(
            namespace,
            name,
            issuer
        )

        if my_output is not None:
            my_output.default(yaml.dump(body), before_newline=True, wrap='~~~')

        if confirmation:
            if not get_confirmation():
                return False
        
        success = self.create_certificate_mo(body)
        if not success:
            if my_output is not None:
                my_output.error('Certificate create failed')
            return False

        if my_output is not None:
            my_output.default('- certificate created')
        
        if not wait:
            return True
        
        if my_output is not None:
            my_output.default('- wait until certificate found...')

        success = self.wait_certificate(namespace, name, max_time=60)
        if not success:
            if my_output is not None:
                my_output.error('Timed out')                
            return False
        
        return True
    
    def wait_certificate(self, namespace, name, max_time=60):
        start_time = int(time.time())
        while True:
            info = self.get_certificate(
                namespace,
                name,
                cache_enabled=False
            )
            if info is not None:
                return True

            duration = int(time.time()) - start_time
            if duration > max_time:
                self.log.error(
                    'k8s.wait_certificate',
                    'Max time reached: %s/%s' % (namespace, name)
                )
                return False

            time.sleep(5)

    def delete_certificate(self, namespace, name, my_output=None, wait=True):
        if my_output is not None:
            my_output.default('Delete Certificate', before_newline=True, underline=True)
            my_output.default('- namespace: %s' % (namespace))
            my_output.default('- name: %s' % (name))

        if not self.is_certificate(namespace, name, cache_enabled=False):
            if my_output is not None:
                my_output.default('- already deleted')
            return True

        success = self.delete_certificate_mo(namespace, name)
        if not success:
            if my_output is not None:
                my_output.error('REST API failed')
            return False
        
        if not wait:
            return True
        
        if my_output is not None:
            my_output.default('- wait for no certificate')

        success = self.wait_no_certificate(namespace, name)
        if not success:
            if my_output is not None:
                my_output.error('Timed out')
            return False
        
        return True
    
    def wait_no_certificate(self, namespace, name, max_time=60):
        start_time = int(time.time())
        while True:
            info = self.get_certificate(
                namespace,
                name,
                cache_enabled=False
            )
            if info is None:
                return True

            duration = int(time.time()) - start_time
            if duration > max_time:
                self.log.error(
                    'k8s.wait_no_certificate',
                    'Max time reached: %s/%s' % (namespace, name)
                )
                return False

            time.sleep(5)

    def wipe_certificates(self):
        certificates_mo = self.get_certificates(return_mo=True)
        if certificates_mo is None:
            return False
        
        for certificate_mo in certificates_mo:
            success = self.delete_certificate_mo(
                certificate_mo['metadata']['namespace'],
                certificate_mo['metadata']['name']
            )
            if not success:
                return False
            
        return True
    