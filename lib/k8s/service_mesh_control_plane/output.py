class K8sServiceMeshControlPlaneOutput():
    def __init__(self):
        pass

    def print_service_mesh_control_planes(self, info):
        self.my_output.my_table_ng(
            info,
            [
                ['Service Mesh Contol Plane', 'namespace_nameT'],
                ['Version', 'version'],
                ['Ready', 'readyTick'],
                ['Conditions', 'conditions'],
                ['Components', 'componentsT'],
                ['Disabled', 'disabledT'],
                ['Members', 'membersT']
            ]
        )

    def print_service_mesh_control_plane(self, info):
        self.print_service_mesh_control_planes([info])
        self.my_output.default('')
        self.print_service_mesh_control_plane_ingress_gateway(
            info['istio-ingress-gateway']
        )
        self.print_service_mesh_control_plane_egress_gateway(
            info['istio-egress-gateway']
        )
        self.print_service_mesh_control_plane_api_gateway(
            info['api-gateway']
        )
        self.print_service_mesh_control_plane_cni(
            info['istio-cni']
        )
        self.print_service_mesh_control_plane_prometheus(
            info['prometheus']
        )
        self.print_service_mesh_control_plane_grafana(
            info['grafana']
        )
        self.print_service_mesh_control_plane_kiali(
            info['kiali']
        )
        self.print_service_mesh_control_plane_telemetry(
            info['telemetry']
        )
        self.print_service_mesh_control_plane_tracing(
            info['tracing']
        )

    def print_service_mesh_control_plane_ingress_gateway(self, info):
        if info is None:
            self.my_output.default('Istio Ingress Gateway', before_newline=True, underline=True)
            self.my_output.default('Disabled')
            return
    
        self.my_output.dictionary_ng(
            'Istio Ingress Gateway',
            info, 
            [
                ['Name', 'name'],
                ['Enabled', 'enabled'],
                ['Auto Scale', 'autoscaleEnabled'],
                ['Istio Openshift Routing (ior)', 'ior_enabled']
            ],
            start=''
        )

        if 'deployment' in info and info['deployment'] is not None:
            self.my_output.dictionary_ng(
                'Deployment',
                info['deployment'], 
                [
                    ['Name', 'namespace_name'],
                    ['Replicas', 'readyT'],
                    ['Ready', 'ready'],
                ],
                underline=False,
                start=''
            )

        if 'service' in info and info['service'] is not None:
            self.my_output.dictionary_ng(
                'Service',
                info['service'], 
                [
                    ['Name', 'namespace_name'],
                    ['Port', 'portT'],
                    ['POD', 'podT'],
                    ['Endpoint', 'addressT'],
                ],
                underline=False,
                start=''
            )

    def print_service_mesh_control_plane_egress_gateway(self, info):
        if info is None:
            self.my_output.default('Istio Egress Gateway', before_newline=True, underline=True)
            self.my_output.default('Disabled')
            return
    
        self.my_output.dictionary_ng(
            'Istio Egress Gateway',
            info, 
            [
                ['Name', 'name'],
                ['Enabled', 'enabled'],
                ['Auto Scale', 'autoscaleEnabled']
            ],
            start=''
        )

        if 'deployment' in info and info['deployment'] is not None:
            self.my_output.dictionary_ng(
                'Deployment',
                info['deployment'], 
                [
                    ['Name', 'namespace_name'],
                    ['Replicas', 'readyT'],
                    ['Ready', 'ready'],
                ],
                underline=False,
                start=''
            )

        if 'service' in info and info['service'] is not None:
            self.my_output.dictionary_ng(
                'Service',
                info['service'], 
                [
                    ['Name', 'namespace_name'],
                    ['Port', 'portT'],
                    ['POD', 'podT'],
                    ['Endpoint', 'addressT'],
                ],
                underline=False,
                start=''
            )

    def print_service_mesh_control_plane_api_gateway(self, info):
        if info is None:
            self.my_output.default('API Gateway', before_newline=True, underline=True)
            self.my_output.default('Disabled')
            return
    
        self.my_output.dictionary_ng(
            'API Gateway',
            info, 
            [
                ['Enabled', 'enabled'],
                ['Contoller mode', 'controllerMode']
            ],
            start=''
        )

    def print_service_mesh_control_plane_grafana(self, info):
        if info is None:
            self.my_output.default('Grafana', before_newline=True, underline=True)
            self.my_output.default('Disabled')
            return
    
        self.my_output.dictionary_ng(
            'Grafana',
            info, 
            [
                ['Enabled', 'enabled'],
                ['Ingress', 'ingress.enabled']
            ],
            start=''
        )

    def print_service_mesh_control_plane_cni(self, info):
        if info is None:
            self.my_output.default('CNI', before_newline=True, underline=True)
            self.my_output.default('Disabled')
            return
    
        self.my_output.dictionary_ng(
            'CNI',
            info, 
            [
                ['Enabled', 'enabled'],
                ['Chained', 'chained'],
                ['Network', 'istio_cni_network']
            ],
            start=''
        )

    def print_service_mesh_control_plane_kiali(self, info):
        if info is None:
            self.my_output.default('Kiali', before_newline=True, underline=True)
            self.my_output.default('Disabled')
            return
    
        self.my_output.dictionary_ng(
            'Kiali',
            info, 
            [
                ['Enabled', 'enabled'],
                ['Ingress', 'ingress.enabled']
            ],
            start=''
        )

    def print_service_mesh_control_plane_prometheus(self, info):
        if info is None:
            self.my_output.default('Prometheus', before_newline=True, underline=True)
            self.my_output.default('Disabled')
            return
    
        self.my_output.dictionary_ng(
            'Prometheus',
            info, 
            [
                ['Enabled', 'enabled'],
                ['Ingress', 'ingress.enabled']
            ],
            start=''
        )

    def print_service_mesh_control_plane_telemetry(self, info):
        if info is None:
            self.my_output.default('Telemetry', before_newline=True, underline=True)
            self.my_output.default('Disabled')
            return
    
        self.my_output.dictionary_ng(
            'Telemetry',
            info, 
            [
                ['Enabled', 'enabled'],
                ['Implementation', 'implementation']
            ],
            start=''
        )


    def print_service_mesh_control_plane_tracing(self, info):
        if info is None:
            self.my_output.default('Tracing', before_newline=True, underline=True)
            self.my_output.default('Disabled')
            return
    
        self.my_output.dictionary_ng(
            'Tracing',
            info, 
            [
                ['Enabled', 'enabled'],
                ['Ingress', 'ingress.enabled']
            ],
            start=''
        )