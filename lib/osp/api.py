import traceback

import keystoneclient.v2_0.client as ksclient
import glanceclient.v2.client as glclient
import novaclient.client as nvclient
from neutronclient.v2_0 import client as neutronclient
from cinderclient.v3 import client as cinderclient

# Exceptions
from keystoneclient.v2_0.client import exceptions as ksexceptions
from novaclient import exceptions as nexceptions
from cinderclient import exceptions as cinceptions
from neutronclient.v2_0.client import exceptions as neuceptions

# Keystone v3 support
from keystoneauth1.identity import v3
from keystoneauth1 import session
from keystoneclient.v3 import client

from lib import file_helper


class OspApi():
    def __init__(self, openrc_filename, cert_filename):
        self.api_version = None
        self.keystone_session = None
        self.api = {}
        self.api['keystone'] = None

        self.api_timeout_seconds = 10
        self.connect_timeout_seconds = 10
        self.api_retries = 1

        self.cert_filename = cert_filename
        self.cert = None
        if self.cert_filename is not None:
            self.cert = file_helper.get_file_text(cert_filename)
            if self.cert is None:
                raise ValueError('Cert load failed')

        self.openrc = self.load_openrc(openrc_filename)
        if self.openrc is None:
            raise ValueError('Openstack openrc parse failed')

    def parse_openrc(self, openrc_filename):
        content = file_helper.get_file_text(openrc_filename)
        if content is None:
            self.log.error(
                'parse_openrc',
                'Openrc file read failed: %s' % (openrc_filename)
            )
            return None

        openrc_content = {}

        for line in content.split('\n'):
            if line.startswith('export '):
                if len(line.split('export ')[1].split('=')) == 2:
                    (key, value) = line.split('export ')[1].split('=')
                    openrc_content[key.upper()] = value

        return openrc_content

    def load_openrc(self, openrc_filename):
        openrc_content = self.parse_openrc(openrc_filename)
        if openrc_content is None:
            return None

        if 'OS_IDENTITY_API_VERSION' not in openrc_content:
            self.log.error(
                'load_openrc',
                'Identity key not found'
            )
            return None

        if openrc_content['OS_IDENTITY_API_VERSION'] == '3':
            self.api_version = 3

        if openrc_content['OS_IDENTITY_API_VERSION'] in ['2', '2.0']:
            self.api_version = 2

        if self.api_version is None:
            self.log.error(
                'load_openrc',
                'Unsupported version: %s' % openrc_content['OS_IDENTITY_API_VERSION']
            )
            return None

        openrc = {}
        for key in openrc_content:
            if key.startswith('OS_'):
                openrc[key] = openrc_content[key]

        return openrc

    def get_api_keystone_session(self, cache_enabled=True):
        if cache_enabled and self.keystone_session is not None:
            return self.keystone_session

        self.get_api_keystone(cache_enabled=cache_enabled)
        return self.keystone_session

    def get_api_keystone_v2(self):
        for key in ['OS_AUTH_URL', 'OS_USERNAME', 'OS_PASSWORD', 'OS_TENANT_NAME', 'OS_REGION_NAME']:
            if key not in self.openrc:
                self.log.error(
                    'get_api_keystone_v2',
                    'Required key missing: %s' % (key)
                )
                return None

        keystone_handler = None
        try:
            keystone_handler = ksclient.Client(
                auth_url=self.openrc['OS_AUTH_URL'],
                username=self.openrc['OS_USERNAME'],
                password=self.openrc['OS_PASSWORD'],
                tenant_name=self.openrc['OS_TENANT_NAME'],
                region_name=self.openrc['OS_REGION_NAME'],
                timeout=self.api_timeout_seconds
            )

        except ksexceptions.VersionNotAvailable:
            self.log.error(
                'get_api_keystone_v2',
                'Suitable Keystone v2 client not found'
            )
            self.log.error(
                'get_api_keystone_v2',
                traceback.format_exc()
            )
            return None

        except ksexceptions.DiscoveryFailure:
            self.log.error(
                'get_api_keystone_v2',
                'Keystone v2 server response invalid'
            )
            self.log.error(
                'get_api_keystone_v2',
                traceback.format_exc()
            )
            return None

        except ksexceptions.ClientException:
            self.log.error(
                'get_api_keystone_v2',
                'Failed to initiate Keystone v3 clien'
            )
            self.log.error(
                'get_api_keystone_v2',
                traceback.format_exc()
            )
            return None

        except BaseException:
            self.log.error(
                'get_api_keystone_v2',
                'Keystone v2 authentication failed'
            )
            self.log.error(
                'get_api_keystone_v2',
                traceback.format_exc()
            )
            return None

        if keystone_handler is None:
            self.log.error(
                'get_api_keystone_v2',
                'Unsuccessful'
            )
            return None

        self.log.debug(
            'get_api_keystone_v2',
            'Keystone v2 authentication successful (%s)' % (self.openrc['OS_AUTH_URL'])
        )

        self.api['keystone'] = keystone_handler
        return self.api['keystone']

    def get_api_keystone_v3(self):
        for key in ['OS_AUTH_URL', 'OS_USERNAME', 'OS_PASSWORD', 'OS_PROJECT_NAME', 'OS_USER_DOMAIN_NAME', 'OS_PROJECT_DOMAIN_NAME']:
            if key not in self.openrc:
                self.log.error(
                    'get_api_keystone_v3',
                    'Required key missing: %s' % (key)
                )
                return None

        keystone_handler = None
        try:
            auth = v3.Password(
                auth_url=self.openrc['OS_AUTH_URL'],
                username=self.openrc['OS_USERNAME'],
                password=self.openrc['OS_PASSWORD'],
                project_name=self.openrc['OS_PROJECT_NAME'],
                user_domain_name=self.openrc['OS_USER_DOMAIN_NAME'],
                project_domain_name=self.openrc['OS_PROJECT_DOMAIN_NAME']
            )
            # https://docs.openstack.org/python-keystoneclient/ocata/using-api-v3.html
            # Note: The session.Session() method is deprecated
            # and may be removed in future versions of Keystone.
            if self.cert is None:
                self.keystone_session = session.Session(
                    auth=auth,
                    verify=False,
                    timeout=self.api_timeout_seconds
                )
                keystone_handler = client.Client(
                    session=self.keystone_session,
                    interface='public'
                )

            else:
                self.keystone_session = session.Session(
                    auth=auth,
                    verify=self.cert_filename,
                    timeout=self.api_timeout_seconds
                )

                keystone_handler = client.Client(
                    session=self.keystone_session,
                    interface='public'
                )

        except ksexceptions.VersionNotAvailable:
            self.log.error(
                'get_api_keystone_v3',
                'Suitable Keystone v3 client not found'
            )
            self.log.error(
                'get_api_keystone_v3',
                traceback.format_exc()
            )
            return None

        except ksexceptions.DiscoveryFailure:
            self.log.error(
                'get_api_keystone_v3',
                'Keystone v3 server response invalid'
            )
            self.log.error(
                'get_api_keystone_v3',
                traceback.format_exc()
            )
            return None

        except ksexceptions.ClientException:
            self.log.error(
                'get_api_keystone_v3',
                'Failed to initiate Keystone v3 client'
            )
            self.log.error(
                'get_api_keystone_v3',
                traceback.format_exc()
            )
            return None

        except BaseException:
            self.log.error(
                'get_api_keystone_v3',
                'Keystone v3 authentication failed'
            )
            self.log.error(
                'get_api_keystone_v3',
                traceback.format_exc()
            )
            return None

        if keystone_handler is None:
            self.log.error(
                'get_api_keystone_v3',
                'Unsuccessful'
            )
            return None

        self.log.debug(
            'get_api_keystone_v3',
            'Keystone v3 authentication successful (%s)' % (self.openrc['OS_AUTH_URL'])
        )

        self.api['keystone'] = keystone_handler
        return self.api['keystone']

    def get_api_keystone(self, cache_enabled=True):
        if cache_enabled:
            if 'keystone' in self.api:
                if self.api['keystone'] is not None:
                    return self.api['keystone']

        if self.api_version == 2:
            return self.get_api_keystone_v2()

        if self.api_version == 3:
            return self.get_api_keystone_v3()

        return None

    def get_api_cinder_v2(self):
        for key in ['OS_AUTH_URL', 'OS_USERNAME', 'OS_PASSWORD', 'OS_TENANT_NAME']:
            if key not in self.openrc:
                self.log.error(
                    'get_api_cinder_v2',
                    'Required key missing: %s' % (key)
                )
                return None

        cinder_handler = None
        try:
            cinder_handler = cinderclient.Client(
                self.openrc['OS_USERNAME'],
                self.openrc['OS_PASSWORD'],
                self.openrc['OS_TENANT_NAME'],
                self.openrc['OS_AUTH_URL'],
                service_type='volume'
            )

        except cinceptions.UnsupportedVersion:
            self.log.error(
                'get_api_cinder_v2',
                'Invalid Cinder version'
            )
            self.log.error(
                'get_api_cinder_v2',
                traceback.format_exc()
            )
            return None

        except cinceptions.ClientException:
            self.log.error(
                'get_api_cinder_v2',
                'Authentication failed'
            )
            self.log.error(
                'get_api_cinder_v2',
                traceback.format_exc()
            )
            return None

        except BaseException:
            self.log.error(
                'get_api_cinder_v2',
                'General failure'
            )
            self.log.error(
                'get_api_cinder_v2',
                traceback.format_exc()
            )
            return None

        if cinder_handler is None:
            self.log.error(
                'get_api_cinder_v2',
                'Unsuccessful'
            )
            return None

        self.log.debug(
            'get_api_cinder_v2',
            'Cinder authentication successful'
        )

        self.api['cinder'] = cinder_handler
        return self.api['cinder']

    def get_api_cinder_v3(self, cache_enabled=True):
        cinder_handler = None
        keystone_session = self.get_api_keystone_session(cache_enabled=cache_enabled)
        if keystone_session is None:
            return None

        try:
            cinder_handler = cinderclient.Client(
                service_type='volumev2',
                session=keystone_session
            )

        except cinceptions.UnsupportedVersion:
            self.log.error(
                'get_api_cinder_v3',
                'Invalid Cinder version'
            )
            self.log.error(
                'get_api_cinder_v3',
                traceback.format_exc()
            )
            return None

        except cinceptions.ClientException:
            self.log.error(
                'get_api_cinder_v3',
                'Authentication failed'
            )
            self.log.error(
                'get_api_cinder_v3',
                traceback.format_exc()
            )
            return None

        except BaseException:
            self.log.error(
                'get_api_cinder_v3',
                'General failure'
            )
            self.log.error(
                'get_api_cinder_v3',
                traceback.format_exc()
            )
            return None

        if cinder_handler is None:
            self.log.error(
                'get_api_cinder_v3',
                'Unsuccessful'
            )
            return None

        self.log.debug(
            'get_api_cinder_v3',
            'Cinder authentication successful'
        )

        self.api['cinder'] = cinder_handler
        return self.api['cinder']

    def get_api_cinder(self, cache_enabled=True):
        if cache_enabled:
            if 'cinder' in self.api:
                if self.api['cinder'] is not None:
                    return self.api['cinder']

        if 'OS_VOLUME_API_VERSION' in self.openrc:
            if self.openrc['OS_VOLUME_API_VERSION'] == '2':
                return self.get_api_cinder_v2()

            if self.openrc['OS_VOLUME_API_VERSION'] == '3':
                return self.get_api_cinder_v3(cache_enabled=cache_enabled)

        if 'OS_VOLUME_API_VERSION' not in self.openrc:
            if self.api_version == 2:
                return self.get_api_cinder_v2()

            if self.api_version == 3:
                return self.get_api_cinder_v3(cache_enabled=cache_enabled)

        self.log.error(
            'get_api_cinder',
            'Unsupported cinder api version: %s' % (self.api_version)
        )
        return None

    def get_api_glance_v2(self, cache_enabled=True):
        keystone_handler = self.get_api_keystone()
        if keystone_handler is None:
            return None

        keystone_session = self.get_api_keystone_session(cache_enabled=cache_enabled)
        if keystone_session is None:
            return None

        glance_handler = None
        try:
            glance_handler = glclient.Client(
                session=self.keystone_session
            )
        except BaseException:
            glance_handler = None

        try:
            if glance_handler is None:
                for service in keystone_handler.services.list():
                    if service.name == 'glance':
                        glance_endpoint = service.links['self']
                        glance_id = service.id

                for endpoint in keystone_handler.endpoints.list():
                    if endpoint.service_id == glance_id and endpoint.interface == 'public':
                        glance_endpoint = endpoint.url

                glance_handler = glclient.Client(
                    endpoint=glance_endpoint,
                    session=keystone_session
                )

        except ksexceptions.EmptyCatalog:
            self.log.error(
                'get_api_glance_v2',
                'Keystone service catalog empty. Cannot fetch Glance endpoint.'
            )
            self.log.error(
                'get_api_glance_v2',
                traceback.format_exc()
            )
            return None

        except RuntimeError:
            self.log.error(
                'get_api_glance_v2',
                'Glance authentication failed with runtime error.'
            )
            self.log.error(
                'get_api_glance_v2',
                traceback.format_exc()
            )
            return None

        except BaseException:
            self.log.error(
                'get_api_glance_v2',
                'Glance authentication failed.'
            )
            self.log.error(
                'get_api_glance_v2',
                traceback.format_exc()
            )
            return None

        if glance_handler is None:
            self.log.error(
                'get_api_glance_v2',
                'Unsuccessful'
            )
            return None

        self.log.debug(
            'get_api_glance_v2',
            'Glance authentication successful.'
        )

        self.api['glance'] = glance_handler
        return self.api['glance']

    def get_api_glance_v3(self, cache_enabled=True):
        keystone_handler = self.get_api_keystone()
        if keystone_handler is None:
            return None

        keystone_session = self.get_api_keystone_session(cache_enabled=cache_enabled)
        if keystone_session is None:
            return None

        try:
            for service in keystone_handler.services.list():
                if service.name == 'glance':
                    glance_endpoint = service.links['self']
                    glance_id = service.id

            for endpoint in keystone_handler.endpoints.list():
                if endpoint.service_id == glance_id and endpoint.interface == 'public':
                    glance_endpoint = endpoint.url

            glance_handler = glclient.Client(
                endpoint=glance_endpoint,
                session=keystone_session
            )

        except ksexceptions.EmptyCatalog:
            self.log.error(
                'get_api_glance_v3',
                'Keystone service catalog empty. Cannot fetch Glance endpoint.'
            )
            self.log.error(
                'get_api_glance_v3',
                traceback.format_exc()
            )
            return None

        except RuntimeError:
            self.log.error(
                'get_api_glance_v3',
                'Glance authentication failed with runtime error.'
            )
            self.log.error(
                'get_api_glance_v3',
                traceback.format_exc()
            )
            return None

        except BaseException:
            self.log.error(
                'get_api_glance_v3',
                'Glance authentication failed.'
            )
            self.log.error(
                'get_api_glance_v3',
                traceback.format_exc()
            )
            return None

        if glance_handler is None:
            self.log.error(
                'get_api_glance_v3',
                'Unsuccessful'
            )
            return None

        self.log.debug(
            'get_api_glance_v3',
            'Glance authentication successful.'
        )

        self.api['glance'] = glance_handler
        return self.api['glance']

    def get_api_glance(self, cache_enabled=True):
        if cache_enabled:
            if 'glance' in self.api:
                if self.api['glance'] is not None:
                    return self.api['glance']

        if 'OS_IMAGE_API_VERSION' in self.openrc:
            if self.openrc['OS_IMAGE_API_VERSION'] == '2':
                return self.get_api_glance_v2(cache_enabled=cache_enabled)

            if self.openrc['OS_IMAGE_API_VERSION'] == '3':
                return self.get_api_glance_v3(cache_enabled=cache_enabled)

        if 'OS_IMAGE_API_VERSION' not in self.openrc:
            if self.api_version == 2:
                return self.get_api_glance_v2(cache_enabled=cache_enabled)

            if self.api_version == 3:
                return self.get_api_glance_v3(cache_enabled=cache_enabled)

        self.log.error(
            'get_api_glance',
            'Unsupported glance api version: %s' % (self.api_version)
        )
        return None

    def get_api_neutron_v2(self):
        neutron_handler = None
        try:
            neutron_handler = neutronclient.Client(
                auth_url=self.openrc['OS_AUTH_URL'],
                username=self.openrc['OS_USERNAME'],
                password=self.openrc['OS_PASSWORD'],
                tenant_name=self.openrc['OS_TENANT_NAME']
            )

        except neuceptions.NeutronClientException:
            self.log.error(
                'get_api_neutron_v2',
                'Neutron authentication failed'
            )
            self.log.error(
                'get_api_neutron_v2',
                traceback.format_exc()
            )
            return None

        except BaseException:
            self.log.error(
                'get_api_neutron_v2',
                'Neutron authentication failed'
            )
            self.log.error(
                'get_api_neutron_v2',
                traceback.format_exc()
            )
            return None

        if neutron_handler is None:
            self.log.error(
                'get_api_neutron_v2',
                'Unsuccessful'
            )
            return None

        self.log.debug(
            'get_api_neutron_v2',
            'Neutron authentication successful.'
        )

        self.api['neutron'] = neutron_handler
        return self.api['neutron']

    def get_api_neutron_v3(self, cache_enabled=True):
        neutron_handler = None
        keystone_session = self.get_api_keystone_session(cache_enabled=cache_enabled)
        if keystone_session is None:
            return None

        try:
            neutron_handler = neutronclient.Client(
                session=keystone_session
            )

        except cinceptions.UnsupportedVersion:
            self.log.error(
                'get_api_neutron_v3',
                'Invalid Cinder version'
            )
            self.log.error(
                'get_api_neutron_v3',
                traceback.format_exc()
            )
            return None

        except cinceptions.ClientException:
            self.log.error(
                'get_api_neutron_v3',
                'Authentication failed'
            )
            self.log.error(
                'get_api_neutron_v3',
                traceback.format_exc()
            )
            return None

        except BaseException:
            self.log.error(
                'get_api_neutron_v3',
                'General failure'
            )
            self.log.error(
                'get_api_neutron_v3',
                traceback.format_exc()
            )
            return None

        if neutron_handler is None:
            self.log.error(
                'get_api_neutron_v3',
                'Unsuccessful'
            )
            return None

        self.log.debug(
            'get_api_neutron_v3',
            'Neutron authentication successful.'
        )

        self.api['neutron'] = neutron_handler
        return self.api['neutron']

    def get_api_neutron(self, cache_enabled=True):
        if cache_enabled:
            if 'neutron' in self.api:
                if self.api['neutron'] is not None:
                    return self.api['neutron']

        if self.api_version == 2:
            return self.get_api_neutron_v2()

        if self.api_version == 3:
            return self.get_api_neutron_v3(cache_enabled=cache_enabled)

        self.log.error(
            'get_api_neutron',
            'Unsupported neutron api version: %s' % (self.api_version)
        )
        return None

    def get_api_nova_v2(self):
        for key in ['OS_AUTH_URL', 'OS_USERNAME', 'OS_PASSWORD', 'OS_TENANT_NAME', 'OS_REGION_NAME']:
            if key not in self.openrc:
                self.log.error(
                    'get_api_nova_v2',
                    'Required key missing: %s' % (key)
                )
                return None

        nova_handler = None
        try:
            nova_handler = nvclient.Client(
                auth_url=self.openrc['OS_AUTH_URL'],
                username=self.openrc['OS_USERNAME'],
                password=self.openrc['OS_PASSWORD'],
                tenant_name=self.openrc['OS_TENANT_NAME'],
                region_name=self.openrc['OS_REGION_NAME'],
                version=2
            )
        except nexceptions.ClientException:
            self.log.error(
                'get_api_nova_v2',
                'Nova authentication failed'
            )
            self.log.error(
                'get_api_nova_v3',
                traceback.format_exc()
            )
            return None

        except BaseException:
            self.log.error(
                'get_api_nova_v2',
                'Nova authentication failed'
            )
            self.log.error(
                'get_api_nova_v2',
                traceback.format_exc()
            )
            return None

        if nova_handler is None:
            self.log.error(
                'get_api_nova_v2',
                'Unsuccessful'
            )
            return None

        self.log.debug(
            'get_api_nova_v2',
            'Nova authentication successful.'
        )

        self.api['nova'] = nova_handler
        return self.api['nova']

    def get_api_nova_v3(self):
        for key in ['OS_AUTH_URL', 'OS_USERNAME', 'OS_PASSWORD', 'OS_PROJECT_NAME', 'OS_REGION_NAME', 'OS_USER_DOMAIN_NAME', 'OS_PROJECT_DOMAIN_NAME']:
            if key not in self.openrc:
                self.log.error(
                    'get_api_nova_v2',
                    'Required key missing: %s' % (key)
                )
                return None

        nova_handler = None
        try:
            if self.cert_filename is not None:
                nova_handler = nvclient.Client(
                    auth_url=self.openrc['OS_AUTH_URL'],
                    username=self.openrc['OS_USERNAME'],
                    password=self.openrc['OS_PASSWORD'],
                    project_name=self.openrc['OS_PROJECT_NAME'],
                    region_name=self.openrc['OS_REGION_NAME'],
                    user_domain_name=self.openrc['OS_USER_DOMAIN_NAME'],
                    project_domain_name=self.openrc['OS_PROJECT_DOMAIN_NAME'],
                    cacert=self.cert_filename,
                    version=2
                )
            else:
                nova_handler = nvclient.Client(
                    auth_url=self.openrc['OS_AUTH_URL'],
                    username=self.openrc['OS_USERNAME'],
                    password=self.openrc['OS_PASSWORD'],
                    project_name=self.openrc['OS_PROJECT_NAME'],
                    region_name=self.openrc['OS_REGION_NAME'],
                    user_domain_name=self.openrc['OS_USER_DOMAIN_NAME'],
                    project_domain_name=self.openrc['OS_PROJECT_DOMAIN_NAME'],
                    insecure=True,
                    version=2
                )

        except nexceptions.ClientException:
            self.log.error(
                'get_api_nova_v3',
                'Nova authentication failed'
            )
            self.log.error(
                'get_api_nova_v3',
                traceback.format_exc()
            )
            return None

        except BaseException:
            self.log.error(
                'get_api_nova_v3',
                'Nova authentication failed'
            )
            self.log.error(
                'get_api_nova_v3',
                traceback.format_exc()
            )
            return None

        if nova_handler is None:
            self.log.error(
                'get_api_nova_v3',
                'Unsuccessful'
            )
            return None

        self.log.debug(
            'get_api_nova_v3',
            'Nova authentication successful.'
        )

        self.api['nova'] = nova_handler
        return self.api['nova']

    def get_api_nova(self, cache_enabled=True):
        if cache_enabled:
            if 'nova' in self.api:
                if self.api['nova'] is not None:
                    return self.api['nova']

        if 'OS_COMPUTE_API_VERSION' in self.openrc:
            if self.openrc['OS_COMPUTE_API_VERSION'].startswith('1'):
                return self.get_api_nova_v2()

            if self.openrc['OS_COMPUTE_API_VERSION'].startswith('2'):
                return self.get_api_nova_v3()

        if 'OS_COMPUTE_API_VERSION' not in self.openrc:
            if self.api_version == 2:
                return self.get_api_nova_v2()

            if self.api_version == 3:
                return self.get_api_nova_v3()

        self.log.error(
            'get_api_nova',
            'Unsupported nova api version: %s' % (self.api_version)
        )
        return None
