import copy
import json

from lib import filter_helper


class K8sPodInfo():
    def __init__(self):
        self.pod = None

    def get_pod_networks_info(self, pod_mo):
        networks = []

        if 'annotations' in pod_mo['metadata'] and pod_mo['metadata']['annotations'] is not None:
            for annotation in pod_mo['metadata']['annotations']:
                if annotation == 'k8s.v1.cni.cncf.io/networks-status':
                    try:
                        networks = json.loads(
                            pod_mo['metadata']['annotations'][annotation]
                        )
                    except BaseException:
                        pass

        return networks

    def get_pod_info(self, pod_mo):
        info = copy.deepcopy(pod_mo)
        info['networks'] = self.get_pod_networks_info(
            pod_mo
        )
        return info

    def get_pods_info(self, cache=True):
        if cache and self.pod is not None:
            return self.pod

        pods_mo = self.get_pods_mo(cache=cache)
        if pods_mo is None:
            return None

        self.pod = []
        for pod_mo in pods_mo:
            self.pod.append(
                self.get_pod_info(
                    pod_mo
                )
            )

        self.log.k8s_mo(
            'pod.info',
            self.pod
        )

        return self.pod

    def match_pod(self, pod_info, pod_filter):
        if pod_filter is None or len(pod_filter) == 0:
            return True

        for ap_rule in pod_filter:
            key = ap_rule.split(':')[0]
            value = ':'.join(ap_rule.split(':')[1:])

            if key == 'namespace':
                if not filter_helper.match_string(value, pod_info['metadata']['namespace']):
                    return False

            if key == 'name':
                if not filter_helper.match_string(value, pod_info['metadata']['name']):
                    return False

            if key == 'label':
                if 'labels' not in pod_info['metadata']:
                    return False

                if pod_info['metadata']['labels'] is None:
                    return False

                found = False
                for label in pod_info['metadata']['labels']:
                    if filter_helper.match_string(value.split(':', maxsplit=1)[0], label):
                        if filter_helper.match_string(value.split(':')[1], pod_info['metadata']['labels'][label]):
                            found = True

                if not found:
                    return False

            if key == 'mac':
                found = False
                for network in pod_info['networks']:
                    if 'mac' in network:
                        if filter_helper.match_string(value, network['mac']):
                            found = True

                if not found:
                    return False

            if key == 'network':
                found = False
                for network in pod_info['networks']:
                    if 'mac' in network:
                        if filter_helper.match_string(value, network['name']):
                            found = True

                if not found:
                    return False

        return True

    def get_pods(self, pod_filter=None, cache=True):
        all_pods = self.get_pods_info(cache=cache)
        if all_pods is None:
            return None

        pods = []
        for pod_info in all_pods:
            if not self.match_pod(pod_info, pod_filter):
                continue

            pods.append(
                pod_info
            )

        return pods

    # def get_pod_replicaset_info(self, pod_id):
    #     try:
    #         data = dict()

    #         pod = self.get_pod_summary(self.get_pod(pod_id))
    #         if pod is None:
    #             return None

    #         replicaset_name = pod['replicaset_name']
    #         data['name'] = replicaset_name
    #         if data['name'] is not None:
    #             data['data'] = self.get_replica_set(
    #                 replicaset_name,
    #                 pod['namespace'],
    #                 summary = True
    #             )
    #             data['pods'] = self.get_pods_with_replica_set(
    #                 replicaset_name,
    #                 exclude_pod_id = pod_id
    #             )

    #     except:
    #         self.log.error('k8s_pods.get_pod_replicaset_info', traceback.format_exc())

    #     return data

    # def get_pod_replicaset_name(self, pod):
    #     try:
    #         for owner_reference in pod['metadata']['owner_references']:
    #             if owner_reference['kind'] == 'ReplicaSet':
    #                 return owner_reference['name']
    #     except:
    #         self.log.error('k8s_pods.get_pod_replicaset_name', traceback.format_exc())
    #     return None

    # def is_pod_ready(self, pod):
    #     try:
    #         ready = True

    #         if pod['status']['conditions'] is None:
    #             return False

    #         for c in pod['status']['conditions']:
    #             if c['type'] == 'Ready':
    #                 if c['status'] != 'True':
    #                     ready = False

    #     except:
    #         self.log.error('k8s_pods.is_pod_ready', traceback.format_exc())
    #         self.log.error('k8s_pods.is_pod_ready', pod)
    #         return False

    #     return ready

    # def get_pod_job(self, pod):
    #     try:
    #         for owner_reference in pod['metadata']['owner_references']:
    #             if owner_reference['kind'] == 'Job':
    #                 return owner_reference['name']

    #     except:
    #         self.log.error('k8s_pods.get_pod_job', traceback.format_exc())
    #         self.log.error('k8s_pods.get_pod_job', pod)

    #     return None

    # def is_pod_scheduled(self, pod):
    #     try:
    #         scheduled = True

    #         if pod['status']['conditions'] is None:
    #             return False

    #         for c in pod['status']['conditions']:
    #             if c['type'] == 'PodScheduled':
    #                 if c['status'] != 'True':
    #                     scheduled = False

    #     except:
    #         self.log.error('k8s_pods.is_pod_scheduled', traceback.format_exc())
    #         self.log.error('k8s_pods.is_pod_scheduled', pod)
    #         return False

    #     return scheduled

    # def get_pod_scheduling_problem(self, node_labels, node_selector):
    #     try:
    #         scheduling_problem = None
    #         if node_selector is not None:
    #             for s in node_selector:
    #                 if s['match_expressions'] is not None:
    #                     for m in s['match_expressions']:
    #                         if m['operator'] == 'In':
    #                             k = m['key']
    #                             for v in m['values']:
    #                                 node_exists = False
    #                                 for label in node_labels:
    #                                     if label['key'] == k and label['value'] == v:
    #                                         node_exists = True

    #                                 if not node_exists:
    #                                     scheduling_problem = 'No node with label %s:%s' % (k, v)

    #     except:
    #         self.log.error('k8s_pods.get_pod_scheduling_problem', traceback.format_exc())
    #         return None

    #     return scheduling_problem

    # def are_pods_scheduled(self, pods):
    #     try:
    #         scheduled = True
    #         for p in pods:
    #             scheduled = scheduled and p['scheduled']
    #             if not scheduled:
    #                 break

    #     except:
    #         self.log.error('k8s_pods.are_pods_scheduled', traceback.format_exc())
    #         return False

    #     return scheduled

    # def get_pods_ready_count(self):
    #     count = 0
    #     try:
    #         for p in self.pods:
    #             if p['ready']:
    #                 count = count + 1

    #     except:
    #         self.log.error('k8s_pods.get_pods_ready_count', traceback.format_exc())

    #     return count

    # def get_pods_status_summary(self, pods):
    #     try:
    #         status = dict()
    #         for p in pods:
    #             if p['job_name'] is None:
    #                 if p['ready']:
    #                     if 'Ready' in status:
    #                         status['Ready'] = status['Ready'] + 1
    #                     else:
    #                         status['Ready'] = 1

    #                 if not p['ready']:
    #                     if 'Not Ready' in status:
    #                         status['Not Ready'] = status['Not Ready'] + 1
    #                     else:
    #                         status['Not Ready'] = 1

    #             if p['job_name'] is not None:
    #                 if p['job_succeeded']:
    #                     if 'Succeeded' in status:
    #                         status['Succeeded'] = status['Succeeded'] + 1
    #                     else:
    #                         status['Succeeded'] = 1
    #                 else:
    #                     if 'Not Succeeded' in status:
    #                         status['Not Succeeded'] = status['Not Succeeded'] + 1
    #                     else:
    #                         status['Not Succeeded'] = 1

    #         summary = []
    #         for s in status:
    #             summary.append(dict(status=s, count=status[s]))

    #         summary = sorted(summary, key = lambda i: i['status'])

    #     except:
    #         self.log.error('k8s_pods.get_pods_status_summary', traceback.format_exc())
    #         return None

    #     return summary

    # def get_pod_container_summary(self, pod, job_name):
    #     '''
    #         {
    #             "ready": 1,
    #             "completed": 0,
    #             "count": 1,
    #             "restarts": 0,
    #             "reasons": []
    #         }
    #     '''
    #     summary = dict()
    #     summary['ready'] = 0
    #     summary['completed'] = 0
    #     summary['count'] = 0
    #     summary['restarts'] = 0
    #     summary['reasons'] = []

    #     if pod['status']['container_statuses'] is not None:
    #         for c in pod['status']['container_statuses']:
    #             summary['count'] = summary['count'] + 1
    #             summary['restarts'] = summary['restarts'] + c['restart_count']
    #             if c['ready']:
    #                 summary['ready'] = summary['ready'] + 1
    #             else:
    #                 try:
    #                     reason = c['state']['waiting']['reason']
    #                     if reason is not None and reason not in summary['reasons']:
    #                         summary['reasons'].append(reason)
    #                 except:
    #                     pass

    #             if job_name is not None:
    #                 try:
    #                     if c['state']['terminated']['reason'] == 'Completed':
    #                         summary['completed'] = summary['completed'] + 1
    #                 except:
    #                     pass

    #     return summary

    # def get_pod_summary(self, pod):
    #     '''
    #     {
    #         "namespace": "iks",
    #         "labels": {
    #             "app.kubernetes.io/component": "controller",
    #             "app.kubernetes.io/instance": "essential-nginx-ingress",
    #             "app.kubernetes.io/name": "ingress-nginx",
    #             "controller-revision-hash": "794954b8c6",
    #             "pod-template-generation": "1"
    #         },
    #         "name": "essential-nginx-ingress-ingress-nginx-controller-2nk8m",
    #         "uid": "8b2bcc15-da82-4092-9381-71ffca698158",
    #         "age": 249258,
    #         "node": "milan-kali-worker-4078840427",
    #         "replicaset_name": null,
    #         "scheduled": true,
    #         "status": "Running",
    #         "ready": true,
    #         "pod_ip": "100.64.208.72",
    #         "cni": {
    #             "ip": "100.64.208.72",
    #             "ports": [
    #                 {
    #                     "container_port": 80,
    #                     "host_ip": null,
    #                     "host_port": null,
    #                     "name": "http",
    #                     "protocol": "TCP"
    #                 },
    #                 {
    #                     "container_port": 443,
    #                     "host_ip": null,
    #                     "host_port": null,
    #                     "name": "https",
    #                     "protocol": "TCP"
    #                 }
    #             ]
    #         },
    #         "job_name": null,
    #         "job_succeeded": false,
    #         "healthy": true,
    #         "containers": {
    #             "ready": 1,
    #             "completed": 0,
    #             "count": 1,
    #             "restarts": 0,
    #             "reasons": []
    #         },
    #         "node_selector": [
    #             {
    #                 "match_expressions": null,
    #                 "match_fields": [
    #                     {
    #                         "key": "metadata.name",
    #                         "operator": "In",
    #                         "values": [
    #                             "milan-kali-worker-4078840427"
    #                         ]
    #                     }
    #                 ]
    #             }
    #         ],
    #         "scheduling_problem": null
    #     }
    #     '''
    #     try:
    #         summary = dict()

    #         summary['namespace'] = pod['metadata']['namespace']
    #         summary['labels'] = pod['metadata']['labels']
    #         summary['name'] = pod['metadata']['name']
    #         summary['uid'] = pod['metadata']['uid']
    #         summary['age'] = int(time.time()) - pod['metadata']['creation_timestamp']
    #         summary['node'] = pod['spec']['node_name']
    #         summary['replicaset_name'] = self.get_pod_replicaset_name(pod)

    #         summary['scheduled'] = self.is_pod_scheduled(pod)
    #         summary['status'] = pod['status']['phase']
    #         summary['ready'] = self.is_pod_ready(pod)

    #         summary['pod_ip'] = pod['status']['pod_ip']
    #         summary['cni'] = None
    #         cni = self.get_pod_calico_ip(pod['metadata']['uid'], pod=pod)
    #         if cni is not None:
    #             summary['cni'] = dict()
    #             summary['cni']['ip'] = cni['ip']
    #             summary['cni']['ports'] = cni['ports']

    #         summary['job_name'] = self.get_pod_job(pod)
    #         summary['job_succeeded'] = False
    #         summary['healthy'] = False
    #         if summary['ready']:
    #             summary['healthy'] = True
    #         if not summary['ready'] and summary['job_name'] is not None and summary['status'] == 'Succeeded':
    #             summary['job_succeeded'] = True
    #             summary['healthy'] = True

    #         summary['containers'] = self.get_pod_container_summary(pod, summary['job_name'])

    #         try:
    #             summary['node_selector'] = pod['spec']['affinity']['node_affinity']['required_during_scheduling_ignored_during_execution']['node_selector_terms']
    #         except:
    #             summary['node_selector'] = None

    #         summary['scheduling_problem'] = None
    #         if summary['node_selector'] is not None:
    #             labels = self.get_nodes_labels()
    #             summary['scheduling_problem'] = self.get_pod_scheduling_problem(labels, summary['node_selector'])

    #     except:
    #         self.log.error('k8s_pods.get_pod_summary', traceback.format_exc())
    #         self.log.error('k8s_pods.get_pod_summary', pod)
    #         return None

    #     return summary

    # def get_pods_namespaces(self):
    #     namespaces = dict()
    #     try:
    #         for p in self.pods:
    #             namespace = p['namespace']
    #             if namespace not in namespaces:
    #                 namespaces[namespace] = dict()

    #     except:
    #         self.log.error('k8s_pods.get_pods_namespaces', traceback.format_exc())

    #     return namespaces

    # def get_pods_in_namespace(self, namespace):
    #     pods = []
    #     try:
    #         for p in self.pods:
    #             if p['namespace'] == namespace:
    #                 pods.append(p)

    #     except:
    #         self.log.error('k8s_pods.get_pods_in_namespace', traceback.format_exc())

    #     return pods

    # def get_pod_nodes(self, pods=None):
    #     nodes = []
    #     try:
    #         for p in self.pods:
    #             if p['node'] not in nodes:
    #                 nodes.append(p['node'])

    #     except:
    #         self.log.error('k8s_pods.get_pod_nodes', traceback.format_exc())

    #     return nodes

    # def get_pod_id(self, namespace, name, cache=True):
    #     try:
    #         for p in self.pods:
    #             if p['metadata']['name'] == name and p['metadata']['namespace'] == namespace:
    #                 return p['metadata']['uid']
    #     except:
    #         self.log.error('k8s_pods.get_pod_id', traceback.format_exc())
    #     return None

    # def get_pod(self, pod_id, cache=True, nice=True, events=False):
    #     try:
    #         for p in self.pods:
    #             if p['metadata']['uid'] == pod_id:
    #                 if not nice:
    #                     return p

    #                 info = dict()
    #                 info['pod'] = p
    #                 info['summary'] = self.get_pod_summary(p)
    #                 info['timestamp'] = self.get_pods_cache_timestamp()
    #                 info['age'] = int(time.time()*1000) - info['timestamp']

    #                 if events:
    #                     field_selector = 'involvedObject.uid=%s' % (
    #                         info['summary']['uid']
    #                     )
    #                     info['events'] = self.get_namespace_events(
    #                         info['summary']['namespace'],
    #                         field_selector = field_selector
    #                     )

    #                 return info

    #     except:
    #         self.log.error('k8s_pods.get_pod', traceback.format_exc())

    #     return None

    # def get_pods_state(self, summary_only=False):
    #     try:
    #         pods = self.get_pods_summary()
    #         if pods is None:
    #             return None

    #         state = dict()
    #         state['summary'] = dict()
    #         state['summary']['count'] = pods['count']
    #         state['summary']['ready'] = pods['ready']
    #         state['summary']['job_succeeded'] = pods['job_succeeded']
    #         state['summary']['healthy'] = pods['healthy']
    #         state['summary']['scheduled'] = pods['scheduled']
    #         state['summary']['functional'] = False
    #         if state['summary']['count'] > 0:
    #             if state['summary']['count'] == state['summary']['healthy']:
    #                 if state['summary']['count'] == state['summary']['scheduled']:
    #                     state['summary']['functional'] = True

    #         state['summary']['status'] = pods['status']

    #         if summary_only:
    #             return state['summary']

    #         state['pods'] = pods['pods']

    #         state['namespaces'] = self.get_pods_namespaces()
    #         for n in state['namespaces']:
    #             npods = self.get_pods_in_namespace(n)
    #             state['namespaces'][n]['pods'] = npods
    #             state['namespaces'][n]['summary'] = dict()
    #             state['namespaces'][n]['summary']['count'] = len(npods)
    #             state['namespaces'][n]['summary']['status'] = self.get_pods_status_summary(npods)
    #             state['namespaces'][n]['summary']['scheduled'] = self.are_pods_scheduled(npods)
    #             state['namespaces'][n]['nodes'] = self.get_pod_nodes(pods=npods)

    #     except:
    #         self.log.error('k8s_pods.get_pods_state', traceback.format_exc())
    #         return None

    #     return state

    # def get_pods_calico_ip(self, cache=True):
    #     try:
    #         pods = self.get_pods(cache=cache)
    #         if pods is None:
    #             return None

    #         ip = []
    #         for p in pods:
    #             try:
    #                 i = dict()
    #                 i['pod'] = p['metadata']['name']
    #                 i['pod_id'] = p['metadata']['uid']
    #                 i['node'] = p['spec']['node_name']
    #                 i['ip'] = p['metadata']['annotations']['cni.projectcalico.org/podIP'].split('/')[0]
    #                 i['ports'] = []
    #                 for c in p['spec']['containers']:
    #                     if c['ports'] is not None:
    #                         i['ports'] = i['ports'] + c['ports']

    #                 ip.append(i)

    #             except:
    #                 pass

    #     except:
    #         self.log.error('k8s_pods.get_pods_calico_ip', traceback.format_exc())
    #         return None

    #     return ip

    # def get_pod_calico_ip(self, pod_id, pod=None, cache=True):
    #     try:
    #         if pod is None:
    #             pods = self.get_pods(cache=cache)
    #             if pods is None:
    #                 return None

    #             for p in pods:
    #                 if p['metadata']['uid'] == pod_id:
    #                     pod = p

    #         if pod is None:
    #             self.log.error('k8s_pods.get_pod_calico_ip', 'POD not found: %s' % (pod_id))
    #             return None

    #         cni = dict()
    #         cni['pod'] = pod['metadata']['name']
    #         cni['pod_id'] = pod['metadata']['uid']
    #         cni['node'] = pod['spec']['node_name']
    #         try:
    #             cni['ip'] = pod['metadata']['annotations']['cni.projectcalico.org/podIP'].split('/')[0]
    #         except:
    #             return None

    #         cni['ports'] = []
    #         for c in pod['spec']['containers']:
    #             if c['ports'] is not None:
    #                 cni['ports'] = cni['ports'] + c['ports']

    #     except:
    #         self.log.error('k8s_pods.get_pod_calico_ip', traceback.format_exc())
    #         return None

    #     return cni

    # def get_pods_summary(self, namespaces=None):
    #     try:
    #         my_pods = []
    #         for p in self.pods:
    #             pod = self.get_pod_summary(p)
    #             if pod is not None:
    #                 if namespaces is None or pod['namespace'] in namespaces:
    #                     my_pods.append(pod)

    #         summary = dict()
    #         summary['count'] = len(my_pods)
    #         summary['scheduled'] = 0
    #         summary['ready'] = 0
    #         summary['job_succeeded'] = 0
    #         summary['healthy'] = 0
    #         summary['status'] = self.get_pods_status_summary(my_pods)

    #         for pod in my_pods:
    #             if pod['ready']:
    #                 summary['ready'] = summary['ready'] + 1
    #             if pod['job_name'] is not None and pod['job_succeeded']:
    #                 summary['job_succeeded'] = summary['job_succeeded'] + 1
    #             if pod['scheduled']:
    #                 summary['scheduled'] = summary['scheduled'] + 1
    #             if pod['healthy']:
    #                 summary['healthy'] = summary['healthy'] + 1

    #         summary['functional'] = False
    #         if summary['count'] > 0 and summary['count'] == summary['healthy']:
    #             summary['functional'] = True

    #     except:
    #         self.log.error('k8s_pods.get_pods_summary', traceback.format_exc())
    #         return None

    #     return summary

    # def get_pods_health_summary(self, namespaces=None):
    #     try:
    #         my_pods = []
    #         for p in self.pods:
    #             pod = self.get_pod_summary(p)
    #             if pod is not None:
    #                 if namespaces is None or pod['namespace'] in namespaces:
    #                     my_pods.append(pod)

    #         return self.get_selected_pods_health_summary(my_pods)
    #     except:
    #         self.log.error('k8s_pods.get_pods_summary', traceback.format_exc())
    #         return None

    # def get_selected_pods_health_summary(self, my_pods, no_pods_unhealthy = True):
    #     '''
    #         {
    #             "pods_count": 63,
    #             "pods_scheduled": 63,
    #             "pods_ready": 46,
    #             "pods_job_succeeded": 13,
    #             "pods_all_good": 59,
    #             "pods_healthy": false,
    #             "pods_status": [
    #                 {
    #                     "status": "Not Ready",
    #                     "count": 4
    #                 },
    #                 {
    #                     "status": "Ready",
    #                     "count": 46
    #                 },
    #                 {
    #                     "status": "Succeeded",
    #                     "count": 13
    #                 }
    #             ]
    #         }
    #     '''
    #     try:
    #         summary = dict()
    #         summary['pods_count'] = len(my_pods)
    #         summary['pods_scheduled'] = 0
    #         summary['pods_ready'] = 0
    #         summary['pods_job_succeeded'] = 0
    #         summary['pods_all_good'] = 0
    #         summary['pods_status'] = self.get_pods_status_summary(my_pods)

    #         for pod in my_pods:
    #             if pod['ready']:
    #                 summary['pods_ready'] = summary['pods_ready'] + 1
    #             if pod['job_name'] is not None and pod['job_succeeded']:
    #                 summary['pods_job_succeeded'] = summary['pods_job_succeeded'] + 1
    #             if pod['scheduled']:
    #                 summary['pods_scheduled'] = summary['pods_scheduled'] + 1
    #             if pod['healthy']:
    #                 summary['pods_all_good'] = summary['pods_all_good'] + 1

    #         summary['pods_healthy'] = True
    #         if summary['pods_count'] == 0 and no_pods_unhealthy:
    #             summary['pods_healthy'] = False
    #         if summary['pods_all_good'] < summary['pods_count']:
    #             summary['pods_healthy'] = False

    #         summary['pods_state_summary'] = '%s/%s' % (
    #             summary['pods_count'],
    #             summary['pods_all_good']
    #         )

    #     except:
    #         self.log.error('k8s_pods.get_pods_summary', traceback.format_exc())
    #         return None

    #     return summary

    # def get_pod_logs(self, name, namespace):
    #     # https://github.com/kubernetes-client/python/blob/master/kubernetes/docs/CoreV1Api.md#list_secret_for_all_namespaces
    #     try:
    #         start_time = int(time.time()*1000)
    #         response = self.api.read_namespaced_pod_log(name=name, namespace=namespace)
    #         self.api_statistics(
    #             'read_namespaced_pod_log:%s:%s' % (namespace, name),
    #             int(time.time()*1000) - start_time
    #         )

    #     except:
    #         self.log.error('k8s_pods.get_pod_logs', traceback.format_exc())
    #         return None

    #     return response
