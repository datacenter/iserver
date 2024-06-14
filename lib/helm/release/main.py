import json
import yaml

from lib import filter_helper


class HelmRelease():
    def __init__(self):
        self.release_mo = None
        self.release = None
        self.release_values = {}

    def get_release_mo(self, cache_enabled=True):
        if cache_enabled and self.release_mo is not None:
            return self.release_mo

        command = 'helm ls -A --output json'
        success, output, error = self.ssh_handler.run_cmd(
            command
        )
        if not success:
            self.log.error(
                'get_release_mo',
                'Helm command failed at %s: %s' % (self.helm_ip, command)
            )
            return None

        release_mo = ''
        for line in output.split('\n'):
            if line.startswith('WARNING:'):
                continue
            release_mo = '%s%s' % (
                release_mo,
                line
            )

        try:
            self.release_mo = json.loads(
                release_mo
            )
        except BaseException:
            self.log.error(
                'get_release_mo',
                'Helm output parse failed: %s' % (release_mo)
            )
            return None

        return self.release_mo

    def get_release_values(self, namespace, name, cache_enabled=True):
        key = '%s/%s' % (namespace, name)
        if cache_enabled and key in self.release_values:
            return self.release_values[key]

        command = 'helm get all %s -n %s' % (
            name,
            namespace
        )
        success, output, error = self.ssh_handler.run_cmd(
            command
        )
        if not success:
            self.log.error(
                'get_release_values',
                'Helm command failed at %s: %s' % (self.helm_ip, command)
            )
            return None

        values_mo = ''
        values_section = False
        for line in output.split('\n'):
            if line == 'COMPUTED VALUES:':
                values_section = True
                continue

            if line == 'HOOKS:':
                values_section = False
                continue

            if values_section:
                if line == '':
                    continue
                if values_mo == '':
                    values_mo = line
                    continue

                values_mo = '%s\n%s' % (values_mo, line)

        try:
            if len(values_mo) == 0:
                values = dict()
            else:
                values = yaml.safe_load(values_mo)
        except BaseException:
            self.log.error(
                'get_release_values',
                'Failed to json load values: %s' % (values_mo)
            )
            return None

        self.release_values[key] = values
        return self.release_values[key]

    def get_release_info(self, release_mo, cache_enabled=True):
        if cache_enabled and self.release is not None:
            return self.release

        self.release = []

        keys = [
            'name',
            'namespace',
            'revision',
            'updated',
            'status',
            'chart',
            'app_version'
        ]
        for item in release_mo:
            release = {}
            release['__Output'] = {}
            for key in keys:
                release[key] = item[key]

            release['namespace_name'] = '%s/%s' % (
                release['namespace'],
                release['name']
            )

            if release['status'] == 'deployed':
                release['__Output']['status'] = 'Green'
            else:
                release['__Output']['status'] = 'Red'

            self.release.append(
                release
            )

        return self.release

    def match_release(self, release_info, release_filter):
        if release_filter is None or len(release_filter) == 0:
            return True

        for ap_rule in release_filter:
            key = ap_rule.split(':')[0]
            value = ':'.join(ap_rule.split(':')[1:])

            key_found = False

            if key == 'name':
                key_found = True
                if not filter_helper.match_tenant_name(value, release_info['namespace_name']):
                    return False

            if key == 'namespace':
                key_found = True
                if not filter_helper.match_string(value, release_info['namespace']):
                    return False

            if key == 'chart':
                key_found = True
                if not filter_helper.match_string(value, release_info['chart']):
                    return False

            if not key_found:
                self.log.error(
                    'match_release',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_releases(self, release_filter=[], values_info=False, chart_info=False, day0_info=False, cache_enabled=True):
        release_mo = self.get_release_mo(
            cache_enabled=cache_enabled
        )
        if release_mo is None:
            return None

        release_info = self.get_release_info(
            release_mo,
            cache_enabled=cache_enabled
        )
        if release_info is None:
            return None

        release = []
        for item in release_info:
            if not self.match_release(item, release_filter):
                continue

            if values_info or day0_info:
                item['values'] = self.get_release_values(item['namespace'], item['name'], cache_enabled=cache_enabled)
                if item['values'] is None:
                    self.log.error(
                        'get_releases',
                        'Values none: %s/%s' % (item['namespace'], item['name'])
                    )

            if chart_info or day0_info:
                item['chart_name'] = None
                charts = self.get_charts(
                    chart_filter=['chart_version:%s' % (item['chart'])],
                    files_info=True
                )
                if charts is None:
                    self.log.error(
                        'get_releases',
                        'Charts none: %s/%s' % (item['namespace'], item['name'])
                    )

                if charts is not None and len(charts) > 1:
                    self.log.error(
                        'get_releases',
                        'Multiple charts: %s/%s' % (item['namespace'], item['name'])
                    )

                if charts is not None and len(charts) == 1:
                    item['chart_name'] = charts[0]['chart']

            if day0_info:
                item['day0'] = None
                if item['chart_name'] is not None and item['values'] is not None:
                    item['day0'] = self.get_release_day0(
                        item['chart_name'],
                        item['namespace'],
                        item['name'],
                        item['values']
                    )
                    if item['day0'] is None:
                        self.log.error(
                            'get_releases',
                            'Day0 failed: %s/%s' % (item['namespace'], item['name'])
                        )

            release.append(
                item
            )

        return release

    def get_release(self, namespace, name, values_info=False, chart_info=False, day0_info=False, cache_enabled=True):
        release_filter = []
        release_filter.append('namespace:%s' % (namespace))
        release_filter.append('name:%s' % (name))
        releases = self.get_releases(
            release_filter=release_filter,
            values_info=values_info,
            chart_info=chart_info,
            day0_info=day0_info,
            cache_enabled=cache_enabled
        )
        if releases is None or len(releases) != 1:
            return None

        return releases[0]

    def is_release(self, namespace, name, cache_enabled=True):
        if self.get_release(namespace, name, cache_enabled=cache_enabled) is None:
            return False
        return True

    def serialize_values(self, values):
        serialized_values = {}
        for key in values:
            if isinstance(values[key], str):
                serialized_values[key] = values[key]
            if isinstance(values[key], int):
                serialized_values[key] = values[key]
            if isinstance(values[key], bool):
                serialized_values[key] = values[key]
            if isinstance(values[key], dict):
                sub_values = self.serialize_values(values[key])
                for sub_key in sub_values:
                    serialized_values['%s.%s' % (key, sub_key)] = sub_values[sub_key]
        return serialized_values

    def apply_values(self, content, namespace, name, values):
        if content is None:
            return None

        content = content.replace('{{ .Release.Namespace }}', namespace)
        content = content.replace('{{ .Release.Name }}', name)

        serialized_values = self.serialize_values(values)
        for key in serialized_values:
            content = content.replace('{{ .Values.%s }}' % (key), str(serialized_values[key]))

        if '{{ ' in content:
            self.log.error(
                'apply_values',
                'Not all variables replaced: %s' % (content)
            )
            for key in serialized_values:
                self.log.error(
                    'apply_values',
                    '%s => %s' % (
                        key,
                        serialized_values[key]
                    )
                )
            return None

        return content

    def get_release_day0(self, chart_name, namespace, name, values):
        chart_info = self.get_chart(chart_name, files_info=True)
        if chart_info is None:
            self.log.error(
                'get_release_day0',
                'Chart not found: %s' % (chart_name)
            )
            return None

        if len(chart_info['day0']) == 0:
            return []

        day0 = []

        directory_names = []
        for item in chart_info['day0']:
            if item.split('/')[0] not in directory_names:
                directory_names.append(
                    item.split('/')[0]
                )

        for directory_name in directory_names:
            day0_item = {}
            day0_item['dv'] = None
            day0_item['filename'] = None
            day0_item['content'] = None

            for item in chart_info['day0']:
                if item.split('/')[0] == directory_name:
                    if item.split('/')[1] == 'day0.yaml':
                        content = self.apply_values(
                            self.get_chart_file(
                                chart_name,
                                item.split('/')[1],
                                directory='day0/%s' % (directory_name)
                            ),
                            namespace,
                            name,
                            values
                        )
                        if content is None:
                            self.log.error(
                                'get_release_day0',
                                'File read failed: %s' % (item)
                            )
                            return None

                        try:
                            day0_item['dv'] = yaml.safe_load(
                                content
                            )
                        except BaseException:
                            self.log.error(
                                'get_release_day0',
                                'File yaml read failed: %s' % (item)
                            )
                            return None

                    if item.split('/')[1] != 'day0.yaml':
                        day0_item['filename'] = item.split('/')[1]
                        day0_item['content'] = self.apply_values(
                            self.get_chart_file(
                                chart_name,
                                item.split('/')[1],
                                directory='day0/%s' % (directory_name)
                            ),
                            namespace,
                            name,
                            values
                        )

                        if day0_item['content'] is None:
                            self.log.error(
                                'get_release_day0',
                                'Configuration file read failed: %s' % (item)
                            )
                            return None

            day0.append(
                day0_item
            )

        return day0

    def create_release(self, chart_name, namespace, name, values):
        if self.is_release(namespace, name, cache_enabled=False):
            self.log.error(
                'create_release',
                'Release already exists: %s/%s' % (namespace, name)
            )
            return False, 'Release already exists: %s/%s' % (namespace, name)

        chart_info = self.get_chart(chart_name)
        if chart_info is None:
            self.log.error(
                'create_release',
                'Chart not found: %s' % (chart_name)
            )
            return False, 'Chart not found: %s' % (chart_name)

        values_filename = self.ssh_handler.create_file(
            yaml.safe_dump(
                values
            )
        )
        if values_filename is None:
            self.log.error(
                'create_release',
                'Failed to create values file'
            )
            return False, 'Failed to create values file'

        command = 'helm install %s -n %s -f %s %s' % (
            name,
            namespace,
            values_filename,
            chart_info['directory']
        )
        success, output, error = self.ssh_handler.run_cmd(
            command
        )
        self.ssh_handler.delete_file(values_filename)

        if not success:
            reason = 'Helm command failed'
            self.log.error(
                'create_release',
                'Helm command failed at %s: %s' % (self.helm_ip, command)
            )

            if output is not None and len(output) > 0:
                reason = '%s output [%s]' % (reason, output)
                self.log.error(
                    'create_release',
                    output
                )
            if error is not None and len(error) > 0:
                reason = '%s error [%s]' % (reason, error)
                self.log.error(
                    'create_release',
                    error
                )

            return False, reason

        return True, None

    def delete_release(self, namespace, name):
        if not self.is_release(namespace, name, cache_enabled=False):
            return True

        command = 'helm uninstall %s -n %s' % (name, namespace)
        success, output, error = self.ssh_handler.run_cmd(
            command
        )
        if not success:
            self.log.error(
                'delete_release',
                'Helm command failed at %s: %s' % (self.helm_ip, command)
            )
            return False
        return True
