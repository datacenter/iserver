class K8sSubscriptionCnv():
    def __init__(self):
        self.subscription_cnv_resources = [
            {'type': 'deployment', 'namespace': 'openshift-cnv', 'name': 'aaq-operator'},
            {'type': 'deployment', 'namespace': 'openshift-cnv', 'name': 'cdi-operator'},
            {'type': 'deployment', 'namespace': 'openshift-cnv', 'name': 'cluster-network-addons-operator'},
            {'type': 'deployment', 'namespace': 'openshift-cnv', 'name': 'hco-operator'},
            {'type': 'deployment', 'namespace': 'openshift-cnv', 'name': 'hco-webhook'},
            {'type': 'deployment', 'namespace': 'openshift-cnv', 'name': 'hostpath-provisioner-operator'},
            {'type': 'deployment', 'namespace': 'openshift-cnv', 'name': 'hyperconverged-cluster-cli-download'},
            {'type': 'deployment', 'namespace': 'openshift-cnv', 'name': 'ssp-operator'},
            {'type': 'deployment', 'namespace': 'openshift-cnv', 'name': 'virt-operator'}
        ]

        self.hyperconverged_resources = [
            {'type': 'deployment', 'namespace': 'openshift-cnv', 'name': 'cdi-apiserver'},
            {'type': 'deployment', 'namespace': 'openshift-cnv', 'name': 'cdi-deployment'},
            {'type': 'deployment', 'namespace': 'openshift-cnv', 'name': 'cdi-uploadproxy'},
            {'type': 'deployment', 'namespace': 'openshift-cnv', 'name': 'kubemacpool-cert-manager'},
            {'type': 'deployment', 'namespace': 'openshift-cnv', 'name': 'kubemacpool-mac-controller-manager'},
            {'type': 'deployment', 'namespace': 'openshift-cnv', 'name': 'kubevirt-apiserver-proxy'},
            {'type': 'deployment', 'namespace': 'openshift-cnv', 'name': 'kubevirt-console-plugin'},
            {'type': 'deployment', 'namespace': 'openshift-cnv', 'name': 'kubevirt-ipam-controller-manager'},
            {'type': 'deployment', 'namespace': 'openshift-cnv', 'name': 'virt-api'},
            {'type': 'deployment', 'namespace': 'openshift-cnv', 'name': 'virt-controller'},
            {'type': 'deployment', 'namespace': 'openshift-cnv', 'name': 'virt-exportproxy'},
            {'type': 'deployment', 'namespace': 'openshift-cnv', 'name': 'virt-template-validator'},
            {'type': 'daemonset', 'namespace': 'openshift-cnv', 'name': 'bridge-marker'},
            {'type': 'daemonset', 'namespace': 'openshift-cnv', 'name': 'kube-cni-linux-bridge-plugin'},
            {'type': 'daemonset', 'namespace': 'openshift-cnv', 'name': 'passt-binding-cni', 'optional': True},
            {'type': 'daemonset', 'namespace': 'openshift-cnv', 'name': 'virt-handler'}
        ]

    def is_cnv_subscription(self, namespace, name, cache_enabled=True):
        return self.is_subscription(namespace, name, cache_enabled=cache_enabled)
    
    def create_cnv_subscription(self, namespace, name, channel, confirmation=False, my_output=None, wait=True):
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
            success = self.wait_subscription_cnv_ready(my_output=my_output)
            if not success:
                return False
        
        return True

    def delete_cnv_subscription(self, namespace, name, my_output=None, wait=True):
        resources = self.get_subscription_resources(
            self.subscription_cnv_resources + self.hyperconverged_resources,
            cache_enabled=False
        )

        success = self.delete_subscription(
            namespace, 
            name, 
            my_output=my_output, 
            wait=wait
        )        
        if not success:
            return False
        
        if not wait:
            return True
        
        success = self.wait_no_subscription_resources('cnv', resources, my_output=my_output)
        if not success:
            return False
        
        return True

    def is_instance_cnv_ready(self, my_output=None, details=False, break_on_error=False, cache_enabled=False):
        resources = self.hyperconverged_resources
        return self.is_subscription_ready('cnv', resources, my_output=my_output, details=details, break_on_error=break_on_error, cache_enabled=cache_enabled)

    def is_subscription_cnv_ready(self, with_instance=False, my_output=None, details=False, break_on_error=False, cache_enabled=False):
        resources = self.subscription_cnv_resources
        if with_instance:
            resources.extend(self.hyperconverged_resources)

        return self.is_subscription_ready('cnv', resources, my_output=my_output, details=details, break_on_error=break_on_error, cache_enabled=cache_enabled)
        
    def wait_subscription_cnv_ready(self, with_instance=False, my_output=None):
        resources = self.subscription_cnv_resources
        if with_instance:
            resources.extend(self.hyperconverged_resources)

        return self.wait_subscription_resources('cnv', resources, my_output=my_output)

    def wait_instance_cnv_ready(self, my_output=None):
        resources = self.hyperconverged_resources
        return self.wait_subscription_resources('cnv', resources, my_output=my_output)

    def wait_no_instance_cnv(self, my_output=None):
        resources = self.hyperconverged_resources
        return self.wait_no_subscription_resources('cnv', resources, my_output=my_output)