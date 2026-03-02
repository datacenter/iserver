import time


class K8sSubscriptionLocalStorage():
    def __init__(self):
        pass

    def check_local_storage_subscription(self, name, my_output=None, check_ready=True, before_newline=True):
        if my_output is not None:
            my_output.default('Local Storage Operator Subscription', underline=True, before_newline=before_newline)

        subscription = self.get_subscription_by_package(
            name,
            return_mo=False,
            cache_enabled=False
        )
        if subscription is None:
            if my_output is not None:
                my_output.default('Operator %s %s' % (name, my_output.add_color('not found', 'Red')))

            return False
        
        if my_output is not None:
            my_output.default('- subscription: %s' % (subscription['namespace_name']))
            my_output.default('- package: %s' % (name))
            my_output.default('- csv: %s' % (subscription['installed_csv']))

        csv = self.get_cluster_service_version_optimized(
            subscription['namespace'],
            subscription['installed_csv'],
            return_mo=False,
            cache_enabled=False
        )
        if csv is None:
            if my_output is not None:
                my_output.error('Cluster service version not found: %s/%s' % (subscription['namespace'], subscription['installed_csv']))
            return False

        if check_ready:
            return self.is_subscription_local_storage_ready(my_output=my_output)
        
        return True    

    def create_local_storage_subscription(self, namespace, name, channel, confirmation=False, my_output=None, wait=True):
        success = self.create_subscription(
            namespace, 
            name, 
            'Automatic', 
            name, 
            'redhat-operators', 
            'openshift-marketplace', 
            channel=channel,
            confirmation=confirmation, 
            my_output=my_output, 
            wait=wait
        )
        if not success:
            return False
        
        if wait:
            success = self.wait_subscription_local_storage_ready(my_output=my_output)
            if not success:
                return False
        
        return True
    
    def delete_local_storage_subscription(self, namespace, name, my_output=None, wait=True):
        success = self.delete_subscription(
            namespace, 
            name, 
            my_output=my_output, 
            wait=wait
        )        
        if not success:
            return False
        
        if wait:
            success = self.wait_no_subscription_local_storage(my_output=my_output)
            if not success:
                return False

            # or check if pods are not yet there... but normally it takes few seconds for them to disappear
            time.sleep(5)

        return True

    def is_subscription_local_storage_ready(self, my_output=None):
        ready = True
        if my_output is not None:
            my_output.default('Local Storage Operator Resources', before_newline=True, underline=True)

        deployments = [
            {'namespace': 'openshift-local-storage', 'name': 'local-storage-operator'}
        ]

        for deployment in deployments:
            if self.is_deployment_ready(deployment['namespace'], deployment['name']):
                if my_output is not None:
                    my_output.default(
                        '- deployment %s/%s %s' % (
                            deployment['namespace'], 
                            deployment['name'],
                            my_output.add_color('ready', 'Green')
                        )
                    )
            else:
                if my_output is not None:
                    my_output.default(
                        '- deployment %s/%s %s' % (
                            deployment['namespace'], 
                            deployment['name'],
                            my_output.add_color('not ready', 'Red')
                        )
                    )
                ready = False

        return ready

    def wait_subscription_local_storage_ready(self, my_output=None):
        deployments = [
            {'namespace': 'openshift-local-storage', 'name': 'local-storage-operator'}
        ]
        success = self.wait_deployments_ready_state(deployments, my_output=my_output, optional=False)
        if not success:
            return False

        return True

    def wait_no_subscription_local_storage(self, my_output=None):
        deployments = [
            {'namespace': 'openshift-local-storage', 'name': 'local-storage-operator'}
        ]
        success = self.wait_no_deployments(deployments, my_output=my_output, optional=False)
        if not success:
            return False

        return True
    

    # delete lvs (can take time)

    # what about disks?

    # nbd0    43:0    0     0B  0 disk
    # nbd1    43:32   0     0B  0 disk
    # nbd2    43:64   0     0B  0 disk
    # nbd3    43:96   0     0B  0 disk
    # nbd4    43:128  0     0B  0 disk
    # nbd5    43:160  0     0B  0 disk
    # nbd6    43:192  0     0B  0 disk
    # nbd7    43:224  0     0B  0 disk
    # nbd8    43:256  0     0B  0 disk
    # nbd9    43:288  0     0B  0 disk
    # nbd10   43:320  0     0B  0 disk
    # nbd11   43:352  0     0B  0 disk
    # nbd12   43:384  0     0B  0 disk
    # nbd13   43:416  0     0B  0 disk
    # nbd14   43:448  0     0B  0 disk
    # nbd15   43:480  0     0B  0 disk 

    # reload solved the problem...