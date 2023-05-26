import json
import openshift as oc


class OcpApiCsv():
    def __init__(self):
        pass

    def is_ocp_csv(self, csv_name, csv_namespace):
        if self.get_ocp_csv(csv_name, csv_namespace) is None:
            return False
        return True

    def get_ocp_csv(self, csv_name, csv_namespace):
        csvs = self.get_ocp_csvs()
        for csv in csvs:
            if csv['name'] == csv_name and csv['namespace'] == csv_namespace:
                return csv
        return None

    def get_ocp_csvs(self):
        csvs = []
        with oc.client_host(
            hostname=self.ocp_cluster_settings['parameters']['installer']['vm']['ip'],
            username=self.ocp_cluster_settings['parameters']['installer']['vm']['username'],
            password=self.ocp_cluster_settings['parameters']['installer']['vm']['password'],
            auto_add_host=True
            ):
            for obj in oc.selector('csv', all_namespaces=True).objects():
                csv = {}
                csv['name'] = obj.name()
                csv['namespace'] = obj.namespace()

                obj_json = json.loads(obj.as_json())
                csv['phase'] = obj_json['status']['phase']

                csvs.append(
                    csv
                )

        return csvs
