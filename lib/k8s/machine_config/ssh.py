class K8sMachineConfigSsh():
    def __init__(self):
        pass

    def get_machine_config_ssh_keys_per_role(self, role):
        keys = []

        info = self.get_machine_config('99-%s-ssh' % (role), return_mo=False, cache_enabled=False)
        if info is None:
            return keys
        
        if 'users' in info and info['users'] is not None and len(info['users']) > 0:
            for user in info['users']:
                if user['username'] == 'core':
                    if 'keys' in user and user['keys'] is not None:
                        for key in user['keys']:
                            keys.append(key)

        return keys

    def get_machine_config_ssh_keys(self):
        keys = []

        machine_configs = self.get_machine_configs()
        if machine_configs is None:
            return None
        
        for machine_config in machine_configs:
            if machine_config['owner_kind'] == 'MachineConfigPool':
                continue

            for user in machine_config['users']:
                for key in user['keys']:
                    if key not in keys:
                        keys.append(key)

        return keys
    

    def get_machine_config_ssh_info(self):
        info = []

        machine_configs = self.get_machine_configs()
        if machine_configs is None:
            return None
        
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

    def get_machine_config_ssh_body(self, role):
        body = {}
        body['apiVersion'] = 'machineconfiguration.openshift.io/v1'
        body['kind'] = 'MachineConfig'
        body['metadata'] = {}
        body['metadata']['name'] = '99-%s-ssh' % (role)
        body['metadata']['labels'] = {}
        body['metadata']['labels']['machineconfiguration.openshift.io/role'] = role
        body['spec'] = {}
        body['spec']['baseOSExtensionsContainerImage'] = ''
        body['spec']['fips'] = False
        body['spec']['kernelArguments'] = None
        body['spec']['kernelType'] = ''
        body['spec']['osImageURL'] = ''
        body['spec']['config'] = {}
        body['spec']['config']['ignition'] = {}
        body['spec']['config']['ignition']['version'] = '3.2.0'
        body['spec']['config']['passwd'] = {}
        
        user_mo = {}
        user_mo['name'] = 'core'
        user_mo['sshAuthorizedKeys'] = []
        body['spec']['config']['passwd']['users'] = [user_mo]

        return body
    
    def add_machine_config_ssh_mo(self, keys, role):
        create = False
        machine_config_mo = self.get_machine_config('99-%s-ssh' % (role), return_mo=True, cache_enabled=False)
        if machine_config_mo is None:
            create = True
            machine_config_mo = self.get_machine_config_ssh_body(role)

        for user_mo in machine_config_mo['spec']['config']['passwd']['users']:
            if user_mo['name'] == 'core':
                for key in keys:
                    user_mo['sshAuthorizedKeys'].append(
                        key
                    )

        if create:
            if not self.create_machine_config_mo(machine_config_mo):
                error = 'Machine config create failed: 99-%s-ssh' % (role)
                self.log.error(
                    'add_machine_config_ssh_mo',
                    error
                )
                return False, error, False

        if not create:
            if not self.set_machine_config_mo(machine_config_mo):
                error = 'Machine config update failed: 99-%s-ssh' % (role)
                self.log.error(
                    'add_machine_config_ssh_mo',
                    error
                )
                return False, error, False
        
        return True, None, True

    def add_machine_config_ssh(self, keys, role, my_output=None, wait=True):
        wait_for = []

        if role in ['any', 'master']:
            current = self.get_machine_config_ssh_keys_per_role('master')

            new_keys = []
            for key in keys:
                if key in current:
                    continue

                new_keys.append(key)

            if len(new_keys) == 0:
                if my_output is not None:
                    my_output.default('No new master keys to add')            
            else:
                if my_output is not None:
                    my_output.default('New master keys [%s] will be added' % (len(new_keys)))

                success, error, modified = self.add_machine_config_ssh_mo(new_keys, 'master')
                if not success:
                    if my_output is not None:
                        my_output.error(error)
                    return False

                if modified:
                    wait_for.append('99-master-ssh')

        if role in ['any', 'worker']:
            current = self.get_machine_config_ssh_keys_per_role('worker')

            new_keys = []
            for key in keys:
                if key in current:
                    continue

                new_keys.append(key)

            if len(new_keys) == 0:
                if my_output is not None:
                    my_output.default('No new worker keys to add')
            else:
                if my_output is not None:
                    my_output.default('New worker keys [%s] will be added' % (len(new_keys)))

                success, error, modified = self.add_machine_config_ssh_mo(new_keys, 'worker')
                if not success:
                    if my_output is not None:
                        my_output.error(error)
                    return False

                if modified:
                    wait_for.append('99-worker-ssh')

        if not wait or len(wait_for) == 0:
            return True

        success = self.wait_machine_config_pool_update(
            wait_for, 
            output_handler=my_output
        )
        return success
    
    def delete_machine_config_ssh_mo(self, key_matches, role):
        machine_config = self.get_machine_config('99-%s-ssh' % (role))
        if machine_config is None:
            error = 'Machine config not found: 99-%s-ssh' % (role)
            self.log.error(
                'delete_machine_config_ssh_mo',
                error
            )
            return False, error, False

        new_keys = []
        for user_info in machine_config['users']:
            if user_info['username'] == 'core':
                for key in user_info['keys']:
                    to_delete = False
                    for key_match in key_matches:
                        if key_match in key:
                            to_delete = True
                            break

                    if not to_delete:
                        new_keys.append(key)

        if len(new_keys) == 0:
            return False, 'Cannot delete all keys for core user', False

        machine_config_mo = self.get_machine_config('99-%s-ssh' % (role), return_mo=True, cache_enabled=False)

        for user_mo in machine_config_mo['spec']['config']['passwd']['users']:
            if user_mo['name'] == 'core':
                if len(new_keys) == len(user_mo['sshAuthorizedKeys']):
                    return True, None, False
                
                user_mo['sshAuthorizedKeys'] = new_keys

        if not self.set_machine_config_mo(machine_config_mo):
            error = 'Machine config update failed: 99-%s-ssh' % (role)
            self.log.error(
                'delete_machine_config_ssh_mo',
                error
            )
            return False, error, False
        
        return True, None, True

    def delete_machine_config_ssh(self, key_matches, role, my_output=None, wait=True):
        wait_for = []

        if role in ['any', 'master']:
            success, error, modified = self.delete_machine_config_ssh_mo(key_matches, 'master')
            if not success:
                if my_output is not None:
                    my_output.error(error)
                return False

            if modified:
                wait_for.append('99-master-ssh')

        if role in ['any', 'worker']:
            success, error, modified = self.delete_machine_config_ssh_mo(key_matches, 'worker')
            if not success:
                if my_output is not None:
                    my_output.error(error)
                return False

            if modified:
                wait_for.append('99-worker-ssh')

        if not wait or len(wait_for) == 0:
            return True
        
        success = self.wait_machine_config_pool_update(
            wait_for, 
            output_handler=my_output
        )
        return success
    