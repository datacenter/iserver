import time


class K8sGrafanaWait():
    def __init__(self):
        pass

    def wait_prometheus_user_workload_monitoring(self, my_output=None):
        deployments = [
            {'namespace': 'openshift-user-workload-monitoring', 'name': 'prometheus-operator'}
        ]
        success = self.wait_deployments_ready_state(deployments, my_output=my_output, optional=False)
        if not success:
            return False

        stateful_sets = [
            {'namespace': 'openshift-user-workload-monitoring', 'name': 'prometheus-user-workload'},
            {'namespace': 'openshift-user-workload-monitoring', 'name': 'thanos-ruler-user-workload'}
        ]
        success = self.wait_stateful_sets_ready_state(stateful_sets, my_output=my_output, optional=False)
        if not success:
            return False
        
        return True
    
    def wait_prometheus_no_user_workload_monitoring(self, my_output=None):
        deployments = [
            {'namespace': 'openshift-user-workload-monitoring', 'name': 'prometheus-operator'}
        ]
        success = self.wait_no_deployments(deployments, my_output=my_output, optional=False)
        if not success:
            return False

        stateful_sets = [
            {'namespace': 'openshift-user-workload-monitoring', 'name': 'prometheus-user-workload'},
            {'namespace': 'openshift-user-workload-monitoring', 'name': 'thanos-ruler-user-workload'}
        ]
        success = self.wait_no_stateful_sets(stateful_sets, my_output=my_output, optional=False)
        if not success:
            return False
        
        return True
    
    def wait_grafana(self, namespace, name, max_time=60):
        start_time = int(time.time())
        while True:
            grafana_info = self.get_grafana(
                namespace,
                name,
                cache_enabled=False
            )
            if grafana_info is not None:
                return True

            duration = int(time.time()) - start_time
            if duration > max_time:
                self.log.error(
                    'k8s.wait_no_grafana',
                    'Max time reached: %s/%s' % (namespace, name)
                )
                return False

            time.sleep(5)

    def wait_grafana_resources(self, namespace, name, my_output=None):
        deployments = [
            {'namespace': namespace, 'name': '%s-deployment' % (name)}
        ]
        success = self.wait_deployments_ready_state(deployments, my_output=my_output, optional=False)
        if not success:
            return None
        
        return True

    def wait_no_grafana(self, namespace, name, max_time=60):
        start_time = int(time.time())
        while True:
            grafana_info = self.get_grafana(
                namespace,
                name,
                cache_enabled=False
            )
            if grafana_info is None:
                return True

            duration = int(time.time()) - start_time
            if duration > max_time:
                self.log.error(
                    'k8s.wait_no_grafana',
                    'Max time reached: %s/%s' % (namespace, name)
                )
                return False

            time.sleep(5)

    def wait_no_grafana_resources(self, namespace, name, my_output=None):
        deployments = [
            {'namespace': namespace, 'name': '%s-deployment' % (name)}
        ]
        success = self.wait_no_deployments(deployments, my_output=my_output, optional=False)
        if not success:
            return None
        
        return True
