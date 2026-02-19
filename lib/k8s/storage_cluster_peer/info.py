from lib import filter_helper


class K8sStorageClusterPeerInfo():
    def __init__(self):
        self.storage_cluster_peer = None

    def get_storage_cluster_peer_info(self, storage_cluster_peer_mo):
        if storage_cluster_peer_mo is None:
            return None

        info = {}
        info['__Output'] = {}

        metadata_info = self.get_metadata_info(
            storage_cluster_peer_mo
        )
        info.update(metadata_info)

        info['spec'] = self.get(storage_cluster_peer_mo, 'spec')
        info['status'] = self.get(storage_cluster_peer_mo, 'status')
        return info

    def get_storage_cluster_peers_info(self, cache_enabled=True):
        if cache_enabled:
            if self.storage_cluster_peer is not None:
                return self.storage_cluster_peer

        managed_objects = self.get_storage_cluster_peer_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.storage_cluster_peer = []
        for managed_object in managed_objects:
            storage_cluster_peer_info = {}
            storage_cluster_peer_info['info'] = self.get_storage_cluster_peer_info(
                managed_object
            )
            storage_cluster_peer_info['mo'] = managed_object
            self.storage_cluster_peer.append(
                storage_cluster_peer_info
            )

        return self.storage_cluster_peer

    def match_storage_cluster_peer(self, storage_cluster_peer_info, object_filter):
        if object_filter is None or len(object_filter) == 0:
            return True

        for rule in object_filter:
            (key, value) = rule.split(':')

            key_found = False

            if key == 'namespace':
                key_found = True
                if not filter_helper.match_string(value, storage_cluster_peer_info['namespace']):
                    return False

            if key == 'name':
                key_found = True
                if not filter_helper.match_string(value, storage_cluster_peer_info['name']):
                    return False

            if not key_found:
                self.log.error(
                    'match_storage_cluster_peer',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_storage_cluster_peers(self, object_filter=None, return_mo=False, cache_enabled=True):
        all_storage_cluster_peers = self.get_storage_cluster_peers_info(cache_enabled=cache_enabled)
        if all_storage_cluster_peers is None:
            return None

        storage_cluster_peers = []

        for storage_cluster_peer_info in all_storage_cluster_peers:
            if not self.match_storage_cluster_peer(storage_cluster_peer_info['info'], object_filter):
                continue

            if return_mo:
                storage_cluster_peers.append(
                    storage_cluster_peer_info['mo']
                )
                continue

            storage_cluster_peers.append(
                storage_cluster_peer_info['info']
            )

        return storage_cluster_peers

    def is_storage_cluster_peer(self, namespace, name, cache_enabled=True):
        if self.get_storage_cluster_peer(namespace, name, cache_enabled=cache_enabled) is None:
            return False
        return True

    def get_storage_cluster_peer(self, namespace, name, return_mo=False, cache_enabled=True):
        object_filter = []
        object_filter.append(
            'namespace:%s' % (namespace)
        )
        object_filter.append(
            'name:%s' % (name)
        )
        storage_cluster_peers = self.get_storage_cluster_peers(
            object_filter=object_filter,
            return_mo=return_mo,
            cache_enabled=cache_enabled
        )
        if storage_cluster_peers is None:
            return None

        if len(storage_cluster_peers) == 1:
            return storage_cluster_peers[0]

        return None
