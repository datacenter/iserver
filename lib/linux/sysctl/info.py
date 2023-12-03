import re

from lib import filter_helper


class LinuxSysctlInfo():
    def __init__(self):
        self.sysctl = None

    def get_sysctl_info(self):
        if self.sysctl is not None:
            return self.sysctl

        output = self.get_sysctl_cmd()
        if output is None:
            return None

        self.sysctl = []
        for line in output.split('\n'):
            if len(line.split(' = ')) == 2:
                (key, value) = line.split(' = ')

                item = {}
                item['key'] = key
                item['value'] = re.sub(' +', ' ', value).replace('\t', ' ')
                self.sysctl.append(
                    item
                )

        return self.sysctl

    def match_sysctl(self, sysctl_info, sysctl_filter):
        if sysctl_filter is None or len(sysctl_filter) == 0:
            return True

        for ap_rule in sysctl_filter:
            (key, value) = ap_rule.split(':')

            key_found = False

            if key == 'key':
                key_found = True
                if not filter_helper.match_string(value, sysctl_info['key']):
                    return False

            if not key_found:
                self.log.error(
                    'match_sysctl',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_sysctl(self, sysctl_filter=None):
        all_sysctl = self.get_sysctl_info()
        if all_sysctl is None:
            return None

        sysctl = []

        for sysctl_info in all_sysctl:
            if not self.match_sysctl(sysctl_info, sysctl_filter):
                continue

            sysctl.append(
                sysctl_info
            )

        return sysctl
