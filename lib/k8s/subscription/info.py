class K8sSubscriptionInfo():
    def __init__(self):
        self.subscription = None

    def get_subscription_info(self, managed_object):
        if managed_object is None:
            return None

        info = self.get_base_info(managed_object)

        info['channel'] = self.get(managed_object, 'spec:channel')
        info['package'] = self.get(managed_object, 'spec:name')
        info['source'] = self.get(managed_object, 'spec:source')
        info['source_namespace'] = self.get(managed_object, 'spec:sourceNamespace')
        info['packageT'] = '%s/%s/%s' % (
            info['source_namespace'],
            info['source'],
            info['package']
        )

        info['install_plan_approval'] = self.get(managed_object, 'spec:installPlanApproval')
        info['install_plan_namespace'] = self.get(managed_object, 'status:installPlanRef:namespace')
        info['install_plan_name'] = self.get(managed_object, 'status:installPlanRef:name')
        info['install_planT'] = '%s/%s' % (
            info['install_plan_namespace'],
            info['install_plan_name']
        )

        info['current_csv'] = self.get(managed_object, 'status:currentCSV')
        info['installed_csv'] = self.get(managed_object, 'status:installedCSV')
        info['csvT'] = info['installed_csv']
        if info['csvT'] is None:
            info['csvT'] = '---'
            
        if info['current_csv'] == info['installed_csv']:
            info['is_latest_csv'] = True
            info['csvTick'] = '\u2713'
            info['__Output']['csvTick'] = 'Green'
        else:
            info['is_latest_csv'] = False
            info['csvTick'] = '\u2717'
            info['__Output']['csvTick'] = 'Red'

        return info

    def get_subscriptions(self, object_filter=None, csv_info=False, plan_info=False, return_mo=False, cache_enabled=True):
        infos = self.get_infos(
            'subscription', 
            object_filter=object_filter, 
            return_mo=return_mo, 
            cache_enabled=cache_enabled
        )
        if return_mo:
            return infos
        
        # Populate csv local cache
        if csv_info and not cache_enabled:
            self.get_cluster_service_versions(cache_enabled=False)

        # populate install plan cache
        if plan_info and not cache_enabled:
            self.get_installplans(cache_enabled=False)

        subscriptions = []

        for subscription_info in infos:
            if not self.match_subscription(subscription_info, object_filter):
                continue

            if csv_info:
                subscription_info['csv'] = None
                if subscription_info['installed_csv'] is not None:
                    subscription_info['csv'] = self.get_cluster_service_version(
                        subscription_info['namespace'],
                        subscription_info['installed_csv'],
                        cache_enabled=True
                    )

            if plan_info:
                subscription_info['installplan'] = None
                if ['install_plan_namespace'] is not None and subscription_info['install_plan_name'] is not None:
                    subscription_info['installplan'] = self.get_installplan(
                        subscription_info['install_plan_namespace'],
                        subscription_info['install_plan_name'],
                        cache_enabled=True
                    )

            subscriptions.append(
                subscription_info
            )

        return subscriptions

    def is_subscription(self, namespace, name, cache_enabled=True, optimized=True):
        if self.get_subscription(namespace, name, cache_enabled=cache_enabled, optimized=optimized) is None:
            return False
        return True

    def get_subscription(self, namespace, name, csv_info=False, plan_info=False, return_mo=False, cache_enabled=True, optimized=True):
        info = self.get_info(
            'subscription', 
            name,
            namespace=namespace,
            return_mo=return_mo, 
            cache_enabled=cache_enabled,
            optimized=optimized
        )
        if return_mo:
            return info

        if info is None:
            return None
        
        if csv_info:
            info['csv'] = None
            if info['installed_csv'] is not None:
                info['csv'] = self.get_cluster_service_version(
                    info['namespace'],
                    info['installed_csv'],
                    cache_enabled=cache_enabled
                )

        if plan_info:
            info['installplan'] = None
            if info['install_plan_namespace'] is not None and info['install_plan_name'] is not None:
                info['installplan'] = self.get_installplan(
                    info['install_plan_namespace'],
                    info['install_plan_name'],
                    cache_enabled=cache_enabled
                )

        return info

    def get_subscription_by_package(self, package, csv_info=False, plan_info=False, return_mo=False, cache_enabled=True):
        object_filter = []
        object_filter.append(
            'package:%s' % (package)
        )
        subscriptions = self.get_subscriptions(
            object_filter=object_filter,
            csv_info=csv_info,
            plan_info=plan_info,
            return_mo=return_mo,
            cache_enabled=cache_enabled
        )
        if subscriptions is None:
            return None

        if len(subscriptions) == 1:
            return subscriptions[0]

        return None

    def is_subscription_by_package(self, package, cache_enabled=True):
        if self.get_subscription_by_package(package, cache_enabled=cache_enabled):
            return True
        return False

    def is_subscription_ready(self, subscription_name, resources, my_output=None, details=False, break_on_error=False, cache_enabled=False):
        if my_output is not None and details:
            my_output.default('Operator resources', before_newline=True, underline=True)

        for resource in resources:
            if resource['type'] not in ['deployment', 'daemonset']:
                if my_output is not None:
                    my_output.error('Unsupported resource type: %s' % (resource['type']))                    
                return False

        if not cache_enabled:
            resource_types = []
            for resource in resources:
                if resource['type'] not in resource_types:
                    resource_types.append(resource['type'])

            for resource_type in resource_types:
                if resource_type == 'deployment':
                    self.get_deployments(cache_enabled=False)

                if resource_type == 'daemonset':
                    self.get_daemon_sets(cache_enabled=False)


        ready = True
        for resource in resources:
            if 'optional' not in resource:
                resource['optional'] = False

            if resource['type'] == 'deployment':
                success = self.is_deployment_ready(resource['namespace'], resource['name'], cache_enabled=True)

            if resource['type'] == 'daemonset':
                success = self.is_daemon_set_ready(resource['namespace'], resource['name'], cache_enabled=True)

            if not success and not resource['optional']:
                ready = False

            if my_output is not None and details:
                if success:
                    my_output.default(
                        '- %s %s/%s: %s' % (
                            resource['type'],
                            resource['namespace'], 
                            resource['name'],
                            my_output.add_color('ready', 'Green')
                        )
                    )
                
                if not success:
                    if resource['optional']:
                        my_output.default(
                            '- (optional) %s %s/%s: %s' % (
                                resource['type'],
                                resource['namespace'], 
                                resource['name'],
                                my_output.add_color('not ready', 'Yellow')
                            )
                        )
                    else:
                        my_output.default(
                            '- %s %s/%s: %s' % (
                                resource['type'],
                                resource['namespace'], 
                                resource['name'],
                                my_output.add_color('not ready', 'Red')
                            )
                        )

            if not ready and break_on_error:
                break

        if not ready:
            if my_output is not None:
                my_output.default(
                    'Subscription %s %s' % (
                        subscription_name,
                        my_output.add_color('not ready', 'Red')
                    )
                )
        
        if my_output is not None:
            my_output.default(
                'Subscription %s %s' % (
                    subscription_name,
                    my_output.add_color('ready', 'Green')
                )

            )
        return True
    
    def get_subscription_resources(self, resources, extra=None, cache_enabled=True):
        if extra is not None:
            resources.extend(extra)

        for resource in resources:
            if resource['type'] == 'deployment':
                resource['resources'] = self.get_deployment_resources(
                    resource['namespace'],
                    resource['name'],
                    cache_enabled=cache_enabled
                )

            if resource['type'] == 'daemonset':
                resource['resources'] = self.get_daemon_set_resources(
                    resource['namespace'],
                    resource['name'],
                    cache_enabled=cache_enabled
                )

        return resources