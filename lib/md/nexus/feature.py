class MdNexusFeatureOutput():
    def __init__(self):
        self.nexus_feature_mapping = {}
        self.nexus_feature_mapping['scpServer'] = 'scp'
        self.nexus_feature_mapping['sftpServer'] = 'sftp'
        self.nexus_feature_mapping['sshServer'] = 'ssh'
        self.nexus_feature_mapping['bash-shell'] = 'bash'
        self.nexus_feature_mapping['license-smart'] = 'lic'
        self.nexus_feature_mapping['interface_vlan'] = 'int_vlan'

    def get_nexus_features_output_data(self, features):
        nexus_features = self.xd_handler.get_nexus_feature()
        data = []

        for device_name in self.nexus_device_names:
            item = {}
            item['device'] = device_name
            for feature in features:
                item[feature] = False
                for nexus_feature in nexus_features[device_name]:
                    if nexus_feature['name'] == feature:
                        item[feature] = nexus_feature['enabled']
                        break

            data.append(
                item
            )
        return data

    def print_nexus_features(self):
        features = self.xd_handler.get_enabled_feature_names(self.nexus_device_names)

        self.print_page_header('Nexus Devices SW Features')
        self.print_nexus_overview_bar('features')

        chunk_size = 12
        for i in range(0, len(features), chunk_size):
            chunk = features[i:i+chunk_size]

            order = ['Device']
            for item in chunk:
                if item in self.nexus_feature_mapping:
                    order.append(self.nexus_feature_mapping[item])
                else:
                    order.append(item)
            self.print_table_header(order)

            data = self.get_nexus_features_output_data(chunk)
            for item in data:
                line = '%s |' % (item['device'])
                for feature in chunk:
                    if item[feature]:
                        line = '%s Yes |' % (line)
                    else:
                        line = '%s |' % (line)

                self.my_output.print_stream(line, 'output')

            self.my_output.print_stream(
                '\n\n',
                'output'
            )

        self.save_output('features', subdir='nexus')
