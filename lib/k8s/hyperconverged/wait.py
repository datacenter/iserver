import time


class K8sHyperConvergedWait():
    def __init__(self):
        self.hyperconverged_deployments = [
            {'namespace': 'openshift-cnv', 'name': 'cdi-apiserver'},
            {'namespace': 'openshift-cnv', 'name': 'cdi-deployment'},
            {'namespace': 'openshift-cnv', 'name': 'cdi-uploadproxy'},
            {'namespace': 'openshift-cnv', 'name': 'kubemacpool-cert-manager'},
            {'namespace': 'openshift-cnv', 'name': 'kubemacpool-mac-controller-manager'},
            {'namespace': 'openshift-cnv', 'name': 'kubevirt-apiserver-proxy'},
            {'namespace': 'openshift-cnv', 'name': 'kubevirt-console-plugin'},
            {'namespace': 'openshift-cnv', 'name': 'kubevirt-ipam-controller-manager'},
            {'namespace': 'openshift-cnv', 'name': 'virt-api'},
            {'namespace': 'openshift-cnv', 'name': 'virt-controller'},
            {'namespace': 'openshift-cnv', 'name': 'virt-exportproxy'},
            {'namespace': 'openshift-cnv', 'name': 'virt-template-validator'}
        ]
        self.hyperconverged_daemon_sets = [
            {'namespace': 'openshift-cnv', 'name': 'bridge-marker'},
            {'namespace': 'openshift-cnv', 'name': 'kube-cni-linux-bridge-plugin'},
            {'namespace': 'openshift-cnv', 'name': 'passt-binding-cni'},
            {'namespace': 'openshift-cnv', 'name': 'virt-handler'}
        ]
    
    def wait_hyperconverged(self, max_time=60):
        start_time = int(time.time())
        while True:
            info = self.get_hyperconverged(
                cache_enabled=False
            )
            if info is not None:
                return True

            duration = int(time.time()) - start_time
            if duration > max_time:
                self.log.error(
                    'k8s.wait_hyperconverged',
                    'Max time reached'
                )
                return False

            time.sleep(5)

    def wait_no_hyperconverged(self, max_time=60):
        start_time = int(time.time())
        while True:
            info = self.get_hyperconverged(
                cache_enabled=False
            )
            if info is None:
                return True

            duration = int(time.time()) - start_time
            if duration > max_time:
                self.log.error(
                    'k8s.wait_no_hyperconverged',
                    'Max time reached'
                )
                return False

            time.sleep(5)

    def wait_hyperconverged_ready(self, my_output=None):
        if not self.wait_hyperconverged(max_time=60):
            if my_output is not None:
                my_output.error('Timed out')

        success = self.wait_deployments_ready_state(self.hyperconverged_deployments, my_output=my_output, optional=True)
        if not success:
            return False

        success = self.wait_daemon_sets_ready_state(self.hyperconverged_daemon_sets, my_output=my_output, optional=True)
        if not success:
            return False

        return True

    def wait_no_hyperconverged_resources(self, my_output=None):
        success = self.wait_no_deployments(self.hyperconverged_deployments, my_output=my_output, optional=False)
        if not success:
            return False

        success = self.wait_no_daemon_sets(self.hyperconverged_daemon_sets, my_output=my_output, optional=False)
        if not success:
            return False
        
        if not self.wait_no_hyperconverged(max_time=360):
            if my_output is not None:
                my_output.error('Timed out')

        return True