from lib import filter_helper


class K8sMutatingWebhookInfo():
    def __init__(self):
        self.mutating_webhook = None

    def get_mutating_webhook_info(self, mutating_webhook_mo):
        if mutating_webhook_mo is None:
            return None

        info = {}
        info['__Output'] = {}

        metadata_info = self.get_metadata_info(
            mutating_webhook_mo
        )
        info.update(metadata_info)

        info['spec'] = self.get(mutating_webhook_mo, 'spec')
        info['status'] = self.get(mutating_webhook_mo, 'status')
        return info

    def get_mutating_webhooks_info(self, cache_enabled=True):
        if cache_enabled:
            if self.mutating_webhook is not None:
                return self.mutating_webhook

        managed_objects = self.get_mutating_webhook_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.mutating_webhook = []
        for managed_object in managed_objects:
            mutating_webhook_info = {}
            mutating_webhook_info['info'] = self.get_mutating_webhook_info(
                managed_object
            )
            mutating_webhook_info['mo'] = managed_object
            self.mutating_webhook.append(
                mutating_webhook_info
            )

        return self.mutating_webhook

    def match_mutating_webhook(self, mutating_webhook_info, object_filter):
        if object_filter is None or len(object_filter) == 0:
            return True

        for rule in object_filter:
            (key, value) = rule.split(':')

            key_found = False

            if key == 'name':
                key_found = True
                if not filter_helper.match_string(value, mutating_webhook_info['name']):
                    return False

            if not key_found:
                self.log.error(
                    'match_mutating_webhook',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_mutating_webhooks(self, object_filter=None, return_mo=False, cache_enabled=True):
        all_mutating_webhooks = self.get_mutating_webhooks_info(cache_enabled=cache_enabled)
        if all_mutating_webhooks is None:
            return None

        mutating_webhooks = []

        for mutating_webhook_info in all_mutating_webhooks:
            if not self.match_mutating_webhook(mutating_webhook_info['info'], object_filter):
                continue

            if return_mo:
                mutating_webhooks.append(
                    mutating_webhook_info['mo']
                )
                continue

            mutating_webhooks.append(
                mutating_webhook_info['info']
            )

        return mutating_webhooks

    def is_mutating_webhook(self, name, cache_enabled=True):
        if self.get_mutating_webhook(name, cache_enabled=cache_enabled) is None:
            return False
        return True

    def get_mutating_webhook(self, name, return_mo=False, cache_enabled=True):
        object_filter = []
        object_filter.append(
            'name:%s' % (name)
        )
        mutating_webhooks = self.get_mutating_webhooks(
            object_filter=object_filter,
            return_mo=return_mo,
            cache_enabled=cache_enabled
        )
        if mutating_webhooks is None:
            return None

        if len(mutating_webhooks) == 1:
            return mutating_webhooks[0]

        return None
