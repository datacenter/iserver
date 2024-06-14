class OcpTaskNodeUp():
    def __init__(self):
        pass

    def set_ocp_node_vm_up(self, ocp_node_name, node_mo, wait=True):
        node_status = self.get_node_ready_status(node_mo)
        node_ready = self.is_node_ready(node_mo)
        self.my_output.info('Node status: %s' % (node_status))

        node_vm_name = self.get_node_vm_name(node_mo)
        if node_vm_name is None:
            self.log.error(
                'ocp.set_ocp_node_down',
                'node vm unknown: %s' % (self.get_node_name(node_mo))
            )
            return False

        self.my_output.info('Node vm name: %s' % (node_vm_name))
        powered_on = self.is_ocp_node_vm_powered_on(node_vm_name)
        self.my_output.info('Node vm powered on: %s' % (powered_on))

        if powered_on:
            if not node_ready:
                self.my_output.default('Warning: node vm powered on but not ready in kubernetes')
                return True

            self.my_output.default('Node vm powered on and ready in kubernetes')
            return True

        if not self.ocp_vcenter_handler.power_on_vm(node_vm_name):
            return False

        self.my_output.default('Wait for k8s node ready status...')
        if not self.wait_node_ready(ocp_node_name):
            self.my_output.error('K8s node status invalid or timed out reached')
            return False

        self.my_output.default('Node vm powered on and ready in kubernetes')
        return True

    def set_ocp_node_up(self, ocp_node_name, wait=True):
        node_mo = self.get_node_mo(ocp_node_name)
        if node_mo is None:
            self.my_output.error('Node not found: %s' % (ocp_node_name))
            return False

        self.my_output.default('Node found: %s' % (ocp_node_name))
        if self.is_node_vm(node_mo):
            return self.set_ocp_node_vm_up(ocp_node_name, node_mo, wait=wait)

        self.my_output.error('Unsupported node type: %s' % (ocp_node_name))
        return False
