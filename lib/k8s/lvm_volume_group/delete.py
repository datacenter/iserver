import json


class K8sLvmVolumeGroupDelete():
    def __init__(self):
        pass

    def remove_lvm_volume_group_finalizers(self, my_output=None):
        groups = self.get_lvm_volume_groups(return_mo=True, cache_enabled=False)
        if groups is None:
            return False
        
        for group in groups:
            if 'finalizers' not in group['metadata']:
                continue

            if my_output is not None:
                my_output.default('Remove lvm volume group finalizers', underline=True, before_newline=True)
                my_output.default('- group: %s/%s' % (group['metadata']['namespace'], group['metadata']['name']))
                my_output.default(
                    json.dumps(group['metadata']['finalizers'], indent=4), 
                    wrap='~~~'
                )

            del group['metadata']['finalizers']
            success = self.replace_resource(group)
            if not success:
                if my_output is not None:
                    my_output.default('Replace resource %s' % (my_output.add_color('failed', 'Red')))
                return False

            if my_output is not None:
                my_output.default('Finalizers %s' % (my_output.add_color('removed', 'Green')))

        return True