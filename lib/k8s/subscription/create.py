import json
import yaml
from lib import filter_helper
from menu.common import get_confirmation


class K8sSubscriptionCreate():
    def __init__(self):
        pass

    def get_subscription_body(
            self, 
            namespace, 
            name, 
            install_plan_approval, 
            subscription_name, 
            subscrition_source, 
            subscrition_source_namespace, 
            labels=None,
            channel=None,
            starting_csv=None
        ):
        body = {}
        body['apiVersion'] = 'operators.coreos.com/v1alpha1'
        body['kind'] = 'Subscription'
        body['metadata'] = {}
        body['metadata']['namespace'] = namespace
        body['metadata']['name'] = name
        if labels is not None:
            body['metadata']['labels'] = labels
        body['spec'] = {}
        if channel is not None:
            body['spec']['channel'] = channel
        body['spec']['installPlanApproval'] = install_plan_approval
        body['spec']['name'] = subscription_name
        body['spec']['source'] = subscrition_source
        body['spec']['sourceNamespace'] = subscrition_source_namespace
        if starting_csv is not None:
            body['spec']['startingCSV'] = starting_csv

        return body
    
    def create_subscription(
            self, 
            namespace, 
            name, 
            install_plan_approval, 
            subscription_name, 
            subscrition_source, 
            subscrition_source_namespace, 
            channel=None,
            labels=None,
            include_starting_csv=False,
            confirmation=False, 
            my_output=None, 
            wait=True            
        ):
        if my_output is None:
            confirmation = False

        if not self.is_namespace(namespace, cache_enabled=False):
            if my_output is not None:
                my_output.error(
                    'Namespace does not exist: %s' % (namespace)
                )

            self.log.error(
                'create_subscription',
                'Namespace does not exist: %s' % (namespace)
            )
            return False
            
        if my_output is not None:
            my_output.default('Create Subscription', before_newline=True, underline=True)
            my_output.default('Subscription: %s/%s' % (namespace, name))
            my_output.default('Source: %s/%s/%s' % (subscrition_source_namespace, subscrition_source, subscription_name))
            my_output.default('Install plan approval: %s' % (install_plan_approval))
            my_output.default('Getting subscription and packege manifest information...')

        subscription_info = self.get_subscription_by_package(
            subscription_name,
            cache_enabled=False
        )
        if subscription_info is not None:
            if my_output is not None:
                my_output.default('Subscription already defined')
            return True

        package_info = self.get_package(
            subscription_name,
            catalog=subscrition_source
        )
        if package_info is None:
            if my_output is not None:
                my_output.error(
                    'Failed to find package manifest %s in catalog %s' % (
                        subscription_name,
                        subscrition_source
                    )
                )

            self.log.error(
                'create_subscription',
                'Failed to find package manifest: %s' % (name)
            )
            return False

        if channel is not None and channel == '__default__':
            if my_output is not None:
                my_output.default('Resolving channel name...')

            channel = filter_helper.get(package_info, 'status:defaultChannel')
            if channel is None:
                if my_output is not None:
                    my_output.error('Failed to find default channel in package manifest: %s' % (name))
                    my_output.default(json.dumps(package_info, indent=4))

                return False
            
        if channel is not None and my_output is not None:
            my_output.default('Channel: %s' % (channel))

        starting_csv = None
        if channel is not None:
            package_channels = self.get(package_info, 'status:channels')
            if package_channels is None:
                if my_output is not None:
                    my_output.error('Failed to find package channels: %s' % (name))

                self.log.error(
                    'create_subscription',
                    'Failed to find package channels: %s' % (name)
                )
                return False

            found = False
            for package_channel in package_channels:
                if package_channel['name'] == channel:
                    found = True
                    if include_starting_csv:
                        starting_csv = self.get(package_channel, 'currentCSV')
                        
                    if my_output is not None:
                        my_output.default(
                            '- CSV [%s]' % (
                                self.get(package_channel, 'currentCSV')
                            )
                        )
                        my_output.default(
                            '- CSV Display name [%s]' % (
                                self.get(package_channel, 'currentCSVDesc:displayName')
                            )
                        )
                        my_output.default(
                            '- CVS Version [%s]' % (
                                self.get(package_channel, 'currentCSVDesc:version')
                            )
                        )
                        my_output.default(
                            '- CSV Provider [%s]' % (
                                self.get(package_channel, 'currentCSVDesc:provider')
                            )
                        )
                        maturity = self.get(package_channel, 'currentCSVDesc:maturity')
                        if maturity is not None:
                            my_output.default(
                                '- CSV Maturity [%s]' % (
                                    maturity
                                )
                            )

                    break

            if not found:
                if my_output is not None:
                    my_output.error('Failed to find package channel: %s/%s' % (name, channel))

                self.log.error(
                    'create_subscription',
                    'Failed to find package channel: %s/%s' % (name, channel)
                )
                return False
            

        if include_starting_csv:
            if starting_csv is None:
                if my_output is not None:
                    my_output.error('Failed to get starting csv value')
                return False
            
        body = self.get_subscription_body(
            namespace, 
            name, 
            install_plan_approval, 
            subscription_name, 
            subscrition_source, 
            subscrition_source_namespace, 
            labels=labels,
            channel=channel,
            starting_csv=starting_csv
        )
        if my_output is not None:
            my_output.default(yaml.dump(body), before_newline=True, wrap='~~~')

        if confirmation:
            if not get_confirmation():
                return False

        if not self.create_resource(body):
            if my_output is not None:
                my_output.error('REST API failed')
            return False
        
        if my_output is not None:
            my_output.default('Subscription created', before_newline=True, after_newline=True)

        if wait:
            if my_output is not None:
                my_output.default('Wait for subscription install plan started [timeout:360]...')

            install_plan_name = self.wait_subscription_install_plan(namespace, name, max_time=360)
            if install_plan_name is None:
                if my_output is not None:
                    my_output.error('Installation has not started: %s/%s' % (namespace, name))
                
                return False
            
            if my_output is not None:
                my_output.default('Install plan: %s' % (install_plan_name))
                my_output.default('Wait for subscription install plan ready [timeout:600]...')

            if not self.wait_installplan_ready(namespace, install_plan_name, max_time=600):
                if my_output is not None:
                    my_output.error('Timed out')
                
                return False
            
            if my_output is not None:
                my_output.default('Install plan succeeded')

        return True
    