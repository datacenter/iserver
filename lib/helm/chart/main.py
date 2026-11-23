import os

from lib import filter_helper


class HelmChart():
    def __init__(self):
        self.chart_directory = '.\ichart'
        self.chart_names = None
        self.chart_mo = None
        self.chart = None

    def get_chart_names(self, cache_enabled=True):
        if cache_enabled and self.chart_names is not None:
            return self.chart_names

        self.chart_names = self.ssh_handler.get_directories(
            self.chart_directory
        )
        if self.chart_names is None:
            self.log.error(
                'get_chart_mo',
                'Helm command failed'
            )

        return self.chart_names

    def get_chart_filenames_info(self, chart_name):
        info = {}
        info['base'] = []
        info['templates'] = []
        info['charts'] = []
        info['crds'] = []
        info['tests'] = []
        info['day0'] = []
        info['custom'] = []

        directory = os.path.join(
            self.chart_directory,
            chart_name
        )
        info['files'] = self.ssh_handler.get_filenames(
            directory,
            relative=True
        )

        if info['files'] is not None:
            for filename in info['files']:
                if filename in ['Chart.yaml', 'values.yaml', '.helmignore']:
                    info['base'].append(filename)
                    continue

                if filter_helper.match_string('templates/tests/*', filename):
                    info['tests'].append(filename[len('templates/tests/'):])
                    continue

                if filter_helper.match_string('templates/*', filename):
                    if filename in ['templates/NOTES.txt', 'templates/_helpers.tpl']:
                        continue
                    info['templates'].append(filename[len('templates/'):])
                    continue

                if filter_helper.match_string('charts/*', filename):
                    info['charts'].append(filename[len('charts/'):])
                    continue

                if filter_helper.match_string('crds/*', filename):
                    info['crds'].append(filename[len('crds/'):])
                    continue

                if filter_helper.match_string('day0/*', filename):
                    info['day0'].append(filename[len('day0/'):])
                    continue

                info['custom'].append(filename)

        return info

    def get_chart_file(self, chart_name, filename, directory=None, convert_yaml=False):
        if directory is None:
            chart_filename = os.path.join(
                os.path.join(
                    self.chart_directory,
                    chart_name
                ),
                filename
            )
        else:
            chart_filename = os.path.join(
                os.path.join(
                    os.path.join(
                        self.chart_directory,
                        chart_name
                    ),
                    directory
                ),
                filename
            )

        content = self.ssh_handler.get_file(
            chart_filename,
            convert_yaml=convert_yaml
        )
        if content is None:
            self.log.error(
                'get_chart_file',
                'Yaml file not found: %s' % (chart_filename)
            )
            return None

        return content

    def get_chart_info(self, chart_name, cache_enabled=True):
        if cache_enabled:
            if self.chart is not None and chart_name in self.chart:
                return self.chart[chart_name]

        info = {}
        info['chart'] = chart_name
        info['directory'] = os.path.join(
            self.chart_directory,
            chart_name
        ).replace('\\', '/')

        value = self.get_chart_file(chart_name, 'Chart.yaml', convert_yaml=True)
        if value is None:
            self.log.error(
                'get_chart_info',
                'Failed to get Chart.yaml: %s' % (chart_name)
            )
            return None

        for key in value:
            info[key] = value[key]

        info['chart_release'] = '%s-%s' % (
            info['name'],
            info['version']
        )
        if self.chart is None:
            self.chart = {}

        self.chart[chart_name] = info
        return self.chart[chart_name]

    def match_chart(self, chart_info, chart_filter):
        if chart_filter is None or len(chart_filter) == 0:
            return True

        for ap_rule in chart_filter:
            key = ap_rule.split(':')[0]
            value = ':'.join(ap_rule.split(':')[1:])

            key_found = False

            if key == 'chart':
                key_found = True
                if not filter_helper.match_string(value, chart_info['chart']):
                    return False

            if key == 'name':
                key_found = True
                if not filter_helper.match_string(value, chart_info['name']):
                    return False

            if key == 'chart_version':
                key_found = True
                if not filter_helper.match_string(value, '%s-%s' % (chart_info['chart'], chart_info['version'])):
                    return False

            if not key_found:
                self.log.error(
                    'match_chart',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_charts(self, chart_filter=[], release_info=False, values_info=False, files_info=False, cache_enabled=True):
        chart_names = self.get_chart_names(cache_enabled=cache_enabled)
        if chart_names is None:
            return None

        charts = []
        for chart_name in chart_names:
            chart_info = self.get_chart_info(chart_name, cache_enabled=cache_enabled)
            if chart_info is None:
                continue

            if not self.match_chart(chart_info, chart_filter=chart_filter):
                continue

            if values_info:
                chart_info['values'] = self.get_chart_file(
                    chart_info['chart'],
                    'values.yaml'
                )

            if files_info:
                filenames_info = self.get_chart_filenames_info(chart_name)
                if filenames_info is not None:
                    chart_info.update(filenames_info)

            if release_info:
                release_filter = ['chart:%s' % (chart_info['chart_release'])]
                chart_info['release'] = self.get_releases(
                    release_filter=release_filter,
                    cache_enabled=cache_enabled
                )

            charts.append(
                chart_info
            )

        charts = sorted(
            charts,
            key=lambda i: i['chart']
        )

        return charts

    def get_chart(self, chart_name, release_info=False, files_info=False, cache_enabled=True):
        chart_filter = []
        chart_filter.append('name:%s' % (chart_name))
        charts = self.get_charts(chart_filter=chart_filter, release_info=release_info, files_info=files_info, cache_enabled=cache_enabled)
        if charts is None or len(charts) != 1:
            return None
        return charts[0]

    def is_chart(self, chart_name, cache_enabled=True):
        if self.get_chart(chart_name, cache_enabled=cache_enabled) is None:
            return False
        return True

    def is_chart_release(self, chart_name, cache_enabled=True):
        chart_info = self.get_chart(chart_name, release_info=True, cache_enabled=cache_enabled)
        if chart_info is None:
            return False

        if len(chart_info['release']) == 0:
            return False

        return True

    def create_chart(self, chart_name, chart_directory, values_filename, verbose=False):
        destination_chart_directory = os.path.join(
            self.chart_directory,
            chart_name
        )

        if not self.ssh_handler.create_directory(destination_chart_directory):
            self.log.error(
                'create_chart',
                'Directory create failed: %s' % (destination_chart_directory)
            )
            return False

        for chart_component in os.listdir(chart_directory):
            chart_component_path = os.path.join(
                chart_directory,
                chart_component
            )

            if os.path.isdir(chart_component_path):
                destination_directory = os.path.join(
                    destination_chart_directory,
                    chart_component
                )

                if not self.ssh_handler.create_directory(destination_directory):
                    self.log.error(
                        'create_chart',
                        'Directory create failed: %s' % (destination_directory)
                    )
                    return False

                if verbose:
                    print('- %s => %s (dir)' % (chart_component_path, destination_directory))

                if not self.ssh_handler.scp_directory(chart_component_path, destination_directory):
                    self.log.error(
                        'create_chart',
                        'Directory copy failed: %s => %s' % (chart_component_path, destination_directory)
                    )
                    return False

                self.log.debug(
                    'create_chart',
                    'Directory copied: %s => %s' % (chart_component_path, destination_directory)
                )
                continue

            destination_filename = os.path.join(
                destination_chart_directory,
                chart_component
            )

            if chart_component in ['Chart.yaml', '.helmignore']:
                if verbose:
                    print('- %s => %s (file)' % (chart_component_path, destination_filename))

                if not self.ssh_handler.scp_file(chart_component_path, destination_filename):
                    self.log.error(
                        'create_chart',
                        'File copy failed: %s' % (chart_component_path)
                    )
                    return False

                self.log.debug(
                    'create_chart',
                    'File copied: %s => %s' % (chart_component_path, destination_chart_directory)
                )
                continue

            if os.path.basename(destination_filename) == os.path.basename(values_filename):
                destination_values_filename = os.path.join(
                    destination_chart_directory,
                    'values.yaml'
                )

                if verbose:
                    print('- %s => %s (file)' % (chart_component_path, destination_values_filename))

                if not self.ssh_handler.scp_file(chart_component_path, destination_values_filename):
                    self.log.error(
                        'create_chart',
                        'File copy failed: %s' % (chart_component_path)
                    )
                    return False

                self.log.debug(
                    'create_chart',
                    'File copied: %s => %s' % (chart_component_path, destination_values_filename)
                )

        return True

    def delete_chart(self, chart_name):
        directory_name = os.path.join(self.chart_directory, chart_name)
        return self.ssh_handler.delete_directory(directory_name)
