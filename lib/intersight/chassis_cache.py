import time


class ChassisCache():
    def __init__(self):
        pass

    def set_intersight_cache(self, key, chassis_moids, device_moids, serial, filter_length_threshold=20, cache_ttl=None):
        if key == 'fan_control':
            cache_hits = []
            target_chassis_moids = []
            for chassis_moid in chassis_moids:
                if cache_ttl is None or not self.cache_handler.is_intersight_cache('fan_control', subdirectory=chassis_moid, cache_ttl=cache_ttl):
                    target_chassis_moids.append(
                        chassis_moid
                    )
                else:
                    cache_hits.append(
                        chassis_moid
                    )

            if len(cache_hits) > 0:
                self.log_handler.debug(
                    'chassis.set_intersight_cache',
                    'fan control cache hit: %s' % (cache_hits)
                )

            if len(target_chassis_moids) == 0:
                return

            if len(target_chassis_moids) < filter_length_threshold:
                moids_list = []
                for moid in target_chassis_moids:
                    moids_list.append('\'%s\'' % (moid))
                moids_filter = ', '.join(moids_list)

                self.fan_control_handler.set_get_filter(
                    "Parent/Moid in (%s)" % (moids_filter)
                )

                self.log_handler.debug(
                    'chassis_info.set_intersight_cache',
                    'fan control miss w/filter: %s' % (target_chassis_moids)
                )
            else:
                self.log_handler.debug(
                    'chassis_info.set_intersight_cache',
                    'fan control miss wout filter'
                )

            managed_objects = self.fan_control_handler.get_all()
            if managed_objects is None:
                self.log_handler.error(
                    'chassis_info.set_intersight_cache',
                    'fan control failed'
                )
                return

            for chassis_moid in target_chassis_moids:
                chassis_managed_objects = []
                for managed_object in managed_objects:
                    if managed_object['Parent']['Moid'] == chassis_moid:
                        chassis_managed_objects.append(
                            managed_object
                        )

                self.cache_handler.set_intersight_cache_entry(
                    'fan_control',
                    chassis_managed_objects,
                    subdirectory=chassis_moid
                )

            return

        if key == 'fan_module':
            cache_hits = []
            target_chassis_moids = []
            for chassis_moid in chassis_moids:
                if cache_ttl is None or not self.cache_handler.is_intersight_cache('fan_module', subdirectory=chassis_moid, cache_ttl=cache_ttl):
                    target_chassis_moids.append(
                        chassis_moid
                    )
                else:
                    cache_hits.append(
                        chassis_moid
                    )

            if len(cache_hits) > 0:
                self.log_handler.debug(
                    'chassis.set_intersight_cache',
                    'fan module cache hit: %s' % (cache_hits)
                )

            if len(target_chassis_moids) == 0:
                return

            if len(target_chassis_moids) < filter_length_threshold:
                moids_list = []
                for moid in target_chassis_moids:
                    moids_list.append('\'%s\'' % (moid))
                moids_filter = ', '.join(moids_list)

                self.fan_module_handler.set_get_filter(
                    "Parent/Moid in (%s)" % (moids_filter)
                )

                self.log_handler.debug(
                    'chassis_info.set_intersight_cache',
                    'fan module miss w/filter: %s' % (target_chassis_moids)
                )
            else:
                self.log_handler.debug(
                    'chassis_info.set_intersight_cache',
                    'fan module miss wout filter'
                )

            managed_objects = self.fan_module_handler.get_all()
            if managed_objects is None:
                self.log_handler.error(
                    'chassis_info.set_intersight_cache',
                    'fan module failed'
                )
                return

            for chassis_moid in target_chassis_moids:
                chassis_managed_objects = []
                for managed_object in managed_objects:
                    if managed_object['Parent']['Moid'] == chassis_moid:
                        chassis_managed_objects.append(
                            managed_object
                        )

                self.cache_handler.set_intersight_cache_entry(
                    'fan_module',
                    chassis_managed_objects,
                    subdirectory=chassis_moid
                )

            return

        if key == 'fan':
            cache_hits = []
            target_moids = []
            target_chassis_moids = []
            for chassis_moid in chassis_moids:
                if cache_ttl is None or not self.cache_handler.is_intersight_cache('fan', subdirectory=chassis_moid, cache_ttl=cache_ttl):
                    target_moids.append(
                        device_moids[chassis_moid]
                    )
                    target_chassis_moids.append(
                        chassis_moid
                    )
                else:
                    cache_hits.append(
                        chassis_moid
                    )

            if len(cache_hits) > 0:
                self.log_handler.debug(
                    'chassis.set_intersight_cache',
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
                    "RegisteredDevice/Moid in (%s)" % (moids_filter)
                )

                self.log_handler.debug(
                    'chassis_info.set_intersight_cache',
                    'fan miss w/filter: %s' % (target_chassis_moids)
                )
            else:
                self.log_handler.debug(
                    'chassis_info.set_intersight_cache',
                    'fan miss wout filter'
                )

            managed_objects = self.fan_handler.get_all()
            if managed_objects is None:
                self.log_handler.error(
                    'chassis_info.set_intersight_cache',
                    'fan failed'
                )
                return

            for chassis_moid in target_chassis_moids:
                chassis_managed_objects = []
                for managed_object in managed_objects:
                    if managed_object['RegisteredDevice']['Moid'] == device_moids[chassis_moid]:
                        chassis_managed_objects.append(
                            managed_object
                        )

                self.cache_handler.set_intersight_cache_entry(
                    'fan',
                    chassis_managed_objects,
                    subdirectory=chassis_moid
                )

            return

        if key == 'power_control':
            cache_hits = []
            target_chassis_moids = []
            for chassis_moid in chassis_moids:
                if cache_ttl is None or not self.cache_handler.is_intersight_cache('power_control', subdirectory=chassis_moid, cache_ttl=cache_ttl):
                    target_chassis_moids.append(
                        chassis_moid
                    )
                else:
                    cache_hits.append(
                        chassis_moid
                    )

            if len(cache_hits) > 0:
                self.log_handler.debug(
                    'chassis.set_intersight_cache',
                    'power control cache hit: %s' % (cache_hits)
                )

            if len(target_chassis_moids) == 0:
                return

            if len(target_chassis_moids) < filter_length_threshold:
                moids_list = []
                for moid in target_chassis_moids:
                    moids_list.append('\'%s\'' % (moid))
                moids_filter = ', '.join(moids_list)

                self.power_control_state_handler.set_get_filter(
                    "Parent/Moid in (%s)" % (moids_filter)
                )

                self.log_handler.debug(
                    'chassis_info.set_intersight_cache',
                    'power control miss w/filter: %s' % (target_chassis_moids)
                )
            else:
                self.log_handler.debug(
                    'chassis_info.set_intersight_cache',
                    'power control miss wout filter'
                )

            managed_objects = self.power_control_state_handler.get_all()
            if managed_objects is None:
                self.log_handler.error(
                    'chassis_info.set_intersight_cache',
                    'power control failed'
                )
                return

            for chassis_moid in target_chassis_moids:
                chassis_managed_objects = []
                for managed_object in managed_objects:
                    if managed_object['Parent']['Moid'] == chassis_moid:
                        chassis_managed_objects.append(
                            managed_object
                        )

                self.cache_handler.set_intersight_cache_entry(
                    'power_control',
                    chassis_managed_objects,
                    subdirectory=chassis_moid
                )

            return

        if key == 'psu_control':
            cache_hits = []
            target_moids = []
            target_chassis_moids = []
            for chassis_moid in chassis_moids:
                if cache_ttl is None or not self.cache_handler.is_intersight_cache('psu_control', subdirectory=chassis_moid, cache_ttl=cache_ttl):
                    target_moids.append(
                        chassis_moid
                    )
                    target_chassis_moids.append(
                        chassis_moid
                    )
                else:
                    cache_hits.append(
                        chassis_moid
                    )

            if len(cache_hits) > 0:
                self.log_handler.debug(
                    'chassis.set_intersight_cache',
                    'psu control cache hit: %s' % (cache_hits)
                )

            if len(target_moids) == 0:
                return

            if len(target_moids) < filter_length_threshold:
                moids_list = []
                for moid in target_moids:
                    moids_list.append('\'%s\'' % (moid))
                moids_filter = ', '.join(moids_list)

                self.psu_control_handler.set_get_filter(
                    "Parent/Moid in (%s)" % (moids_filter)
                )

                self.log_handler.debug(
                    'chassis_info.set_intersight_cache',
                    'psu control miss w/filter: %s' % (target_chassis_moids)
                )
            else:
                self.log_handler.debug(
                    'chassis_info.set_intersight_cache',
                    'psu control miss wout filter'
                )

            managed_objects = self.psu_control_handler.get_all()
            if managed_objects is None:
                self.log_handler.error(
                    'chassis_info.set_intersight_cache',
                    'psu control failed'
                )
                return

            for chassis_moid in target_chassis_moids:
                chassis_managed_objects = []
                for managed_object in managed_objects:
                    if managed_object['Parent']['Moid'] == chassis_moid:
                        chassis_managed_objects.append(
                            managed_object
                        )

                self.cache_handler.set_intersight_cache_entry(
                    'psu_control',
                    chassis_managed_objects,
                    subdirectory=chassis_moid
                )

            return

        if key == 'psu':
            cache_hits = []
            target_chassis_moids = []
            for chassis_moid in chassis_moids:
                if cache_ttl is None or not self.cache_handler.is_intersight_cache('psu', subdirectory=chassis_moid, cache_ttl=cache_ttl):
                    target_chassis_moids.append(
                        chassis_moid
                    )
                else:
                    cache_hits.append(
                        chassis_moid
                    )

            if len(cache_hits) > 0:
                self.log_handler.debug(
                    'chassis.set_intersight_cache',
                    'psu cache hit: %s' % (cache_hits)
                )

            if len(target_chassis_moids) == 0:
                return

            if len(target_chassis_moids) < filter_length_threshold:
                moids_list = []
                for moid in target_chassis_moids:
                    moids_list.append('\'%s\'' % (moid))
                moids_filter = ', '.join(moids_list)

                self.psu_handler.set_get_filter(
                    "Parent/Moid in (%s)" % (moids_filter)
                )

                self.log_handler.debug(
                    'chassis_info.set_intersight_cache',
                    'psu miss w/filter: %s' % (target_chassis_moids)
                )
            else:
                self.log_handler.debug(
                    'chassis_info.set_intersight_cache',
                    'psu miss wout filter'
                )

            managed_objects = self.psu_handler.get_all()
            if managed_objects is None:
                self.log_handler.error(
                    'chassis_info.set_intersight_cache',
                    'psu failed'
                )
                return

            for chassis_moid in target_chassis_moids:
                chassis_managed_objects = []
                for managed_object in managed_objects:
                    if managed_object['Parent']['Moid'] == chassis_moid:
                        chassis_managed_objects.append(
                            managed_object
                        )

                self.cache_handler.set_intersight_cache_entry(
                    'psu',
                    chassis_managed_objects,
                    subdirectory=chassis_moid
                )

            return

        if key == 'iocard':
            cache_hits = []
            target_moids = []
            target_chassis_moids = []
            for chassis_moid in chassis_moids:
                if cache_ttl is None or not self.cache_handler.is_intersight_cache('iocard', subdirectory=chassis_moid, cache_ttl=cache_ttl):
                    target_moids.append(
                        device_moids[chassis_moid]
                    )
                    target_chassis_moids.append(
                        chassis_moid
                    )
                else:
                    cache_hits.append(
                        chassis_moid
                    )

            if len(cache_hits) > 0:
                self.log_handler.debug(
                    'chassis.set_intersight_cache',
                    'iocard cache hit: %s' % (cache_hits)
                )

            if len(target_moids) == 0:
                return

            if len(target_moids) < filter_length_threshold:
                moids_list = []
                for moid in target_moids:
                    moids_list.append('\'%s\'' % (moid))
                moids_filter = ', '.join(moids_list)

                self.iocard_handler.set_get_filter(
                    "RegisteredDevice/Moid in (%s)" % (moids_filter)
                )

                self.log_handler.debug(
                    'chassis_info.set_intersight_cache',
                    'iocard miss w/filter: %s' % (target_chassis_moids)
                )
            else:
                self.log_handler.debug(
                    'chassis_info.set_intersight_cache',
                    'iocard miss wout filter'
                )

            managed_objects = self.iocard_handler.get_all()
            if managed_objects is None:
                self.log_handler.error(
                    'chassis_info.set_intersight_cache',
                    'iocard failed'
                )
                return

            for chassis_moid in target_chassis_moids:
                chassis_managed_objects = []
                for managed_object in managed_objects:
                    if managed_object['RegisteredDevice']['Moid'] == device_moids[chassis_moid]:
                        chassis_managed_objects.append(
                            managed_object
                        )

                self.cache_handler.set_intersight_cache_entry(
                    'iocard',
                    chassis_managed_objects,
                    subdirectory=chassis_moid
                )

            return

        if key == 'ether_host_port':
            cache_hits = []
            target_moids = []
            target_chassis_moids = []
            for chassis_moid in chassis_moids:
                if cache_ttl is None or not self.cache_handler.is_intersight_cache('ether_host_port', subdirectory=chassis_moid, cache_ttl=cache_ttl):
                    target_moids.append(
                        device_moids[chassis_moid]
                    )
                    target_chassis_moids.append(
                        chassis_moid
                    )
                else:
                    cache_hits.append(
                        chassis_moid
                    )

            if len(cache_hits) > 0:
                self.log_handler.debug(
                    'chassis.set_intersight_cache',
                    'ether host port cache hit: %s' % (cache_hits)
                )

            if len(target_moids) == 0:
                return

            if len(target_moids) < filter_length_threshold:
                moids_list = []
                for moid in target_moids:
                    moids_list.append('\'%s\'' % (moid))
                moids_filter = ', '.join(moids_list)

                self.ether_host_port_handler.set_get_filter(
                    "RegisteredDevice/Moid in (%s)" % (moids_filter)
                )

                self.log_handler.debug(
                    'chassis_info.set_intersight_cache',
                    'ether host port miss w/filter: %s' % (target_chassis_moids)
                )
            else:
                self.log_handler.debug(
                    'chassis_info.set_intersight_cache',
                    'ether host port miss wout filter'
                )

            managed_objects = self.ether_host_port_handler.get_all()
            if managed_objects is None:
                self.log_handler.error(
                    'chassis_info.set_intersight_cache',
                    'ether host port failed'
                )
                return

            for chassis_moid in target_chassis_moids:
                chassis_managed_objects = []
                for managed_object in managed_objects:
                    if managed_object['RegisteredDevice']['Moid'] == device_moids[chassis_moid]:
                        chassis_managed_objects.append(
                            managed_object
                        )

                self.cache_handler.set_intersight_cache_entry(
                    'ether_host_port',
                    chassis_managed_objects,
                    subdirectory=chassis_moid
                )

            return

        if key == 'ether_network_port':
            cache_hits = []
            target_moids = []
            target_chassis_moids = []
            for chassis_moid in chassis_moids:
                if cache_ttl is None or not self.cache_handler.is_intersight_cache('ether_network_port', subdirectory=chassis_moid, cache_ttl=cache_ttl):
                    target_moids.append(
                        device_moids[chassis_moid]
                    )
                    target_chassis_moids.append(
                        chassis_moid
                    )
                else:
                    cache_hits.append(
                        chassis_moid
                    )

            if len(cache_hits) > 0:
                self.log_handler.debug(
                    'chassis.set_intersight_cache',
                    'ether network port cache hit: %s' % (cache_hits)
                )

            if len(target_moids) == 0:
                return

            if len(target_moids) < filter_length_threshold:
                moids_list = []
                for moid in target_moids:
                    moids_list.append('\'%s\'' % (moid))
                moids_filter = ', '.join(moids_list)

                self.ether_network_port_handler.set_get_filter(
                    "RegisteredDevice/Moid in (%s)" % (moids_filter)
                )

                self.log_handler.debug(
                    'chassis_info.set_intersight_cache',
                    'ether network port miss w/filter: %s' % (target_chassis_moids)
                )
            else:
                self.log_handler.debug(
                    'chassis_info.set_intersight_cache',
                    'ether network port miss wout filter'
                )

            managed_objects = self.ether_network_port_handler.get_all()
            if managed_objects is None:
                self.log_handler.error(
                    'chassis_info.set_intersight_cache',
                    'ether network port failed'
                )
                return

            for chassis_moid in target_chassis_moids:
                chassis_managed_objects = []
                for managed_object in managed_objects:
                    if managed_object['RegisteredDevice']['Moid'] == device_moids[chassis_moid]:
                        chassis_managed_objects.append(
                            managed_object
                        )

                self.cache_handler.set_intersight_cache_entry(
                    'ether_network_port',
                    chassis_managed_objects,
                    subdirectory=chassis_moid
                )

            return

        if key == 'ether_physical_port':
            cache_hits = []
            target_moids = []
            target_chassis_moids = []
            for chassis_moid in chassis_moids:
                if cache_ttl is None or not self.cache_handler.is_intersight_cache('ether_physical_port', subdirectory=chassis_moid, cache_ttl=cache_ttl):
                    target_moids.append(
                        device_moids[chassis_moid]
                    )
                    target_chassis_moids.append(
                        chassis_moid
                    )
                else:
                    cache_hits.append(
                        chassis_moid
                    )

            if len(cache_hits) > 0:
                self.log_handler.debug(
                    'chassis.set_intersight_cache',
                    'ether phy port cache hit: %s' % (cache_hits)
                )

            if len(target_moids) == 0:
                return

            if len(target_moids) < filter_length_threshold:
                moids_list = []
                for moid in target_moids:
                    moids_list.append('\'%s\'' % (moid))
                moids_filter = ', '.join(moids_list)

                self.ether_physical_port_handler.set_get_filter(
                    "RegisteredDevice/Moid in (%s)" % (moids_filter)
                )

                self.log_handler.debug(
                    'chassis_info.set_intersight_cache',
                    'ether phy port miss w/filter: %s' % (target_chassis_moids)
                )
            else:
                self.log_handler.debug(
                    'chassis_info.set_intersight_cache',
                    'ether phy port miss wout filter'
                )

            managed_objects = self.ether_physical_port_handler.get_all()
            if managed_objects is None:
                self.log_handler.error(
                    'chassis_info.set_intersight_cache',
                    'ether phy port failed'
                )
                return

            for chassis_moid in target_chassis_moids:
                chassis_managed_objects = []
                for managed_object in managed_objects:
                    if managed_object['RegisteredDevice']['Moid'] == device_moids[chassis_moid]:
                        chassis_managed_objects.append(
                            managed_object
                        )

                self.cache_handler.set_intersight_cache_entry(
                    'ether_physical_port',
                    chassis_managed_objects,
                    subdirectory=chassis_moid
                )

            return

        if key == 'blade':
            cache_hits = []
            target_moids = []
            target_chassis_moids = []
            for chassis_moid in chassis_moids:
                if cache_ttl is None or not self.cache_handler.is_intersight_cache('blade', subdirectory=chassis_moid, cache_ttl=cache_ttl):
                    target_moids.append(
                        device_moids[chassis_moid]
                    )
                    target_chassis_moids.append(
                        chassis_moid
                    )
                else:
                    cache_hits.append(
                        chassis_moid
                    )

            if len(cache_hits) > 0:
                self.log_handler.debug(
                    'chassis.set_intersight_cache',
                    'blade cache hit: %s' % (cache_hits)
                )

            if len(target_moids) == 0:
                return

            if len(target_moids) < filter_length_threshold:
                moids_list = []
                for moid in target_moids:
                    moids_list.append('\'%s\'' % (moid))
                moids_filter = ', '.join(moids_list)

                self.blade_handler.set_get_filter(
                    "RegisteredDevice/Moid in (%s)" % (moids_filter)
                )

                self.log_handler.debug(
                    'chassis_info.set_intersight_cache',
                    'blade miss w/filter: %s' % (target_chassis_moids)
                )
            else:
                self.log_handler.debug(
                    'chassis_info.set_intersight_cache',
                    'blade miss wout filter'
                )

            managed_objects = self.blade_handler.get_all()
            if managed_objects is None:
                self.log_handler.error(
                    'chassis_info.set_intersight_cache',
                    'blade failed'
                )
                return

            for chassis_moid in target_chassis_moids:
                chassis_managed_objects = []
                for managed_object in managed_objects:
                    if managed_object['RegisteredDevice']['Moid'] == device_moids[chassis_moid]:
                        chassis_managed_objects.append(
                            managed_object
                        )

                self.cache_handler.set_intersight_cache_entry(
                    'blade',
                    chassis_managed_objects,
                    subdirectory=chassis_moid
                )

            return

        if key == 'adapter':
            cache_hits = []
            target_moids = []
            target_chassis_moids = []
            for chassis_moid in chassis_moids:
                if cache_ttl is None or not self.cache_handler.is_intersight_cache('adapter', subdirectory=chassis_moid, cache_ttl=cache_ttl):
                    target_moids.append(
                        device_moids[chassis_moid]
                    )
                    target_chassis_moids.append(
                        chassis_moid
                    )
                else:
                    cache_hits.append(
                        chassis_moid
                    )

            if len(cache_hits) > 0:
                self.log_handler.debug(
                    'chassis.set_intersight_cache',
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
                    "RegisteredDevice/Moid in (%s)" % (moids_filter)
                )

                self.log_handler.debug(
                    'chassis_info.set_intersight_cache',
                    'adapter miss w/filter: %s' % (target_chassis_moids)
                )
            else:
                self.log_handler.debug(
                    'chassis_info.set_intersight_cache',
                    'adapter miss wout filter'
                )

            managed_objects = self.adapter_unit_handler.get_all()
            if managed_objects is None:
                self.log_handler.error(
                    'chassis_info.set_intersight_cache',
                    'adapter failed'
                )
                return

            for chassis_moid in target_chassis_moids:
                chassis_managed_objects = []
                for managed_object in managed_objects:
                    if managed_object['RegisteredDevice']['Moid'] == device_moids[chassis_moid]:
                        chassis_managed_objects.append(
                            managed_object
                        )

                self.cache_handler.set_intersight_cache_entry(
                    'adapter',
                    chassis_managed_objects,
                    subdirectory=chassis_moid
                )

            return

        if key == 'interface':
            cache_hits = []
            target_moids = []
            target_chassis_moids = []
            for chassis_moid in chassis_moids:
                if cache_ttl is None or not self.cache_handler.is_intersight_cache('interface', subdirectory=chassis_moid, cache_ttl=cache_ttl):
                    target_moids.append(
                        device_moids[chassis_moid]
                    )
                    target_chassis_moids.append(
                        chassis_moid
                    )
                else:
                    cache_hits.append(
                        chassis_moid
                    )

            if len(cache_hits) > 0:
                self.log_handler.debug(
                    'chassis.set_intersight_cache',
                    'interface cache hit: %s' % (cache_hits)
                )

            if len(target_moids) == 0:
                return

            if len(target_moids) < filter_length_threshold:
                moids_list = []
                for moid in target_moids:
                    moids_list.append('\'%s\'' % (moid))
                moids_filter = ', '.join(moids_list)

                self.adapter_ext_eth_interface_handler.set_get_filter(
                    "RegisteredDevice/Moid in (%s)" % (moids_filter)
                )

                self.log_handler.debug(
                    'chassis_info.set_intersight_cache',
                    'interface miss w/filter: %s' % (target_chassis_moids)
                )
            else:
                self.log_handler.debug(
                    'chassis_info.set_intersight_cache',
                    'interface miss wout filter'
                )

            managed_objects = self.adapter_ext_eth_interface_handler.get_all()
            if managed_objects is None:
                self.log_handler.error(
                    'chassis_info.set_intersight_cache',
                    'interface failed'
                )
                return

            for chassis_moid in target_chassis_moids:
                chassis_managed_objects = []
                for managed_object in managed_objects:
                    if managed_object['RegisteredDevice']['Moid'] == device_moids[chassis_moid]:
                        chassis_managed_objects.append(
                            managed_object
                        )

                self.cache_handler.set_intersight_cache_entry(
                    'interface',
                    chassis_managed_objects,
                    subdirectory=chassis_moid
                )

            return

        if key == 'alarm':
            cache_hits = []
            target_moids = []
            target_chassis_moids = []
            for chassis_moid in chassis_moids:
                if cache_ttl is None or not self.cache_handler.is_intersight_cache('alarm', subdirectory=chassis_moid, cache_ttl=cache_ttl):
                    target_moids.append(
                        device_moids[chassis_moid]
                    )
                    target_chassis_moids.append(
                        chassis_moid
                    )
                else:
                    cache_hits.append(
                        chassis_moid
                    )

            if len(cache_hits) > 0:
                self.log_handler.debug(
                    'chassis.set_intersight_cache',
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
                    'chassis_info.set_intersight_cache',
                    'alarm miss w/filter: %s' % (target_chassis_moids)
                )
            else:
                self.log_handler.debug(
                    'chassis_info.set_intersight_cache',
                    'alarm miss wout filter'
                )

            managed_objects = self.cond_alarm_handler.get_all()
            if managed_objects is None:
                self.log_handler.error(
                    'chassis_info.set_intersight_cache',
                    'alarm failed'
                )
                return

            for chassis_moid in target_chassis_moids:
                chassis_managed_objects = []
                for managed_object in managed_objects:
                    if managed_object['RegisteredDevice']['Moid'] == device_moids[chassis_moid]:
                        chassis_managed_objects.append(
                            managed_object
                        )

                self.cache_handler.set_intersight_cache_entry(
                    'alarm',
                    chassis_managed_objects,
                    subdirectory=chassis_moid
                )

            return

        if key == 'advisory':
            cache_hits = []
            target_moids = []
            target_chassis_moids = []
            for chassis_moid in chassis_moids:
                if cache_ttl is None or not self.cache_handler.is_intersight_cache('advisory', subdirectory=chassis_moid, cache_ttl=cache_ttl):
                    target_moids.append(
                        device_moids[chassis_moid]
                    )
                    target_chassis_moids.append(
                        chassis_moid
                    )
                else:
                    cache_hits.append(
                        chassis_moid
                    )

            if len(cache_hits) > 0:
                self.log_handler.debug(
                    'chassis.set_intersight_cache',
                    'advisory cache hit: %s' % (cache_hits)
                )

            if len(target_moids) == 0:
                return

            if len(target_moids) < filter_length_threshold:
                moids_list = []
                for moid in target_moids:
                    moids_list.append('\'%s\'' % (moid))
                moids_filter = ', '.join(moids_list)

                self.tam_advisory_instance_handler.set_get_filter(
                    "RegisteredDevice/Moid in (%s)" % (moids_filter)
                )

                self.log_handler.debug(
                    'chassis_info.set_intersight_cache',
                    'advisory miss w/filter: %s' % (target_chassis_moids)
                )
            else:
                self.log_handler.debug(
                    'chassis_info.set_intersight_cache',
                    'advisory miss wout filter'
                )

            managed_objects = self.tam_advisory_instance_handler.get_all()
            if managed_objects is None:
                self.log_handler.error(
                    'chassis_info.set_intersight_cache',
                    'advisory failed'
                )
                return

            for chassis_moid in target_chassis_moids:
                chassis_managed_objects = []
                for managed_object in managed_objects:
                    if managed_object['RegisteredDevice']['Moid'] == device_moids[chassis_moid]:
                        chassis_managed_objects.append(
                            managed_object
                        )

                self.cache_handler.set_intersight_cache_entry(
                    'advisory',
                    chassis_managed_objects,
                    subdirectory=chassis_moid
                )

            return

        if key == 'contract':
            cache_hits = []
            target_moids = []
            target_chassis_moids = []
            for chassis_moid in serial:
                if cache_ttl is None or not self.cache_handler.is_intersight_cache('contract', subdirectory=chassis_moid, cache_ttl=cache_ttl):
                    target_moids.append(
                        serial[chassis_moid]
                    )
                    target_chassis_moids.append(
                        chassis_moid
                    )
                else:
                    cache_hits.append(
                        chassis_moid
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

            for chassis_moid in target_chassis_moids:
                chassis_managed_objects = []
                for managed_object in managed_objects:
                    if serial[chassis_moid] == managed_object['DeviceId']:
                        chassis_managed_objects.append(
                            managed_object
                        )

                self.cache_handler.set_intersight_cache_entry(
                    'contract',
                    chassis_managed_objects,
                    subdirectory=chassis_moid
                )

            return

        if key == 'network':
            cache_hits = []
            target_moids = []
            target_chassis_moids = []
            for chassis_moid in chassis_moids:
                if cache_ttl is None or not self.cache_handler.is_intersight_cache('network', subdirectory=chassis_moid, cache_ttl=cache_ttl):
                    target_moids.append(
                        device_moids[chassis_moid]
                    )
                    target_chassis_moids.append(
                        chassis_moid
                    )
                else:
                    cache_hits.append(
                        chassis_moid
                    )

            if len(cache_hits) > 0:
                self.log_handler.debug(
                    'chassis.set_intersight_cache',
                    'network cache hit: %s' % (cache_hits)
                )

            if len(target_moids) == 0:
                return

            if len(target_moids) < filter_length_threshold:
                moids_list = []
                for moid in target_moids:
                    moids_list.append('\'%s\'' % (moid))
                moids_filter = ', '.join(moids_list)

                self.network_element_summary_handler.set_get_filter(
                    "RegisteredDevice/Moid in (%s)" % (moids_filter)
                )

                self.log_handler.debug(
                    'chassis_info.set_intersight_cache',
                    'network miss w/filter: %s' % (target_chassis_moids)
                )
            else:
                self.log_handler.debug(
                    'chassis_info.set_intersight_cache',
                    'network miss wout filter'
                )

            managed_objects = self.network_element_summary_handler.get_all()
            if managed_objects is None:
                self.log_handler.error(
                    'chassis_info.set_intersight_cache',
                    'network failed'
                )
                return

            for chassis_moid in target_chassis_moids:
                chassis_managed_objects = []
                for managed_object in managed_objects:
                    if managed_object['RegisteredDevice']['Moid'] == device_moids[chassis_moid]:
                        chassis_managed_objects.append(
                            managed_object
                        )

                self.cache_handler.set_intersight_cache_entry(
                    'network',
                    chassis_managed_objects,
                    subdirectory=chassis_moid
                )

            return

        if key == 'profile':
            cache_hits = []
            target_moids = []
            target_chassis_moids = []
            for chassis_moid in chassis_moids:
                if cache_ttl is None or not self.cache_handler.is_intersight_cache('profile', subdirectory=chassis_moid, cache_ttl=cache_ttl):
                    target_moids.append(
                        chassis_moid
                    )
                    target_chassis_moids.append(
                        chassis_moid
                    )
                else:
                    cache_hits.append(
                        chassis_moid
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

                self.chassis_profile_handler.set_get_filter(
                    "AssignedChassis/Moid in (%s)" % (moids_filter)
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

            managed_objects = self.chassis_profile_handler.get_all()
            if managed_objects is None:
                self.log_handler.error(
                    'compute.set_intersight_cache',
                    'profile failed'
                )
                return

            for chassis_moid in target_chassis_moids:
                chassis_managed_objects = []
                for managed_object in managed_objects:
                    if 'AssignedChassis' in managed_object and managed_object['AssignedChassis'] is not None:
                        if chassis_moid == managed_object['AssignedChassis']['Moid']:
                            chassis_managed_objects.append(
                                managed_object
                            )

                self.cache_handler.set_intersight_cache_entry(
                    'profile',
                    chassis_managed_objects,
                    subdirectory=chassis_moid
                )

            return

        self.log_handler.error(
            'set_intersight_cache',
            'Unsupported key: %s' % (key)
        )
        return

    def set_cache(self, chassiz_mo, cache_settings, cache_ttl, parallel=False):
        start_time = int(time.time() * 1000)
        self.log_handler.debug(
            'chassis.set_cache',
            'Start cache population'
        )

        moids = []
        device_moids = {}
        serial = {}

        for chassis_mo in chassiz_mo:
            moids.append(chassis_mo['Moid'])
            device_moids[chassis_mo['Moid']] = chassis_mo['DeviceMoId']
            serial[chassis_mo['Moid']] = chassis_mo['Serial']

        keys = []
        keys.append('fan_control')
        keys.append('fan_module')
        keys.append('fan')

        keys.append('psu_control')
        keys.append('power_control')
        keys.append('psu')

        keys.append('iocard')
        keys.append('ether_host_port')
        keys.append('ether_network_port')
        keys.append('ether_physical_port')

        keys.append('blade')
        keys.append('adapter')
        keys.append('interface')
        keys.append('alarm')
        keys.append('advisory')
        keys.append('contract')
        keys.append('network')
        keys.append('profile')

        if len(keys) > 0:
            for key in keys:
                self.set_intersight_cache(
                    key,
                    moids,
                    device_moids,
                    serial,
                    cache_ttl=cache_ttl
                )

        duration = int(time.time() * 1000) - start_time
        self.log_handler.debug(
            'chassis.set_cache',
            'Cache populated in %s ms' % (duration)
        )
