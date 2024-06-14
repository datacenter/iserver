#!usr/bin/env python

import os
import base64
import json
import time
import traceback

class K8sServices():
    def __init__(self):
        self.services = None

    def convert_service_output_json(self, output):
        try:
            if output is None:
                return None

            output = str(output)

            if 'last-applied-configuration' in output:
                '''
                Not sure how to change that...
                {"kubectl.kubernetes.io/last-applied-configuration":
                    "{"apiVersion":"v1","kind":"Service","metadata":{"annotations":{},
                    "labels":{"k8s-app":"calico-typha"},"name":"calico-typha","namespace":"kube-system"},
                    "spec":{"clusterIP":"<ip>",
                    "ports":[{"name":"calico-typha","port":5473,"protocol":"TCP","targetPort":"calico-typha"}],
                    "selector":{"k8s-app":"calico-typha"}}}\n"}
                '''
                return None

            output = output.replace('\'', '\"')
            output = output.replace(': None', ': null')
            output = output.replace(': True', ': true')
            output = output.replace(': False', ': false')
            return json.loads(output)
        except:
            self.log.error('k8s_services.convert_service_output_json', output)
            self.log.error('k8s_services.convert_service_output_json', traceback.format_exc())
            return None

    def convert_service_metadata_managed_fields(self, mfs):
        try:
            if mfs is None:
                return None

            n = []
            for mf in mfs:
                t = dict()
                t['api_version'] = mf.api_version
                t['fields'] = mf.fields_v1
                t['manager'] = mf.manager
                t['operation'] = mf.operation
                t['time'] = self.convert_timestamp(mf.time)
                n.append(t)

        except:
            self.log.error('k8s_services.convert_service_metadata_managed_fields', traceback.format_exc())
            return None

        return n

    def convert_service_metadata(self, metadata):
        try:
            n = dict()
            n['uid'] = metadata.uid
            n['self_link'] = metadata.self_link
            n['resource_version'] = metadata.resource_version
            if metadata.owner_references is None:
                n['owner_references'] = None
            else:
                n['owner_references'] = str(metadata.owner_references)
            n['name'] = metadata.name
            n['namespace'] = metadata.namespace
            n['annotations'] = self.convert_service_output_json(metadata.annotations)
            n['labels'] = self.convert_service_output_json(metadata.labels)
            n['managed_fields'] = self.convert_service_metadata_managed_fields(metadata.managed_fields)
            n['creation_timestamp'] = self.convert_timestamp(metadata.creation_timestamp)

        except:
            self.log.error('k8s_services.convert_service_metadata', traceback.format_exc())
            return None

        return n

    def convert_service(self, service):
        try:
            n = dict()
            n['metadata'] = self.convert_service_metadata(service.metadata)
            n['spec'] = self.convert_service_output_json(service.spec)
            n['status'] = self.convert_service_output_json(service.status)
        except:
            self.log.error('k8s_services.convert_service', traceback.format_exc())
            return None

        return n

    def get_service_summary(self, service):
        '''
        {
            "name": "my-nginx-service-1",
            "namespace": "default",
            "type": "LoadBalancer",
            "ip": "<ip>",
            "external_ip_list": [
                "<ip>"
            ],
            "external_ips": null,
            "lb_ingress_ip": [
                {
                    "hostname": null,
                    "ip": "<ip>",
                    "ports": null
                }
            ],
            "external_ip": "<ip>",
            "ports": "18080/TCP",
            "ports_list": [
                {
                    "app_protocol": null,
                    "name": "http",
                    "node_port": 31103,
                    "port": 80,
                    "protocol": "TCP",
                    "target_port": "http"
                },
                {
                    "app_protocol": null,
                    "name": "https",
                    "node_port": 30212,
                    "port": 443,
                    "protocol": "TCP",
                    "target_port": "https"
                }
            ],
            "selector": {
                "app": "my-nginx-1"
            },
            "age": 51731,
            "creation_timestamp": 1651519900
        }
        '''
        try:
            summary = dict()
            summary['name'] = service['metadata']['name']
            summary['namespace'] = service['metadata']['namespace']
            summary['type'] = service['spec']['type']

            summary['ip'] = service['spec']['cluster_ip']
            if summary['ip'] == 'None':
                summary['ip'] = None

            summary['external_ip_list'] = []

            if service['spec']['external_i_ps'] is None:
                summary['external_ips'] = None
            else:
                summary['external_ips'] = service['spec']['external_i_ps']
                summary['external_ip_list'] = service['external_ip_list'] + n['external_ips']

            if service['status']['load_balancer']['ingress'] is None:
                summary['lb_ingress_ip'] = None
            else:
                summary['lb_ingress_ip'] = service['status']['load_balancer']['ingress']
                for lb_ip in summary['lb_ingress_ip']:
                    summary['external_ip_list'].append(lb_ip['ip'])

            summary['external_ip'] = ','.join(summary['external_ip_list'])

            ports = []
            for p in service['spec']['ports']:
                ports.append('%s/%s' % (p['port'], p['protocol']))
            summary['ports'] = ','.join(ports)
            summary['ports_list'] = service['spec']['ports']

            summary['selector'] = service['spec']['selector']

            summary['age'] = int(time.time()) - service['metadata']['creation_timestamp']
            summary['creation_timestamp'] = service['metadata']['creation_timestamp']

        except:
            self.log.error('k8s_services.get_service_summary', traceback.format_exc())
            return None

        return summary

    def get_service(self, namespace, name):
        self.get_services()
        if self.services is not None:
            for service in self.services:
                info = self.get_service_summary(service)
                if info is not None:
                    if info['name'] == name and info['namespace'] == namespace:
                        return info

        return None

    def get_lb_services(self, summary = False):
        return self.get_services_type('LoadBalancer', summary = summary)

    def get_services_type(self, service_type, summary = False):
        self.get_services()
        services = []
        if self.services is not None:
            for service in self.services:
                if service['spec']['type'] == service_type:
                    if summary:
                        s = self.get_service_summary(service)
                        if s is not None:
                            services.append(s)
                    else:
                        services.append(service)

        return services

    def get_services(self):
        if self.services is not None:
            return self.services

        # https://github.com/kubernetes-client/python/blob/master/kubernetes/docs/CoreV1Api.md#list_service_for_all_namespaces
        try:
            self.services = []
            start_time = int(time.time()*1000)
            response = self.api.list_service_for_all_namespaces(timeout_seconds=self.api_timeout_seconds)
            self.api_statistics('list_service_for_all_namespaces', int(time.time()*1000) - start_time)

            if response is not None:
                for i in response.items:
                    service = self.convert_service(i)
                    if service is not None:
                        self.services.append(service)

        except:
            self.log.error('k8s_services.get_services', traceback.format_exc())
            return None

        return self.services

    def get_service_pods(self, service):
        '''
        [
            {
                "namespace": "iks",
                "labels": {
                    "app.kubernetes.io/component": "controller",
                    "app.kubernetes.io/instance": "essential-nginx-ingress",
                    "app.kubernetes.io/name": "ingress-nginx",
                    "controller-revision-hash": "794954b8c6",
                    "pod-template-generation": "1"
                },
                "name": "essential-nginx-ingress-ingress-nginx-controller-2nk8m",
                "uid": "8b2bcc15-da82-4092-9381-71ffca698158",
                "age": 258092,
                "node": "milan-kali-worker-4078840427",
                "replicaset_name": null,
                "scheduled": true,
                "status": "Running",
                "ready": true,
                "pod_ip": "<ip>",
                "cni": {
                    "ip": "<ip>",
                    "ports": [
                        {
                            "container_port": 80,
                            "host_ip": null,
                            "host_port": null,
                            "name": "http",
                            "protocol": "TCP"
                        },
                        {
                            "container_port": 443,
                            "host_ip": null,
                            "host_port": null,
                            "name": "https",
                            "protocol": "TCP"
                        }
                    ]
                },
                "job_name": null,
                "job_succeeded": false,
                "healthy": true,
                "containers": {
                    "ready": 1,
                    "completed": 0,
                    "count": 1,
                    "restarts": 0,
                    "reasons": []
                },
                "node_selector": [
                    {
                        "match_expressions": null,
                        "match_fields": [
                            {
                                "key": "metadata.name",
                                "operator": "In",
                                "values": [
                                    "milan-kali-worker-4078840427"
                                ]
                            }
                        ]
                    }
                ],
                "scheduling_problem": null
            }
        ]
        '''
        my_pods = []
        try:
            if self.pods is not None:
                for p in self.pods:
                    pod = self.get_pod_summary(p)
                    if pod is not None:
                        found = True
                        if pod['labels'] is None:
                            continue

                        for selector_key in service['selector']:
                            if selector_key not in pod['labels']:
                                found = False
                                break

                            if pod['labels'][selector_key] != service['selector'][selector_key]:
                                found = False
                                break

                        if found:
                            my_pods.append(pod)

        except:
            self.log.error('k8s_services.get_service_pods', traceback.format_exc())

        return my_pods

    def get_service_pods_health_summary(self, service):
        try:
            my_pods = self.get_service_pods(service)
            return self.get_selected_pods_health_summary(my_pods)
        except:
            self.log.error('k8s_services.get_service_pods_health_summary', traceback.format_exc())
            return None