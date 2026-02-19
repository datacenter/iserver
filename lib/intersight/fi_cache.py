import time


class FiCache():
    def __init__(self):
        pass

    def set_intersight_cache(self, key, fi_moids, device_moids, serial, filter_length_threshold=20, cache_ttl=None):
        if key == 'summary':
            cache_hits = []
            target_moids = []
            for fi_moid in fi_moids:
                if cache_ttl is None or not self.cache_handler.is_intersight_cache('summary', subdirectory=fi_moid, cache_ttl=cache_ttl):
                    target_moids.append(
                        fi_moid
                    )
                else:
                    cache_hits.append(
                        fi_moid
                    )

            if len(cache_hits) > 0:
                self.log_handler.debug(
                    'fi.set_intersight_cache',
                    'summary cache hit: %s' % (cache_hits)
                )

            if len(target_moids) == 0:
                return

            chunk_id = 0
            fi_managed_objects = {}
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
                self.network_element_summary_handler.set_get_filter(
                    "Moid in (%s)" % (moids_filter)
                )

                self.log_handler.debug(
                    'fi_info.set_intersight_cache',
                    'summary miss w/filter: %s' % (chunk_target_moids)
                )

                managed_objects = self.network_element_summary_handler.get_all()
                if managed_objects is None:
                    self.log_handler.error(
                        'fi_info.set_intersight_cache',
                        'summary failed'
                    )
                    return

                for fi_moid in target_moids:
                    for managed_object in managed_objects:
                        if managed_object['Moid'] == fi_moid:
                            fi_managed_objects[fi_moid] = managed_object

            for target_moid in target_moids:
                self.cache_handler.set_intersight_cache_entry(
                    'summary',
                    fi_managed_objects[target_moid],
                    subdirectory=target_moid
                )

            return

        if key == 'eth':
            cache_hits = []
            target_moids = []
            target_fi_moids = []
            for fi_moid in fi_moids:
                if target_fi_moids is None or not self.cache_handler.is_intersight_cache('eth', subdirectory=fi_moid, cache_ttl=cache_ttl):
                    target_fi_moids.append(
                        fi_moid
                    )
                    target_moids.append(
                        device_moids[fi_moid]
                    )
                else:
                    cache_hits.append(
                        fi_moid
                    )

            if len(cache_hits) > 0:
                self.log_handler.debug(
                    'fi.set_intersight_cache',
                    'eth cache hit: %s' % (cache_hits)
                )

            if len(target_moids) == 0:
                return

            fi_managed_objects = {}
            for target_moid in target_fi_moids:
                fi_managed_objects[target_moid] = []

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

                self.ethernet_physical_port_handler.set_get_expand('AcknowledgedPeerInterface($expand=Ancestors($expand=RegisteredDevice($select=DeviceHostname)))')

                self.ethernet_physical_port_handler.set_get_filter(
                    "DeviceMoId in (%s)" % (moids_filter)
                )

                self.log_handler.debug(
                    'fi_info.set_intersight_cache',
                    'eth miss w/filter: %s' % (chunk_target_moids)
                )

                managed_objects = self.ethernet_physical_port_handler.get_all()
                if managed_objects is None:
                    self.log_handler.error(
                        'fi_info.set_intersight_cache',
                        'summary failed'
                    )
                    return

                for fi_moid in fi_managed_objects:
                    for managed_object in managed_objects:
                        if managed_object['DeviceMoId'] == device_moids[fi_moid]:
                            for ancestor_mo in managed_object['Ancestors']:
                                if ancestor_mo['ObjectType'] == 'network.Element':
                                    if ancestor_mo['Moid'] == fi_moid:
                                        fi_managed_objects[fi_moid].append(
                                            managed_object
                                        )


            for target_moid in target_fi_moids:
                self.cache_handler.set_intersight_cache_entry(
                    'eth',
                    fi_managed_objects[target_moid],
                    subdirectory=target_moid
                )

            return

        if key == 'pc':
            cache_hits = []
            target_moids = []
            target_fi_moids = []
            for fi_moid in fi_moids:
                if target_fi_moids is None or not self.cache_handler.is_intersight_cache('pc', subdirectory=fi_moid, cache_ttl=cache_ttl):
                    target_fi_moids.append(
                        fi_moid
                    )
                    target_moids.append(
                        device_moids[fi_moid]
                    )
                else:
                    cache_hits.append(
                        fi_moid
                    )

            if len(cache_hits) > 0:
                self.log_handler.debug(
                    'fi.set_intersight_cache',
                    'pc cache hit: %s' % (cache_hits)
                )

            if len(target_moids) == 0:
                return

            fi_managed_objects = {}
            for target_moid in target_fi_moids:
                fi_managed_objects[target_moid] = []

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

                self.ethernet_port_channel_handler.set_get_filter(
                    "DeviceMoId in (%s)" % (moids_filter)
                )

                self.log_handler.debug(
                    'fi_info.set_intersight_cache',
                    'pc miss w/filter: %s' % (chunk_target_moids)
                )

                managed_objects = self.ethernet_port_channel_handler.get_all()
                if managed_objects is None:
                    self.log_handler.error(
                        'fi_info.set_intersight_cache',
                        'pc failed'
                    )
                    return

                for fi_moid in fi_managed_objects:
                    for managed_object in managed_objects:
                        if managed_object['DeviceMoId'] == device_moids[fi_moid]:
                            for ancestor_mo in managed_object['Ancestors']:
                                if ancestor_mo['ObjectType'] == 'network.Element':
                                    if ancestor_mo['Moid'] == fi_moid:
                                        fi_managed_objects[fi_moid].append(
                                            managed_object
                                        )


            for target_moid in target_fi_moids:
                self.cache_handler.set_intersight_cache_entry(
                    'pc',
                    fi_managed_objects[target_moid],
                    subdirectory=target_moid
                )

            return

        self.log_handler.error(
            'fi.set_intersight_cache',
            'Unsupported key: %s' % (key)
        )
        return

    def set_cache(self, fis_mo, cache_settings, cache_ttl, ctx=None):
        start_time = int(time.time() * 1000)
        self.log_handler.debug(
            'fi.set_cache',
            'Start cache population'
        )

        moids = []
        device_moids = {}
        serial = {}

        for fi_mo in fis_mo:
            moids.append(fi_mo['Moid'])
            device_moids[fi_mo['Moid']] = fi_mo['DeviceMoId']
            serial[fi_mo['Moid']] = fi_mo['Serial']

        keys = []

        if 'summary' in cache_settings and cache_settings['summary']:
            keys.append('summary')

        if 'eth' in cache_settings and cache_settings['eth']:
            keys.append('eth')

        if 'pc' in cache_settings and cache_settings['pc']:
            keys.append('pc')

        if len(keys) > 0:
            for key in keys:
                if ctx is not None:
                    ctx.my_output.debug('- %s' % (key))

                self.set_intersight_cache(
                    key,
                    moids,
                    device_moids,
                    serial,
                    cache_ttl=cache_ttl
                )

        duration = int(time.time() * 1000) - start_time
        self.log_handler.debug(
            'fi.set_cache',
            'Cache populated in %s ms' % (duration)
        )

