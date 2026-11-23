import json

class AssistedInstallManifestApi():
    def __init__(self):
        self.assisted_install_manifest_api_version = 'v2'
        self.assisted_install_manifest_url = '%s/clusters' % (
            self.assisted_install_manifest_api_version
        )

    def get_assisted_install_manifest_mo(self, cluster_id):
        url = '%s/%s/manifests' % (
            self.assisted_install_manifest_url,
            cluster_id
        )

        response = self.get_assisted_install_mo(
            url
        )

        return response

    def create_assisted_install_manifest(self, cluster_id, filename, content):
        url = '%s/%s/manifests' % (
            self.assisted_install_manifest_url,
            cluster_id
        )

        data = {}
        data['file_name'] = filename
        data['folder'] = 'manifests'
        data['content'] = content

        response = self.post_assisted_install_mo(
            url,
            data=json.dumps(data)
        )

        if response is None:
            return False

        return True
