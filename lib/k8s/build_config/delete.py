from menu.common import get_confirmation


class K8sBuildConfigDelete():
    def __init__(self):
        pass

    def delete_build_configs(self, object_filter=None, my_output=None, wait=True, confirmation=False):
        if my_output is None:
            confirmation = False

        if my_output is not None:
            my_output.default('Delete Build Configs', before_newline=True, underline=True)

        streams = self.get_build_configs(
            object_filter=object_filter,
            cache_enabled=False
        )
        if streams is None:
            if my_output is not None:
                my_output.error('Failed to get build configs')
            return False

        if len(streams) == 0:
            if my_output is not None:
                my_output.default('- no build config found')
            return True

        if confirmation:
            for stream in streams:
                if my_output is not None:
                    my_output.default('- %s' % (stream['namespace_name']))

            if not get_confirmation():
                return False

        for stream in streams:
            if my_output is not None:
                my_output.default('- %s' % (stream['namespace_name']))

            success = self.delete_build_config_mo(
                stream['namespace'],
                stream['name']
            )
            if not success:
                if my_output is not None:
                    my_output.error('build config delete failed')

                return False

            if wait:
                if my_output is not None:
                    my_output.default('- wait for no build config')

                if not self.wait_no_build_config(stream['namespace'], stream['name']):
                    if my_output is not None:
                        my_output.error('Time out')
                    return False
            
        return True

    def delete_build_config(self, namespace, name, my_output=None, wait=True, confirmation=False):
        if my_output is None:
            confirmation = False

        if my_output is not None:
            my_output.default('Delete Build Config', before_newline=True, underline=True)
            my_output.default('- namespace: %s' % (namespace))
            my_output.default('- name: %s' % (name))

        stream = self.get_build_config(
            namespace,
            name,
            cache_enabled=False
        )
        if stream is None:
            if my_output is not None:
                my_output.default('- already deleted')
            return True

        if confirmation:
            if not get_confirmation():
                return False
                    
        success = self.delete_build_config_mo(
            stream['namespace'],
            stream['name']
        )
        if not success:
            if my_output is not None:
                my_output.error('build config delete failed')

            return False

        if wait:
            if my_output is not None:
                my_output.default('- wait for no build config')

            if not self.wait_no_build_config(stream['namespace'], stream['name']):
                if my_output is not None:
                    my_output.error('Time out')
                return False
            
        return True
    