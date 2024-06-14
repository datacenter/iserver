import time

from lib.imc.cli import endpoint as imc_endpoint
from lib.redfish import endpoint as redfish_endpoint


class ComputeCache():
    def __init__(self):
        self.memory_array_moids = {}

    def get_redfish_endpoint_template(self, endpoint_id, template_name):
        endpoint_settings = self.redfish_endpoint_settings_handler.get_redfish_endpoint_settings(endpoint_id)
        if endpoint_settings is None:
            return None

        redfish_handler = redfish_endpoint.RedfishEndpoint(
            endpoint_settings['endpoint']['type'],
            endpoint_settings['endpoint']['ip'],
            endpoint_settings['endpoint']['port'],
            endpoint_settings['endpoint']['username'],
            endpoint_settings['endpoint']['password'],
            log_id=self.log_id
        )

        if not redfish_handler.is_connected():
            return None

        if endpoint_settings['endpoint']['type'] == 'fi':
            redfish_handler.endpoint_handler.set_inventory(
                endpoint_settings['endpoint']['inventory_type'],
                endpoint_settings['endpoint']['inventory_id']
            )

        return redfish_handler.endpoint_handler.get_template_properties(template_name)

    def get_imc_endpoint_template(self, endpoint_id, template_name):
        endpoint_settings = self.redfish_endpoint_settings_handler.get_redfish_endpoint_settings(endpoint_id)
        if endpoint_settings is None:
            return None

        imc_handler = imc_endpoint.ImcCliEndpoint(
            endpoint_settings['endpoint']['ip'],
            22,
            endpoint_settings['endpoint']['username'],
            endpoint_settings['endpoint']['password'],
            log_id=self.log_id
        )

        if template_name == 'psu':
            return imc_handler.get_psu()

        return None

    def set_redfish_cache(self, key, server_moids, server_serial, cache_ttl=None):
        if key == 'psu-imc':
            for server_moid in server_moids:
                if cache_ttl is None or not self.cache_handler.is_intersight_cache('psu-imc', subdirectory=server_moid, cache_ttl=cache_ttl):
                    psu_info = self.get_imc_endpoint_template(
                        server_serial[server_moid],
                        'psu'
                    )

                    if psu_info is not None:
                        self.cache_handler.set_intersight_cache_entry(
                            'psu-imc',
                            psu_info,
                            subdirectory=server_moid
                        )

        if key == 'power':
            for server_moid in server_moids:
                if cache_ttl is None or not self.cache_handler.is_intersight_cache('power', subdirectory=server_moid, cache_ttl=cache_ttl):
                    power_info = self.get_redfish_endpoint_template(
                        server_serial[server_moid],
                        'power'
                    )

                    if power_info is not None:
                        self.cache_handler.set_intersight_cache_entry(
                            'power',
                            power_info,
                            subdirectory=server_moid
                        )

        if key == 'power-ucsm':
            for server_moid in server_moids:
                if cache_ttl is None or not self.cache_handler.is_intersight_cache('power', subdirectory=server_moid, cache_ttl=cache_ttl):
                    power_info = power_info = self.ucsm_endpoint_settings_handler.get_ucsm_endpoint_template(
                        server_serial[server_moid],
                        'power'
                    )

                    if power_info is not None:
                        self.cache_handler.set_intersight_cache_entry(
                            'power',
                            power_info,
                            subdirectory=server_moid
                        )

        if key == 'thermal':
            for server_moid in server_moids:
                if cache_ttl is None or not self.cache_handler.is_intersight_cache('thermal', subdirectory=server_moid, cache_ttl=cache_ttl):
                    power_info = self.get_redfish_endpoint_template(
                        server_serial[server_moid],
                        'thermal'
                    )

                    if power_info is not None:
                        self.cache_handler.set_intersight_cache_entry(
                            'thermal',
                            power_info,
                            subdirectory=server_moid
                        )

        if key == 'thermal-ucsm':
            for server_moid in server_moids:
                if cache_ttl is None or not self.cache_handler.is_intersight_cache('thermal', subdirectory=server_moid, cache_ttl=cache_ttl):
                    power_info = power_info = self.ucsm_endpoint_settings_handler.get_ucsm_endpoint_template(
                        server_serial[server_moid],
                        'thermal'
                    )

                    if power_info is not None:
                        self.cache_handler.set_intersight_cache_entry(
                            'thermal',
                            power_info,
                            subdirectory=server_moid
                        )

    def set_intersight_cache(
            self,
            key,
            expand,
            server_moids,
            rack_moids,
            blade_moids,
            registration_moids,
            board_moids,
            adapter_moids,
            boot_moids,
            device_moids,
            gcard_moids,
            serial,
            workflow_seconds,
            filter_length_threshold=20,
            cache_ttl=None
        ):
        if key == 'adapter':
            cache_hits = []
            target_moids = []
            target_server_moids = []
            for server_moid in adapter_moids:
                if cache_ttl is None or not self.cache_handler.is_intersight_cache('adapter', subdirectory=server_moid, cache_ttl=cache_ttl):
                    for adapter_moid in adapter_moids[server_moid]:
                        target_moids.append(
                            adapter_moid
                        )
                        if server_moid not in target_server_moids:
                            target_server_moids.append(
                                server_moid
                            )
                else:
                    cache_hits.append(
                        server_moid
                    )

            if len(cache_hits) > 0:
                self.log_handler.debug(
                    'compute_info.set_intersight_cache',
                    'adapter cache hit: %s' % (cache_hits)
                )

            if len(target_moids) == 0:
                return

            if 'adapter' in expand and len(expand['adapter']) > 0:
                self.adapter_unit_handler.set_get_expand(
                    ','.join(expand['adapter'])
                )

            server_managed_objects = {}
            for target_moid in target_server_moids:
                server_managed_objects[target_moid] = []

            chunk_id = 0
            while True:
                if chunk_id >= len(target_moids):
                    break

                chunk_target_moids = []
                index = 0
                for target_moid in target_moids:
                    if index >= chunk_id and len(chunk_target_moids) < filter_length_threshold:
                        chunk_target_moids.append(
                            target_moid
                        )

                    index = index + 1

                chunk_id = chunk_id + len(chunk_target_moids)

                moids_list = []
                for moid in chunk_target_moids:
                    moids_list.append('\'%s\'' % (moid))
                moids_filter = ', '.join(moids_list)

                self.adapter_unit_handler.set_get_filter(
                    "Moid in (%s)" % (moids_filter)
                )

                self.log_handler.debug(
                    'compute_info.set_intersight_cache',
                    'adapter miss w/filter: %s' % (chunk_target_moids)
                )

                managed_objects = self.adapter_unit_handler.get_all()
                if managed_objects is None:
                    self.log_handler.error(
                        'compute.set_intersight_cache',
                        'adapter failed'
                    )
                    return

                self.log_handler.set_log(
                    'intersight.adapter_unit',
                    managed_objects,
                    json_conversion=True
                )

                for server_moid in target_server_moids:
                    for managed_object in managed_objects:
                        if managed_object['Moid'] in adapter_moids[server_moid]:
                            server_managed_objects[server_moid].append(
                                managed_object
                            )

            for target_moid in target_server_moids:
                self.cache_handler.set_intersight_cache_entry(
                    'adapter',
                    server_managed_objects[target_moid],
                    subdirectory=target_moid
                )

                if 'adapter' in expand:
                    for expanded_item in expand['adapter']:
                        if expanded_item not in ['ExtEthIfs', 'HostEthIfs', 'HostFcIfs']:
                            self.log_handler.error(
                                'compute.set_intersight_cache',
                                'unsupported adapter expand: %s' % (expanded_item)
                            )
                            continue

                        if expanded_item == 'ExtEthIfs':
                            server_expanded_managed_objects = []
                            for server_managed_object in server_managed_objects[target_moid]:
                                for server_expanded_managed_object in server_managed_object['ExtEthIfs']:
                                    server_expanded_managed_objects.append(
                                        server_expanded_managed_object
                                    )

                            self.cache_handler.set_intersight_cache_entry(
                                'adapter_ext_eth_interface',
                                server_expanded_managed_objects,
                                subdirectory=target_moid
                            )

                        if expanded_item == 'HostEthIfs':
                            server_expanded_managed_objects = []
                            for server_managed_object in server_managed_objects[target_moid]:
                                for server_expanded_managed_object in server_managed_object['HostEthIfs']:
                                    server_expanded_managed_objects.append(
                                        server_expanded_managed_object
                                    )

                            self.cache_handler.set_intersight_cache_entry(
                                'adapter_host_eth_interface',
                                server_expanded_managed_objects,
                                subdirectory=target_moid
                            )

                        if expanded_item == 'HostFcIfs':
                            server_expanded_managed_objects = []
                            for server_managed_object in server_managed_objects[target_moid]:
                                for server_expanded_managed_object in server_managed_object['HostFcIfs']:
                                    server_expanded_managed_objects.append(
                                        server_expanded_managed_object
                                    )

                            self.cache_handler.set_intersight_cache_entry(
                                'adapter_host_fc_interface',
                                server_expanded_managed_objects,
                                subdirectory=target_moid
                            )

            return

        if key == 'adapter_ext_eth_interface':
            cache_hits = []
            target_moids = []
            target_server_moids = []
            for server_moid in adapter_moids:
                if cache_ttl is None or not self.cache_handler.is_intersight_cache('adapter_ext_eth_interface', subdirectory=server_moid, cache_ttl=cache_ttl):
                    for adapter_moid in adapter_moids[server_moid]:
                        target_moids.append(
                            adapter_moid
                        )
                        if server_moid not in target_server_moids:
                            target_server_moids.append(
                                server_moid
                            )
                else:
                    cache_hits.append(
                        server_moid
                    )

            if len(cache_hits) > 0:
                self.log_handler.debug(
                    'compute_info.set_intersight_cache',
                    'adapter ext eth interface cache hit: %s' % (cache_hits)
                )

            if len(target_moids) == 0:
                return

            if len(target_moids) < filter_length_threshold:
                moids_list = []
                for moid in target_moids:
                    moids_list.append('\'%s\'' % (moid))
                moids_filter = ', '.join(moids_list)

                self.adapter_ext_eth_interface_handler.set_get_filter(
                    "AdapterUnit/Moid in (%s)" % (moids_filter)
                )

                self.log_handler.debug(
                    'compute_info.set_intersight_cache',
                    'adapter ext eth interface miss w/filter: %s' % (target_moids)
                )
            else:
                self.log_handler.debug(
                    'compute_info.set_intersight_cache',
                    'adapter ext eth interface miss wout filter'
                )

            managed_objects = self.adapter_ext_eth_interface_handler.get_all()
            if managed_objects is None:
                self.log_handler.error(
                    'compute.set_intersight_cache',
                    'adapter ext eth interface failed'
                )
                return

            self.log_handler.set_log(
                'intersight.adapter_ext_eth_interface',
                managed_objects,
                json_conversion=True
            )

            for server_moid in target_server_moids:
                server_managed_objects = []
                for managed_object in managed_objects:
                    if 'AdapterUnit' in managed_object and managed_object['AdapterUnit'] is not None:
                        if managed_object['AdapterUnit']['Moid'] in adapter_moids[server_moid]:
                            server_managed_objects.append(
                                managed_object
                            )

                self.cache_handler.set_intersight_cache_entry(
                    'adapter_ext_eth_interface',
                    server_managed_objects,
                    subdirectory=server_moid
                )

            return

        if key == 'adapter_host_eth_interface':
            cache_hits = []
            target_moids = []
            target_server_moids = []
            for server_moid in adapter_moids:
                if cache_ttl is None or not self.cache_handler.is_intersight_cache('adapter_host_eth_interface', subdirectory=server_moid, cache_ttl=cache_ttl):
                    for adapter_moid in adapter_moids[server_moid]:
                        target_moids.append(
                            adapter_moid
                        )
                        if server_moid not in target_server_moids:
                            target_server_moids.append(
                                server_moid
                            )
                else:
                    cache_hits.append(
                        server_moid
                    )

            if len(cache_hits) > 0:
                self.log_handler.debug(
                    'compute_info.set_intersight_cache',
                    'adapter host eth interface cache hit: %s' % (cache_hits)
                )

            if len(target_moids) == 0:
                return

            if len(target_moids) < filter_length_threshold:
                moids_list = []
                for moid in target_moids:
                    moids_list.append('\'%s\'' % (moid))
                moids_filter = ', '.join(moids_list)

                self.adapter_host_eth_interface_handler.set_get_filter(
                    "AdapterUnit/Moid in (%s)" % (moids_filter)
                )

                self.log_handler.debug(
                    'compute_info.set_intersight_cache',
                    'adapter host eth interface miss w/filter: %s' % (target_moids)
                )
            else:
                self.log_handler.debug(
                    'compute_info.set_intersight_cache',
                    'adapter host eth interface miss wout filter'
                )

            managed_objects = self.adapter_host_eth_interface_handler.get_all()
            if managed_objects is None:
                self.log_handler.error(
                    'compute.set_intersight_cache',
                    'adapter host eth interface failed'
                )
                return

            self.log_handler.set_log(
                'intersight.adapter_host_eth_interface',
                managed_objects,
                json_conversion=True
            )

            for server_moid in target_server_moids:
                server_managed_objects = []
                for managed_object in managed_objects:
                    if 'AdapterUnit' in managed_object and managed_object['AdapterUnit'] is not None:
                        if managed_object['AdapterUnit']['Moid'] in adapter_moids[server_moid]:
                            server_managed_objects.append(
                                managed_object
                            )

                self.cache_handler.set_intersight_cache_entry(
                    'adapter_host_eth_interface',
                    server_managed_objects,
                    subdirectory=server_moid
                )

            return

        if key == 'adapter_host_fc_interface':
            cache_hits = []
            target_moids = []
            target_server_moids = []
            for server_moid in adapter_moids:
                if cache_ttl is None or not self.cache_handler.is_intersight_cache('adapter_host_fc_interface', subdirectory=server_moid, cache_ttl=cache_ttl):
                    for adapter_moid in adapter_moids[server_moid]:
                        target_moids.append(
                            adapter_moid
                        )
                        if server_moid not in target_server_moids:
                            target_server_moids.append(
                                server_moid
                            )
                else:
                    cache_hits.append(
                        server_moid
                    )

            if len(cache_hits) > 0:
                self.log_handler.debug(
                    'compute_info.set_intersight_cache',
                    'adapter fc eth interface cache hit: %s' % (cache_hits)
                )

            if len(target_moids) == 0:
                return

            if len(target_moids) < filter_length_threshold:
                moids_list = []
                for moid in target_moids:
                    moids_list.append('\'%s\'' % (moid))
                moids_filter = ', '.join(moids_list)

                self.adapter_host_fc_interface_handler.set_get_filter(
                    "AdapterUnit/Moid in (%s)" % (moids_filter)
                )

                self.log_handler.debug(
                    'compute_info.set_intersight_cache',
                    'adapter fc eth interface miss w/filter: %s' % (target_moids)
                )
            else:
                self.log_handler.debug(
                    'compute_info.set_intersight_cache',
                    'adapter fc eth interface miss wout filter'
                )

            managed_objects = self.adapter_host_fc_interface_handler.get_all()
            if managed_objects is None:
                self.log_handler.error(
                    'compute.set_intersight_cache',
                    'adapter fc eth interface failed'
                )
                return

            self.log_handler.set_log(
                'intersight.adapter_host_fc_interface',
                managed_objects,
                json_conversion=True
            )

            for server_moid in target_server_moids:
                server_managed_objects = []
                for managed_object in managed_objects:
                    if 'AdapterUnit' in managed_object and managed_object['AdapterUnit'] is not None:
                        if managed_object['AdapterUnit']['Moid'] in adapter_moids[server_moid]:
                            server_managed_objects.append(
                                managed_object
                            )

                self.cache_handler.set_intersight_cache_entry(
                    'adapter_host_fc_interface',
                    server_managed_objects,
                    subdirectory=server_moid
                )

            return

        if key == 'advisories':
            if cache_ttl is None or not self.cache_handler.is_intersight_cache('advisory_security', cache_ttl=cache_ttl):
                managed_objects = self.tam_security_advisory_handler.get_all()
                if managed_objects is None:
                    self.log_handler.error(
                        'compute.set_intersight_cache',
                        'security advisory failed'
                    )
                    return

                self.cache_handler.set_intersight_cache_entry(
                    'advisory_security',
                    managed_objects
                )

            if cache_ttl is None or not self.cache_handler.is_intersight_cache('advisory_definition', cache_ttl=cache_ttl):
                managed_objects = self.tam_advisory_definition_handler.get_all()
                if managed_objects is None:
                    self.log_handler.error(
                        'compute.set_intersight_cache',
                        'advisory definition failed'
                    )
                    return

                self.log_handler.set_log(
                    'intersight.advisory_definition',
                    managed_objects,
                    json_conversion=True
                )

                self.cache_handler.set_intersight_cache_entry(
                    'advisory_definition',
                    managed_objects
                )

            return

        if key == 'advisory':
            cache_hits = []
            target_moids = []
            target_server_moids = []
            for server_moid in server_moids:
                if cache_ttl is None or not self.cache_handler.is_intersight_cache('advisory', subdirectory=server_moid, cache_ttl=cache_ttl):
                    target_moids.append(
                        server_moid
                    )
                    target_server_moids.append(
                        server_moid
                    )
                else:
                    cache_hits.append(
                        server_moid
                    )

            if len(cache_hits) > 0:
                self.log_handler.debug(
                    'compute_info.set_intersight_cache',
                    'advirosy cache hit: %s' % (cache_hits)
                )

            if len(target_moids) == 0:
                return

            if len(target_moids) < filter_length_threshold:
                moids_list = []
                for moid in target_moids:
                    moids_list.append('\'%s\'' % (moid))
                moids_filter = ', '.join(moids_list)

                self.tam_advisory_instance_handler.set_get_filter(
                    "AffectedObject/Moid in (%s)" % (moids_filter)
                )

                self.log_handler.debug(
                    'compute_info.set_intersight_cache',
                    'advisory cache miss w/filter: %s' % (target_moids)
                )
            else:
                self.log_handler.debug(
                    'compute_info.set_intersight_cache',
                    'advisory cache miss wout filter'
                )

            managed_objects = self.tam_advisory_instance_handler.get_all()
            if managed_objects is None:
                self.log_handler.error(
                    'compute.set_intersight_cache',
                    'advisory failed'
                )
                return

            self.log_handler.set_log(
                'intersight.advisory',
                managed_objects,
                json_conversion=True
            )

            for server_moid in target_server_moids:
                server_managed_objects = []
                for managed_object in managed_objects:
                    if 'AffectedObject' in managed_object and managed_object['AffectedObject'] is not None:
                        if server_moid == managed_object['AffectedObject']['Moid']:
                            server_managed_objects.append(
                                managed_object
                            )

                self.cache_handler.set_intersight_cache_entry(
                    'advisory',
                    server_managed_objects,
                    subdirectory=server_moid
                )

            return

        if key == 'alarm':
            cache_hits = []
            target_moids = []
            target_server_moids = []
            for server_moid in registration_moids:
                if cache_ttl is None or not self.cache_handler.is_intersight_cache('alarm', subdirectory=server_moid, cache_ttl=cache_ttl):
                    target_moids.append(
                        registration_moids[server_moid]
                    )
                    target_server_moids.append(
                        server_moid
                    )
                else:
                    cache_hits.append(
                        server_moid
                    )

            if len(cache_hits) > 0:
                self.log_handler.debug(
                    'compute_info.set_intersight_cache',
                    'alarm cache hit: %s' % (cache_hits)
                )

            if len(target_moids) == 0:
                return

            if len(target_moids) < filter_length_threshold:
                moids_list = []
                for moid in target_moids:
                    moids_list.append('\'%s\'' % (moid))
                moids_filter = ', '.join(moids_list)

                self.cond_alarm_handler.set_get_filter(
                    "RegisteredDevice/Moid in (%s)" % (moids_filter)
                )

                self.log_handler.debug(
                    'compute_info.set_intersight_cache',
                    'alarm cache miss w/filter: %s' % (target_moids)
                )
            else:
                self.log_handler.debug(
                    'compute_info.set_intersight_cache',
                    'alarm cache miss wout filter'
                )

            managed_objects = self.cond_alarm_handler.get_all()
            if managed_objects is None:
                self.log_handler.error(
                    'compute.set_intersight_cache',
                    'alarm failed'
                )
                return

            self.log_handler.set_log(
                'intersight.cond_alarm',
                managed_objects,
                json_conversion=True
            )

            for server_moid in target_server_moids:
                server_managed_objects = []
                for managed_object in managed_objects:
                    if 'RegisteredDevice' in managed_object and managed_object['RegisteredDevice'] is not None:
                        if registration_moids[server_moid] == managed_object['RegisteredDevice']['Moid']:
                            server_managed_objects.append(
                                managed_object
                            )

                self.cache_handler.set_intersight_cache_entry(
                    'alarm',
                    server_managed_objects,
                    subdirectory=server_moid
                )

            return

        if key == 'board':
            cache_hits = []
            target_moids = []
            target_rack_moids = []
            target_blade_moids = []
            target_server_moids = []
            for server_moid in server_moids:
                if cache_ttl is None or not self.cache_handler.is_intersight_cache('board', subdirectory=server_moid, cache_ttl=cache_ttl):
                    target_moids.append(
                        server_moid
                    )
                    if server_moid in blade_moids:
                        target_blade_moids.append(
                            server_moid
                        )
                    if server_moid in rack_moids:
                        target_rack_moids.append(
                            server_moid
                        )
                    target_server_moids.append(
                        server_moid
                    )
                else:
                    server_boards_mo = self.cache_handler.get_intersight_cache_entry(
                        'board',
                        subdirectory=server_moid,
                        cache_ttl=cache_ttl
                    )
                    if server_boards_mo is None:
                        self.log_handler.error(
                            'set_intersight_cache',
                            'board cache read failed: %s' % (server_moid)
                        )
                    else:
                        self.memory_array_moids[server_moid] = []
                        for server_board_mo in server_boards_mo:
                            for memory_array_mo in server_board_mo['MemoryArrays']:
                                self.memory_array_moids[server_moid].append(
                                    memory_array_mo['Moid']
                                )

                    cache_hits.append(
                        server_moid
                    )

            if len(cache_hits) > 0:
                self.log_handler.debug(
                    'compute_info.set_intersight_cache',
                    'board cache hit: %s' % (cache_hits)
                )

            if len(target_moids) == 0:
                return

            if 'board' in expand and len(expand['board']) > 0:
                self.compute_board_handler.set_get_expand(
                    ','.join(expand['board'])
                )

            server_managed_objects = {}
            for target_moid in target_moids:
                server_managed_objects[target_moid] = []
                self.memory_array_moids[target_moid] = []

            if len(target_rack_moids) > 0:
                chunk_id = 0
                while True:
                    if chunk_id >= len(target_rack_moids):
                        break

                    chunk_target_moids = []
                    index = 0
                    for target_moid in target_rack_moids:
                        if index >= chunk_id and len(chunk_target_moids) < filter_length_threshold:
                            chunk_target_moids.append(
                                target_moid
                            )

                        index = index + 1

                    chunk_id = chunk_id + len(chunk_target_moids)

                    moids_list = []
                    for moid in chunk_target_moids:
                        moids_list.append('\'%s\'' % (moid))
                    moids_filter = ', '.join(moids_list)

                    self.compute_board_handler.set_get_filter(
                        "ComputeRackUnit/Moid in (%s)" % (moids_filter)
                    )

                    self.log_handler.debug(
                        'compute_info.set_intersight_cache',
                        'board cache miss w/filter: %s' % (chunk_target_moids)
                    )

                    managed_objects = self.compute_board_handler.get_all()
                    if managed_objects is None:
                        self.log_handler.error(
                            'compute.set_intersight_cache',
                            'board failed'
                        )
                        return

                    self.log_handler.set_log(
                        'intersight.compute_board',
                        managed_objects,
                        json_conversion=True
                    )

                    for server_moid in target_rack_moids:
                        for managed_object in managed_objects:
                            if 'Parent' in managed_object and managed_object['Parent'] is not None:
                                if server_moid == managed_object['Parent']['Moid']:
                                    server_managed_objects[server_moid].append(
                                        managed_object
                                    )

                                    for memory_array_mo in managed_object['MemoryArrays']:
                                        self.memory_array_moids[server_moid].append(
                                            memory_array_mo['Moid']
                                        )

                for server_moid in target_rack_moids:
                    self.cache_handler.set_intersight_cache_entry(
                        'board',
                        server_managed_objects[server_moid],
                        subdirectory=server_moid
                    )

                    if 'board' in expand:
                        for expanded_item in expand['board']:
                            if expanded_item not in ['Processors']:
                                self.log_handler.error(
                                    'compute.set_intersight_cache',
                                    'unsupported board expand: %s' % (expanded_item)
                                )
                                continue

                            if expanded_item == 'Processors':
                                server_cpu_managed_objects = []
                                for server_managed_object in server_managed_objects[server_moid]:
                                    for server_cpu_managed_object in server_managed_object['Processors']:
                                        server_cpu_managed_objects.append(
                                            server_cpu_managed_object
                                        )

                                self.cache_handler.set_intersight_cache_entry(
                                    'cpu',
                                    server_cpu_managed_objects,
                                    subdirectory=server_moid
                                )

            if len(target_blade_moids) > 0:
                chunk_id = 0
                while True:
                    if chunk_id >= len(target_blade_moids):
                        break

                    chunk_target_moids = []
                    index = 0
                    for target_moid in target_blade_moids:
                        if index >= chunk_id and len(chunk_target_moids) < filter_length_threshold:
                            chunk_target_moids.append(
                                target_moid
                            )

                        index = index + 1

                    chunk_id = chunk_id + len(chunk_target_moids)

                    moids_list = []
                    for moid in chunk_target_moids:
                        moids_list.append('\'%s\'' % (moid))
                    moids_filter = ', '.join(moids_list)

                    self.compute_board_handler.set_get_filter(
                        "ComputeBlade/Moid in (%s)" % (moids_filter)
                    )

                    self.log_handler.debug(
                        'compute_info.set_intersight_cache',
                        'board cache miss w/filter: %s' % (target_blade_moids)
                    )

                    managed_objects = self.compute_board_handler.get_all()
                    if managed_objects is None:
                        self.log_handler.error(
                            'compute.set_intersight_cache',
                            'board failed'
                        )
                        return

                    for server_moid in target_blade_moids:
                        for managed_object in managed_objects:
                            if 'Parent' in managed_object and managed_object['Parent'] is not None:
                                if server_moid == managed_object['Parent']['Moid']:
                                    server_managed_objects[server_moid].append(
                                        managed_object
                                    )

                                    for memory_array_mo in managed_object['MemoryArrays']:
                                        self.memory_array_moids[server_moid].append(
                                            memory_array_mo['Moid']
                                        )

                for server_moid in target_blade_moids:
                    self.cache_handler.set_intersight_cache_entry(
                        'board',
                        server_managed_objects[server_moid],
                        subdirectory=server_moid
                    )

                    if 'board' in expand:
                        for expanded_item in expand['board']:
                            if expanded_item not in ['Processors']:
                                self.log_handler.error(
                                    'compute.set_intersight_cache',
                                    'unsupported board expand: %s' % (expanded_item)
                                )
                                continue

                            if expanded_item == 'Processors':
                                server_cpu_managed_objects = []
                                for server_managed_object in server_managed_objects[server_moid]:
                                    for server_cpu_managed_object in server_managed_object['Processors']:
                                        server_cpu_managed_objects.append(
                                            server_cpu_managed_object
                                        )

                                self.cache_handler.set_intersight_cache_entry(
                                    'cpu',
                                    server_cpu_managed_objects,
                                    subdirectory=server_moid
                                )

            return

        if key == 'boot_bios':
            cache_hits = []
            target_moids = []
            target_rack_moids = []
            target_blade_moids = []
            target_server_moids = []
            for server_moid in server_moids:
                if cache_ttl is None or not self.cache_handler.is_intersight_cache('boot_bios', subdirectory=server_moid, cache_ttl=cache_ttl):
                    target_moids.append(
                        server_moid
                    )
                    if server_moid in blade_moids:
                        target_blade_moids.append(
                            server_moid
                        )
                    if server_moid in rack_moids:
                        target_rack_moids.append(
                            server_moid
                        )
                else:
                    cache_hits.append(
                        server_moid
                    )

            if len(cache_hits) > 0:
                self.log_handler.debug(
                    'compute_info.set_intersight_cache',
                    'boot bios cache hit: %s' % (cache_hits)
                )

            if len(target_moids) == 0:
                return

            if len(target_rack_moids) > 0:
                if len(target_rack_moids) < filter_length_threshold:
                    moids_list = []
                    for moid in target_rack_moids:
                        moids_list.append('\'%s\'' % (moid))
                    moids_filter = ', '.join(moids_list)

                    self.bios_boot_mode_handler.set_get_filter(
                        "ComputeRackUnit/Moid in (%s)" % (moids_filter)
                    )

                    self.log_handler.debug(
                        'compute_info.set_intersight_cache',
                        'boot bios cache miss w/filter: %s' % (target_rack_moids)
                    )
                else:
                    self.log_handler.debug(
                        'compute_info.set_intersight_cache',
                        'boot mode cache miss wout filter'
                    )

                managed_objects = self.bios_boot_mode_handler.get_all()
                if managed_objects is None:
                    self.log_handler.error(
                        'compute.set_intersight_cache',
                        'boot bios failed'
                    )
                    return

                self.log_handler.set_log(
                    'intersight.bios_boot_mode',
                    managed_objects,
                    json_conversion=True
                )

                for server_moid in target_rack_moids:
                    server_managed_objects = []
                    for managed_object in managed_objects:
                        if 'ComputeRackUnit' in managed_object and managed_object['ComputeRackUnit'] is not None:
                            if server_moid == managed_object['ComputeRackUnit']['Moid']:
                                server_managed_objects.append(
                                    managed_object
                                )

                    self.cache_handler.set_intersight_cache_entry(
                        'boot_bios',
                        server_managed_objects,
                        subdirectory=server_moid
                    )

            if len(target_blade_moids) > 0:
                if len(target_blade_moids) < filter_length_threshold:
                    moids_list = []
                    for moid in target_blade_moids:
                        moids_list.append('\'%s\'' % (moid))
                    moids_filter = ', '.join(moids_list)

                    self.bios_boot_mode_handler.set_get_filter(
                        "ComputeBlade/Moid in (%s)" % (moids_filter)
                    )

                    self.log_handler.debug(
                        'compute_info.set_intersight_cache',
                        'boot bios cache miss w/filter: %s' % (target_blade_moids)
                    )
                else:
                    self.log_handler.debug(
                        'compute_info.set_intersight_cache',
                        'boot mode cache miss wout filter'
                    )

                managed_objects = self.bios_boot_mode_handler.get_all()
                if managed_objects is None:
                    self.log_handler.error(
                        'compute.set_intersight_cache',
                        'boot bios failed'
                    )
                    return

                self.log_handler.set_log(
                    'intersight.bios_boot_mode',
                    managed_objects,
                    json_conversion=True
                )

                for server_moid in target_blade_moids:
                    server_managed_objects = []
                    for managed_object in managed_objects:
                        if 'ComputeBlade' in managed_object and managed_object['ComputeBlade'] is not None:
                            if server_moid == managed_object['ComputeBlade']['Moid']:
                                server_managed_objects.append(
                                    managed_object
                                )

                    self.cache_handler.set_intersight_cache_entry(
                        'boot_bios',
                        server_managed_objects,
                        subdirectory=server_moid
                    )

            return

        if key == 'boot_mode':
            cache_hits = []
            target_moids = []
            target_rack_moids = []
            target_blade_moids = []
            target_server_moids = []
            for server_moid in server_moids:
                if cache_ttl is None or not self.cache_handler.is_intersight_cache('boot_mode', subdirectory=server_moid, cache_ttl=cache_ttl):
                    target_moids.append(
                        server_moid
                    )
                    if server_moid in blade_moids:
                        target_blade_moids.append(
                            server_moid
                        )
                    if server_moid in rack_moids:
                        target_rack_moids.append(
                            server_moid
                        )
                else:
                    cache_hits.append(
                        server_moid
                    )

            if len(cache_hits) > 0:
                self.log_handler.debug(
                    'compute_info.set_intersight_cache',
                    'boot mode cache hit: %s' % (cache_hits)
                )

            if len(target_moids) == 0:
                return

            if len(target_rack_moids) > 0:
                if len(target_rack_moids) < filter_length_threshold:
                    moids_list = []
                    for moid in target_rack_moids:
                        moids_list.append('\'%s\'' % (moid))
                    moids_filter = ', '.join(moids_list)

                    self.boot_device_boot_mode_handler.set_get_filter(
                        "ComputeRackUnit/Moid in (%s)" % (moids_filter)
                    )

                    self.log_handler.debug(
                        'compute_info.set_intersight_cache',
                        'boot mode cache miss w/filter: %s' % (target_rack_moids)
                    )
                else:
                    self.log_handler.debug(
                        'compute_info.set_intersight_cache',
                        'boot mode cache miss wout filter'
                    )

                managed_objects = self.boot_device_boot_mode_handler.get_all()
                if managed_objects is None:
                    self.log_handler.error(
                        'compute.set_intersight_cache',
                        'boot mode failed'
                    )
                    return

                self.log_handler.set_log(
                    'intersight.boot_device_boot_mode',
                    managed_objects,
                    json_conversion=True
                )
                for server_moid in target_rack_moids:
                    server_managed_objects = []
                    for managed_object in managed_objects:
                        if 'ComputeRackUnit' in managed_object and managed_object['ComputeRackUnit'] is not None:
                            if server_moid == managed_object['ComputeRackUnit']['Moid']:
                                server_managed_objects.append(
                                    managed_object
                                )

                    self.cache_handler.set_intersight_cache_entry(
                        'boot_mode',
                        server_managed_objects,
                        subdirectory=server_moid
                    )

            if len(target_blade_moids) > 0:
                if len(target_blade_moids) < filter_length_threshold:
                    moids_list = []
                    for moid in target_blade_moids:
                        moids_list.append('\'%s\'' % (moid))
                    moids_filter = ', '.join(moids_list)

                    self.boot_device_boot_mode_handler.set_get_filter(
                        "ComputeBlade/Moid in (%s)" % (moids_filter)
                    )

                    self.log_handler.debug(
                        'compute_info.set_intersight_cache',
                        'boot mode cache miss w/filter: %s' % (target_blade_moids)
                    )
                else:
                    self.log_handler.debug(
                        'compute_info.set_intersight_cache',
                        'boot mode cache miss wout filter'
                    )

                managed_objects = self.boot_device_boot_mode_handler.get_all()
                if managed_objects is None:
                    self.log_handler.error(
                        'compute.set_intersight_cache',
                        'boot mode failed'
                    )
                    return

                self.log_handler.set_log(
                    'intersight.boot_device_boot_mode',
                    managed_objects,
                    json_conversion=True
                )

                for server_moid in target_blade_moids:
                    server_managed_objects = []
                    for managed_object in managed_objects:
                        if 'ComputeBlade' in managed_object and managed_object['ComputeBlade'] is not None:
                            if server_moid == managed_object['ComputeBlade']['Moid']:
                                server_managed_objects.append(
                                    managed_object
                                )

                    self.cache_handler.set_intersight_cache_entry(
                        'boot_mode',
                        server_managed_objects,
                        subdirectory=server_moid
                    )

            return

        if key == 'boot_security':
            cache_hits = []
            target_moids = []
            for server_moid in server_moids:
                if cache_ttl is None or not self.cache_handler.is_intersight_cache('boot_security', subdirectory=server_moid, cache_ttl=cache_ttl):
                    target_moids.append(
                        server_moid
                    )
                else:
                    cache_hits.append(
                        server_moid
                    )

            if len(cache_hits) > 0:
                self.log_handler.debug(
                    'compute_info.set_intersight_cache',
                    'boot security cache hit: %s' % (cache_hits)
                )

            if len(target_moids) == 0:
                return

            if len(target_moids) < filter_length_threshold:
                moids_list = []
                for moid in target_moids:
                    moids_list.append('\'%s\'' % (moid))
                moids_filter = ', '.join(moids_list)

                self.boot_device_boot_security_handler.set_get_filter(
                    "ComputePhysical/Moid in (%s)" % (moids_filter)
                )

                self.log_handler.debug(
                    'compute_info.set_intersight_cache',
                    'boot security cache miss w/filter: %s' % (target_moids)
                )
            else:
                self.log_handler.debug(
                    'compute_info.set_intersight_cache',
                    'boot security cache miss wout filter'
                )

            managed_objects = self.boot_device_boot_security_handler.get_all()
            if managed_objects is None:
                self.log_handler.error(
                    'compute.set_intersight_cache',
                    'boot security failed'
                )
                return

            self.log_handler.set_log(
                'intersight.boot_device_boot_security',
                managed_objects,
                json_conversion=True
            )

            for server_moid in target_moids:
                server_managed_objects = []
                for managed_object in managed_objects:
                    if 'ComputePhysical' in managed_object and managed_object['ComputePhysical'] is not None:
                        if server_moid == managed_object['ComputePhysical']['Moid']:
                            server_managed_objects.append(
                                managed_object
                            )

                self.cache_handler.set_intersight_cache_entry(
                    'boot_security',
                    server_managed_objects,
                    subdirectory=server_moid
                )

            return

        if key == 'boot_cdd':
            cache_hits = []
            target_moids = []
            target_server_moids = []
            for server_moid in boot_moids:
                if cache_ttl is None or not self.cache_handler.is_intersight_cache('boot_cdd', subdirectory=server_moid, cache_ttl=cache_ttl):
                    if len(boot_moids[server_moid]['cdd']) == 0:
                        self.cache_handler.set_intersight_cache_entry(
                            'boot_cdd',
                            [],
                            subdirectory=server_moid
                        )
                        cache_hits.append(
                            server_moid
                        )
                        continue

                    target_server_moids.append(
                        server_moid
                    )
                    for boot_id in boot_moids[server_moid]['cdd']:
                        target_moids.append(
                            boot_id
                        )
                else:
                    cache_hits.append(
                        server_moid
                    )

            if len(cache_hits) > 0:
                self.log_handler.debug(
                    'compute_info.set_intersight_cache',
                    'boot cdd cache hit: %s' % (cache_hits)
                )

            if len(target_moids) == 0:
                return

            if len(target_moids) < filter_length_threshold:
                moids_list = []
                for moid in target_moids:
                    moids_list.append('\'%s\'' % (moid))
                moids_filter = ', '.join(moids_list)

                self.boot_cdd_device_handler.set_get_filter(
                    "Moid in (%s)" % (moids_filter)
                )

                self.log_handler.debug(
                    'compute_info.set_intersight_cache',
                    'boot cdd cache miss w/filter: %s' % (target_moids)
                )
            else:
                self.log_handler.debug(
                    'compute_info.set_intersight_cache',
                    'boot cdd cache miss wout filter'
                )

            managed_objects = self.boot_cdd_device_handler.get_all()
            if managed_objects is None:
                self.log_handler.error(
                    'compute.set_intersight_cache',
                    'boot cdd failed'
                )
                return

            self.log_handler.set_log(
                'intersight.boot_cdd_device',
                managed_objects,
                json_conversion=True
            )

            for server_moid in target_server_moids:
                server_managed_objects = []
                for managed_object in managed_objects:
                    if 'ComputePhysical' in managed_object and managed_object['ComputePhysical'] is not None:
                        if server_moid == managed_object['ComputePhysical']['Moid']:
                            server_managed_objects.append(
                                managed_object
                            )

                self.cache_handler.set_intersight_cache_entry(
                    'boot_cdd',
                    server_managed_objects,
                    subdirectory=server_moid
                )

            return

        if key == 'boot_hdd':
            cache_hits = []
            target_moids = []
            target_server_moids = []
            for server_moid in boot_moids:
                if cache_ttl is None or not self.cache_handler.is_intersight_cache('boot_hdd', subdirectory=server_moid, cache_ttl=cache_ttl):
                    if len(boot_moids[server_moid]['hdd']) == 0:
                        self.cache_handler.set_intersight_cache_entry(
                            'boot_hdd',
                            [],
                            subdirectory=server_moid
                        )
                        cache_hits.append(
                            server_moid
                        )
                        continue

                    target_server_moids.append(
                        server_moid
                    )
                    for boot_id in boot_moids[server_moid]['hdd']:
                        target_moids.append(
                            boot_id
                        )
                else:
                    cache_hits.append(
                        server_moid
                    )

            if len(cache_hits) > 0:
                self.log_handler.debug(
                    'compute_info.set_intersight_cache',
                    'boot hdd cache hit: %s' % (cache_hits)
                )

            if len(target_moids) == 0:
                return

            if len(target_moids) < filter_length_threshold:
                moids_list = []
                for moid in target_moids:
                    moids_list.append('\'%s\'' % (moid))
                moids_filter = ', '.join(moids_list)

                self.boot_hdd_device_handler.set_get_filter(
                    "Moid in (%s)" % (moids_filter)
                )

                self.log_handler.debug(
                    'compute_info.set_intersight_cache',
                    'boot hdd cache miss w/filter: %s' % (target_moids)
                )
            else:
                self.log_handler.debug(
                    'compute_info.set_intersight_cache',
                    'boot hdd cache miss wout filter'
                )

            managed_objects = self.boot_hdd_device_handler.get_all()
            if managed_objects is None:
                self.log_handler.error(
                    'compute.set_intersight_cache',
                    'boot hdd failed'
                )
                return

            self.log_handler.set_log(
                'intersight.boot_hdd_device',
                managed_objects,
                json_conversion=True
            )

            for server_moid in target_server_moids:
                server_managed_objects = []
                for managed_object in managed_objects:
                    if 'ComputePhysical' in managed_object and managed_object['ComputePhysical'] is not None:
                        if server_moid == managed_object['ComputePhysical']['Moid']:
                            server_managed_objects.append(
                                managed_object
                            )

                self.cache_handler.set_intersight_cache_entry(
                    'boot_hdd',
                    server_managed_objects,
                    subdirectory=server_moid
                )

            return

        if key == 'boot_iscsi':
            cache_hits = []
            target_moids = []
            target_server_moids = []
            for server_moid in boot_moids:
                if cache_ttl is None or not self.cache_handler.is_intersight_cache('boot_iscsi', subdirectory=server_moid, cache_ttl=cache_ttl):
                    if len(boot_moids[server_moid]['iscsi']) == 0:
                        self.cache_handler.set_intersight_cache_entry(
                            'boot_iscsi',
                            [],
                            subdirectory=server_moid
                        )
                        cache_hits.append(
                            server_moid
                        )
                        continue

                    target_server_moids.append(
                        server_moid
                    )
                    for boot_id in boot_moids[server_moid]['iscsi']:
                        target_moids.append(
                            boot_id
                        )
                else:
                    cache_hits.append(
                        server_moid
                    )

            if len(cache_hits) > 0:
                self.log_handler.debug(
                    'compute_info.set_intersight_cache',
                    'boot iscsi cache hit: %s' % (cache_hits)
                )

            if len(target_moids) == 0:
                return

            if len(target_moids) < filter_length_threshold:
                moids_list = []
                for moid in target_moids:
                    moids_list.append('\'%s\'' % (moid))
                moids_filter = ', '.join(moids_list)

                self.boot_iscsi_device_handler.set_get_filter(
                    "Moid in (%s)" % (moids_filter)
                )

                self.log_handler.debug(
                    'compute_info.set_intersight_cache',
                    'boot iscsi cache miss w/filter: %s' % (target_moids)
                )
            else:
                self.log_handler.debug(
                    'compute_info.set_intersight_cache',
                    'boot iscsi cache miss wout filter'
                )

            managed_objects = self.boot_iscsi_device_handler.get_all()
            if managed_objects is None:
                self.log_handler.error(
                    'compute.set_intersight_cache',
                    'boot iscsi failed'
                )
                return

            self.log_handler.set_log(
                'intersight.boot_iscsi_device',
                managed_objects,
                json_conversion=True
            )

            for server_moid in target_server_moids:
                server_managed_objects = []
                for managed_object in managed_objects:
                    if 'ComputePhysical' in managed_object and managed_object['ComputePhysical'] is not None:
                        if server_moid == managed_object['ComputePhysical']['Moid']:
                            server_managed_objects.append(
                                managed_object
                            )

                self.cache_handler.set_intersight_cache_entry(
                    'boot_iscsi',
                    server_managed_objects,
                    subdirectory=server_moid
                )

            return

        if key == 'boot_nvme':
            cache_hits = []
            target_moids = []
            target_server_moids = []
            for server_moid in boot_moids:
                if cache_ttl is None or not self.cache_handler.is_intersight_cache('boot_nvme', subdirectory=server_moid, cache_ttl=cache_ttl):
                    if len(boot_moids[server_moid]['nvme']) == 0:
                        self.cache_handler.set_intersight_cache_entry(
                            'boot_nvme',
                            [],
                            subdirectory=server_moid
                        )
                        cache_hits.append(
                            server_moid
                        )
                        continue

                    target_server_moids.append(
                        server_moid
                    )
                    for boot_id in boot_moids[server_moid]['nvme']:
                        target_moids.append(
                            boot_id
                        )
                else:
                    cache_hits.append(
                        server_moid
                    )

            if len(cache_hits) > 0:
                self.log_handler.debug(
                    'compute_info.set_intersight_cache',
                    'boot nvme cache hit: %s' % (cache_hits)
                )

            if len(target_moids) == 0:
                return

            if len(target_moids) < filter_length_threshold:
                moids_list = []
                for moid in target_moids:
                    moids_list.append('\'%s\'' % (moid))
                moids_filter = ', '.join(moids_list)

                self.boot_nvme_device_handler.set_get_filter(
                    "Moid in (%s)" % (moids_filter)
                )

                self.log_handler.debug(
                    'compute_info.set_intersight_cache',
                    'boot nvme cache miss w/filter: %s' % (target_moids)
                )
            else:
                self.log_handler.debug(
                    'compute_info.set_intersight_cache',
                    'boot nvme cache miss wout filter'
                )

            managed_objects = self.boot_nvme_device_handler.get_all()
            if managed_objects is None:
                self.log_handler.error(
                    'compute.set_intersight_cache',
                    'boot nvme failed'
                )
                return

            self.log_handler.set_log(
                'intersight.boot_nvme_device',
                managed_objects,
                json_conversion=True
            )

            for server_moid in target_server_moids:
                server_managed_objects = []
                for managed_object in managed_objects:
                    if 'ComputePhysical' in managed_object and managed_object['ComputePhysical'] is not None:
                        if server_moid == managed_object['ComputePhysical']['Moid']:
                            server_managed_objects.append(
                                managed_object
                            )

                self.cache_handler.set_intersight_cache_entry(
                    'boot_nvme',
                    server_managed_objects,
                    subdirectory=server_moid
                )

            return

        if key == 'boot_pxe':
            cache_hits = []
            target_moids = []
            target_server_moids = []
            for server_moid in boot_moids:
                if cache_ttl is None or not self.cache_handler.is_intersight_cache('boot_pxe', subdirectory=server_moid, cache_ttl=cache_ttl):
                    if len(boot_moids[server_moid]['pxe']) == 0:
                        self.cache_handler.set_intersight_cache_entry(
                            'boot_pxe',
                            [],
                            subdirectory=server_moid
                        )
                        cache_hits.append(
                            server_moid
                        )
                        continue

                    target_server_moids.append(
                        server_moid
                    )
                    for boot_id in boot_moids[server_moid]['pxe']:
                        target_moids.append(
                            boot_id
                        )
                else:
                    cache_hits.append(
                        server_moid
                    )

            if len(cache_hits) > 0:
                self.log_handler.debug(
                    'compute_info.set_intersight_cache',
                    'boot pxe cache hit: %s' % (cache_hits)
                )

            if len(target_moids) == 0:
                return

            if len(target_moids) < filter_length_threshold:
                moids_list = []
                for moid in target_moids:
                    moids_list.append('\'%s\'' % (moid))
                moids_filter = ', '.join(moids_list)

                self.boot_pxe_device_handler.set_get_filter(
                    "Moid in (%s)" % (moids_filter)
                )

                self.log_handler.debug(
                    'compute_info.set_intersight_cache',
                    'boot pxe cache miss w/filter: %s' % (target_moids)
                )
            else:
                self.log_handler.debug(
                    'compute_info.set_intersight_cache',
                    'boot pxe cache miss wout filter'
                )

            managed_objects = self.boot_pxe_device_handler.get_all()
            if managed_objects is None:
                self.log_handler.error(
                    'compute.set_intersight_cache',
                    'boot pxe failed'
                )
                return

            self.log_handler.set_log(
                'intersight.boot_pxe_device',
                managed_objects,
                json_conversion=True
            )

            for server_moid in target_server_moids:
                server_managed_objects = []
                for managed_object in managed_objects:
                    if 'ComputePhysical' in managed_object and managed_object['ComputePhysical'] is not None:
                        if server_moid == managed_object['ComputePhysical']['Moid']:
                            server_managed_objects.append(
                                managed_object
                            )

                self.cache_handler.set_intersight_cache_entry(
                    'boot_pxe',
                    server_managed_objects,
                    subdirectory=server_moid
                )

            return

        if key == 'boot_san':
            cache_hits = []
            target_moids = []
            target_server_moids = []
            for server_moid in boot_moids:
                if cache_ttl is None or not self.cache_handler.is_intersight_cache('boot_san', subdirectory=server_moid, cache_ttl=cache_ttl):
                    if len(boot_moids[server_moid]['san']) == 0:
                        self.cache_handler.set_intersight_cache_entry(
                            'boot_san',
                            [],
                            subdirectory=server_moid
                        )
                        cache_hits.append(
                            server_moid
                        )
                        continue

                    target_server_moids.append(
                        server_moid
                    )
                    for boot_id in boot_moids[server_moid]['san']:
                        target_moids.append(
                            boot_id
                        )
                else:
                    cache_hits.append(
                        server_moid
                    )

            if len(cache_hits) > 0:
                self.log_handler.debug(
                    'compute_info.set_intersight_cache',
                    'boot san cache hit: %s' % (cache_hits)
                )

            if len(target_moids) == 0:
                return

            if len(target_moids) < filter_length_threshold:
                moids_list = []
                for moid in target_moids:
                    moids_list.append('\'%s\'' % (moid))
                moids_filter = ', '.join(moids_list)

                self.boot_san_device_handler.set_get_filter(
                    "Moid in (%s)" % (moids_filter)
                )

                self.log_handler.debug(
                    'compute_info.set_intersight_cache',
                    'boot san cache miss w/filter: %s' % (target_moids)
                )
            else:
                self.log_handler.debug(
                    'compute_info.set_intersight_cache',
                    'boot san cache miss wout filter'
                )

            managed_objects = self.boot_san_device_handler.get_all()
            if managed_objects is None:
                self.log_handler.error(
                    'compute.set_intersight_cache',
                    'boot san failed'
                )
                return

            self.log_handler.set_log(
                'intersight.boot_san_device',
                managed_objects,
                json_conversion=True
            )

            for server_moid in target_server_moids:
                server_managed_objects = []
                for managed_object in managed_objects:
                    if 'ComputePhysical' in managed_object and managed_object['ComputePhysical'] is not None:
                        if server_moid == managed_object['ComputePhysical']['Moid']:
                            server_managed_objects.append(
                                managed_object
                            )

                self.cache_handler.set_intersight_cache_entry(
                    'boot_san',
                    server_managed_objects,
                    subdirectory=server_moid
                )

            return

        if key == 'boot_sd':
            cache_hits = []
            target_moids = []
            target_server_moids = []
            for server_moid in boot_moids:
                if cache_ttl is None or not self.cache_handler.is_intersight_cache('boot_sd', subdirectory=server_moid, cache_ttl=cache_ttl):
                    if len(boot_moids[server_moid]['sd']) == 0:
                        self.cache_handler.set_intersight_cache_entry(
                            'boot_sd',
                            [],
                            subdirectory=server_moid
                        )
                        cache_hits.append(
                            server_moid
                        )
                        continue

                    target_server_moids.append(
                        server_moid
                    )
                    for boot_id in boot_moids[server_moid]['sd']:
                        target_moids.append(
                            boot_id
                        )
                else:
                    cache_hits.append(
                        server_moid
                    )

            if len(cache_hits) > 0:
                self.log_handler.debug(
                    'compute_info.set_intersight_cache',
                    'boot sd cache hit: %s' % (cache_hits)
                )

            if len(target_moids) == 0:
                return

            if len(target_moids) < filter_length_threshold:
                moids_list = []
                for moid in target_moids:
                    moids_list.append('\'%s\'' % (moid))
                moids_filter = ', '.join(moids_list)

                self.boot_sd_device_handler.set_get_filter(
                    "Moid in (%s)" % (moids_filter)
                )

                self.log_handler.debug(
                    'compute_info.set_intersight_cache',
                    'boot sd cache miss w/filter: %s' % (target_moids)
                )
            else:
                self.log_handler.debug(
                    'compute_info.set_intersight_cache',
                    'boot sd cache miss wout filter'
                )

            managed_objects = self.boot_sd_device_handler.get_all()
            if managed_objects is None:
                self.log_handler.error(
                    'compute.set_intersight_cache',
                    'boot sd failed'
                )
                return

            self.log_handler.set_log(
                'intersight.boot_sd_device',
                managed_objects,
                json_conversion=True
            )

            for server_moid in target_server_moids:
                server_managed_objects = []
                for managed_object in managed_objects:
                    if 'ComputePhysical' in managed_object and managed_object['ComputePhysical'] is not None:
                        if server_moid == managed_object['ComputePhysical']['Moid']:
                            server_managed_objects.append(
                                managed_object
                            )

                self.cache_handler.set_intersight_cache_entry(
                    'boot_sd',
                    server_managed_objects,
                    subdirectory=server_moid
                )

            return

        if key == 'boot_uefi':
            cache_hits = []
            target_moids = []
            target_server_moids = []
            for server_moid in boot_moids:
                if cache_ttl is None or not self.cache_handler.is_intersight_cache('boot_uefi', subdirectory=server_moid, cache_ttl=cache_ttl):
                    if len(boot_moids[server_moid]['uefi']) == 0:
                        self.cache_handler.set_intersight_cache_entry(
                            'boot_uefi',
                            [],
                            subdirectory=server_moid
                        )
                        cache_hits.append(
                            server_moid
                        )
                        continue

                    target_server_moids.append(
                        server_moid
                    )
                    for boot_id in boot_moids[server_moid]['uefi']:
                        target_moids.append(
                            boot_id
                        )
                else:
                    cache_hits.append(
                        server_moid
                    )

            if len(cache_hits) > 0:
                self.log_handler.debug(
                    'compute_info.set_intersight_cache',
                    'boot uefi cache hit: %s' % (cache_hits)
                )

            if len(target_moids) == 0:
                return

            if len(target_moids) < filter_length_threshold:
                moids_list = []
                for moid in target_moids:
                    moids_list.append('\'%s\'' % (moid))
                moids_filter = ', '.join(moids_list)

                self.boot_uefi_device_handler.set_get_filter(
                    "Moid in (%s)" % (moids_filter)
                )

                self.log_handler.debug(
                    'compute_info.set_intersight_cache',
                    'boot uefi cache miss w/filter: %s' % (target_moids)
                )
            else:
                self.log_handler.debug(
                    'compute_info.set_intersight_cache',
                    'boot uefi cache miss wout filter'
                )

            managed_objects = self.boot_uefi_device_handler.get_all()
            if managed_objects is None:
                self.log_handler.error(
                    'compute.set_intersight_cache',
                    'boot uefi failed'
                )
                return

            self.log_handler.set_log(
                'intersight.boot_uefi_device',
                managed_objects,
                json_conversion=True
            )

            for server_moid in target_server_moids:
                server_managed_objects = []
                for managed_object in managed_objects:
                    if 'ComputePhysical' in managed_object and managed_object['ComputePhysical'] is not None:
                        if server_moid == managed_object['ComputePhysical']['Moid']:
                            server_managed_objects.append(
                                managed_object
                            )

                self.cache_handler.set_intersight_cache_entry(
                    'boot_uefi',
                    server_managed_objects,
                    subdirectory=server_moid
                )

            return

        if key == 'boot_usb':
            cache_hits = []
            target_moids = []
            target_server_moids = []
            for server_moid in boot_moids:
                if cache_ttl is None or not self.cache_handler.is_intersight_cache('boot_usb', subdirectory=server_moid, cache_ttl=cache_ttl):
                    if len(boot_moids[server_moid]['usb']) == 0:
                        self.cache_handler.set_intersight_cache_entry(
                            'boot_usb',
                            [],
                            subdirectory=server_moid
                        )
                        cache_hits.append(
                            server_moid
                        )
                        continue

                    target_server_moids.append(
                        server_moid
                    )
                    for boot_id in boot_moids[server_moid]['usb']:
                        target_moids.append(
                            boot_id
                        )
                else:
                    cache_hits.append(
                        server_moid
                    )

            if len(cache_hits) > 0:
                self.log_handler.debug(
                    'compute_info.set_intersight_cache',
                    'boot usb cache hit: %s' % (cache_hits)
                )

            if len(target_moids) == 0:
                return

            if len(target_moids) < filter_length_threshold:
                moids_list = []
                for moid in target_moids:
                    moids_list.append('\'%s\'' % (moid))
                moids_filter = ', '.join(moids_list)

                self.boot_usb_device_handler.set_get_filter(
                    "Moid in (%s)" % (moids_filter)
                )

                self.log_handler.debug(
                    'compute_info.set_intersight_cache',
                    'boot usb cache miss w/filter: %s' % (target_moids)
                )
            else:
                self.log_handler.debug(
                    'compute_info.set_intersight_cache',
                    'boot usb cache miss wout filter'
                )

            managed_objects = self.boot_usb_device_handler.get_all()
            if managed_objects is None:
                self.log_handler.error(
                    'compute.set_intersight_cache',
                    'boot usb failed'
                )
                return

            self.log_handler.set_log(
                'intersight.boot_usb_device',
                managed_objects,
                json_conversion=True
            )

            for server_moid in target_server_moids:
                server_managed_objects = []
                for managed_object in managed_objects:
                    if 'ComputePhysical' in managed_object and managed_object['ComputePhysical'] is not None:
                        if server_moid == managed_object['ComputePhysical']['Moid']:
                            server_managed_objects.append(
                                managed_object
                            )

                self.cache_handler.set_intersight_cache_entry(
                    'boot_usb',
                    server_managed_objects,
                    subdirectory=server_moid
                )

            return

        if key == 'boot_vmedia':
            cache_hits = []
            target_moids = []
            target_server_moids = []
            for server_moid in boot_moids:
                if cache_ttl is None or not self.cache_handler.is_intersight_cache('boot_vmedia', subdirectory=server_moid, cache_ttl=cache_ttl):
                    if len(boot_moids[server_moid]['vmedia']) == 0:
                        self.cache_handler.set_intersight_cache_entry(
                            'boot_vmedia',
                            [],
                            subdirectory=server_moid
                        )
                        cache_hits.append(
                            server_moid
                        )
                        continue

                    target_server_moids.append(
                        server_moid
                    )
                    for boot_id in boot_moids[server_moid]['vmedia']:
                        target_moids.append(
                            boot_id
                        )
                else:
                    cache_hits.append(
                        server_moid
                    )

            if len(cache_hits) > 0:
                self.log_handler.debug(
                    'compute_info.set_intersight_cache',
                    'boot vmedia cache hit: %s' % (cache_hits)
                )

            if len(target_moids) == 0:
                return

            if len(target_moids) < filter_length_threshold:
                moids_list = []
                for moid in target_moids:
                    moids_list.append('\'%s\'' % (moid))
                moids_filter = ', '.join(moids_list)

                self.boot_vmedia_device_handler.set_get_filter(
                    "Moid in (%s)" % (moids_filter)
                )

                self.log_handler.debug(
                    'compute_info.set_intersight_cache',
                    'boot vmedia cache miss w/filter: %s' % (target_moids)
                )
            else:
                self.log_handler.debug(
                    'compute_info.set_intersight_cache',
                    'boot vmedia cache miss wout filter'
                )

            managed_objects = self.boot_vmedia_device_handler.get_all()
            if managed_objects is None:
                self.log_handler.error(
                    'compute.set_intersight_cache',
                    'boot vmedia failed'
                )
                return

            self.log_handler.set_log(
                'intersight.boot_vmedia_device',
                managed_objects,
                json_conversion=True
            )

            for server_moid in target_server_moids:
                server_managed_objects = []
                for managed_object in managed_objects:
                    if 'ComputePhysical' in managed_object and managed_object['ComputePhysical'] is not None:
                        if server_moid == managed_object['ComputePhysical']['Moid']:
                            server_managed_objects.append(
                                managed_object
                            )

                self.cache_handler.set_intersight_cache_entry(
                    'boot_vmedia',
                    server_managed_objects,
                    subdirectory=server_moid
                )

            return

        if key == 'cimc':
            cache_hits = []
            target_moids = []
            target_server_moids = []
            for server_moid in rack_moids:
                if cache_ttl is None or not self.cache_handler.is_intersight_cache('cimc', subdirectory=server_moid, cache_ttl=cache_ttl):
                    target_moids.append(
                        device_moids[server_moid]
                    )
                    target_server_moids.append(
                        server_moid
                    )
                else:
                    cache_hits.append(
                        server_moid
                    )

            if len(cache_hits) > 0:
                self.log_handler.debug(
                    'compute_info.set_intersight_cache',
                    'cimc cache hit: %s' % (cache_hits)
                )

            if len(target_moids) == 0:
                return

            server_managed_objects = {}
            for target_moid in target_server_moids:
                server_managed_objects[target_moid] = []

            chunk_id = 0
            while True:
                if chunk_id >= len(target_moids):
                    break

                chunk_target_moids = []
                index = 0
                for target_moid in target_moids:
                    if index >= chunk_id and len(chunk_target_moids) < filter_length_threshold:
                        chunk_target_moids.append(
                            target_moid
                        )

                    index = index + 1

                chunk_id = chunk_id + len(chunk_target_moids)

                moids_list = []
                for moid in chunk_target_moids:
                    moids_list.append('\'%s\'' % (moid))
                moids_filter = ', '.join(moids_list)

                self.management_interface_handler.set_get_filter(
                    "DeviceMoId in (%s)" % (moids_filter)
                )

                self.log_handler.debug(
                    'compute_info.set_intersight_cache',
                    'cimc miss w/filter: %s' % (chunk_target_moids)
                )

                managed_objects = self.management_interface_handler.get_all()
                if managed_objects is None:
                    self.log_handler.error(
                        'compute.set_intersight_cache',
                        'cimc failed'
                    )
                    return

                self.log_handler.set_log(
                    'intersight.management_interface',
                    managed_objects,
                    json_conversion=True
                )

                for server_moid in target_server_moids:
                    for managed_object in managed_objects:
                        if managed_object['DeviceMoId'] == device_moids[server_moid]:
                            for ancestor_mo in managed_object['Ancestors']:
                                if ancestor_mo['ObjectType'] == 'compute.RackUnit':
                                    if ancestor_mo['Moid'] == server_moid:
                                        server_managed_objects[server_moid].append(
                                            managed_object
                                        )

            for target_moid in target_server_moids:
                self.cache_handler.set_intersight_cache_entry(
                    'cimc',
                    server_managed_objects[target_moid],
                    subdirectory=target_moid
                )

            return

        if key == 'connector':
            cache_hits = []
            target_moids = []
            target_server_moids = []
            for server_moid in registration_moids:
                if cache_ttl is None or not self.cache_handler.is_intersight_cache('connector', subdirectory=server_moid, cache_ttl=cache_ttl):
                    target_moids.append(
                        registration_moids[server_moid]
                    )
                    target_server_moids.append(
                        server_moid
                    )
                else:
                    cache_hits.append(
                        server_moid
                    )

            if len(cache_hits) > 0:
                self.log_handler.debug(
                    'compute_info.set_intersight_cache',
                    'connector cache hit: %s' % (cache_hits)
                )

            if len(target_moids) == 0:
                return

            if len(target_moids) < filter_length_threshold:
                moids_list = []
                for moid in target_moids:
                    moids_list.append('\'%s\'' % (moid))
                moids_filter = ', '.join(moids_list)

                self.asset_device_registration_handler.set_get_filter(
                    "Moid in (%s)" % (moids_filter)
                )

                self.log_handler.debug(
                    'compute_info.set_intersight_cache',
                    'connector cache miss w/filter: %s' % (target_moids)
                )
            else:
                self.log_handler.debug(
                    'compute_info.set_intersight_cache',
                    'connector cache miss wout filter'
                )

            managed_objects = self.asset_device_registration_handler.get_all()
            if managed_objects is None:
                self.log_handler.error(
                    'compute.set_intersight_cache',
                    'connector failed'
                )
                return

            self.log_handler.set_log(
                'intersight.asset_device_registration',
                managed_objects,
                json_conversion=True
            )

            for server_moid in target_server_moids:
                server_managed_objects = []
                for managed_object in managed_objects:
                    if registration_moids[server_moid] == managed_object['Moid']:
                        server_managed_objects.append(
                            managed_object
                        )

                self.cache_handler.set_intersight_cache_entry(
                    'connector',
                    server_managed_objects,
                    subdirectory=server_moid
                )

            return

        if key == 'contract':
            cache_hits = []
            target_moids = []
            target_server_moids = []
            for server_moid in serial:
                if cache_ttl is None or not self.cache_handler.is_intersight_cache('contract', subdirectory=server_moid, cache_ttl=cache_ttl):
                    target_moids.append(
                        serial[server_moid]
                    )
                    target_server_moids.append(
                        server_moid
                    )
                else:
                    cache_hits.append(
                        server_moid
                    )

            if len(cache_hits) > 0:
                self.log_handler.debug(
                    'compute_info.set_intersight_cache',
                    'contract cache hit: %s' % (cache_hits)
                )

            if len(target_moids) == 0:
                return

            if len(target_moids) < filter_length_threshold:
                moids_list = []
                for moid in target_moids:
                    moids_list.append('\'%s\'' % (moid))
                moids_filter = ', '.join(moids_list)

                self.asset_device_contract_information_handler.set_get_filter(
                    "DeviceId in (%s)" % (moids_filter)
                )

                self.log_handler.debug(
                    'compute_info.set_intersight_cache',
                    'contract cache miss w/filter: %s' % (target_moids)
                )
            else:
                self.log_handler.debug(
                    'compute_info.set_intersight_cache',
                    'contract cache miss wout filter'
                )

            managed_objects = self.asset_device_contract_information_handler.get_all()
            if managed_objects is None:
                self.log_handler.error(
                    'compute.set_intersight_cache',
                    'contract failed'
                )
                return

            self.log_handler.set_log(
                'intersight.asset_device_contract_information',
                managed_objects,
                json_conversion=True
            )

            for server_moid in target_server_moids:
                server_managed_objects = []
                for managed_object in managed_objects:
                    if serial[server_moid] == managed_object['DeviceId']:
                        server_managed_objects.append(
                            managed_object
                        )

                self.cache_handler.set_intersight_cache_entry(
                    'contract',
                    server_managed_objects,
                    subdirectory=server_moid
                )

            return

        if key == 'cpu':
            cache_hits = []
            target_moids = []
            target_server_moids = []
            for server_moid in board_moids:
                if cache_ttl is None or not self.cache_handler.is_intersight_cache('cpu', subdirectory=server_moid, cache_ttl=cache_ttl):
                    target_moids.append(
                        board_moids[server_moid]
                    )
                    target_server_moids.append(
                        server_moid
                    )
                else:
                    cache_hits.append(
                        server_moid
                    )

            if len(cache_hits) > 0:
                self.log_handler.debug(
                    'compute_info.set_intersight_cache',
                    'cpu cache hit: %s' % (cache_hits)
                )

            if len(target_moids) == 0:
                return

            if len(target_moids) < filter_length_threshold:
                moids_list = []
                for moid in target_moids:
                    moids_list.append('\'%s\'' % (moid))
                moids_filter = ', '.join(moids_list)

                self.processor_unit_handler.set_get_filter(
                    "ComputeBoard/Moid in (%s)" % (moids_filter)
                )

                self.log_handler.debug(
                    'compute_info.set_intersight_cache',
                    'cpu cache miss w/filter: %s' % (target_moids)
                )
            else:
                self.log_handler.debug(
                    'compute_info.set_intersight_cache',
                    'cpu cache miss wout filter'
                )

            managed_objects = self.processor_unit_handler.get_all()
            if managed_objects is None:
                self.log_handler.error(
                    'compute.set_intersight_cache',
                    'cpu failed'
                )
                return

            self.log_handler.set_log(
                'intersight.processor_unit',
                managed_objects,
                json_conversion=True
            )

            for server_moid in target_server_moids:
                server_managed_objects = []
                for managed_object in managed_objects:
                    if 'ComputeBoard' in managed_object and managed_object['ComputeBoard'] is not None:
                        if board_moids[server_moid] == managed_object['ComputeBoard']['Moid']:
                            server_managed_objects.append(
                                managed_object
                            )

                self.cache_handler.set_intersight_cache_entry(
                    'cpu',
                    server_managed_objects,
                    subdirectory=server_moid
                )

            return

        if key == 'disk_group':
            cache_hits = []
            target_moids = []
            target_server_moids = []
            for server_moid in server_moids:
                if cache_ttl is None or not self.cache_handler.is_intersight_cache('disk_group', subdirectory=server_moid, cache_ttl=cache_ttl):
                    target_moids.append(
                        server_moid
                    )
                    target_server_moids.append(
                        server_moid
                    )
                else:
                    cache_hits.append(
                        server_moid
                    )

            if len(cache_hits) > 0:
                self.log_handler.debug(
                    'compute_info.set_intersight_cache',
                    'disk group cache hit: %s' % (cache_hits)
                )

            if len(target_moids) == 0:
                return

            server_storage_controller_map = {}
            storage_controller_moids = []
            for server_moid in target_moids:
                storage_controller_mos = self.cache_handler.get_intersight_cache_entry(
                    'storage_controller',
                    subdirectory=server_moid
                )
                if storage_controller_mos is None:
                    continue

                for storage_controller_mo in storage_controller_mos:
                    server_storage_controller_map[storage_controller_mo['Moid']] = server_moid
                    storage_controller_moids.append(
                        storage_controller_mo['Moid']
                    )

            if len(storage_controller_moids) > 0:
                if len(storage_controller_moids) < filter_length_threshold:
                    storage_controller_moids_list = []
                    for storage_controller_moid in storage_controller_moids:
                        storage_controller_moids_list.append('\'%s\'' % (storage_controller_moid))
                    storage_controller_moids_filter = ', '.join(storage_controller_moids_list)
                    self.storage_disk_group_handler.set_get_filter(
                        "StorageController/Moid in (%s)" % (storage_controller_moids_filter)
                    )

            self.storage_disk_group_handler.set_get_expand(
                'Spans'
            )
            managed_objects = self.storage_disk_group_handler.get_all()
            if managed_objects is None:
                self.log_handler.error(
                    'compute_extra_attributes.set_cache',
                    'storage disk group failed'
                )
                return

            self.log_handler.set_log(
                'intersight.storage_disk_group',
                managed_objects,
                json_conversion=True
            )

            for server_moid in target_server_moids:
                server_managed_objects = []
                for managed_object in managed_objects:
                    if 'StorageController' in managed_object and managed_object['StorageController'] is not None:
                        if managed_object['StorageController']['Moid'] in server_storage_controller_map:
                            if server_storage_controller_map[managed_object['StorageController']['Moid']] == server_moid:
                                server_managed_objects.append(
                                    managed_object
                                )

                self.cache_handler.set_intersight_cache_entry(
                    'disk_group',
                    server_managed_objects,
                    subdirectory=server_moid
                )

            return

        if key == 'fanmodule':
            # Server rack only
            cache_hits = []
            target_moids = []
            target_server_moids = []
            for server_moid in rack_moids:
                if cache_ttl is None or not self.cache_handler.is_intersight_cache('fanmodule', subdirectory=server_moid, cache_ttl=cache_ttl):
                    target_moids.append(
                        server_moid
                    )
                    target_server_moids.append(
                        server_moid
                    )
                else:
                    cache_hits.append(
                        server_moid
                    )

            if len(cache_hits) > 0:
                self.log_handler.debug(
                    'compute_info.set_intersight_cache',
                    'fan module cache hit: %s' % (cache_hits)
                )

            if len(target_moids) == 0:
                return

            server_managed_objects = {}
            for target_moid in target_moids:
                server_managed_objects[target_moid] = []

            chunk_id = 0
            while True:
                if chunk_id >= len(target_moids):
                    break

                chunk_target_moids = []
                index = 0
                for target_moid in target_moids:
                    if index >= chunk_id and len(chunk_target_moids) < filter_length_threshold:
                        chunk_target_moids.append(
                            target_moid
                        )

                    index = index + 1

                chunk_id = chunk_id + len(chunk_target_moids)

                moids_list = []
                for moid in chunk_target_moids:
                    moids_list.append('\'%s\'' % (moid))
                moids_filter = ', '.join(moids_list)

                self.fan_module_handler.set_get_filter(
                    "Parent/Moid in (%s)" % (moids_filter)
                )

                self.log_handler.debug(
                    'compute_info.set_intersight_cache',
                    'fan module cache miss w/filter: %s' % (chunk_target_moids)
                )

                managed_objects = self.fan_module_handler.get_all()
                if managed_objects is None:
                    self.log_handler.error(
                        'compute.set_intersight_cache',
                        'Fanmodule failed'
                    )
                    return

                self.log_handler.set_log(
                    'intersight.fan_module',
                    managed_objects,
                    json_conversion=True
                )

                for server_moid in target_server_moids:
                    for managed_object in managed_objects:
                        if 'Parent' in managed_object and managed_object['Parent'] is not None:
                            if server_moid == managed_object['Parent']['Moid']:
                                server_managed_objects[server_moid].append(
                                    managed_object
                                )

            for target_moid in target_moids:
                self.cache_handler.set_intersight_cache_entry(
                    'fanmodule',
                    server_managed_objects[target_moid],
                    subdirectory=target_moid
                )

            return

        if key == 'fan':
            cache_hits = []
            target_moids = []
            target_server_moids = []
            for server_moid in rack_moids:
                if cache_ttl is None or not self.cache_handler.is_intersight_cache('fan', subdirectory=server_moid, cache_ttl=cache_ttl):
                    target_moids.append(
                        server_moid
                    )
                    target_server_moids.append(
                        server_moid
                    )
                else:
                    cache_hits.append(
                        server_moid
                    )

            if len(cache_hits) > 0:
                self.log_handler.debug(
                    'compute_info.set_intersight_cache',
                    'fan cache hit: %s' % (cache_hits)
                )

            if len(target_moids) == 0:
                return

            detail_moids = []
            server_detail_moids = {}

            for server_moid in target_server_moids:
                server_detail_moids[server_moid] = []
                fan_module_mos = self.cache_handler.get_intersight_cache_entry(
                    'fanmodule',
                    subdirectory=server_moid
                )
                if fan_module_mos is None:
                    self.log_handler.error(
                        'compute_info.set_intersight_cache',
                        'fan module cache miss: %s' % (server_moid)
                    )
                    return

                for fan_module_mo in fan_module_mos:
                    server_detail_moids[server_moid].append(
                        fan_module_mo['Moid']
                    )
                    if fan_module_mo['Moid'] not in detail_moids:
                        detail_moids.append(
                            fan_module_mo['Moid']
                        )

            server_managed_objects = {}
            for target_moid in target_moids:
                server_managed_objects[target_moid] = []

            chunk_id = 0
            while True:
                if chunk_id >= len(detail_moids):
                    break

                chunk_target_moids = []
                index = 0
                for target_moid in detail_moids:
                    if index >= chunk_id and len(chunk_target_moids) < filter_length_threshold:
                        chunk_target_moids.append(
                            target_moid
                        )

                    index = index + 1

                chunk_id = chunk_id + len(chunk_target_moids)

                moids_list = []
                for moid in chunk_target_moids:
                    moids_list.append('\'%s\'' % (moid))
                moids_filter = ', '.join(moids_list)

                self.fan_handler.set_get_filter(
                    "Parent/Moid in (%s)" % (moids_filter)
                )

                self.log_handler.debug(
                    'compute_info.set_intersight_cache',
                    'fan cache miss w/filter: %s' % (chunk_target_moids)
                )

                managed_objects = self.fan_handler.get_all()
                if managed_objects is None:
                    self.log_handler.error(
                        'compute.set_intersight_cache',
                        'Fan failed'
                    )
                    return

                self.log_handler.set_log(
                    'intersight.fan',
                    managed_objects,
                    json_conversion=True
                )

                for server_moid in target_server_moids:
                    for managed_object in managed_objects:
                        if 'Parent' in managed_object and managed_object['Parent'] is not None:
                            for module_id in server_detail_moids[server_moid]:
                                if module_id == managed_object['Parent']['Moid']:
                                    server_managed_objects[server_moid].append(
                                        managed_object
                                    )

            for target_moid in target_moids:
                self.cache_handler.set_intersight_cache_entry(
                    'fan',
                    server_managed_objects[target_moid],
                    subdirectory=target_moid
                )

            return

        if key == 'firmware':
            cache_hits = []
            target_moids = []
            target_server_moids = []
            for server_moid in server_moids:
                if cache_ttl is None or not self.cache_handler.is_intersight_cache('firmware', subdirectory=server_moid, cache_ttl=cache_ttl):
                    target_moids.append(
                        server_moid
                    )
                    target_server_moids.append(
                        server_moid
                    )
                else:
                    cache_hits.append(
                        server_moid
                    )

            if len(cache_hits) > 0:
                self.log_handler.debug(
                    'compute_info.set_intersight_cache',
                    'firmware cache hit: %s' % (cache_hits)
                )

            if len(target_moids) == 0:
                return

            managed_objects = self.running_firmware_handler.get_all()
            if managed_objects is None:
                self.log_handler.error(
                    'compute.set_intersight_cache',
                    'firmware failed'
                )
                return

            self.log_handler.set_log(
                'intersight.running_firmware',
                managed_objects,
                json_conversion=True
            )

            for server_moid in target_server_moids:
                server_managed_objects = []
                for managed_object in managed_objects:
                    if 'Ancestors' in managed_object and managed_object['Ancestors'] is not None:
                        for ancestor_mo in managed_object['Ancestors']:
                            if ancestor_mo['Moid'] == server_moid:
                                server_managed_objects.append(
                                    managed_object
                                )
                                break

                self.cache_handler.set_intersight_cache_entry(
                    'firmware',
                    server_managed_objects,
                    subdirectory=server_moid
                )

            return

        if key == 'gcard':
            cache_hits = []
            target_moids = []
            target_server_moids = []
            for server_moid in blade_moids:
                if cache_ttl is None or not self.cache_handler.is_intersight_cache('gcard', subdirectory=server_moid, cache_ttl=cache_ttl):
                    target_moids = target_moids + gcard_moids[server_moid]
                    target_server_moids.append(
                        server_moid
                    )
                else:
                    cache_hits.append(
                        server_moid
                    )

            if len(cache_hits) > 0:
                self.log_handler.debug(
                    'compute_info.set_intersight_cache',
                    'gcard cache hit: %s' % (cache_hits)
                )

            if len(target_moids) == 0:
                return

            if len(target_moids) < filter_length_threshold:
                moids_list = []
                for moid in target_moids:
                    moids_list.append('\'%s\'' % (moid))
                moids_filter = ', '.join(moids_list)

                self.graphics_card_handler.set_get_filter(
                    "Moid in (%s)" % (moids_filter)
                )

                self.log_handler.debug(
                    'compute_info.set_intersight_cache',
                    'gcard cache miss w/filter: %s' % (target_moids)
                )
            else:
                self.log_handler.debug(
                    'compute_info.set_intersight_cache',
                    'gcard cache miss wout filter'
                )

            self.graphics_card_handler.set_get_expand(
                'GraphicsControllers,PciNode'
            )
            managed_objects = self.graphics_card_handler.get_all()
            if managed_objects is None:
                self.log_handler.error(
                    'compute.set_intersight_cache',
                    'gcard failed'
                )
                return

            self.log_handler.set_log(
                'intersight.graphics_card',
                managed_objects,
                json_conversion=True
            )

            for server_moid in target_server_moids:
                server_managed_objects = []
                for managed_object in managed_objects:
                    if 'PciNode' in managed_object and managed_object['PciNode'] is not None:
                        if 'ComputeBlade' in managed_object['PciNode'] and managed_object['PciNode']['ComputeBlade'] is not None:
                            if server_moid == managed_object['PciNode']['ComputeBlade']['Moid']:
                                server_managed_objects.append(
                                    managed_object
                                )

                self.cache_handler.set_intersight_cache_entry(
                    'gcard',
                    server_managed_objects,
                    subdirectory=server_moid
                )

            return

        if key == 'gpu':
            return

        if key == 'hcl':
            cache_hits = []
            target_moids = []
            target_server_moids = []
            for server_moid in server_moids:
                if cache_ttl is None or not self.cache_handler.is_intersight_cache('hcl', subdirectory=server_moid, cache_ttl=cache_ttl):
                    target_moids.append(
                        server_moid
                    )
                    target_server_moids.append(
                        server_moid
                    )
                else:
                    cache_hits.append(
                        server_moid
                    )

            if len(cache_hits) > 0:
                self.log_handler.debug(
                    'compute_info.set_intersight_cache',
                    'hcl cache hit: %s' % (cache_hits)
                )

            if len(target_moids) == 0:
                return

            if len(target_moids) < filter_length_threshold:
                moids_list = []
                for moid in target_moids:
                    moids_list.append('\'%s\'' % (moid))
                moids_filter = ', '.join(moids_list)

                self.cond_hclstatus_handler.set_get_filter(
                    "ManagedObject/Moid in (%s)" % (moids_filter)
                )

                self.log_handler.debug(
                    'compute_info.set_intersight_cache',
                    'hcl cache miss w/filter: %s' % (target_moids)
                )
            else:
                self.log_handler.debug(
                    'compute_info.set_intersight_cache',
                    'hcl cache miss wout filter'
                )

            managed_objects = self.cond_hclstatus_handler.get_all()
            if managed_objects is None:
                self.log_handler.error(
                    'compute.set_intersight_cache',
                    'hcl failed'
                )
                return

            self.log_handler.set_log(
                'intersight.cond_hclstatus',
                managed_objects,
                json_conversion=True
            )

            for server_moid in target_server_moids:
                server_managed_objects = []
                for managed_object in managed_objects:
                    if server_moid == managed_object['ManagedObject']['Moid']:
                        server_managed_objects.append(
                            managed_object
                        )

                self.cache_handler.set_intersight_cache_entry(
                    'hcl',
                    server_managed_objects,
                    subdirectory=server_moid
                )

            return

        if key == 'hcl_detail':
            cache_hits = []
            target_moids = []
            target_server_moids = []
            for server_moid in server_moids:
                if cache_ttl is None or not self.cache_handler.is_intersight_cache('hcl_detail', subdirectory=server_moid, cache_ttl=cache_ttl):
                    target_moids.append(
                        server_moid
                    )
                    target_server_moids.append(
                        server_moid
                    )
                else:
                    cache_hits.append(
                        server_moid
                    )

            if len(cache_hits) > 0:
                self.log_handler.debug(
                    'compute_info.set_intersight_cache',
                    'hcl status cache hit: %s' % (cache_hits)
                )

            if len(target_moids) == 0:
                return

            detail_moids = []
            server_detail_moids = {}

            for server_moid in target_server_moids:
                server_detail_moids[server_moid] = []
                hcl_mos = self.cache_handler.get_intersight_cache_entry(
                    'hcl',
                    subdirectory=server_moid
                )
                if hcl_mos is None:
                    self.log_handler.error(
                        'compute_info.set_intersight_cache',
                        'hcl cache miss: %s' % (server_moid)
                    )
                    return

                for hcl_mo in hcl_mos:
                    for detail_mo in hcl_mo['Details']:
                        server_detail_moids[server_moid].append(
                            detail_mo['Moid']
                        )
                        if detail_mo not in detail_moids:
                            detail_moids.append(
                                detail_mo['Moid']
                            )

            if len(detail_moids) < filter_length_threshold:
                moids_list = []
                for moid in detail_moids:
                    moids_list.append('\'%s\'' % (moid))
                moids_filter = ', '.join(moids_list)

                self.cond_hclstatus_detail_handler.set_get_filter(
                    "Moid in (%s)" % (moids_filter)
                )

                self.log_handler.debug(
                    'compute_info.set_intersight_cache',
                    'hcl detail cache miss w/filter: %s' % (target_moids)
                )
            else:
                self.log_handler.debug(
                    'compute_info.set_intersight_cache',
                    'hcl detail cache miss wout filter'
                )

            managed_objects = self.cond_hclstatus_detail_handler.get_all()
            if managed_objects is None:
                self.log_handler.error(
                    'compute.set_intersight_cache',
                    'hcl detail failed'
                )
                return

            self.log_handler.set_log(
                'intersight.cond_hclstatus_detail',
                managed_objects,
                json_conversion=True
            )

            for server_moid in target_server_moids:
                server_managed_objects = []
                for managed_object in managed_objects:
                    if managed_object['Moid'] in server_detail_moids[server_moid]:
                        server_managed_objects.append(
                            managed_object
                        )

                self.cache_handler.set_intersight_cache_entry(
                    'hcl_detail',
                    server_managed_objects,
                    subdirectory=server_moid
                )

            return

        if key == 'memory':
            cache_hits = []
            target_moids = []
            target_server_moids = []
            for server_moid in registration_moids:
                if cache_ttl is None or not self.cache_handler.is_intersight_cache('memory', subdirectory=server_moid, cache_ttl=cache_ttl):
                    target_moids.append(
                        server_moid
                    )
                    target_server_moids.append(
                        server_moid
                    )
                else:
                    cache_hits.append(
                        server_moid
                    )

            if len(cache_hits) > 0:
                self.log_handler.debug(
                    'compute_info.set_intersight_cache',
                    'memory cache hit: %s' % (cache_hits)
                )

            if len(target_moids) == 0:
                return

            server_managed_objects = {}
            for target_moid in target_moids:
                server_managed_objects[target_moid] = []

            chunk_id = 0
            while True:
                if chunk_id >= len(target_moids):
                    break

                chunk_target_moids = []
                index = 0
                for target_moid in target_moids:
                    if index >= chunk_id and len(chunk_target_moids) < filter_length_threshold:
                        chunk_target_moids.append(
                            target_moid
                        )

                    index = index + 1

                chunk_id = chunk_id + len(chunk_target_moids)

                moids_list = []
                for target_server_moid in chunk_target_moids:
                    for moid in self.memory_array_moids[target_server_moid]:
                        moids_list.append('\'%s\'' % (moid))
                moids_filter = ', '.join(moids_list)

                self.memory_unit_handler.set_get_filter(
                    "MemoryArray/Moid in (%s)" % (moids_filter)
                )

                self.log_handler.debug(
                    'compute_info.set_intersight_cache',
                    'memory cache miss w/filter for memory array: %s' % (moids_filter)
                )

                managed_objects = self.memory_unit_handler.get_all()
                if managed_objects is None:
                    self.log_handler.error(
                        'compute.set_intersight_cache',
                        'memory failed'
                    )
                    return

                self.log_handler.set_log(
                    'intersight.memory_unit',
                    managed_objects,
                    json_conversion=True
                )

                for server_moid in target_server_moids:
                    for managed_object in managed_objects:
                        if managed_object['MemoryArray']['Moid'] in self.memory_array_moids[server_moid]:
                            server_managed_objects[server_moid].append(
                                managed_object
                            )

            for target_moid in target_moids:
                self.cache_handler.set_intersight_cache_entry(
                    'memory',
                    server_managed_objects[target_moid],
                    subdirectory=target_moid
                )

            return

        if key == 'pci':
            cache_hits = []
            target_moids = []
            target_server_moids = []
            for server_moid in server_moids:
                if cache_ttl is None or not self.cache_handler.is_intersight_cache('pci', subdirectory=server_moid, cache_ttl=cache_ttl):
                    target_moids.append(
                        server_moid
                    )
                    target_server_moids.append(
                        server_moid
                    )
                else:
                    cache_hits.append(
                        server_moid
                    )

            if len(cache_hits) > 0:
                self.log_handler.debug(
                    'compute_info.set_intersight_cache',
                    'pci cache hit: %s' % (cache_hits)
                )

            if len(target_moids) == 0:
                return

            if len(target_moids) < filter_length_threshold:
                moids_list = []
                for moid in target_moids:
                    moids_list.append('\'%s\'' % (moid))
                moids_filter = ', '.join(moids_list)

                self.pci_handler.set_get_filter(
                    "Parent/Moid in (%s)" % (moids_filter)
                )

                self.log_handler.debug(
                    'compute_info.set_intersight_cache',
                    'pci cache miss w/filter: %s' % (target_moids)
                )
            else:
                self.log_handler.debug(
                    'compute_info.set_intersight_cache',
                    'pci cache miss wout filter'
                )

            managed_objects = self.pci_handler.get_all()
            if managed_objects is None:
                self.log_handler.error(
                    'compute.set_intersight_cache',
                    'pci failed'
                )
                return

            self.log_handler.set_log(
                'intersight.pci_handler',
                managed_objects,
                json_conversion=True
            )

            for server_moid in target_server_moids:
                server_managed_objects = []
                for managed_object in managed_objects:
                    if 'Parent' in managed_object and managed_object['Parent'] is not None:
                        if server_moid == managed_object['Parent']['Moid']:
                            server_managed_objects.append(
                                managed_object
                            )

                self.cache_handler.set_intersight_cache_entry(
                    'pci',
                    server_managed_objects,
                    subdirectory=server_moid
                )

            return

        if key == 'physical_disk':
            cache_hits = []
            target_moids = []
            target_server_moids = []
            for server_moid in registration_moids:
                if cache_ttl is None or not self.cache_handler.is_intersight_cache('physical_disk', subdirectory=server_moid, cache_ttl=cache_ttl):
                    target_moids.append(
                        registration_moids[server_moid]
                    )
                    target_server_moids.append(
                        server_moid
                    )
                else:
                    cache_hits.append(
                        server_moid
                    )

            if len(cache_hits) > 0:
                self.log_handler.debug(
                    'compute_info.set_intersight_cache',
                    'physical disk cache hit: %s' % (cache_hits)
                )

            if len(target_moids) == 0:
                return

            if len(target_moids) < filter_length_threshold:
                moids_list = []
                for moid in target_moids:
                    moids_list.append('\'%s\'' % (moid))
                moids_filter = ', '.join(moids_list)

                self.storage_physical_disk_handler.set_get_filter(
                    "RegisteredDevice/Moid in (%s)" % (moids_filter)
                )

                self.log_handler.debug(
                    'compute_info.set_intersight_cache',
                    'physical disk cache miss w/filter: %s' % (target_moids)
                )
            else:
                self.log_handler.debug(
                    'compute_info.set_intersight_cache',
                    'physical disk cache miss wout filter'
                )

            managed_objects = self.storage_physical_disk_handler.get_all()
            if managed_objects is None:
                self.log_handler.error(
                    'compute.set_intersight_cache',
                    'physical disk failed'
                )
                return

            self.log_handler.set_log(
                'intersight.storage_physical_disk',
                managed_objects,
                json_conversion=True
            )

            for server_moid in target_server_moids:
                server_managed_objects = []
                if server_moid in rack_moids:
                    for managed_object in managed_objects:
                        if 'RegisteredDevice' in managed_object and managed_object['RegisteredDevice'] is not None:
                            if registration_moids[server_moid] == managed_object['RegisteredDevice']['Moid']:
                                server_managed_objects.append(
                                    managed_object
                                )

                if server_moid in blade_moids:
                    for managed_object in managed_objects:
                        for ancestor_mo in managed_object['Ancestors']:
                            if ancestor_mo['ObjectType'] == 'compute.Blade' and ancestor_mo['Moid'] == server_moid:
                                server_managed_objects.append(
                                    managed_object
                                )

                self.cache_handler.set_intersight_cache_entry(
                    'physical_disk',
                    server_managed_objects,
                    subdirectory=server_moid
                )

            return

        if key == 'physical_disk_usage':
            cache_hits = []
            target_moids = []
            target_server_moids = []
            for server_moid in server_moids:
                if cache_ttl is None or not self.cache_handler.is_intersight_cache('physical_disk_usage', subdirectory=server_moid, cache_ttl=cache_ttl):
                    target_moids.append(
                        server_moid
                    )
                    target_server_moids.append(
                        server_moid
                    )
                else:
                    cache_hits.append(
                        server_moid
                    )

            if len(cache_hits) > 0:
                self.log_handler.debug(
                    'compute_info.set_intersight_cache',
                    'physical disk usage cache hit: %s' % (cache_hits)
                )

            if len(target_moids) == 0:
                return

            server_virtual_drive_map = {}
            virtual_drive_moids = []
            for server_moid in target_moids:
                virtual_drive_mos = self.cache_handler.get_intersight_cache_entry(
                    'virtual_drive',
                    subdirectory=server_moid
                )
                if virtual_drive_mos is None:
                    continue

                for virtual_drive_mo in virtual_drive_mos:
                    server_virtual_drive_map[virtual_drive_mo['Moid']] = server_moid
                    virtual_drive_moids.append(
                        virtual_drive_mo['Moid']
                    )

            if len(virtual_drive_moids) > 0:
                if len(virtual_drive_moids) < filter_length_threshold:
                    virtual_drive_moids_list = []
                    for virtual_drive_moid in virtual_drive_moids:
                        virtual_drive_moids_list.append('\'%s\'' % (virtual_drive_moid))
                    virtual_drive_moids_filter = ', '.join(virtual_drive_moids_list)
                    self.storage_physical_disk_usage_handler.set_get_filter(
                        "StorageVirtualDrive/Moid in (%s)" % (virtual_drive_moids_filter)
                    )

            managed_objects = self.storage_physical_disk_usage_handler.get_all()
            if managed_objects is None:
                self.log_handler.error(
                    'compute_extra_attributes.set_cache',
                    'physical disk usage failed'
                )
                return

            self.log_handler.set_log(
                'intersight.storage_physical_disk_usage',
                managed_objects,
                json_conversion=True
            )

            for server_moid in target_server_moids:
                server_managed_objects = []
                for managed_object in managed_objects:
                    if 'StorageVirtualDrive' in managed_object and managed_object['StorageVirtualDrive'] is not None:
                        if managed_object['StorageVirtualDrive']['Moid'] in server_virtual_drive_map:
                            if server_virtual_drive_map[managed_object['StorageVirtualDrive']['Moid']] == server_moid:
                                server_managed_objects.append(
                                    managed_object
                                )

                self.cache_handler.set_intersight_cache_entry(
                    'physical_disk_usage',
                    server_managed_objects,
                    subdirectory=server_moid
                )

            return

        if key == 'profile':
            cache_hits = []
            target_moids = []
            target_server_moids = []
            for server_moid in server_moids:
                if cache_ttl is None or not self.cache_handler.is_intersight_cache('profile', subdirectory=server_moid, cache_ttl=cache_ttl):
                    target_moids.append(
                        server_moid
                    )
                    target_server_moids.append(
                        server_moid
                    )
                else:
                    cache_hits.append(
                        server_moid
                    )

            if len(cache_hits) > 0:
                self.log_handler.debug(
                    'compute_info.set_intersight_cache',
                    'profile cache hit: %s' % (cache_hits)
                )

            if len(target_moids) == 0:
                return

            if len(target_moids) < filter_length_threshold:
                moids_list = []
                for moid in target_moids:
                    moids_list.append('\'%s\'' % (moid))
                moids_filter = ', '.join(moids_list)

                self.server_profile_handler.set_get_filter(
                    "AssignedServer/Moid in (%s)" % (moids_filter)
                )

                self.log_handler.debug(
                    'compute_info.set_intersight_cache',
                    'profile cache miss w/filter: %s' % (target_moids)
                )
            else:
                self.log_handler.debug(
                    'compute_info.set_intersight_cache',
                    'profile cache miss wout filter'
                )

            managed_objects = self.server_profile_handler.get_all()
            if managed_objects is None:
                self.log_handler.error(
                    'compute.set_intersight_cache',
                    'profile failed'
                )
                return

            self.log_handler.set_log(
                'intersight.server_profile',
                managed_objects,
                json_conversion=True
            )

            for server_moid in target_server_moids:
                server_managed_objects = []
                for managed_object in managed_objects:
                    if 'AssignedServer' in managed_object and managed_object['AssignedServer'] is not None:
                        if server_moid == managed_object['AssignedServer']['Moid']:
                            server_managed_objects.append(
                                managed_object
                            )

                self.cache_handler.set_intersight_cache_entry(
                    'profile',
                    server_managed_objects,
                    subdirectory=server_moid
                )

            return

        if key == 'psu':
            # Rack servers only
            cache_hits = []
            target_moids = []
            target_server_moids = []
            for server_moid in rack_moids:
                if cache_ttl is None or not self.cache_handler.is_intersight_cache('psu', subdirectory=server_moid, cache_ttl=cache_ttl):
                    target_moids.append(
                        server_moid
                    )
                    target_server_moids.append(
                        server_moid
                    )
                else:
                    cache_hits.append(
                        server_moid
                    )

            if len(cache_hits) > 0:
                self.log_handler.debug(
                    'compute_info.set_intersight_cache',
                    'psu cache hit: %s' % (cache_hits)
                )

            if len(target_moids) == 0:
                return

            if len(target_moids) < filter_length_threshold:
                moids_list = []
                for moid in target_moids:
                    moids_list.append('\'%s\'' % (moid))
                moids_filter = ', '.join(moids_list)

                self.psu_handler.set_get_filter(
                    "Parent/Moid in (%s)" % (moids_filter)
                )

                self.log_handler.debug(
                    'compute_info.set_intersight_cache',
                    'psu cache miss w/filter: %s' % (target_moids)
                )
            else:
                self.log_handler.debug(
                    'compute_info.set_intersight_cache',
                    'psu cache miss wout filter'
                )

            managed_objects = self.psu_handler.get_all()
            if managed_objects is None:
                self.log_handler.error(
                    'compute.set_intersight_cache',
                    'psu failed'
                )
                return

            self.log_handler.set_log(
                'intersight.psu',
                managed_objects,
                json_conversion=True
            )

            for server_moid in target_server_moids:
                server_managed_objects = []
                for managed_object in managed_objects:
                    if 'Parent' in managed_object and managed_object['Parent'] is not None:
                        if server_moid == managed_object['Parent']['Moid']:
                            server_managed_objects.append(
                                managed_object
                            )

                self.cache_handler.set_intersight_cache_entry(
                    'psu',
                    server_managed_objects,
                    subdirectory=server_moid
                )

            return

        if key == 'storage_controller':
            cache_hits = []
            target_moids = []
            target_server_moids = []

            # Rack server links to board
            for server_moid in rack_moids:
                if cache_ttl is None or not self.cache_handler.is_intersight_cache('storage_controller', subdirectory=server_moid, cache_ttl=cache_ttl):
                    target_moids.append(
                        board_moids[server_moid]
                    )
                    target_server_moids.append(
                        server_moid
                    )
                else:
                    cache_hits.append(
                        server_moid
                    )

            # Blade server links to moid or board
            for server_moid in blade_moids:
                if cache_ttl is None or not self.cache_handler.is_intersight_cache('storage_controller', subdirectory=server_moid, cache_ttl=cache_ttl):
                    target_moids.append(
                        board_moids[server_moid]
                    )
                    target_moids.append(
                        server_moid
                    )
                    target_server_moids.append(
                        server_moid
                    )
                else:
                    cache_hits.append(
                        server_moid
                    )

            if len(cache_hits) > 0:
                self.log_handler.debug(
                    'compute_info.set_intersight_cache',
                    'storage controller cache hit: %s' % (cache_hits)
                )

            if len(target_moids) == 0:
                return

            if 'storage' in expand and len(expand['storage']) > 0:
                self.storage_controller_handler.set_get_expand(
                    ','.join(expand['storage'])
                )

            server_managed_objects = {}
            for target_moid in target_server_moids:
                server_managed_objects[target_moid] = []

            chunk_id = 0
            while True:
                if chunk_id >= len(target_moids):
                    break

                chunk_target_moids = []
                index = 0
                for target_moid in target_moids:
                    if index >= chunk_id and len(chunk_target_moids) < filter_length_threshold:
                        chunk_target_moids.append(
                            target_moid
                        )

                    index = index + 1

                chunk_id = chunk_id + len(chunk_target_moids)

                moids_list = []
                for moid in chunk_target_moids:
                    moids_list.append('\'%s\'' % (moid))
                moids_filter = ', '.join(moids_list)

                self.storage_controller_handler.set_get_filter(
                    "Parent/Moid in (%s)" % (moids_filter)
                )

                self.log_handler.debug(
                    'compute_info.set_intersight_cache',
                    'storage controller cache miss w/filter: %s' % (chunk_target_moids)
                )

                managed_objects = self.storage_controller_handler.get_all()
                if managed_objects is None:
                    self.log_handler.error(
                        'compute.set_intersight_cache',
                        'cpu failed'
                    )
                    return

                self.log_handler.set_log(
                    'intersight.storage_controller',
                    managed_objects,
                    json_conversion=True
                )

                for server_moid in target_server_moids:
                    for managed_object in managed_objects:
                        if 'Parent' in managed_object and managed_object['Parent'] is not None:
                            if server_moid in rack_moids:
                                if board_moids[server_moid] == managed_object['Parent']['Moid']:
                                    server_managed_objects[server_moid].append(
                                        managed_object
                                    )

                            if server_moid in blade_moids:
                                if server_moid == managed_object['Parent']['Moid']:
                                    server_managed_objects[server_moid].append(
                                        managed_object
                                    )
                                if board_moids[server_moid] == managed_object['Parent']['Moid']:
                                    server_managed_objects[server_moid].append(
                                        managed_object
                                    )

            for target_moid in target_server_moids:
                self.cache_handler.set_intersight_cache_entry(
                    'storage_controller',
                    server_managed_objects[target_moid],
                    subdirectory=target_moid
                )

                if 'storage' in expand:
                    for expanded_item in expand['storage']:
                        if expanded_item not in ['PhysicalDisks', 'VirtualDrives']:
                            self.log_handler.error(
                                'compute.set_intersight_cache',
                                'unsupported storage controller expand: %s' % (expanded_item)
                            )
                            continue

                        if expanded_item == 'PhysicalDisks':
                            server_expanded_managed_objects = []
                            for server_managed_object in server_managed_objects[target_moid]:
                                for server_expanded_managed_object in server_managed_object['PhysicalDisks']:
                                    server_expanded_managed_objects.append(
                                        server_expanded_managed_object
                                    )

                            self.cache_handler.set_intersight_cache_entry(
                                'physical_disk',
                                server_expanded_managed_objects,
                                subdirectory=target_moid
                            )

                        if expanded_item == 'VirtualDrives':
                            server_expanded_managed_objects = []
                            for server_managed_object in server_managed_objects[target_moid]:
                                for server_expanded_managed_object in server_managed_object['VirtualDrives']:
                                    server_expanded_managed_objects.append(
                                        server_expanded_managed_object
                                    )

                            self.cache_handler.set_intersight_cache_entry(
                                'virtual_drive',
                                server_expanded_managed_objects,
                                subdirectory=target_moid
                            )

            return

        if key == 'tpm':
            cache_hits = []
            target_moids = []
            target_server_moids = []
            for server_moid in server_moids:
                if cache_ttl is None or not self.cache_handler.is_intersight_cache('tpm', subdirectory=server_moid, cache_ttl=cache_ttl):
                    target_moids.append(
                        server_moid
                    )
                    target_server_moids.append(
                        server_moid
                    )
                else:
                    cache_hits.append(
                        server_moid
                    )

            if len(cache_hits) > 0:
                self.log_handler.debug(
                    'compute_info.set_intersight_cache',
                    'tpm cache hit: %s' % (cache_hits)
                )

            if len(target_moids) == 0:
                return

            tpm_server_map = {}
            tpm_moids = []
            for server_moid in target_moids:
                self.cache_handler.set_intersight_cache_entry(
                    'tpm',
                    [],
                    subdirectory=server_moid
                )
                board_mos = self.cache_handler.get_intersight_cache_entry(
                    'board',
                    subdirectory=server_moid
                )
                if board_mos is None:
                    continue

                for board_mo in board_mos:
                    for tpm_mo in board_mo['EquipmentTpms']:
                        tpm_moids.append(
                            tpm_mo['Moid']
                        )
                        tpm_server_map[tpm_mo['Moid']] = server_moid

            if len(tpm_moids) == 0:
                return

            if len(tpm_moids) > 0:
                if len(tpm_moids) < filter_length_threshold:
                    tpm_moids_list = []
                    for tpm_moid in tpm_moids:
                        tpm_moids_list.append('\'%s\'' % (tpm_moid))
                    tpm_moids_filter = ', '.join(tpm_moids_list)
                    self.equipment_tpm_handler.set_get_filter(
                        "Moid in (%s)" % (tpm_moids_filter)
                    )

            managed_objects = self.equipment_tpm_handler.get_all()
            if managed_objects is None:
                self.log_handler.error(
                    'compute_extra_attributes.set_cache',
                    'tpm usage failed'
                )
                return

            self.log_handler.set_log(
                'intersight.equipment_tpm',
                managed_objects,
                json_conversion=True
            )

            for server_moid in target_server_moids:
                server_managed_objects = []
                for managed_object in managed_objects:
                    if managed_object['Moid'] in tpm_server_map:
                        if tpm_server_map[managed_object['Moid']] == server_moid:
                            server_managed_objects.append(
                                managed_object
                            )

                self.cache_handler.set_intersight_cache_entry(
                    'tpm',
                    server_managed_objects,
                    subdirectory=server_moid
                )

            return

        if key == 'virtual_drive':
            cache_hits = []
            target_moids = []
            target_server_moids = []
            for server_moid in registration_moids:
                if cache_ttl is None or not self.cache_handler.is_intersight_cache('virtual_drive', subdirectory=server_moid, cache_ttl=cache_ttl):
                    target_moids.append(
                        registration_moids[server_moid]
                    )
                    target_server_moids.append(
                        server_moid
                    )
                else:
                    cache_hits.append(
                        server_moid
                    )

            if len(cache_hits) > 0:
                self.log_handler.debug(
                    'compute_info.set_intersight_cache',
                    'virtual drive cache hit: %s' % (cache_hits)
                )

            if len(target_moids) == 0:
                return

            if len(target_moids) < filter_length_threshold:
                moids_list = []
                for moid in target_moids:
                    moids_list.append('\'%s\'' % (moid))
                moids_filter = ', '.join(moids_list)

                self.storage_virtual_drive_handler.set_get_filter(
                    "RegisteredDevice/Moid in (%s)" % (moids_filter)
                )

                self.log_handler.debug(
                    'compute_info.set_intersight_cache',
                    'virtual drive cache miss w/filter: %s' % (target_moids)
                )
            else:
                self.log_handler.debug(
                    'compute_info.set_intersight_cache',
                    'virtual drive cache miss wout filter'
                )

            managed_objects = self.storage_virtual_drive_handler.get_all()
            if managed_objects is None:
                self.log_handler.error(
                    'compute.set_intersight_cache',
                    'virtual drive failed'
                )
                return

            self.log_handler.set_log(
                'intersight.storage_virtual_drive',
                managed_objects,
                json_conversion=True
            )

            for server_moid in target_server_moids:
                server_managed_objects = []
                if server_moid in rack_moids:
                    for managed_object in managed_objects:
                        if 'RegisteredDevice' in managed_object and managed_object['RegisteredDevice'] is not None:
                            if registration_moids[server_moid] == managed_object['RegisteredDevice']['Moid']:
                                server_managed_objects.append(
                                    managed_object
                                )

                if server_moid in blade_moids:
                    for managed_object in managed_objects:
                        for ancestor_mo in managed_object['Ancestors']:
                            if ancestor_mo['ObjectType'] == 'compute.Blade' and ancestor_mo['Moid'] == server_moid:
                                server_managed_objects.append(
                                    managed_object
                                )

                self.cache_handler.set_intersight_cache_entry(
                    'virtual_drive',
                    server_managed_objects,
                    subdirectory=server_moid
                )

            return

        if key == 'workflow':
            cache_hits = []
            target_moids = []
            target_server_moids = []
            for server_moid in server_moids:
                if cache_ttl is None or not self.cache_handler.is_intersight_cache('workflow', subdirectory=server_moid, cache_ttl=cache_ttl):
                    target_moids.append(
                        server_moid
                    )
                    target_server_moids.append(
                        server_moid
                    )
                else:
                    cache_hits.append(
                        server_moid
                    )

            if len(cache_hits) > 0:
                self.log_handler.debug(
                    'compute_info.set_intersight_cache',
                    'fan cache hit: %s' % (cache_hits)
                )

            if len(target_moids) == 0:
                return

            workflows_mo = self.cache_handler.get_intersight_cache_entry(
                'workflows',
                check_ttl=False
            )
            if workflows_mo is None:
                self.log_handler.error(
                    'compute.set_intersight_cache',
                    'workflows cache not found'
                )
                return

            for server_moid in target_server_moids:
                server_managed_objects = []
                for workflow_mo in workflows_mo:
                    if self.workflow_handler.is_server_workflow(server_moid, workflow_mo):
                        server_managed_objects.append(
                            workflow_mo
                        )

                self.cache_handler.set_intersight_cache_entry(
                    'workflow',
                    server_managed_objects,
                    subdirectory=server_moid
                )

            return

        if key == 'workflows':
            if cache_ttl is None or not self.cache_handler.is_intersight_cache('workflows'):
                start_time = int(time.time()) - workflow_seconds
                reference_time = '%s.000Z' % (
                    time.strftime('%Y-%m-%dT%H:%M:%S', time.localtime(int(start_time)))
                )
                self.workflow_handler.set_get_filter('CreateTime gt %s' % (reference_time))

                managed_objects = self.workflow_handler.get_all()
                if managed_objects is None:
                    self.log_handler.error(
                        'compute.set_intersight_cache',
                        'workflows'
                    )
                    return

                self.log_handler.set_log(
                    'intersight.workflow',
                    managed_objects,
                    json_conversion=True
                )

                self.cache_handler.set_intersight_cache_entry(
                    'workflows',
                    managed_objects
                )

            return

        self.log_handler.error(
            'set_intersight_cache',
            'Unsupported key: %s' % (key)
        )
        return

    def set_cache(self, servers_mo, cache_settings, cache_ttl, ctx=None):
        start_time = int(time.time() * 1000)
        self.log_handler.debug(
            'compute.set_cache',
            'Start cache population'
        )

        # Expanded data in servers_mo is always 'fresh'

        expanded = []
        for server_mo in servers_mo:
            self.cache_handler.set_intersight_cache_entry(
                'server',
                server_mo,
                subdirectory=server_mo['Moid']
            )

            if 'PciDevices' in server_mo:
                if len(server_mo['PciDevices']) == 0:
                    self.cache_handler.set_intersight_cache_entry(
                        'pci',
                        [],
                        subdirectory=server_mo['Moid']
                    )

                if len(server_mo['PciDevices']) > 0:
                    if 'link' not in server_mo['PciDevices'][0]:
                        if 'pci' not in expanded:
                            expanded.append('pci')

                        self.cache_handler.set_intersight_cache_entry(
                            'pci',
                            server_mo['PciDevices'],
                            subdirectory=server_mo['Moid']
                        )

            if 'PciNodes' in server_mo:
                if len(server_mo['PciNodes']) == 0:
                    self.cache_handler.set_intersight_cache_entry(
                        'pci_nodes',
                        [],
                        subdirectory=server_mo['Moid']
                    )

                if len(server_mo['PciNodes']) > 0:
                    if 'link' not in server_mo['PciNodes'][0]:
                        if 'pci_node' not in expanded:
                            expanded.append('pci_node')

                        self.cache_handler.set_intersight_cache_entry(
                            'pci_node',
                            server_mo['PciNodes'],
                            subdirectory=server_mo['Moid']
                        )

            if 'Fanmodules' in server_mo:
                if len(server_mo['Fanmodules']) == 0:
                    self.cache_handler.set_intersight_cache_entry(
                        'fanmodule',
                        [],
                        subdirectory=server_mo['Moid']
                    )

                if len(server_mo['Fanmodules']) > 0:
                    if 'link' not in server_mo['Fanmodules'][0]:
                        if 'fanmodule' not in expanded:
                            expanded.append('fanmodule')

                        self.cache_handler.set_intersight_cache_entry(
                            'fanmodule',
                            server_mo['Fanmodules'],
                            subdirectory=server_mo['Moid']
                        )

            if 'Psus' in server_mo:
                if len(server_mo['Psus']) == 0:
                    self.cache_handler.set_intersight_cache_entry(
                        'psu',
                        [],
                        subdirectory=server_mo['Moid']
                    )

                if len(server_mo['Psus']) > 0:
                    if 'link' not in server_mo['Psus'][0]:
                        if 'psu' not in expanded:
                            expanded.append('psu')

                        self.cache_handler.set_intersight_cache_entry(
                            'psu',
                            server_mo['Psus'],
                            subdirectory=server_mo['Moid']
                        )

            if 'RegisteredDevice' in server_mo:
                if 'link' not in server_mo['RegisteredDevice']:
                    expanded.append('connector')
                    self.cache_handler.set_intersight_cache_entry(
                        'connector',
                        [server_mo['RegisteredDevice']],
                        subdirectory=server_mo['Moid']
                    )

        # Collect identifiers

        moids = []
        rack = []
        blade = []
        serial = {}
        registration_moids = {}
        board_moids = {}
        adapter_moids = {}
        boot_moids = {}
        device_moids = {}
        gcard_moids = {}

        for server_mo in servers_mo:
            moids.append(server_mo['Moid'])
            if server_mo['ObjectType'] == 'compute.RackUnit':
                rack.append(server_mo['Moid'])
                device_moids[server_mo['Moid']] = server_mo['DeviceMoId']
            if server_mo['ObjectType'] == 'compute.Blade':
                blade.append(server_mo['Moid'])
            serial[server_mo['Moid']] = server_mo['Serial']
            registration_moids[server_mo['Moid']] = server_mo['RegisteredDevice']['Moid']
            board_moids[server_mo['Moid']] = server_mo['Board']['Moid']

            adapter_moids[server_mo['Moid']] = []
            for adapter_mo in server_mo['Adapters']:
                adapter_moids[server_mo['Moid']].append(
                    adapter_mo['Moid']
                )

            boot_moids[server_mo['Moid']] = {}

            boot_moids[server_mo['Moid']]['cdd'] = []
            for item in server_mo['BootCddDevices']:
                boot_moids[server_mo['Moid']]['cdd'].append(
                    item['Moid']
                )

            boot_moids[server_mo['Moid']]['cdd'] = []
            for item in server_mo['BootCddDevices']:
                boot_moids[server_mo['Moid']]['cdd'].append(
                    item['Moid']
                )

            boot_moids[server_mo['Moid']]['cdd'] = []
            for item in server_mo['BootCddDevices']:
                boot_moids[server_mo['Moid']]['cdd'].append(
                    item['Moid']
                )

            boot_moids[server_mo['Moid']]['hdd'] = []
            for item in server_mo['BootHddDevices']:
                boot_moids[server_mo['Moid']]['hdd'].append(
                    item['Moid']
                )

            boot_moids[server_mo['Moid']]['iscsi'] = []
            for item in server_mo['BootIscsiDevices']:
                boot_moids[server_mo['Moid']]['iscsi'].append(
                    item['Moid']
                )

            boot_moids[server_mo['Moid']]['nvme'] = []
            for item in server_mo['BootNvmeDevices']:
                boot_moids[server_mo['Moid']]['nvme'].append(
                    item['Moid']
                )

            boot_moids[server_mo['Moid']]['pxe'] = []
            for item in server_mo['BootPxeDevices']:
                boot_moids[server_mo['Moid']]['pxe'].append(
                    item['Moid']
                )

            boot_moids[server_mo['Moid']]['san'] = []
            for item in server_mo['BootSanDevices']:
                boot_moids[server_mo['Moid']]['san'].append(
                    item['Moid']
                )

            boot_moids[server_mo['Moid']]['sd'] = []
            for item in server_mo['BootSdDevices']:
                boot_moids[server_mo['Moid']]['sd'].append(
                    item['Moid']
                )

            boot_moids[server_mo['Moid']]['uefi'] = []
            for item in server_mo['BootUefiShellDevices']:
                boot_moids[server_mo['Moid']]['uefi'].append(
                    item['Moid']
                )

            boot_moids[server_mo['Moid']]['usb'] = []
            for item in server_mo['BootUsbDevices']:
                boot_moids[server_mo['Moid']]['usb'].append(
                    item['Moid']
                )

            boot_moids[server_mo['Moid']]['vmedia'] = []
            for item in server_mo['BootVmediaDevices']:
                boot_moids[server_mo['Moid']]['vmedia'].append(
                    item['Moid']
                )

            gcard_moids[server_mo['Moid']] = []
            if 'PciNodes' in server_mo:
                for pci_node_mo in server_mo['PciNodes']:
                    if 'GraphicsCards' in pci_node_mo:
                        for gcard_mo in pci_node_mo['GraphicsCards']:
                            gcard_moids[server_mo['Moid']].append(
                                gcard_mo['Moid']
                            )

        # Set cache keys and expansion rules

        keys = []
        expand = {}

        if 'board' in cache_settings and cache_settings['board']:
            keys.append('board')
            expand['board'] = []

        if 'cpu' in cache_settings and cache_settings['cpu']:
            if 'board' in keys:
                expand['board'].append('Processors')
            else:
                keys.append('cpu')

        if 'gpu' in cache_settings and cache_settings['gpu']:
            keys.append('gpu')
            keys.append('gcard')

        if 'fan' in cache_settings and cache_settings['fan']:
            if 'fanmodule' not in expanded:
                keys.append('fanmodule')
            keys.append('fan')

        if 'memory' in cache_settings and cache_settings['memory']:
            if 'board' not in keys:
                keys.append('board')
            keys.append('memory')

        if 'pci' in cache_settings and cache_settings['pci'] and 'pci' not in expanded:
            keys.append('pci')

        if 'net' in cache_settings and cache_settings['net']:
            keys.append('cimc')
            keys.append('adapter')
            expand['adapter'] = []
            expand['adapter'].append(
                'ExtEthIfs'
            )
            expand['adapter'].append(
                'HostEthIfs'
            )
            expand['adapter'].append(
                'HostFcIfs'
            )

        if 'psu' in cache_settings and cache_settings['psu'] and 'psu' not in expanded:
            keys.append('psu')

        if 'storage' in cache_settings and cache_settings['storage']:
            keys.append('storage_controller')
            expand['storage'] = []
            expand['storage'].append(
                'PhysicalDisks'
            )
            expand['storage'].append(
                'VirtualDrives'
            )
            keys.append('physical_disk_usage')
            keys.append('disk_group')

        if 'fw' in cache_settings and cache_settings['fw']:
            keys.append('firmware')

        if 'boot' in cache_settings and cache_settings['boot']:
            keys.append('boot_bios')
            keys.append('boot_mode')
            keys.append('boot_security')
            keys.append('boot_hdd')
            keys.append('boot_cdd')
            keys.append('boot_iscsi')
            keys.append('boot_nvme')
            keys.append('boot_pxe')
            keys.append('boot_san')
            keys.append('boot_sd')
            keys.append('boot_uefi')
            keys.append('boot_usb')
            keys.append('boot_vmedia')

        if 'advisory' in cache_settings and cache_settings['advisory']:
            keys.append('advisories')
            keys.append('advisory')

        if 'alarm' in cache_settings and cache_settings['alarm']:
            keys.append('alarm')

        if 'connector' in cache_settings and cache_settings['connector'] and 'connector' not in expanded:
            keys.append('connector')

        if 'contract' in cache_settings and cache_settings['contract']:
            keys.append('contract')

        if 'hcl' in cache_settings and cache_settings['hcl']:
            keys.append('hcl')
            keys.append('hcl_detail')

        if 'profile' in cache_settings and cache_settings['profile']:
            keys.append('profile')

        if 'workflow' not in cache_settings:
            cache_settings['workflow'] = None

        if cache_settings['workflow'] is not None:
            keys.append('workflows')
            keys.append('workflow')

        if 'tpm' in cache_settings and cache_settings['tpm']:
            keys.append('tpm')

        # Collect cache data

        if len(keys) > 0:
            for key in keys:
                if ctx is not None:
                    ctx.my_output.debug('- %s' % (key))

                self.set_intersight_cache(
                    key,
                    expand,
                    moids,
                    rack,
                    blade,
                    registration_moids,
                    board_moids,
                    adapter_moids,
                    boot_moids,
                    device_moids,
                    gcard_moids,
                    serial,
                    cache_settings['workflow'],
                    cache_ttl=cache_ttl
                )

        if 'power' in cache_settings and cache_settings['power']:
            if ctx is not None:
                ctx.my_output.debug('- power')

            for server_mo in servers_mo:
                if server_mo['ManagementMode'] == 'UCSM':
                    if self.ucsm_endpoint_settings_handler.is_ucsm_endpoint(server_mo['Serial']):
                        server_serial = {}
                        server_serial[server_mo['Moid']] = server_mo['Serial']
                        self.set_redfish_cache(
                            'power-ucsm',
                            [server_mo['Moid']],
                            server_serial,
                            cache_ttl=cache_ttl
                        )
                    else:
                        self.log_handler.error(
                            'set_cache',
                            'Server in ucsm mode is not ucsm-enabled endpoint: %s' % (server_mo['Moid'])
                        )

                if server_mo['ManagementMode'] != 'UCSM':
                    if self.redfish_endpoint_settings_handler.is_redfish_endpoint(server_mo['Serial']):
                        server_serial = {}
                        server_serial[server_mo['Moid']] = server_mo['Serial']
                        self.set_redfish_cache(
                            'power',
                            [server_mo['Moid']],
                            server_serial,
                            cache_ttl=cache_ttl
                        )
                    else:
                        self.log_handler.error(
                            'set_cache',
                            'Server in IMM mode is not redfish-enabled endpoint: %s' % (server_mo['Moid'])
                        )

        if 'thermal' in cache_settings and cache_settings['thermal']:
            if ctx is not None:
                ctx.my_output.debug('- thermal')

            for server_mo in servers_mo:
                if server_mo['OperPowerState'] == 'on':
                    if server_mo['ManagementMode'] == 'UCSM':
                        if self.ucsm_endpoint_settings_handler.is_ucsm_endpoint(server_mo['Serial']):
                            server_serial = {}
                            server_serial[server_mo['Moid']] = server_mo['Serial']
                            self.set_redfish_cache(
                                'thernal-ucsm',
                                [server_mo['Moid']],
                                server_serial,
                                cache_ttl=cache_ttl
                            )
                        else:
                            self.log_handler.error(
                                'set_cache',
                                'Server in ucsm mode is not ucsm-enabled endpoint: %s' % (server_mo['Moid'])
                            )

                    if server_mo['ManagementMode'] != 'UCSM':
                        if self.redfish_endpoint_settings_handler.is_redfish_endpoint(server_mo['Serial']):
                            server_serial = {}
                            server_serial[server_mo['Moid']] = server_mo['Serial']
                            self.set_redfish_cache(
                                'thermal',
                                [server_mo['Moid']],
                                server_serial,
                                cache_ttl=cache_ttl
                            )
                        else:
                            self.log_handler.error(
                                'set_cache',
                                'Server in IMM mode is not redfish-enabled endpoint: %s' % (server_mo['Moid'])
                            )

        duration = int(time.time() * 1000) - start_time
        self.log_handler.debug(
            'compute.set_cache',
            'Cache populated in %s ms' % (duration)
        )
