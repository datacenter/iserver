import json


class AssistedInstallInfraApi():
    def __init__(self):
        self.assisted_install_infra_mo = None

        self.assisted_install_infra_api_version = 'v2'
        self.assisted_install_infra_url = '%s/infra-envs' % (
            self.assisted_install_infra_api_version
        )

    def get_assisted_install_infra_mo(self, cache_enabled=True):
        if cache_enabled and self.assisted_install_infra_mo is not None:
            return self.assisted_install_infra_mo

        self.assisted_install_infra_mo = self.get_assisted_install_mo(
            self.assisted_install_infra_url
        )

        self.log.openshift_mo(
            'assisted_install_infra.mo',
            self.assisted_install_infra_mo
        )

        return self.assisted_install_infra_mo

    def create_assisted_install_infra(self, data):
        response = self.post_assisted_install_mo(
            self.assisted_install_infra_url,
            data=json.dumps(data)
        )

        if response is None:
            return None

        return response['id']

    def update_assisted_install_infra_hostname(self, infra_id, host_id, hostname):
        url = '%s/%s/hosts/%s' % (
            self.assisted_install_infra_url,
            infra_id,
            host_id
        )

        data = {}
        data['host_name'] = hostname

        response = self.patch_assisted_install_mo(
            url,
            data=json.dumps(data)
        )

        return response
