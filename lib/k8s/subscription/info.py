from lib import filter_helper


class K8sSubscriptionInfo():
    def __init__(self):
        self.subscription = None

    def get_subscription_info(self, subscription_mo):
        if subscription_mo is None:
            return None

        info = {}
        info['__Output'] = {}

        metadata_info = self.get_metadata_info(
            subscription_mo
        )
        info.update(metadata_info)

        info['status'] = self.get(subscription_mo, 'status')
        info['spec'] = self.get(subscription_mo, 'spec')

        info['channel'] = self.get(subscription_mo, 'spec:channel')
        info['package'] = self.get(subscription_mo, 'spec:name')
        info['source'] = self.get(subscription_mo, 'spec:source')
        info['source_namespace'] = self.get(subscription_mo, 'spec:sourceNamespace')
        info['packageT'] = '%s/%s/%s' % (
            info['source_namespace'],
            info['source'],
            info['package']
        )

        info['install_plan_approval'] = self.get(subscription_mo, 'spec:installPlanApproval')
        info['install_plan_namespace'] = self.get(subscription_mo, 'status:installPlanRef:namespace')
        info['install_plan_name'] = self.get(subscription_mo, 'status:installPlanRef:name')
        info['install_planT'] = '%s/%s' % (
            info['install_plan_namespace'],
            info['install_plan_name']
        )

        info['current_csv'] = self.get(subscription_mo, 'status:currentCSV')
        info['installed_csv'] = self.get(subscription_mo, 'status:installedCSV')
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

    def get_subscriptions_info(self, cache_enabled=True):
        if cache_enabled:
            if self.subscription is not None:
                return self.subscription

        managed_objects = self.get_subscription_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.subscription = []
        for managed_object in managed_objects:
            subscription_info = {}
            subscription_info['info'] = self.get_subscription_info(
                managed_object
            )
            subscription_info['mo'] = managed_object
            self.subscription.append(
                subscription_info
            )

        return self.subscription

    def match_subscription(self, subscription_info, object_filter):
        if object_filter is None or len(object_filter) == 0:
            return True

        for rule in object_filter:
            (key, value) = rule.split(':')

            key_found = False

            if key == 'namespace':
                key_found = True
                if not filter_helper.match_string(value, subscription_info['namespace']):
                    return False

            if key == 'name':
                key_found = True
                if not filter_helper.match_namespace_name(value, '%s/%s' % (subscription_info['namespace'], subscription_info['name'])):
                    return False

            if key == 'package':
                key_found = True
                if not filter_helper.match_string(value, subscription_info['package']):
                    return False

            if not key_found:
                self.log.error(
                    'match_subscription',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_subscriptions(self, object_filter=None, csv_info=False, plan_info=False, return_mo=False, cache_enabled=True):
        all_subscriptions = self.get_subscriptions_info(cache_enabled=cache_enabled)
        if all_subscriptions is None:
            return None

        # Populate csv local cache
        if csv_info and not cache_enabled:
            self.get_cluster_service_versions(cache_enabled=False)

        # populate install plan cache
        if plan_info and not cache_enabled:
            self.get_installplans(cache_enabled=False)

        subscriptions = []

        for subscription_info in all_subscriptions:
            if not self.match_subscription(subscription_info['info'], object_filter):
                continue

            if return_mo:
                subscriptions.append(
                    subscription_info['mo']
                )
                continue

            if csv_info:
                subscription_info['info']['csv'] = self.get_cluster_service_version(
                    subscription_info['info']['namespace'],
                    subscription_info['info']['installed_csv'],
                    cache_enabled=True
                )

            if plan_info:
                subscription_info['info']['installplan'] = self.get_installplan(
                    subscription_info['info']['install_plan_namespace'],
                    subscription_info['info']['install_plan_name'],
                    cache_enabled=True
                )

            subscriptions.append(
                subscription_info['info']
            )

        return subscriptions

    def is_subscription(self, namespace, name, cache_enabled=True):
        if self.get_subscription(namespace, name, cache_enabled=cache_enabled) is None:
            return False
        return True

    def get_subscription(self, namespace, name, csv_info=False, plan_info=False, return_mo=False, cache_enabled=True):
        object_filter = []
        object_filter.append(
            'namespace:%s' % (namespace)
        )
        object_filter.append(
            'name:%s' % (name)
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
