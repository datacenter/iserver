import openshift as oc


class OcpApiOperatorGroup():
    def __init__(self):
        pass

    def is_ocp_operator_group(self, operator_group_name, operator_group_namespace):
        if self.get_ocp_operator_group(operator_group_name, operator_group_namespace) is None:
            return False
        return True

    def get_ocp_operator_group(self, operator_group_name, operator_group_namespace):
        operator_groups = self.get_ocp_operator_groups()
        for operator_group in operator_groups:
            if operator_group['name'] == operator_group_name and operator_group['namespace'] == operator_group_namespace:
                return operator_group
        return None

    def get_ocp_operator_groups(self):
        operator_groups = []
        with oc.client_host(
            hostname=self.ocp_cluster_settings['parameters']['installer']['vm']['ip'],
            username=self.ocp_cluster_settings['parameters']['installer']['vm']['username'],
            password=self.ocp_cluster_settings['parameters']['installer']['vm']['password'],
            auto_add_host=True
            ):
            for obj in oc.selector('operatorgroup', all_namespaces=True).objects():
                operator_group = {}
                operator_group['name'] = obj.name()
                operator_group['namespace'] = obj.namespace()
                operator_groups.append(
                    operator_group
                )

        return operator_groups
