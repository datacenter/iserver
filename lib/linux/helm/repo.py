from lib import filter_helper


class LinuxHelmRepoInfo():
    def __init__(self):
        self.helm_repo = None

    def get_helm_repo_info(self, managed_object):
        info = {}
        info['name'] = filter_helper.get(managed_object, 'name')
        info['url'] = filter_helper.get(managed_object, 'url')
        return info
    
    def get_helm_repos(self, object_filter=[], cache_enabled=True):
        if cache_enabled and self.helm_repo is not None:
            return self.helm_repo

        self.helm_repo = self.get_json_infos('helm_repo', object_filter, cache_enabled=cache_enabled)
        return self.helm_repo
    
    def get_helm_repo(self, object_filter=[], cache_enabled=True):
        return self.get_json_info('helm_repo', object_filter, cache_enabled=cache_enabled)