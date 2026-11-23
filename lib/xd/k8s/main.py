from lib.k8s import settings as k8s_settings
from lib.xd.k8s.cni import K8sCni
from lib.xd.k8s.co import K8sCo
from lib.xd.k8s.nns import K8sNns
from lib.xd.k8s.node import K8sNode
from lib.xd.k8s.sub import K8sSub
from lib.xd.k8s.ver import K8sVer


class K8s(
        K8sCni,
        K8sCo,
        K8sNns,
        K8sNode,
        K8sSub,
        K8sVer
    ):
    def __init__(self):
        self.k8s_clusters = None

        K8sCni.__init__(self)
        K8sCo.__init__(self)
        K8sNns.__init__(self)
        K8sNode.__init__(self)
        K8sSub.__init__(self)
        K8sVer.__init__(self)

    def load_pre_k8s_clusters(self):
        self.k8s_clusters = self.get_pre_cache_content('k8s-clusters')
        if self.k8s_clusters is None:
            return False
        return True

    def load_pre_k8s(self):
        if not self.load_pre_k8s_clusters():
            return False

        if not self.load_pre_k8s_cni():
            return False

        if not self.load_pre_k8s_co():
            return False

        if not self.load_pre_k8s_nns():
            return False

        if not self.load_pre_k8s_node():
            return False

        if not self.load_pre_k8s_sub():
            return False

        if not self.load_pre_k8s_ver():
            return False

        return True

    def prepare_k8s_clusters(self):
        k8s_settings_handler = k8s_settings.K8sSettings(log_id=self.log_id)
        k8s_clusters = k8s_settings_handler.get_k8s_clusters(
            cluster_filter=['domain:%s' % (self.domain_name)]
        )
        if k8s_clusters is None:
            return False

        self.k8s_clusters = []
        for k8s_cluster in k8s_clusters:
            self.k8s_clusters.append(
                k8s_cluster['name']
            )

        self.set_cache(
            'k8s-clusters',
            self.k8s_clusters
        )

        return True

    def prepare_k8s(self, allow_partial=False):
        success = True

        self.my_output.debug('Get k8s access...')
        if not self.prepare_k8s_clusters():
            self.my_output.error('Get k8s clusters failed')
            success = False
            if not allow_partial:
                return False

        self.my_output.debug('Get k8s cluster cni...')
        if not self.prepare_k8s_cni():
            self.my_output.error('Get k8s cluster cni failed')
            success = False
            if not allow_partial:
                return False

        self.my_output.debug('Get k8s cluster operator...')
        if not self.prepare_k8s_co():
            self.my_output.error('Get k8s cluster operator failed')
            success = False
            if not allow_partial:
                return False

        self.my_output.debug('Get k8s cluster nns...')
        if not self.prepare_k8s_nns():
            self.my_output.error('Get k8s cluster ndde network state failed')
            success = False
            if not allow_partial:
                return False

        self.my_output.debug('Get k8s cluster nodes...')
        if not self.prepare_k8s_node():
            self.my_output.error('Get k8s cluster nodes failed')
            success = False
            if not allow_partial:
                return False

        self.my_output.debug('Get k8s cluster sub...')
        if not self.prepare_k8s_sub():
            self.my_output.error('Get k8s cluster subscriptions failed')
            success = False
            if not allow_partial:
                return False

        self.my_output.debug('Get k8s cluster ver...')
        if not self.prepare_k8s_ver():
            self.my_output.error('Get k8s cluster ver failed')
            success = False
            if not allow_partial:
                return False

        return success

    def run_k8s(self):
        self.my_output.debug('\t- clusters')
        if not self.set_post_k8s_clusters():
            return False

        self.my_output.debug('\t- cni')
        if not self.run_k8s_cni():
            return False

        self.my_output.debug('\t- co')
        if not self.run_k8s_co():
            return False

        self.my_output.debug('\t- node')
        if not self.run_k8s_node():
            return False

        self.my_output.debug('\t- nns')
        if not self.run_k8s_nns():
            return False

        self.my_output.debug('\t- sub')
        if not self.run_k8s_sub():
            return False

        self.my_output.debug('\t- ver')
        if not self.run_k8s_ver():
            return False

        return True

    def load_post_k8s_clusters(self):
        self.k8s_clusters = self.get_post_cache('k8s-clusters')
        if self.k8s_clusters is None:
            return False
        return True

    def set_post_k8s_clusters(self):
        return self.set_post_cache('k8s-clusters', self.k8s_clusters)

    def load_post_k8s(self):
        if not self.load_post_k8s_clusters():
            self.my_output.debug('K8s cluster failed')
            return False

        if not self.load_post_k8s_cni():
            self.my_output.debug('K8s cluster cni failed')
            return False

        if not self.load_post_k8s_co():
            self.my_output.debug('K8s cluster co failed')
            return False

        if not self.load_post_k8s_nns():
            self.my_output.debug('K8s cluster nns failed')
            return False

        if not self.load_post_k8s_node():
            self.my_output.debug('K8s cluster node failed')
            return False

        if not self.load_post_k8s_sub():
            self.my_output.debug('K8s cluster sub failed')
            return False

        if not self.load_post_k8s_ver():
            self.my_output.debug('K8s cluster ver failed')
            return False

        return True
