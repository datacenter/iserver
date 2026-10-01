import json


class K8sPackageExample():
    def __init__(self):
        pass

    def get_package_channel(self, package_name, catalog, channel_name, cache_enabled=True):
        try:
            package_info = self.get_package_catalog(package_name, catalog, cache_enabled=cache_enabled)
            for channel in package_info['status']['channels']:
                if channel['name'] == channel_name:
                    return channel
        except BaseException:
            pass

        return None
    
    def get_package_channel_example(self, package_name, catalog, channel_name, example_kind, examples='currentCSVDesc:annotations:alm-examples', cache_enabled=True):
        channel = self.get_package_channel(package_name, catalog, channel_name, cache_enabled=cache_enabled)
        if channel is None:
            self.log.error(
                'get_package_channel_example',
                'package %s channel %s not found' % (package_name, channel_name)
            )
            return None
        
        examples = self.get(channel, examples)
        if examples is None:
            self.log.error(
                'get_package_channel_example',
                '%s not found in channel %s' % (examples, channel_name)
            )
            return None
        
        example = None
        try:
            for item in json.loads(examples):
                if item['kind'] == example_kind:
                    example = item
        except BaseException:
            self.log.error(
                'get_package_channel_example',
                'Examples json parse failed'
            )

        return example