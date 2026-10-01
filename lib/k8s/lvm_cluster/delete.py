import json


class K8sLvmClusterDelete():
    def __init__(self):
        pass

    def remove_lvm_cluster_finalizers(self, my_output=None):
        if my_output is not None:
            my_output.default('Remove lvm cluster finalizers', underline=True, before_newline=True)

        cluster_mo = self.get_lvm_cluster(return_mo=True, cache_enabled=False)
        if cluster_mo is None:
            if my_output is not None:
                my_output.default('LVM cluster %s' % (my_output.add_color('not fouhd', 'Red')))

            return False
        
        if 'finalizers' not in cluster_mo['metadata']:
            if my_output is not None:
                my_output.default('Finalizers found in lvm cluster object')
            return True

        if my_output is not None:
            my_output.default(
                json.dumps(cluster_mo['metadata']['finalizers'], indent=4), 
                wrap='~~~'
            )

        del cluster_mo['metadata']['finalizers']
        success = self.replace_resource(cluster_mo)
        if not success:
            if my_output is not None:
                my_output.default('Replace resource %s' % (my_output.add_color('failed', 'Red')))
        else:
            if my_output is not None:
                my_output.default('Finalizers %s' % (my_output.add_color('removed', 'Green')))

        return success
    
    def delete_lvm_cluster(self, my_output=None, wait=True):
        if my_output is not None:
            my_output.default('Delete LVM Cluster', before_newline=True, underline=True)

        info = self.get_lvm_cluster(cache_enabled=False)
        if info is None:
            if my_output is not None:
                my_output.default('- already deleted')

        if info is not None:
            if my_output is not None:
                my_output.default('- namespace: %s' % (info['namespace']))
                my_output.default('- name: %s' % (info['name']))
            
            if not self.delete_lvm_cluster_mo(info['namespace'], info['name']):
                if my_output is not None:
                    my_output.error('Failed to delete lvm cluster')
                return False

            if not wait:
                return True
            
            if my_output is not None:
                my_output.default('- wait for no lvm cluster [timeout:300s]')

            if self.wait_no_lvm_cluster():
                return True
            
            if my_output is not None:
                my_output.default('LVM Cluster instance still there... checking finalizers...')

            if not self.remove_lvm_cluster_finalizers(my_output=my_output):
                if my_output is not None:
                    my_output.error('Finalizers update failed')
                return False
            
            if my_output is not None:
                my_output.default('Finalizers removed')
                my_output.default('Wait for no lvm cluster [timeout:60s]...')

            success = self.wait_no_lvm_cluster(max_time=60)
            if not success:
                if my_output is not None:
                    my_output.error('Giving up')
                return False

        success = self.remove_lvm_volume_group_finalizers(my_output=my_output)
        if not success:
            return False
        
        success = self.remove_lvm_volume_group_node_status_finalizers(my_output=my_output)
        if not success:
            return False
        
        return True