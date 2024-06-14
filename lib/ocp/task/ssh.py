from lib import file_helper


class OcpTaskSsh():
    def __init__(self):
        pass

    def get_ocp_ssh_authorized_keys(self):
        info = []

        machine_configs = self.k8s_handler.get_machine_configs()
        for machine_config in machine_configs:
            if machine_config['owner_kind'] == 'MachineConfigPool':
                continue

            for user in machine_config['users']:
                for key in user['keys']:
                    item = {}
                    item['node'] = machine_config['node']
                    item['username'] = user['username']
                    item['key'] = key
                    item['mc'] = machine_config['name']
                    info.append(item)

        return info

    def add_ocp_master_ssh_authorized_key(self, pubkey):
        machine_config = self.k8s_handler.get_machine_config('99-master-ssh')
        if machine_config is None:
            self.log.error(
                'add_ocp_master_ssh_authorized_key',
                'Machine config not found: 99-master-ssh'
            )
            return None

        for user_info in machine_config['users']:
            if user_info['username'] == 'core':
                if pubkey in user_info['keys']:
                    return []

        machine_config_mo = self.k8s_handler.get_machine_config('99-master-ssh', return_mo=True)

        for user_mo in machine_config_mo['spec']['config']['passwd']['users']:
            if user_mo['name'] == 'core':
                user_mo['sshAuthorizedKeys'].append(
                    pubkey
                )

        if not self.k8s_handler.set_machine_config_mo(machine_config_mo):
            self.log.error(
                'add_ocp_master_ssh_authorized_key',
                'Machine config update failed: 99-master-ssh'
            )
            return None

        return ['99-master-ssh']

    def add_ocp_worker_ssh_authorized_key(self, pubkey):
        machine_config = self.k8s_handler.get_machine_config('99-worker-ssh')
        if machine_config is None:
            self.log.error(
                'add_ocp_worker_ssh_authorized_key',
                'Machine config not found: 99-worker-ssh'
            )
            return None

        for user_info in machine_config['users']:
            if user_info['username'] == 'core':
                if pubkey in user_info['keys']:
                    return []

        machine_config_mo = self.k8s_handler.get_machine_config('99-worker-ssh', return_mo=True)

        for user_mo in machine_config_mo['spec']['config']['passwd']['users']:
            if user_mo['name'] == 'core':
                user_mo['sshAuthorizedKeys'].append(
                    pubkey
                )

        if not self.k8s_handler.set_machine_config_mo(machine_config_mo):
            self.log.error(
                'add_ocp_worker_ssh_authorized_key',
                'Machine config update failed: 99-worker-ssh'
            )
            return None

        return ['99-worker-ssh']

    def add_ocp_ssh_authorized_key(self, filename, node_role):
        content = file_helper.get_file(filename).split('\n')[0].rstrip('\r')

        machine_configs = []
        if node_role in ['master', 'any']:
            mcs = self.add_ocp_master_ssh_authorized_key(content)
            if mcs is None:
                return None

            for machine_config in mcs:
                if machine_config not in machine_configs:
                    machine_configs.append(
                        machine_config
                    )

        if node_role in ['worker', 'any']:
            mcs = self.add_ocp_worker_ssh_authorized_key(content)
            if mcs is None:
                return None

            for machine_config in mcs:
                if machine_config not in machine_configs:
                    machine_configs.append(
                        machine_config
                    )

        return machine_configs

    def delete_ocp_master_ssh_authorized_key(self, match):
        machine_config = self.k8s_handler.get_machine_config('99-master-ssh')
        if machine_config is None:
            self.log.error(
                'delete_ocp_master_ssh_authorized_key',
                'Machine config not found: 99-master-ssh'
            )
            return None

        found = False
        new_keys = []
        for user_info in machine_config['users']:
            if user_info['username'] == 'core':
                for key in user_info['keys']:
                    if match in key:
                        found = True
                        continue
                    new_keys.append(key)

        if not found:
            return []

        machine_config_mo = self.k8s_handler.get_machine_config('99-master-ssh', return_mo=True)

        for user_mo in machine_config_mo['spec']['config']['passwd']['users']:
            if user_mo['name'] == 'core':
                user_mo['sshAuthorizedKeys'] = new_keys

        if not self.k8s_handler.set_machine_config_mo(machine_config_mo):
            self.log.error(
                'delete_ocp_master_ssh_authorized_key',
                'Machine config update failed: 99-master-ssh'
            )
            return None

        return ['99-master-ssh']

    def delete_ocp_worker_ssh_authorized_key(self, match):
        machine_config = self.k8s_handler.get_machine_config('99-worker-ssh')
        if machine_config is None:
            self.log.error(
                'delete_ocp_worker_ssh_authorized_key',
                'Machine config not found: 99-worker-ssh'
            )
            return None

        found = False
        new_keys = []
        for user_info in machine_config['users']:
            if user_info['username'] == 'core':
                for key in user_info['keys']:
                    if match in key:
                        found = True
                        continue
                    new_keys.append(key)

        if not found:
            return []

        machine_config_mo = self.k8s_handler.get_machine_config('99-worker-ssh', return_mo=True)

        for user_mo in machine_config_mo['spec']['config']['passwd']['users']:
            if user_mo['name'] == 'core':
                user_mo['sshAuthorizedKeys'] = new_keys

        if not self.k8s_handler.set_machine_config_mo(machine_config_mo):
            self.log.error(
                'delete_ocp_worker_ssh_authorized_key',
                'Machine config update failed: 99-worker-ssh'
            )
            return None

        return ['99-worker-ssh']

    def delete_ocp_ssh_authorized_key(self, match, node_role):
        machine_configs = []
        if node_role in ['master', 'any']:
            mcs = self.delete_ocp_master_ssh_authorized_key(match)
            if mcs is None:
                return None

            for machine_config in mcs:
                if machine_config not in machine_configs:
                    machine_configs.append(
                        machine_config
                    )

        if node_role in ['worker', 'any']:
            mcs = self.delete_ocp_worker_ssh_authorized_key(match)
            if mcs is None:
                return None

            for machine_config in mcs:
                if machine_config not in machine_configs:
                    machine_configs.append(
                        machine_config
                    )

        return machine_configs
