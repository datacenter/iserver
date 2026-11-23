from lib.cnc import main as cnc


class CncNode():
    def __init__(self):
        self.cnc_node = None

    def load_pre_cnc_nodes(self):
        self.cnc_node = self.get_pre_cache('cnc', 'node')
        if self.cnc_node is None:
            return False
        return True

    def set_post_cnc_nodes(self):
        return self.set_post_cache('cnc-node', self.cnc_node)

    def load_post_cnc_nodes(self):
        self.cnc_node = self.get_post_cache('cnc-node')
        if self.cnc_node is None:
            return False
        return True

    def get_cnc_node(self):
        info = []
        for controller_name in self.cnc_node:
            for node_info in self.cnc_node[controller_name]:
                info.append(
                    node_info
                )

        return info

    def prepare_cnc_nodes(self, cache_enabled=True):
        self.cnc_node = {}

        cnc_controllers = self.get_cnc_handlers()
        if cnc_controllers is None or len(cnc_controllers) == 0:
            return False

        for cnc_controller in cnc_controllers:
            self.my_output.debug('CNC: %s' % (cnc_controller['name']))
            if cache_enabled and self.cache_ttl is not None:
                # L2-cache
                if cnc_controller['name'] in self.cnc_node:
                    self.my_output.debug('L2 Cache hit')
                    continue

                # L3-cache
                cache = self.get_cache('cnc-%s-node' % (cnc_controller['name']))
                if cache is not None:
                    self.cnc_node[cnc_controller['name']] = cache
                    self.my_output.debug('L3 Cache hit')
                    continue

            self.my_output.debug('Cache miss')

            cnc_handler = cnc.Cnc(
                cnc_controller['ip'],
                cnc_controller['port'],
                cnc_controller['username'],
                cnc_controller['password'],
                cnc_name=cnc_controller['name'],
                log_id=self.log_id
            )

            self.cnc_node[cnc_controller['name']] = cnc_handler.get_nodes()

            self.set_cache(
                'cnc-%s-node' % (cnc_controller['name']),
                self.cnc_node[cnc_controller['name']]
            )

        return True

    def run_cnc_nodes(self):
        if not self.set_post_cnc_nodes():
            self.my_output.error('CNC node failed')
            return False

        return True

    def run_cnc_nodes_serial(self):
        serials = []
        for domain_name in self.cnc_node:
            for device in self.cnc_node[domain_name]:
                if device['family'] not in ['Routers']:
                    continue

                item = {}
                item['serial'] = device['sn']
                item['domain'] = domain_name
                item['scope'] = 'cnc'
                item['type'] = 'Router'
                item['description'] = device['type']
                item['parent'] = None

                self.serial.append(
                    item
                )

                serials.append(
                    device['sn']
                )

                parent_sn = device['sn']
                for equipment in device['equipment']:
                    if equipment['sn'] is None:
                        continue

                    if equipment['sn'].lower() in ['na', 'n/a']:
                        continue

                    if equipment['sn'] == parent_sn:
                        continue

                    if equipment['sn'] in serials:
                        continue

                    item = {}
                    item['serial'] = equipment['sn']
                    item['domain'] = domain_name
                    item['scope'] = 'cnc'
                    item['type'] = equipment['type']
                    item['description'] = equipment['description']
                    if equipment['description'] is not None:
                        if 'Pluggable Optics Module' in equipment['description']:
                            item['type'] = 'Optics'

                    if item['type'] is not None:
                        if item['type'] == 'POWERSUPPLY':
                            item['type'] = 'Power Supply'

                        if item['type'] == 'FAN':
                            item['type'] = 'Fan'

                    item['parent'] = parent_sn

                    self.serial.append(
                        item
                    )

                    serials.append(
                        equipment['sn']
                    )

        return True

    def run_cnc_nodes_mac(self):
        return True

