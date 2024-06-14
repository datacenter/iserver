import json
from lib import ip_helper


class AssistedInstallClusterApi():
    def __init__(self):
        self.assisted_install_cluster_mo = None
        self.assisted_install_cluster_install_config_mo = {}
        self.assisted_install_cluster_credentials_mo = {}
        self.assisted_install_cluster_kubeconfig_mo = {}

        self.assisted_install_cluster_api_version = 'v2'
        self.assisted_install_cluster_url = '%s/clusters' % (
            self.assisted_install_cluster_api_version
        )

    def get_assisted_install_cluster_mo(self, cache_enabled=True):
        if cache_enabled and self.assisted_install_cluster_mo is not None:
            return self.assisted_install_cluster_mo

        params = {}
        params['with_hosts'] = True

        self.assisted_install_cluster_mo = self.get_assisted_install_mo(
            self.assisted_install_cluster_url,
            params=params
        )

        self.log.openshift_mo(
            'assisted_install_cluster.mo',
            self.assisted_install_cluster_mo
        )

        return self.assisted_install_cluster_mo

    def get_assisted_install_cluster_install_config_mo(self, cluster_id, cache_enabled=True):
        if cache_enabled and cluster_id in self.assisted_install_cluster_install_config_mo:
            return self.assisted_install_cluster_install_config_mo[cluster_id]

        url = '%s/%s/install-config' % (
            self.assisted_install_cluster_url,
            cluster_id
        )

        self.assisted_install_cluster_install_config_mo[cluster_id] = self.get_assisted_install_mo(
            url
        )

        return self.assisted_install_cluster_install_config_mo[cluster_id]

    def get_assisted_install_cluster_credentials_mo(self, cluster_id, cache_enabled=True):
        if cache_enabled and cluster_id in self.assisted_install_cluster_credentials_mo:
            return self.assisted_install_cluster_credentials_mo[cluster_id]

        url = '%s/%s/credentials' % (
            self.assisted_install_cluster_url,
            cluster_id
        )

        self.assisted_install_cluster_credentials_mo[cluster_id] = self.get_assisted_install_mo(
            url
        )

        return self.assisted_install_cluster_credentials_mo[cluster_id]

    def get_assisted_install_cluster_kubeconfig_mo(self, cluster_id, cache_enabled=True):
        if cache_enabled and cluster_id in self.assisted_install_cluster_kubeconfig_mo:
            return self.assisted_install_cluster_kubeconfig_mo[cluster_id]

        params = {}
        params['file_name'] = 'kubeconfig'

        url = '%s/%s/downloads/credentials-presigned' % (
            self.assisted_install_cluster_url,
            cluster_id
        )

        response = self.get_assisted_install_mo(
            url,
            params=params
        )

        if response is None:
            return None

        filename = '/tmp/%s.kubeconfig' % (cluster_id)
        response = ip_helper.download_url(response['url'], filename)
        if response is None:
            return None

        return filename

    def create_assisted_install_cluster(self, data):
        response = self.post_assisted_install_mo(
            self.assisted_install_cluster_url,
            data=json.dumps(data)
        )

        if response is None:
            return None

        return response['id']

    def patch_assisted_install_cluster(self, cluster_id, data):
        url = '%s/%s' % (
            self.assisted_install_cluster_url,
            cluster_id
        )

        response = self.patch_assisted_install_mo(
            url,
            data=json.dumps(data)
        )
        return response

    def patch_assisted_install_cluster_install_config(self, cluster_id, data):
        url = '%s/%s/install-config' % (
            self.assisted_install_cluster_url,
            cluster_id
        )

        response = self.patch_assisted_install_mo(
            url,
            data=data
        )
        return response

    def action_assisted_install_cluster_install(self, cluster_id):
        url = '%s/%s/actions/install' % (
            self.assisted_install_cluster_url,
            cluster_id
        )

        response = self.post_assisted_install_mo(
            url
        )
        if response is None:
            return False

        return True

    def post_assisted_install_cluster(self, cluster_id, data=None):
        url = '%s/%s' % (
            self.assisted_install_cluster_url,
            cluster_id
        )

        if data is None:
            response = self.post_assisted_install_mo(
                url,
                data=json.dumps(data)
            )
        else:
            response = self.post_assisted_install_mo(
                url
            )

        return response

    def delete_assisted_install_cluster(self, cluster_id):
        url = '%s/%s' % (
            self.assisted_install_cluster_url,
            cluster_id
        )

        success = self.delete_assisted_install_mo(
            url
        )
        return success
