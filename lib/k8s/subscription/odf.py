import time


class K8sSubscriptionOdf():
    def __init__(self):
        self.subscription_odf_deployment = [
            {'namespace': 'openshift-storage', 'name': 'ceph-csi-controller-manager'},
            {'namespace': 'openshift-storage', 'name': 'csi-addons-controller-manager'},
            {'namespace': 'openshift-storage', 'name': 'noobaa-operator'},
            {'namespace': 'openshift-storage', 'name': 'ocs-client-operator-console'},
            {'namespace': 'openshift-storage', 'name': 'ocs-client-operator-controller-manager'},
            {'namespace': 'openshift-storage', 'name': 'ocs-operator'},
            {'namespace': 'openshift-storage', 'name': 'odf-console'},
            {'namespace': 'openshift-storage', 'name': 'odf-operator-controller-manager'},
            {'namespace': 'openshift-storage', 'name': 'prometheus-operator'},
            {'namespace': 'openshift-storage', 'name': 'rook-ceph-operator'},
            {'namespace': 'openshift-storage', 'name': 'ux-backend-server'}
        ]

    def is_odf_subscription(self, namespace, name, cache_enabled=True):
        return self.is_subscription(namespace, name, cache_enabled=cache_enabled)

    def check_odf_subscription(self, name, my_output=None, check_ready=True, before_newline=True):
        if my_output is not None:
            my_output.default('OpenShift Data Foundation (ODF) Subscription', underline=True, before_newline=before_newline)

        subscription = self.get_subscription_by_package(
            name,
            return_mo=False,
            cache_enabled=False
        )
        if subscription is None:
            if my_output is not None:
                my_output.error('Operator %s %s' % (name, my_output.add_color('not found', 'Red')))
            return False
        
        if my_output is not None:
            my_output.default('- subscription: %s' % (subscription['namespace_name']))
            my_output.default('- package: %s' % (name))
            my_output.default('- csv: %s' % (subscription['installed_csv']))

        csv = self.get_cluster_service_version(
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
            return self.is_subscription_odf_ready(my_output=my_output)
        
        return True    

    def create_odf_subscription(self, namespace, name, channel, confirmation=False, my_output=None, wait=True):
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
            success = self.wait_subscription_odf_ready(my_output=my_output)
            if not success:
                return False
        
        return True
    
    def delete_odf_subscription(self, namespace, name, my_output=None, wait=True):
        success = self.delete_subscription(
            namespace, 
            name, 
            my_output=my_output, 
            wait=wait
        )        
        if not success:
            return False
        
        if wait:
            success = self.wait_no_subscription_odf(my_output=my_output)
            if not success:
                return False

            # or check if pods are not yet there... but normally it takes few seconds for them to disappear
            time.sleep(5)

        return True

    def is_subscription_odf_ready(self, my_output=None):
        ready = True
        if my_output is not None:
            my_output.default('OpenShift Data Foundation (ODF) Resources', before_newline=True, underline=True)

        for deployment in self.subscription_odf_deployment:
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
                ready = False
                if my_output is not None:
                    my_output.default(
                        '- deployment %s/%s %s' % (
                            deployment['namespace'], 
                            deployment['name'],
                            my_output.add_color('not ready', 'Red')
                        )
                    )
                
        return ready
    
    def wait_subscription_odf_ready(self, my_output=None):
        success = self.wait_deployments_ready_state(
            self.subscription_odf_deployment, 
            my_output=my_output, 
            optional=False, 
            allow_zero_replicas=True
        )
        if not success:
            return False

        return True

    def wait_no_subscription_odf(self, my_output=None):
        success = self.wait_no_deployments(
            self.subscription_odf_deployment, 
            my_output=my_output, 
            optional=False
        )
        if not success:
            return False

        return True
