class K8sSubscriptionDelete():
    def __init__(self):
        pass

    def delete_subscription(self, namespace, name, my_output=None, wait=True):
        if my_output is not None:
            my_output.default('Delete Subscription', before_newline=True, underline=True)
            my_output.default('- subscription: %s/%s' % (namespace, name))        

        subscription_info = self.get_subscription_by_package(
            name,
            return_mo=False,
            cache_enabled=False
        )
        if subscription_info is None:
            if my_output is not None:
                my_output.default('- already deleted')
            return True
        
        if my_output is not None:
            my_output.default('- checking cluster service version...')

        csv_info = self.get_cluster_service_version(
            subscription_info['namespace'],
            subscription_info['installed_csv'],
            return_mo=False,
            cache_enabled=False
        )
        if csv_info is not None:
            if my_output is not None:
                my_output.default('- csv found and will be deleted: %s/%s' % (subscription_info['namespace'], subscription_info['installed_csv']))
        if csv_info is None:
            if my_output is not None:
                my_output.default('- [WARNING] csv not found: %s/%s' % (subscription_info['namespace'], subscription_info['installed_csv']))

        success = self.delete_subscription_mo(
            subscription_info['namespace'], 
            subscription_info['name']
        )
        if not success:
            if my_output is not None:
                my_output.error('REST API failed')
            return False

        if wait:        
            if my_output is not None:
                my_output.default('- wait for no subscription')

            if not self.wait_no_subscription(subscription_info['namespace'], subscription_info['name']):
                if my_output is not None:
                    my_output.error('Timed out')
                return False

        if my_output is not None:
            my_output.default('- check cluster service version: %s/%s' % (subscription_info['namespace'], subscription_info['installed_csv']))

        if self.is_cluster_service_version(subscription_info['namespace'], subscription_info['installed_csv'], cache_enabled=False):
            success = self.delete_cluster_service_version_mo(
                subscription_info['namespace'], 
                subscription_info['installed_csv']
            )
            if not success:
                if my_output is not None:
                    my_output.error('Delete REST API failed')

                return False

            if wait:        
                if my_output is not None:
                    my_output.default('- wait for no csv')

                if not self.wait_no_cluster_service_version(subscription_info['namespace'], subscription_info['name']):
                    if my_output is not None:
                        my_output.error('Timed out')
                    return False

        return True
