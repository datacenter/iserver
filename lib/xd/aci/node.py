import copy
from lib.aci import apic


class AciNode():
    def __init__(self):
        self.aci_node = None
        self.aci_node_cmd = None

    def load_pre_aci_node(self):
        self.aci_node = self.get_pre_cache('aci', 'node')
        if self.aci_node is None:
            return False
        return True

    def set_post_aci_node(self):
        return self.set_post_cache('aci-node', self.aci_node)

    def load_post_aci_node(self):
        self.aci_node = self.get_post_cache('aci-node')
        if self.aci_node is None:
            return False
        return True

    def load_pre_aci_node_cmd(self):
        self.aci_node_cmd = self.get_pre_cache('aci', 'cmd')
        if self.aci_node_cmd is None:
            return False
        return True

    def set_post_aci_node_cmd(self):
        return self.set_post_cache('aci-cmd', self.aci_node_cmd)

    def load_post_aci_node_cmd(self):
        self.aci_node_cmd = self.get_post_cache('aci-cmd')
        if self.aci_node_cmd is None:
            return False
        return True

    def get_aci_node(self):
        info = copy.deepcopy(self.aci_node)
        return info

    def get_aci_node_cmd(self):
        info = copy.deepcopy(self.aci_node_cmd)
        return info

    def get_aci_node_ids(self):
        ids = {}
        for key in self.aci_node:
            ids[key] = []
            for item in self.aci_node[key]:
                ids[key].append(
                    item['id']
                )

        return ids

    def get_aci_node_names(self):
        names = {}

        for key in self.aci_node:
            names[key] = []
            for item in self.aci_node[key]:
                names[key].append(
                    item['name']
                )

        return names

    def is_aci_node_name(self, name):
        if self.get_aci_node_by_name(name) is None:
            return False
        return True

    def get_aci_node_id_by_name(self, name):
        for key in self.aci_node:
            for item in self.aci_node[key]:
                if item['name'] == name:
                    return item['id']
        return None

    def get_aci_node_by_name(self, name):
        for key in self.aci_node:
            for item in self.aci_node[key]:
                if item['name'] == name:
                    return item
        return None

    def get_aci_node_name_by_id(self, node_id):
        node_info = self.get_aci_node_by_id(node_id)
        if node_info is None:
            return None
        return node_info['node']

    def get_aci_node_by_id(self, node_id):
        mapping = self.get_aci_node_id2name()
        for apic_name in mapping:
            if node_id in mapping[apic_name]:
                info = {}
                info['apic'] = apic_name
                info['node'] = mapping[apic_name][node_id]
                return info
        return None

    def get_aci_node_id2name(self):
        mapping = {}

        for key in self.aci_node:
            mapping[key] = {}
            for item in self.aci_node[key]:
                mapping[key][item['id']] = item['name']

        return mapping

    def prepare_aci_nodes(self, cache_enabled=True):
        aci_controllers = self.get_aci_handlers()
        if aci_controllers is None or len(aci_controllers) == 0:
            return False

        self.aci_node = {}
        self.aci_node_cmd = {}

        for aci_controller in aci_controllers:
            self.my_output.debug('Aci node: %s' % (aci_controller['name']))
            if cache_enabled and self.cache_ttl is not None:
                # L2-cache
                if aci_controller['name'] in self.aci_node:
                    self.my_output.debug('L2 Cache hit')
                    continue

                # L3-cache
                cache = self.get_cache('aci-%s-node' % (aci_controller['name']))
                if cache is not None:
                    self.aci_node[aci_controller['name']] = cache
                    self.my_output.debug('L3 Cache hit')
                    continue

            self.my_output.debug('Cache miss')

            apic_handler = apic.Apic(
                aci_controller['ip'],
                aci_controller['port'],
                aci_controller['username'],
                aci_controller['password'],
                apic_name=aci_controller['name'],
                log_id=self.log_id
            )

            self.aci_node[aci_controller['name']] = apic_handler.get_nodes(
                node_filter=['role:!controller'],
                interfaces_summary_info=True,
                power_info=True,
                temp_info=True,
                psu_info=True,
                sensor_info=True,
                system_info=True
            )

            self.set_cache(
                'aci-%s-node' % (aci_controller['name']),
                self.aci_node[aci_controller['name']]
            )

        for aci_controller in aci_controllers:
            for node_info in self.aci_node[aci_controller['name']]:
                self.prepare_aci_node_exec(
                    aci_controller,
                    node_info['id']
                )

            self.set_cache(
                'aci-%s-cmd' % (aci_controller['name']),
                self.aci_node_cmd[aci_controller['name']]
            )

        return True

    def prepare_aci_node_exec(self, aci_controller, node_id, cache_enabled=True):
        if aci_controller['name'] not in self.aci_node_cmd:
            self.aci_node_cmd[aci_controller['name']] = {}

        if node_id not in self.aci_node_cmd[aci_controller['name']]:
            self.aci_node_cmd[aci_controller['name']][node_id] = {}

        apic_handler = apic.Apic(
            aci_controller['ip'],
            aci_controller['port'],
            aci_controller['username'],
            aci_controller['password'],
            apic_name=aci_controller['name'],
            log_id=self.log_id
        )

        commands = {}
        commands['vlan'] = 'show vlan extended'

        parser = {}
        parser['vlan'] = 'parse_node_vlan_extended'

        for key in commands:
            cache_key = '%s-%s-%s' % (
                aci_controller['name'],
                key,
                node_id
            )
            self.my_output.debug('Aci exec: %s' % (cache_key))

            if cache_enabled and self.cache_ttl is not None:
                # L2-cache
                if key in self.aci_node_cmd[aci_controller['name']][node_id]:
                    self.my_output.debug('L2 Cache hit')
                    continue

                # L3-cache
                cache = self.get_cache('aci-%s' % (cache_key))
                if cache is not None:
                    self.aci_node_cmd[aci_controller['name']][node_id][key] = {}
                    self.aci_node_cmd[aci_controller['name']][node_id][key]['output'] = cache
                    self.aci_node_cmd[aci_controller['name']][node_id][key]['parsed'] = getattr(apic_handler, parser[key])(self.aci_node_cmd[aci_controller['name']][node_id][key]['output'])
                    self.my_output.debug('L3 Cache hit')
                    continue

            self.my_output.debug('Cache miss')

            output = apic_handler.node_run_show_command(node_id, commands[key], debug=True, paranoid=True, ip_type='oob')
            if output is None:
                output = apic_handler.node_run_show_command(node_id, commands[key], debug=True, paranoid=True, ip_type='inb')
                if output is None:
                    self.log.error(
                        'prepare_aci_node_exec',
                        'Exec failed: %s %s %s' % (
                            aci_controller['name'],
                            node_id,
                            key
                        )
                    )

            if output is not None:
                self.set_cache(
                    'aci-%s' % (cache_key),
                    output
                )

                self.aci_node_cmd[aci_controller['name']][node_id][key] = {}
                self.aci_node_cmd[aci_controller['name']][node_id][key]['output'] = output
                self.aci_node_cmd[aci_controller['name']][node_id][key]['parsed'] = getattr(apic_handler, parser[key])(self.aci_node_cmd[aci_controller['name']][node_id][key]['output'])

    def run_aci_node(self):
        if not self.set_post_aci_node():
            return False

        if not self.set_post_aci_node_cmd():
            return False

        return True

    def run_aci_node_serial(self):
        for controller_name in self.aci_node:
            for node in self.aci_node[controller_name]:
                item = {}
                item['serial'] = node['serial']
                item['domain'] = self.domain_name
                item['scope'] = 'aci'
                item['type'] = 'Node'
                item['description'] = node['model']
                item['parent'] = None

                self.serial.append(
                    item
                )

                parent_sn = node['serial']
                for psu in node['psu']:
                    item = {}
                    item['serial'] = psu['ser']
                    item['domain'] = self.domain_name
                    item['scope'] = 'aci'
                    item['type'] = 'Power Supply'
                    item['description'] = node['model']
                    item['parent'] = parent_sn

                    self.serial.append(
                        item
                    )

        return True