import time
import yaml
from menu.common import get_confirmation


class K8sSubscriptionSplunk():
    def __init__(self):
        pass

    def is_splunk_subscription(self, namespace, name, cache_enabled=True):
        return self.is_subscription(namespace, name, cache_enabled=cache_enabled)

    def create_splunk_subscription(self, namespace, name, channel, confirmation=False, my_output=None, wait=True):
        success = self.create_subscription(
            namespace, 
            name, 
            'Automatic', 
            name, 
            'certified-operators', 
            'openshift-marketplace', 
            channel=channel,
            confirmation=confirmation, 
            my_output=my_output, 
            wait=wait
        )
        if not success:
            return False
        
        if wait:
            success = self.wait_subscription_splunk(my_output=my_output)
            if not success:
                return False
        
        return True
    
    def delete_splunk_subscription(self, namespace, name, my_output=None, wait=True):
        success = self.delete_subscription(
            namespace, 
            name, 
            my_output=my_output, 
            wait=wait
        )        
        if not success:
            return False
        
        if wait:
            success = self.wait_no_subscription_splunk(my_output=my_output)
            if not success:
                return False

            # or check if pods are not yet there... but normally it takes few seconds for them to disappear
            time.sleep(5)

        return True

    def wait_subscription_splunk(self, my_output=None):
        deployments = [
            {'namespace': 'splunk-operator', 'name': 'splunk-operator-controller-manager'}
        ]
        success = self.wait_deployments_ready_state(deployments, my_output=my_output, optional=True)
        if not success:
            return False

        return True

    def wait_no_subscription_splunk(self, my_output=None):
        deployments = [
            {'namespace': 'splunk-operator', 'name': 'splunk-operator-controller-manager'}
        ]
        success = self.wait_no_deployments(deployments, my_output=my_output, optional=True)
        if not success:
            return False

        return True

    def update_splunk_subscription_license(self, package, confirmation=False, my_output=None):
        if my_output is None:
            confirmation = False

        if my_output is not None:
            my_output.default('Set Splunk operator subscription license', before_newline=True)
            my_output.default('- subscription package: %s' % (package))

        subscription = self.get_subscription_by_package(
            package,
            csv_info=True, 
            plan_info=True,
            return_mo=False,
            cache_enabled=False
        )
        if subscription is None:
            if my_output is not None:
                my_output.error('Subscription not found')
            return False

        if my_output is not None:
            my_output.default('- subscription found')
            my_output.default('- csv %s/%s' % (subscription['csv']['namespace'], subscription['csv']['namespace']))

        csv_mo = self.get_cluster_service_version(
            subscription['csv']['namespace'],
            subscription['csv']['name'],
            cache_enabled=False,
            return_mo=True
        )
        if csv_mo is None:
            if my_output is not None:
                my_output.error('Cluster service version not found')
            return False

        if my_output is not None:
            my_output.default('- csv found')

        body = {}
        body['apiVersion'] = 'operators.coreos.com/v1alpha1'
        body['kind'] = 'ClusterServiceVersion'
        body['metadata'] = {}
        body['metadata']['namespace'] = subscription['csv']['namespace']
        body['metadata']['name'] = subscription['csv']['name']
        body['spec'] = csv_mo['spec']
        
        deployment_name = None
        try:
            deployment_name = body['spec']['install']['spec']['deployments'][0]['name']
            env_mo = body['spec']['install']['spec']['deployments'][0]['spec']['template']['spec']['containers'][0]['env']
        except BaseException:
            env_mo = None

        if env_mo is None:
            if my_output is not None:
                my_output.error('Unexpected csv spec')
            return False
        
        found = False
        modified = False
        for env in body['spec']['install']['spec']['deployments'][0]['spec']['template']['spec']['containers'][0]['env']:
            if env['name'] == 'SPLUNK_GENERAL_TERMS':
                found = True
                if env['value'] != '--accept-sgt-current-at-splunk-com':
                    env['value'] = '--accept-sgt-current-at-splunk-com'
                    if my_output is not None:
                        my_output.default('- set env SPLUNK_GENERAL_TERMS value to --accept-sgt-current-at-splunk-com')
                    modified = True
                    break

        if not found:
            if my_output is not None:
                my_output.error('Environment variable SPLUNK_GENERAL_TERMS not found in csv spec')
            return False
        
        if not modified:
            if my_output is not None:
                my_output.default('- env SPLUNK_GENERAL_TERMS already set to --accept-sgt-current-at-splunk-com')
            return True

        if my_output is not None:
            my_output.default(yaml.dump(body), wrap='~~~')

        if confirmation:
            if not get_confirmation():
                return False
            
        success = self.patch_resource(
            body
        )
        if not success:
            if my_output is not None:
                my_output.error('rest api failed')
            return False

        if my_output is not None:
            my_output.default('- csv patched')

        my_output.default('- delete deployment %s/%s' % (subscription['csv']['namespace'], deployment_name))
        success = self.delete_deployment_mo(subscription['csv']['namespace'], deployment_name)
        if not success:
            if my_output is not None:
                my_output.error('rest api failed')
            return False
        
        if my_output is not None:
            my_output.default('- wait for deployment ready')

        if not self.wait_deployment_ready_state(subscription['csv']['namespace'], deployment_name):
            if my_output is not None:
                my_output.error('Timed out')
            return False
        
        return True
    
    def create_splunk_subscription_role_binding(self, package, role_binding_name, my_output=None, confirmation=False):
        if my_output is not None:
            my_output.default('Set OpenShift policy for Splunk operator', before_newline=True)
            my_output.default('- subscription package: %s' % (package))

        subscription = self.get_subscription_by_package(
            package,
            csv_info=True, 
            plan_info=True,
            return_mo=False,
            cache_enabled=False
        )
        if subscription is None:
            if my_output is not None:
                my_output.error('Subscription not found')
            return False

        if my_output is not None:
            my_output.default('- subscription found')
            my_output.default('- csv %s/%s' % (subscription['csv']['namespace'], subscription['csv']['namespace']))

        csv_mo = self.get_cluster_service_version(
            subscription['csv']['namespace'],
            subscription['csv']['name'],
            cache_enabled=False,
            return_mo=True
        )
        if csv_mo is None:
            if my_output is not None:
                my_output.error('Cluster service version not found')
            return False

        if my_output is not None:
            my_output.default('- csv found')

        deployment_name = None
        try:
            deployment_name = csv_mo['spec']['install']['spec']['deployments'][0]['name']
        except BaseException:
            pass

        if deployment_name is None:
            if my_output is not None:
                my_output.error('Unexpected csv spec')
            return False

        success = self.create_service_account_role_binding(
            subscription['csv']['namespace'],
            role_binding_name,
            role_binding_name, 
            subscription['csv']['namespace'], 
            'default', 
            my_output=my_output, 
            confirmation=confirmation
        )
        if not success:
            return False
        
        my_output.default('- delete deployment %s/%s' % (subscription['csv']['namespace'], deployment_name))
        success = self.delete_deployment_mo(subscription['csv']['namespace'], deployment_name)
        if not success:
            if my_output is not None:
                my_output.error('rest api failed')
            return False
        
        if my_output is not None:
            my_output.default('- wait for deployment ready')

        if not self.wait_deployment_ready_state(subscription['csv']['namespace'], deployment_name):
            if my_output is not None:
                my_output.error('Timed out')
            return False
        
        return True

    def delete_splunk_subscription_role_binding(self, namespace, role_binding_name, my_output=None):
        if my_output is not None:
            my_output.default('Delete OpenShift policy for Splunk operator', before_newline=True)
            my_output.default('- namespace: %s' % (namespace))
            my_output.default('- name: %s' % (role_binding_name))

        if not self.is_role_binding(namespace, role_binding_name):
            if my_output is not None:
                my_output.default('- already deleted')
            return True
        
        success = self.delete_role_binding_mo(namespace, role_binding_name)
        if not success:
            if my_output is not None:
                my_output.error('rest api failed')
            return False
        
        if my_output is not None:
            my_output.default('- deleted')
            
        return True
    