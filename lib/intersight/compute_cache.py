import time


class ComputeCache():
    def __init__(self):
        pass

    def set_redfish_cache(self, key, server_moids, server_serial, cache_ttl=None):
        if key == 'power':
            for server_moid in server_moids:
                if cache_ttl is None or not self.cache_handler.is_intersight_cache('power', subdirectory=server_moid, cache_ttl=cache_ttl):
                    power_info = self.redfish_endpoint_settings_handler.get_redfish_endpoint_template(
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
                    power_info = self.redfish_endpoint_settings_handler.get_redfish_endpoint_template(
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

    def set_intersight_cache(self, key, server_moids, rack_moids, blade_moids, registration_moids, board_moids, adapter_moids, boot_moids, serial, workflow_seconds, filter_length_threshold=20, cache_ttl=None):
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

            if len(target_moids) < filter_length_threshold:
                moids_list = []
                for moid in target_moids:
                    moids_list.append('\'%s\'' % (moid))
                moids_filter = ', '.join(moids_list)

                self.adapter_unit_handler.set_get_filter(
                    "Moid in (%s)" % (moids_filter)
                )

                self.log_handler.debug(
                    'compute_info.set_intersight_cache',
                    'adapter miss w/filter: %s' % (target_moids)
                )
            else:
                self.log_handler.debug(
                    'compute_info.set_intersight_cache',
                    'adapter miss wout filter'
                )

            managed_objects = self.adapter_unit_handler.get_all()
            if managed_objects is None:
                self.log_handler.error(
                    'compute.set_intersight_cache',
                    'adapter failed'
                )
                return

            for server_moid in target_server_moids:
                server_managed_objects = []
                for managed_object in managed_objects:
                    if managed_object['Moid'] in adapter_moids[server_moid]:
                        server_managed_objects.append(
                            managed_object
                        )

                self.cache_handler.set_intersight_cache_entry(
                    'adapter',
                    server_managed_objects,
                    subdirectory=server_moid
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

            if len(target_rack_moids) > 0:
                if len(target_rack_moids) < filter_length_threshold:
                    moids_list = []
                    for moid in target_rack_moids:
                        moids_list.append('\'%s\'' % (moid))
                    moids_filter = ', '.join(moids_list)

                    self.compute_board_handler.set_get_filter(
                        "ComputeRackUnit/Moid in (%s)" % (moids_filter)
                    )

                    self.log_handler.debug(
                        'compute_info.set_intersight_cache',
                        'board cache miss w/filter: %s' % (target_rack_moids)
                    )
                else:
                    self.log_handler.debug(
                        'compute_info.set_intersight_cache',
                        'board cache miss wout filter'
                    )

                managed_objects = self.compute_board_handler.get_all()
                if managed_objects is None:
                    self.log_handler.error(
                        'compute.set_intersight_cache',
                        'board failed'
                    )
                    return

                for server_moid in target_rack_moids:
                    server_managed_objects = []
                    for managed_object in managed_objects:
                        if 'Parent' in managed_object and managed_object['Parent'] is not None:
                            if server_moid == managed_object['Parent']['Moid']:
                                server_managed_objects.append(
                                    managed_object
                                )

                    self.cache_handler.set_intersight_cache_entry(
                        'board',
                        server_managed_objects,
                        subdirectory=server_moid
                    )

            if len(target_blade_moids) > 0:
                if len(target_blade_moids) < filter_length_threshold:
                    moids_list = []
                    for moid in target_moids:
                        moids_list.append('\'%s\'' % (moid))
                    moids_filter = ', '.join(moids_list)

                    self.compute_board_handler.set_get_filter(
                        "ComputeBlade/Moid in (%s)" % (moids_filter)
                    )

                    self.log_handler.debug(
                        'compute_info.set_intersight_cache',
                        'board cache miss w/filter: %s' % (target_blade_moids)
                    )
                else:
                    self.log_handler.debug(
                        'compute_info.set_intersight_cache',
                        'board cache miss wout filter'
                    )

                managed_objects = self.compute_board_handler.get_all()
                if managed_objects is None:
                    self.log_handler.error(
                        'compute.set_intersight_cache',
                        'board failed'
                    )
                    return

                for server_moid in target_blade_moids:
                    server_managed_objects = []
                    for managed_object in managed_objects:
                        if 'Parent' in managed_object and managed_object['Parent'] is not None:
                            if server_moid == managed_object['Parent']['Moid']:
                                server_managed_objects.append(
                                    managed_object
                                )

                    self.cache_handler.set_intersight_cache_entry(
                        'board',
                        server_managed_objects,
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

        if key == 'fanmodule':
            cache_hits = []
            target_moids = []
            target_server_moids = []
            for server_moid in server_moids:
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
                    'fan cache hit: %s' % (cache_hits)
                )

            if len(target_moids) == 0:
                return

            if len(target_moids) < filter_length_threshold:
                moids_list = []
                for moid in target_moids:
                    moids_list.append('\'%s\'' % (moid))
                moids_filter = ', '.join(moids_list)

                self.fan_handler.set_get_filter(
                    "Parent/Moid in (%s)" % (moids_filter)
                )

                self.log_handler.debug(
                    'compute_info.set_intersight_cache',
                    'fan cache miss w/filter: %s' % (target_moids)
                )
            else:
                self.log_handler.debug(
                    'compute_info.set_intersight_cache',
                    'fan cache miss wout filter'
                )

            managed_objects = self.fan_handler.get_all()
            if managed_objects is None:
                self.log_handler.error(
                    'compute.set_intersight_cache',
                    'Fanmodule failed'
                )
                return

            for server_moid in target_server_moids:
                server_managed_objects = []
                for managed_object in managed_objects:
                    if 'Parent' in managed_object and managed_object['Parent'] is not None:
                        if server_moid == managed_object['Parent']['Moid']:
                            server_managed_objects.append(
                                managed_object
                            )

                self.cache_handler.set_intersight_cache_entry(
                    'fanmodule',
                    server_managed_objects,
                    subdirectory=server_moid
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

        if key == 'locator':
            cache_hits = []
            target_moids = []
            target_server_moids = []
            for server_moid in registration_moids:
                if cache_ttl is None or not self.cache_handler.is_intersight_cache('locator', subdirectory=server_moid, cache_ttl=cache_ttl):
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
                    'locator cache hit: %s' % (cache_hits)
                )

            if len(target_moids) == 0:
                return

            if len(target_moids) < filter_length_threshold:
                moids_list = []
                for moid in target_moids:
                    moids_list.append('\'%s\'' % (moid))
                moids_filter = ', '.join(moids_list)

                self.locator_handler.set_get_filter(
                    "RegisteredDevice/Moid in (%s)" % (moids_filter)
                )

                self.log_handler.debug(
                    'compute_info.set_intersight_cache',
                    'locator cache miss w/filter: %s' % (target_moids)
                )
            else:
                self.log_handler.debug(
                    'compute_info.set_intersight_cache',
                    'locator cache miss wout filter'
                )

            managed_objects = self.locator_handler.get_all()
            if managed_objects is None:
                self.log_handler.error(
                    'compute.set_intersight_cache',
                    'locator failed'
                )
                return

            for server_moid in target_server_moids:
                server_managed_objects = []
                for managed_object in managed_objects:
                    if 'RegisteredDevice' in managed_object and managed_object['RegisteredDevice'] is not None:
                        if registration_moids[server_moid] == managed_object['RegisteredDevice']['Moid']:
                            server_managed_objects.append(
                                managed_object
                            )

                self.cache_handler.set_intersight_cache_entry(
                    'locator',
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
                    'memory cache hit: %s' % (cache_hits)
                )

            if len(target_moids) == 0:
                return

            if len(target_moids) < filter_length_threshold:
                moids_list = []
                for moid in target_moids:
                    moids_list.append('\'%s\'' % (moid))
                moids_filter = ', '.join(moids_list)

                self.memory_unit_handler.set_get_filter(
                    "RegisteredDevice/Moid in (%s)" % (moids_filter)
                )

                self.log_handler.debug(
                    'compute_info.set_intersight_cache',
                    'memory cache miss w/filter: %s' % (target_moids)
                )
            else:
                self.log_handler.debug(
                    'compute_info.set_intersight_cache',
                    'memory cache miss wout filter'
                )

            managed_objects = self.memory_unit_handler.get_all()
            if managed_objects is None:
                self.log_handler.error(
                    'compute.set_intersight_cache',
                    'memory failed'
                )
                return

            for server_moid in target_server_moids:
                server_managed_objects = []
                for managed_object in managed_objects:
                    if 'RegisteredDevice' in managed_object and managed_object['RegisteredDevice'] is not None:
                        if registration_moids[server_moid] == managed_object['RegisteredDevice']['Moid']:
                            server_managed_objects.append(
                                managed_object
                            )

                self.cache_handler.set_intersight_cache_entry(
                    'memory',
                    server_managed_objects,
                    subdirectory=server_moid
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

            for server_moid in target_server_moids:
                server_managed_objects = []
                for managed_object in managed_objects:
                    if 'RegisteredDevice' in managed_object and managed_object['RegisteredDevice'] is not None:
                        if registration_moids[server_moid] == managed_object['RegisteredDevice']['Moid']:
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
            cache_hits = []
            target_moids = []
            target_server_moids = []
            for server_moid in server_moids:
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
            for server_moid in board_moids:
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

            if len(cache_hits) > 0:
                self.log_handler.debug(
                    'compute_info.set_intersight_cache',
                    'storage controller cache hit: %s' % (cache_hits)
                )

            if len(target_moids) == 0:
                return

            if len(target_moids) < filter_length_threshold:
                moids_list = []
                for moid in target_moids:
                    moids_list.append('\'%s\'' % (moid))
                moids_filter = ', '.join(moids_list)

                self.storage_controller_handler.set_get_filter(
                    "Parent/Moid in (%s)" % (moids_filter)
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

            managed_objects = self.storage_controller_handler.get_all()
            if managed_objects is None:
                self.log_handler.error(
                    'compute.set_intersight_cache',
                    'cpu failed'
                )
                return

            for server_moid in target_server_moids:
                server_managed_objects = []
                for managed_object in managed_objects:
                    if 'Parent' in managed_object and managed_object['Parent'] is not None:
                        if board_moids[server_moid] == managed_object['Parent']['Moid']:
                            server_managed_objects.append(
                                managed_object
                            )

                self.cache_handler.set_intersight_cache_entry(
                    'storage_controller',
                    server_managed_objects,
                    subdirectory=server_moid
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

            for server_moid in target_server_moids:
                server_managed_objects = []
                for managed_object in managed_objects:
                    if 'RegisteredDevice' in managed_object and managed_object['RegisteredDevice'] is not None:
                        if registration_moids[server_moid] == managed_object['RegisteredDevice']['Moid']:
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

    def set_cache(self, servers_mo, cache_settings, cache_ttl, parallel=False):
        start_time = int(time.time() * 1000)
        self.log_handler.debug(
            'compute.set_cache',
            'Start cache population'
        )

        moids = []
        rack = []
        blade = []
        serial = {}
        registration_moids = {}
        board_moids = {}
        adapter_moids = {}
        boot_moids = {}

        for server_mo in servers_mo:
            moids.append(server_mo['Moid'])
            if server_mo['ObjectType'] == 'compute.RackUnit':
                rack.append(server_mo['Moid'])
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

        keys = []

        if 'board' in cache_settings and cache_settings['board']:
            keys.append('board')

        if 'cpu' in cache_settings and cache_settings['cpu']:
            keys.append('cpu')

        if 'gpu' in cache_settings and cache_settings['gpu']:
            keys.append('gpu')

        if 'fan' in cache_settings and cache_settings['fan']:
            keys.append('fanmodule')

        if 'memory' in cache_settings and cache_settings['memory']:
            keys.append('memory')

        if 'pci' in cache_settings and cache_settings['pci']:
            keys.append('pci')

        if 'net' in cache_settings and cache_settings['net']:
            keys.append('adapter')
            keys.append('adapter_ext_eth_interface')
            keys.append('adapter_host_eth_interface')
            keys.append('adapter_host_fc_interface')

        if 'psu' in cache_settings and cache_settings['psu']:
            keys.append('psu')

        if 'storage' in cache_settings and cache_settings['storage']:
            keys.append('storage_controller')
            keys.append('virtual_drive')
            keys.append('physical_disk')

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
            keys.append('advisory')
            self.set_intersight_cache(
                'advisories',
                moids,
                rack,
                blade,
                registration_moids,
                board_moids,
                adapter_moids,
                boot_moids,
                serial,
                cache_settings['workflow'],
                cache_ttl=cache_ttl
            )

        if 'alarm' in cache_settings and cache_settings['alarm']:
            keys.append('alarm')

        if 'connector' in cache_settings and cache_settings['connector']:
            keys.append('connector')

        if 'contract' in cache_settings and cache_settings['contract']:
            keys.append('contract')

        if 'hcl' in cache_settings and cache_settings['hcl']:
            keys.append('hcl')

        if 'profile' in cache_settings and cache_settings['profile']:
            keys.append('profile')

        if 'locator' in cache_settings and cache_settings['locator']:
            keys.append('locator')

        if 'workflow' not in cache_settings:
            cache_settings['workflow'] = None

        if cache_settings['workflow'] is not None:
            keys.append('workflow')
            self.set_intersight_cache(
                'workflows',
                moids,
                rack,
                blade,
                registration_moids,
                board_moids,
                adapter_moids,
                boot_moids,
                serial,
                cache_settings['workflow'],
                cache_ttl=cache_ttl
            )

        if len(keys) > 0:
            for key in keys:
                self.set_intersight_cache(
                    key,
                    moids,
                    rack,
                    blade,
                    registration_moids,
                    board_moids,
                    adapter_moids,
                    boot_moids,
                    serial,
                    cache_settings['workflow'],
                    cache_ttl=cache_ttl
                )

        if 'hcl' in cache_settings and cache_settings['hcl']:
            self.set_intersight_cache(
                'hcl_detail',
                moids,
                rack,
                blade,
                registration_moids,
                board_moids,
                adapter_moids,
                boot_moids,
                serial,
                cache_settings['workflow'],
                cache_ttl=cache_ttl
            )

        if 'storage' in cache_settings and cache_settings['storage']:
            self.set_intersight_cache(
                'physical_disk_usage',
                moids,
                rack,
                blade,
                registration_moids,
                board_moids,
                adapter_moids,
                boot_moids,
                serial,
                cache_settings['workflow'],
                cache_ttl=cache_ttl
            )

        if 'tpm' in cache_settings and cache_settings['tpm']:
            self.set_intersight_cache(
                'tpm',
                moids,
                rack,
                blade,
                registration_moids,
                board_moids,
                adapter_moids,
                boot_moids,
                serial,
                cache_settings['workflow'],
                cache_ttl=cache_ttl
            )

        for server_mo in servers_mo:
            if 'power' in cache_settings and cache_settings['power']:
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

            if 'thermal' in cache_settings and cache_settings['thermal']:
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

        duration = int(time.time() * 1000) - start_time
        self.log_handler.debug(
            'compute.set_cache',
            'Cache populated in %s ms' % (duration)
        )
