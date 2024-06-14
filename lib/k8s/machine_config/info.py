import base64
import gzip

from lib import file_helper
from lib import filter_helper


class K8sMachineConfigInfo():
    def __init__(self):
        self.machine_config = None

    def get_machine_config_info(self, machine_config_mo):
        if machine_config_mo is None:
            return None

        info = {}
        info['__Output'] = {}
        info['name'] = self.get(machine_config_mo, 'metadata:name')

        info['generated_by'] = self.get(machine_config_mo, 'metadata:annotations:machineconfiguration.openshift.io/generated-by-controller-version', on_error='--', on_none='--')

        owner = self.get_metadata_owner_info(
            machine_config_mo,
            'metadata:ownerReferences'
        )
        info.update(owner)

        info['label'] = self.get(machine_config_mo, 'metadata:labels', on_error={}, on_none={})
        info['node'] = []
        if info['owner_kind'] != 'MachineConfigPool':
            if 'machineconfiguration.openshift.io/role' not in info['label']:
                self.log.error(
                    'get_machine_config_info',
                    'Unexpected machine config label: %s' % (info['name'])
                )
            else:
                node_role = info['label']['machineconfiguration.openshift.io/role']
                if node_role not in ['master', 'worker']:
                    self.log.error(
                        'get_machine_config_info',
                        'Unexpected machine config node role: %s' % (info['name'])
                    )
                else:
                    if node_role == 'master':
                        info['node'] = self.get_master_nodes_name()

                    if node_role == 'worker':
                        info['node'] = self.get_worker_nodes_name()

        # https://coreos.github.io/ignition/configuration-v3_2/
        info['ignition_version'] = self.get(machine_config_mo, 'spec:config:ignition:version')

        info['file'] = []
        files_mo = self.get(machine_config_mo, 'spec:config:storage:files', on_error=[], on_none=[])
        for file_mo in files_mo:
            file_info = {}
            file_info['path'] = self.get(file_mo, 'path')
            file_info['overwrite'] = self.get(file_mo, 'overwrite', on_error=False, on_none=False)
            file_info['mode'] = self.get(file_mo, 'mode', on_error=420, on_none=420)
            file_info['umode'] = oct(file_info['mode']).replace('0o', '0x')

            file_source = self.get(file_mo, 'contents:source')
            compression = self.get(file_mo, 'contents:compression', on_error=None, on_none=None)
            if file_source is None:
                file_info['content'] = 'Undefined'
            else:
                file_info['content'] = 'Unsupported format'
                if file_source.startswith('data:text/plain;charset=utf-8;base64,'):
                    file_info['content'] = base64.b64decode(
                        file_source.split('data:text/plain;charset=utf-8;base64,')[1]
                    ).decode('utf-8')
                if file_source.startswith('data:;base64,'):
                    if compression is not None and compression == 'gzip':
                        file_info['content'] = gzip.decompress(
                            base64.b64decode(
                                file_source.split('data:;base64,')[1].encode('utf-8')
                            )
                        ).decode('utf-8')

                if file_source.startswith('data:,'):
                    if len(file_source.split('data:,')) == 1:
                        file_info['content'] = ''
                    else:
                        file_info['content'] = file_helper.decode_ascii(
                            file_source.split('data:,')[1]
                        )

            info['file'].append(
                file_info
            )

        info['file'] = sorted(
            info['file'],
            key=lambda i: i['path']
        )
        info['fileCount'] = len(info['file'])

        info['systemd'] = []
        systemds_mo = self.get(machine_config_mo, 'spec:config:systemd:units', on_error=[], on_none=[])
        for systemd_mo in systemds_mo:
            systemd_info = {}
            systemd_info['name'] = self.get(systemd_mo, 'name')
            systemd_info['enabled'] = str(self.get(systemd_mo, 'enabled', on_error='--', on_none='--'))
            systemd_info['content'] = self.get(systemd_mo, 'contents')
            systemd_info['dropin'] = self.get(systemd_mo, 'dropins', on_error=[], on_none=[])
            info['systemd'].append(
                systemd_info
            )

        info['systemd'] = sorted(
            info['systemd'],
            key=lambda i: i['name']
        )
        info['systemdCount'] = len(info['systemd'])

        info['users'] = []
        users_mo = self.get(machine_config_mo, 'spec:config:passwd:users', on_error=[], on_none=[])
        for user_mo in users_mo:
            user_info = {}
            user_info['username'] = self.get(user_mo, 'name')
            user_info['keys'] = self.get(user_mo, 'sshAuthorizedKeys')
            info['users'].append(
                user_info
            )

        info['users'] = sorted(
            info['users'],
            key=lambda i: i['username']
        )
        info['usersCount'] = len(info['users'])

        info['age'] = self.convert_timestamp_to_age(
            self.get(machine_config_mo, 'metadata:creationTimestamp'),
            on_error='--'
        )

        return info

    def get_machine_configs_info(self, cache_enabled=True):
        if cache_enabled:
            if self.machine_config is not None:
                return self.machine_config

        managed_objects = self.get_machine_config_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.machine_config = []
        for managed_object in managed_objects:
            machine_config_info = {}
            machine_config_info['info'] = self.get_machine_config_info(
                managed_object
            )
            machine_config_info['mo'] = managed_object
            self.machine_config.append(
                machine_config_info
            )

        return self.machine_config

    def filter_machine_config_label(self, labels, label_filter):
        new_labels = {}

        if len(label_filter.split(':')) > 2:
            return new_labels

        if len(label_filter.split(':')) == 1:
            label_filter_key = label_filter
            label_filter_value = None

        if len(label_filter.split(':')) == 2:
            (label_filter_key, label_filter_value) = label_filter.split(':')

        for lkey in labels:
            if filter_helper.match_string(label_filter_key, lkey):
                if label_filter_value is None:
                    new_labels[lkey] = labels[lkey]
                    continue

                if filter_helper.match_string(label_filter_value, labels[lkey]):
                    new_labels[lkey] = labels[lkey]
                    continue

        return new_labels

    def match_machine_config(self, machine_config_info, object_filter):
        if object_filter is None or len(object_filter) == 0:
            return True

        for rule in object_filter:
            key = rule.split(':')[0]
            value = ':'.join(rule.split(':')[1:])

            key_found = False

            if key == 'name':
                key_found = True
                if not filter_helper.match_string(value, machine_config_info['name']):
                    return False

            if key == 'path':
                key_found = True

            if key == 'systemd':
                key_found = True

            if key == 'content':
                key_found = True

            if key == 'label':
                key_found = True
                filtered_labels = self.filter_machine_config_label(
                    machine_config_info['label'],
                    value
                )
                if len(filtered_labels) == 0:
                    return False

            if not key_found:
                self.log.error(
                    'match_machine_config',
                    'Unsupported key: %s' % (key)
                )

        return True

    def match_machine_config_file(self, machine_config_file_info, object_filter):
        if object_filter is None or len(object_filter) == 0:
            return True

        for rule in object_filter:
            key = rule.split(':')[0]
            value = ':'.join(rule.split(':')[1:])

            key_found = False

            if key == 'name':
                key_found = True

            if key == 'path':
                key_found = True
                if not filter_helper.match_string(value, machine_config_file_info['path']):
                    return False

            if key == 'systemd':
                key_found = True

            if key == 'content':
                key_found = True
                if not filter_helper.match_string(value, machine_config_file_info['content']):
                    return False

            if key == 'label':
                key_found = True

            if not key_found:
                self.log.error(
                    'match_machine_config_file',
                    'Unsupported key: %s' % (key)
                )

        return True

    def match_machine_config_systemd(self, machine_config_systemd_info, object_filter):
        if object_filter is None or len(object_filter) == 0:
            return True

        for rule in object_filter:
            key = rule.split(':')[0]
            value = ':'.join(rule.split(':')[1:])

            key_found = False

            if key == 'name':
                key_found = True

            if key == 'path':
                key_found = True
                found = False
                for dropin in machine_config_systemd_info['dropin']:
                    if filter_helper.match_string(value, dropin['name']):
                        found = True
                        break

                if not found:
                    return False

            if key == 'systemd':
                key_found = True
                if not filter_helper.match_string(value, machine_config_systemd_info['name']):
                    return False

            if key == 'content':
                key_found = True

                if machine_config_systemd_info['content'] is not None:
                    if not filter_helper.match_string(value, machine_config_systemd_info['content']):
                        return False

                if len(machine_config_systemd_info['dropin']) > 0:
                    found = False
                    for dropin in machine_config_systemd_info['dropin']:
                        if filter_helper.match_string(value, dropin['contents']):
                            found = True
                            break

                    if not found:
                        return False

                if machine_config_systemd_info['content'] is None and len(machine_config_systemd_info['dropin']) == 0:
                    return False

            if key == 'label':
                key_found = True

            if not key_found:
                self.log.error(
                    'match_machine_config_file',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_machine_configs(self, object_filter=None, return_mo=False, cache_enabled=True):
        all_machine_configs = self.get_machine_configs_info(cache_enabled=cache_enabled)
        if all_machine_configs is None:
            return None

        machine_configs = []

        for machine_config_info in all_machine_configs:
            if not self.match_machine_config(machine_config_info['info'], object_filter):
                continue

            if return_mo:
                machine_configs.append(
                    machine_config_info['mo']
                )
                continue

            files_info = []
            for file_info in machine_config_info['info']['file']:
                if self.match_machine_config_file(file_info, object_filter):
                    files_info.append(
                        file_info
                    )
            machine_config_info['info']['file'] = files_info

            systemsd_info = []
            for systemd_info in machine_config_info['info']['systemd']:
                if self.match_machine_config_systemd(systemd_info, object_filter):
                    systemsd_info.append(
                        systemd_info
                    )
            machine_config_info['info']['systemd'] = systemsd_info

            machine_configs.append(
                machine_config_info['info']
            )

        return machine_configs

    def is_machine_config(self, name, cache_enabled=True):
        if self.get_machine_config(name, cache_enabled=cache_enabled) is None:
            return False
        return True

    def get_machine_config(self, name, return_mo=False, cache_enabled=True):
        object_filter = []
        object_filter.append(
            'name:%s' % (name)
        )
        machine_configs = self.get_machine_configs(
            object_filter=object_filter,
            return_mo=return_mo,
            cache_enabled=cache_enabled
        )
        if machine_configs is None:
            return None

        if len(machine_configs) == 1:
            return machine_configs[0]

        return None
