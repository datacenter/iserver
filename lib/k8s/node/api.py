import time
import traceback


class K8sNodeApi():
    def __init__(self):
        self.nodes = None

    def get_nodes(self, cache=True):
        if not self.connect():
            return False

        if self.nodes is not None and cache:
            return True

        # https://github.com/kubernetes-client/python/blob/master/kubernetes/docs/V1NodeList.md
        try:
            start_time = int(time.time() * 1000)
            response = self.api.list_node(
                timeout_seconds=self.api_timeout_seconds
            )
            self.log.k8s(
                'get',
                'nodes',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('k8s_nodes.get_nodes', traceback.format_exc())
            self.log.k8s(
                'get',
                'nodes',
                True,
                int(time.time() * 1000) - start_time
            )
            return False

        self.nodes = []
        for item in response.items:
            node = self.convert_node(item)
            if node is not None:
                self.nodes.append(node)

        return True

    def print_nodes_list(self, nodes):
        # NAME                         STATUS   ROLES    AGE   VERSION           INTERNAL-IP    EXTERNAL-IP    OS-IMAGE                                                        KERNEL-VERSION                 CONTAINER-RUNTIME
        # cluster-wq4jk-master-0       Ready    master   32d   v1.24.0+b62823b   10.58.24.199   10.58.24.199   Red Hat Enterprise Linux CoreOS 411.86.202208291737-0 (Ootpa)   4.18.0-372.19.1.el8_6.x86_64   cri-o://1.24.2-6.rhaos4.11.gitb67c16f.el8
        # cluster-wq4jk-master-1       Ready    master   32d   v1.24.0+b62823b   10.58.24.197   10.58.24.197   Red Hat Enterprise Linux CoreOS 411.86.202208291737-0 (Ootpa)   4.18.0-372.19.1.el8_6.x86_64   cri-o://1.24.2-6.rhaos4.11.gitb67c16f.el8
        # cluster-wq4jk-master-2       Ready    master   32d   v1.24.0+b62823b   10.58.24.198   10.58.24.198   Red Hat Enterprise Linux CoreOS 411.86.202208291737-0 (Ootpa)   4.18.0-372.19.1.el8_6.x86_64   cri-o://1.24.2-6.rhaos4.11.gitb67c16f.el8
        # cluster-wq4jk-worker-27pcr   Ready    worker   32d   v1.24.0+b62823b   10.58.24.201   10.58.24.201   Red Hat Enterprise Linux CoreOS 411.86.202208291737-0 (Ootpa)   4.18.0-372.19.1.el8_6.x86_64   cri-o://1.24.2-6.rhaos4.11.gitb67c16f.el8
        # cluster-wq4jk-worker-hgj67   Ready    worker   32d   v1.24.0+b62823b   10.58.24.200   10.58.24.200   Red Hat Enterprise Linux CoreOS 411.86.202208291737-0 (Ootpa)   4.18.0-372.19.1.el8_6.x86_64   cri-o://1.24.2-6.rhaos4.11.gitb67c16f.el8

        order = [
            'type',
            'name',
            'ready',
            'roles',
            'age',
            'node_info.kubelet_version'
        ]

        headers = [
            'TF',
            'Name',
            'Status',
            'Roles',
            'Age',
            'Version'
        ]

        self.my_output.my_table(
            nodes,
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            row_separator=False,
            table=True
        )

    def print_nodes(self, nodes):
        # NAME                         STATUS   ROLES    AGE   VERSION           INTERNAL-IP    EXTERNAL-IP    OS-IMAGE                                                        KERNEL-VERSION                 CONTAINER-RUNTIME
        # cluster-wq4jk-master-0       Ready    master   32d   v1.24.0+b62823b   10.58.24.199   10.58.24.199   Red Hat Enterprise Linux CoreOS 411.86.202208291737-0 (Ootpa)   4.18.0-372.19.1.el8_6.x86_64   cri-o://1.24.2-6.rhaos4.11.gitb67c16f.el8
        # cluster-wq4jk-master-1       Ready    master   32d   v1.24.0+b62823b   10.58.24.197   10.58.24.197   Red Hat Enterprise Linux CoreOS 411.86.202208291737-0 (Ootpa)   4.18.0-372.19.1.el8_6.x86_64   cri-o://1.24.2-6.rhaos4.11.gitb67c16f.el8
        # cluster-wq4jk-master-2       Ready    master   32d   v1.24.0+b62823b   10.58.24.198   10.58.24.198   Red Hat Enterprise Linux CoreOS 411.86.202208291737-0 (Ootpa)   4.18.0-372.19.1.el8_6.x86_64   cri-o://1.24.2-6.rhaos4.11.gitb67c16f.el8
        # cluster-wq4jk-worker-27pcr   Ready    worker   32d   v1.24.0+b62823b   10.58.24.201   10.58.24.201   Red Hat Enterprise Linux CoreOS 411.86.202208291737-0 (Ootpa)   4.18.0-372.19.1.el8_6.x86_64   cri-o://1.24.2-6.rhaos4.11.gitb67c16f.el8
        # cluster-wq4jk-worker-hgj67   Ready    worker   32d   v1.24.0+b62823b   10.58.24.200   10.58.24.200   Red Hat Enterprise Linux CoreOS 411.86.202208291737-0 (Ootpa)   4.18.0-372.19.1.el8_6.x86_64   cri-o://1.24.2-6.rhaos4.11.gitb67c16f.el8

        order = [
            'type',
            'name',
            'ready',
            'roles',
            'age',
            'node_info.kubelet_version',
            'external_ip',
            'node_info.os_image',
            'node_info.kernel_version',
            'node_info.container_runtime_version'
        ]

        headers = [
            'TF',
            'Name',
            'Status',
            'Roles',
            'Age',
            'Version',
            'External IP',
            'OS Image',
            'Kernel Version',
            'Container Runtime'
        ]

        self.my_output.my_table(
            nodes,
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            row_separator=False,
            table=True
        )
