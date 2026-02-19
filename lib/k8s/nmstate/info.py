import yaml
import time
from lib import filter_helper
from menu.common import get_confirmation


class K8sNmstateInfo():
    def __init__(self):
        self.nmstate = None

    def get_nmstate_info(self, nmstate_mo):
        if nmstate_mo is None:
            return None

        info = {}
        info['__Output'] = {}

        metadata_info = self.get_metadata_info(
            nmstate_mo
        )
        info.update(metadata_info)

        info['spec'] = self.get(nmstate_mo, 'spec')
        return info

    def get_nmstates_info(self, cache_enabled=True):
        if cache_enabled:
            if self.nmstate is not None:
                return self.nmstate

        managed_objects = self.get_nmstate_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.nmstate = []
        for managed_object in managed_objects:
            nmstate_info = {}
            nmstate_info['info'] = self.get_nmstate_info(
                managed_object
            )
            nmstate_info['mo'] = managed_object
            self.nmstate.append(
                nmstate_info
            )

        return self.nmstate

    def match_nmstate(self, nmstate_info, object_filter):
        if object_filter is None or len(object_filter) == 0:
            return True

        for rule in object_filter:
            (key, value) = rule.split(':')

            key_found = False

            if key == 'name':
                key_found = True
                if not filter_helper.match_string(value, nmstate_info['name']):
                    return False

            if not key_found:
                self.log.error(
                    'match_nmstate',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_nmstates(self, object_filter=None, return_mo=False, cache_enabled=True):
        all_nmstates = self.get_nmstates_info(cache_enabled=cache_enabled)
        if all_nmstates is None:
            return None

        nmstates = []

        for nmstate_info in all_nmstates:
            if not self.match_nmstate(nmstate_info['info'], object_filter):
                continue

            if return_mo:
                nmstates.append(
                    nmstate_info['mo']
                )
                continue

            nmstates.append(
                nmstate_info['info']
            )

        return nmstates

    def is_nmstate(self, cache_enabled=True):
        if self.get_nmstate(cache_enabled=cache_enabled) is None:
            return False
        return True

    def is_any_nmstate(self, cache_enabled=True):
        policies = self.get_nmstates(cache_enabled=cache_enabled)
        if policies is None or len(policies) == 0:
            return False
        return True
    
    def get_nmstate(self, return_mo=False, cache_enabled=True):
        nmstates = self.get_nmstates(
            return_mo=return_mo,
            cache_enabled=cache_enabled
        )
        if nmstates is None:
            return None

        if len(nmstates) != 1:
            return None

        return nmstates[0]
    
    def create_nmstate(self, body, confirmation=False, my_output=None, wait=True):
        if my_output is None:
            confirmation = False

        if my_output is not None:
            my_output.default('Create NMState Instance', before_newline=True, underline=True)

        if self.is_nmstate(cache_enabled=False):
            if my_output is not None:
                my_output.default('- already exists')
            return True
        
        if my_output is not None:
            my_output.default(yaml.dump(body), before_newline=True, wrap='~~~')

        if confirmation:
            if not get_confirmation():
                return False

        if not self.create_nmstate_mo(body):
            if my_output is not None:
                my_output.error('REST API failed')
            return False
        
        if my_output is not None:
            my_output.default('NMState instance created', before_newline=True, after_newline=True)

        if not wait:
            return True
        
        if my_output is not None:
            my_output.default('Wait for nmstate instance [timeout:60]...')

        if not self.wait_nmstate(max_time=60):
            if my_output is not None:
                my_output.error('Timed out')
            
            return False

        if my_output is not None:
            my_output.default('Wait for nmstate instance resources...')

        success = self.wait_subscription_nmstate_ready(my_output=my_output, with_instance=True)
        if not success:
            if my_output is not None:
                my_output.error('Timed out')
            return False

        return True    
    
    def wait_nmstate(self, max_time=60):
        start_time = int(time.time())
        while True:
            info = self.get_nmstate(
                cache_enabled=False
            )
            if info is not None:
                return True

            duration = int(time.time()) - start_time
            if duration > max_time:
                self.log.error(
                    'k8s.wait_nmstate',
                    'Max time reached'
                )
                return False

            time.sleep(5)

    def delete_nmstate(self, my_output=None, wait=True):
        if my_output is not None:
            my_output.default('Delete NMState Instance', before_newline=True, underline=True)

        info = self.get_nmstate(cache_enabled=False)
        if info is None:
            if my_output is not None:
                my_output.default('- already deleted')
            return True
        
        if my_output is not None:
            my_output.default('- name: %s' % (info['name']))
        
        success = self.delete_nmstate_mo(info['name'])
        if not success:
            if my_output is not None:
                my_output.error('REST API failed')
            return False
        
        if not wait:
            return True
        
        if my_output is not None:
            my_output.default('- wait for no nmstate instance')

        success = self.wait_no_nmstate()
        if not success:
            if my_output is not None:
                my_output.error('Timed out')
            return False
        
        return True
    
    def wait_no_nmstate(self, max_time=60):
        start_time = int(time.time())
        while True:
            info = self.get_nmstate(
                cache_enabled=False
            )
            if info is None:
                return True

            duration = int(time.time()) - start_time
            if duration > max_time:
                self.log.error(
                    'k8s.wait_no_nmstate',
                    'Max time reached'
                )
                return False

            time.sleep(5)
