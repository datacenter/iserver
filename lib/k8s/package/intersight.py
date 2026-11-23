import json


class K8sPackageIntersight():
    def __init__(self):
        pass

    def get_intersight_package(self, cache_enabled=True):
        object_filter = []
        object_filter.append('catalog:certified-operators')
        object_filter.append('name:cisco-intersight')

        package = self.get_packages(
            object_filter=object_filter,
            return_mo=True,
            cache_enabled=cache_enabled
        )

        if package is None:
            self.log.error(
                'get_intersight_package',
                'failed to get packages'
            )
            return None
        
        if len(package) != 1:
            self.log.error(
                'get_intersight_package',
                'Unexpected package count: %s' % (len(package))
            )
            return None
        
        return package[0]

    def get_intersight_package_channels(self, cache_enabled=True):
        package = self.get_intersight_package(cache_enabled=cache_enabled)
        if package is None:
            return None
        return self.get(package, 'status:channels')

    def get_intersight_package_channel_default_name(self, cache_enabled=True):
        intersight_package = self.get_intersight_package(cache_enabled=cache_enabled)
        if intersight_package is None:
            return None
        
        channel_name = self.get(intersight_package, 'status:defaultChannel')
        if channel_name is None:
            self.log.error(
                'get_intersight_package_channel_default_name',
                'No status:defaultChannel in package'
            )
            return None
        
        return channel_name
    
    def get_intersight_package_channel(self, channel_name, cache_enabled=True):
        if channel_name == '__default__':
            channel_name = self.get_intersight_package_channel_default_name(cache_enabled=cache_enabled)
            if channel_name is None:
                return None
            
        channels = self.get_intersight_package_channels(cache_enabled=cache_enabled)
        if channels is None:
            self.log.error(
                'get_intersight_package_channel',
                'No channels in package'
            )
            return None
        
        for channel in channels:
            if channel['name'] == channel_name:
                return channel
        
        return None

    def get_intersight_package_channel_example(self, channel_name, example_kind, cache_enabled=True):
        channel = self.get_intersight_package_channel(channel_name, cache_enabled=cache_enabled)
        if channel is None:
            self.log.error(
                'get_intersight_package_channel_example',
                'channel not found: %s' % (channel_name)
            )
            return None
        
        examples = self.get(channel, 'currentCSVDesc:annotations:alm-examples')
        if examples is None:
            self.log.error(
                'get_intersight_package_channel_example',
                'currentCSVDesc:annotations:alm-examples not found in channel'
            )
            return None
        
        example = None
        try:
            for item in json.loads(examples):
                if item['kind'] == example_kind:
                    example = item
        except BaseException:
            self.log.error(
                'get_intersight_package_channel_example',
                'Examples json parse failed'
            )

        if example is not None:
            return example
        
        initialization = self.get(channel, 'currentCSVDesc:annotations:operatorframework.io/initialization-resource')
        if initialization is not None:
            try:
                example = json.loads(initialization)
            except BaseException:
                pass
            
        return example
    