from lib.k8s.ceph_block_pool.api import K8sCephBlockPoolApi
from lib.k8s.ceph_block_pool.info import K8sCephBlockPoolInfo


class K8sCephBlockPool(
        K8sCephBlockPoolApi,
        K8sCephBlockPoolInfo
        ):
    def __init__(self):
        K8sCephBlockPoolApi.__init__(self)
        K8sCephBlockPoolInfo.__init__(self)
