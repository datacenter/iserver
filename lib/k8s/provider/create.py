import base64
import yaml
from lib import ip_helper
from menu.common import get_confirmation


class K8sProviderCreate():
    def __init__(self):
        pass

    def get_provider_vcenter_secret_body(self, namespace, name, vc_url, vc_user, vc_pass, vc_ssl):
        body = {}
        body['apiVersion'] = 'v1'
        body['kind'] = 'Secret'
        body['metadata'] = {}
        body['metadata']['namespace'] = namespace
        body['metadata']['name'] = name
        body['type'] = 'Opaque'
        body['data'] = {}
        body['data']['url'] = base64.b64encode(vc_url.encode('utf-8')).decode('utf-8')
        body['data']['user'] = base64.b64encode(vc_user.encode('utf-8')).decode('utf-8')
        body['data']['password'] = base64.b64encode(vc_pass.encode('utf-8')).decode('utf-8')
        if vc_ssl:
            body['data']['insecureSkipVerify'] = base64.b64encode('false'.encode('utf-8')).decode('utf-8')
        else:
            body['data']['insecureSkipVerify'] = base64.b64encode('true'.encode('utf-8')).decode('utf-8')
        return body

    def get_provider_vcenter_body(self, namespace, name, secret_name, vc_url, vddk=None):
        body = {}
        body['apiVersion'] = 'forklift.konveyor.io/v1beta1'
        body['kind'] = 'Provider'
        body['metadata'] = {}
        body['metadata']['namespace'] = namespace
        body['metadata']['name'] = name
        if vddk is None:
            body['metadata']['annotations'] = {}
            body['metadata']['annotations']['forklift.konveyor.io/empty-vddk-init-image'] = 'yes'
        body['spec'] = {}
        body['spec']['secret'] = {}
        body['spec']['secret']['namespace'] = namespace
        body['spec']['secret']['name'] = secret_name
        body['spec']['settings'] = {}
        body['spec']['settings']['sdkEndpoint'] = 'vcenter'
        if vddk is not None:
            body['spec']['settings']['vddkInitImage'] = vddk
        body['spec']['type'] = 'vsphere'
        body['spec']['url'] = vc_url
        return body
    
    def create_provider_vcenter(self, namespace, provider_name, vc_url, vc_user, vc_pass, vc_ssl, vddk=None, confirmation=False, my_output=None, wait=True):
        if my_output is None:
            confirmation = False

        if my_output is not None:
            my_output.default('Create vCenter Provider', before_newline=True, underline=True)
            my_output.default('- namespace: %s' % (namespace))
            my_output.default('- name: %s' % (provider_name))
            my_output.default('- vCenter: %s (%s, %s) ssl[%s]' % (vc_url, vc_user, vc_pass, vc_ssl))
            if vddk is not None:
                my_output.default('- vddk: %s' % (vddk))
                              
        if self.is_provider(namespace, provider_name, cache_enabled=False):
            if my_output is not None:
                my_output.default('- already exists')
            return True
        
        secret_name = provider_name
        if self.is_secret(namespace, secret_name, cache_enabled=False):
            secret_name = '%s-%s' % (secret_name, ip_helper.get_short_uuid())

        secret_body = self.get_provider_vcenter_secret_body(
            namespace,
            secret_name,
            vc_url, 
            vc_user, 
            vc_pass, 
            vc_ssl
        )

        provider_body = self.get_provider_vcenter_body(
            namespace, 
            provider_name, 
            secret_name, 
            vc_url,
            vddk=vddk
        )

        if my_output is not None:
            my_output.default(
                '%s\n---\n%s' % (yaml.dump(secret_body), yaml.dump(provider_body)),
                before_newline=True, 
                wrap='~~~'
            )

        if confirmation:
            if not get_confirmation():
                return False

        if not self.create_secret_mo(namespace, secret_body):
            if my_output is not None:
                my_output.error('Secret REST API failed')
            return False

        if not self.create_provider_mo(provider_body):
            if my_output is not None:
                my_output.error('Provider REST API failed')
            return False
                
        if my_output is not None:
            my_output.default('Secret and provider created', before_newline=True, after_newline=True)

        if not wait:
            return True
        
        if my_output is not None:
            my_output.default('Wait for provider...')

        if not self.wait_provider(namespace, provider_name):
            if my_output is not None:
                my_output.error('timed out')
            return False

        if my_output is not None:
            my_output.default('Wait for provider ready state...')

        if not self.wait_provider_ready(namespace, provider_name):
            info = self.get_provider(namespace, provider_name)
            if info['phase'] == 'ConnectionFailed':
                if my_output is not None:
                    my_output.error('connection failed')
                return False
            
            if my_output is not None:
                my_output.error('timed out')

            return False

        return True    
    