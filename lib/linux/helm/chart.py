from lib import filter_helper


class LinuxHelmChartInfo():
    def __init__(self):
        self.helm_chart = None

    def get_helm_chart_info(self, managed_object):
        info = {}
        info['__Output'] = {}
        for key in ['namespace', 'name', 'revision', 'updated', 'status', 'chart', 'app_version']:
            info[key] = filter_helper.get(managed_object, key)

        info['__Output']['status'] = 'Red'
        if info['status'] == 'deployed':
            info['__Output']['status'] = 'Green'
        
        return info
    
    def get_helm_charts(self, object_filter=[], cache_enabled=True):
        if cache_enabled and self.helm_chart is not None:
            return self.helm_chart

        self.helm_chart = self.get_json_infos('helm_chart', object_filter, cache_enabled=cache_enabled)
        return self.helm_chart
    
    def get_helm_chart(self, object_filter=[], cache_enabled=True):
        return self.get_json_info('helm_chart', object_filter, cache_enabled=cache_enabled)