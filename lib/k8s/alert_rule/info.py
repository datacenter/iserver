import time
import yaml
from lib import filter_helper
from menu.common import get_confirmation


class K8sAlertRuleInfo():
    def __init__(self):
        self.alert_rule = None

    def get_alert_rule_info(self, alert_rule_mo):
        if alert_rule_mo is None:
            return None

        info = {}
        info['__Output'] = {}

        metadata_info = self.get_metadata_info(
            alert_rule_mo
        )
        info.update(metadata_info)

        info['spec'] = self.get(alert_rule_mo, 'spec')
        return info

    def get_alert_rules_info(self, cache_enabled=True):
        if cache_enabled:
            if self.alert_rule is not None:
                return self.alert_rule

        managed_objects = self.get_alert_rule_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.alert_rule = []
        for managed_object in managed_objects:
            alert_rule_info = {}
            alert_rule_info['info'] = self.get_alert_rule_info(
                managed_object
            )
            alert_rule_info['mo'] = managed_object
            self.alert_rule.append(
                alert_rule_info
            )

        return self.alert_rule

    def match_alert_rule(self, alert_rule_info, object_filter):
        if object_filter is None or len(object_filter) == 0:
            return True

        for rule in object_filter:
            (key, value) = rule.split(':')

            key_found = False

            if key == 'name':
                key_found = True
                if not filter_helper.match_string(value, alert_rule_info['name']):
                    return False

            if not key_found:
                self.log.error(
                    'match_alert_rule',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_alert_rules(self, object_filter=None, return_mo=False, cache_enabled=True):
        all_alert_rules = self.get_alert_rules_info(cache_enabled=cache_enabled)
        if all_alert_rules is None:
            return None

        alert_rules = []

        for alert_rule_info in all_alert_rules:
            if not self.match_alert_rule(alert_rule_info['info'], object_filter):
                continue

            if return_mo:
                alert_rules.append(
                    alert_rule_info['mo']
                )
                continue

            alert_rules.append(
                alert_rule_info['info']
            )

        return alert_rules

    def is_alert_rule(self, name, cache_enabled=True):
        if self.get_alert_rule(name, cache_enabled=cache_enabled) is None:
            return False
        return True

    def get_alert_rule(self, name, return_mo=False, cache_enabled=True):
        object_filter = []
        object_filter.append(
            'name:%s' % (name)
        )
        alert_rules = self.get_alert_rules(
            object_filter=object_filter,
            return_mo=return_mo,
            cache_enabled=cache_enabled
        )
        if alert_rules is None:
            return None

        if len(alert_rules) == 1:
            return alert_rules[0]

        return None

    def create_alert_rule(self, body, confirmation=False, my_output=None, wait=True):
        if my_output is None:
            confirmation = False

        if my_output is not None:
            my_output.default('Create Alert Rule', before_newline=True, underline=True)
            my_output.default('- name: %s' % (body['metadata']['name']))

        if self.is_alert_rule(body['metadata']['name']):
            if my_output is not None:
                my_output.default('- already exists')
            return True

        if confirmation:
            if my_output is not None:
                my_output.default(yaml.dump(body), before_newline=True, wrap='~~~')

            if not get_confirmation():
                return False

        if not self.create_alert_rule_mo(body):
            if my_output is not None:
                my_output.error('REST API failed')
            return False
        
        if my_output is not None:
            my_output.default('Alert rule created', before_newline=True, after_newline=True)

        if wait:
            if my_output is not None:
                my_output.default('Wait for alert rule [timeout:60]...')

            if not self.wait_alert_rule(body['metadata']['name'], max_time=30):
                if my_output is not None:
                    my_output.error('Timed out')
                
                return False

        return True    

    def wait_alert_rule(self, name, max_time=60):
        start_time = int(time.time())
        while True:
            info = self.get_alert_rule(
                name,
                cache_enabled=False
            )
            if info is not None:
                return True

            duration = int(time.time()) - start_time
            if duration > max_time:
                self.log.error(
                    'k8s.wait_alert_rule',
                    'Max time reached: %s' % (name)
                )
                return False

            time.sleep(5)

    def delete_alert_rule(self, name, my_output=None, wait=True):
        if my_output is not None:
            my_output.default('Delete Alert Rule', before_newline=True, underline=True)
            my_output.default('- name: %s' % (name))

        info = self.get_alert_rule(name, cache_enabled=False)
        if info is None:
            if my_output is not None:
                my_output.default('- already deleted')
            return True

        if not self.delete_alert_rule_mo(info['name']):
            if my_output is not None:
                my_output.error('Failed to delete alert rule')
            return False

        if wait:
            if my_output is not None:
                my_output.default('- wait for no alert rule')

            if not self.wait_no_alert_rule(info['name']):
                if my_output is not None:
                    my_output.error('Timed out')
                return False
            
        return True

    def wait_no_alert_rule(self, name, max_time=60):
        start_time = int(time.time())
        while True:
            info = self.get_alert_rule(
                name,
                cache_enabled=False
            )
            if info is None:
                return True

            duration = int(time.time()) - start_time
            if duration > max_time:
                self.log.error(
                    'k8s.wait_no_alert_rule',
                    'Max time reached: %s' % (name)
                )
                return False

            time.sleep(5)
