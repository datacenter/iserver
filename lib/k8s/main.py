import os
import time
import traceback

from kubernetes import config
import kubernetes.client

from lib import log_helper
from lib import output_helper

from lib.k8s.common import K8sCommon
from lib.k8s.namespace.main import K8sNamespace
from lib.k8s.node.main import K8sNode
from lib.k8s.pod.main import K8sPod
from lib.k8s.pv.main import K8sPv
from lib.k8s.pvc.main import K8sPvc
from lib.k8s.service.main import K8sService


class K8s(K8sCommon, K8sNamespace, K8sNode, K8sPod, K8sPv, K8sPvc, K8sService):
    def __init__(self, kubeconfig_filename, verbose=False, debug=False, log_id=None):
        K8sCommon.__init__(self)
        K8sNamespace.__init__(self)
        K8sNode.__init__(self)
        K8sPod.__init__(self)
        K8sPv.__init__(self)
        K8sPvc.__init__(self)
        K8sService.__init__(self)

        self.verbose = verbose
        self.debug = debug
        self.log_id = log_id

        self.my_output = output_helper.OutputHelper(
            log_id=log_id,
            verbose=verbose,
            debug=debug
        )
        self.log = log_helper.Log(log_id=log_id)

        self.kubeconfig_filename = kubeconfig_filename

        self.api = None
        self.api_timeout_seconds = 3

    def connect(self):
        if self.api is not None:
            return True

        if not os.path.isfile(self.kubeconfig_filename):
            self.log.error(
                'k8s.connect',
                'Kubeconfig file not found: %s' % (self.kubeconfig_filename)
            )
            return False

        try:
            start_time = int(time.time() * 1000)

            config.load_kube_config(self.kubeconfig_filename)
            self.api = kubernetes.client.CoreV1Api()

            self.log.k8s(
                'connect',
                '-',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error(
                'k8s.connect',
                'Kubeconfig file failed: %s' % (self.kubeconfig_filename)
            )
            self.log.error('k8s.connect', traceback.format_exc())
            return False

        return True

    def is_connected(self, run_api=False):
        if not self.connect():
            return False

        if run_api:
            if not self.get_namespaces():
                return False

        return True
