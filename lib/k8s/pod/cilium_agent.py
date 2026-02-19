import traceback
import json
from lib import filter_helper


class K8sPodCiliumAgent():
    def __init__(self):
        pass

    def is_pod_cilium_agent(self, pod):
        if 'metadata' in pod:
            labels_mo = filter_helper.get(pod, 'metadata:labels')
            if labels_mo is not None:
                if 'app.kubernetes.io/name' in labels_mo:
                    if labels_mo['app.kubernetes.io/name'] == 'cilium-agent':
                        return True
                    
        if 'metadata' not in pod:
            if 'app.kubernetes.io/name' in pod['label']:
                if pod['label']['app.kubernetes.io/name'] == 'cilium-agent':
                    return True
                            
        return False
   
    def get_cilium_agent_pod_map(self, cache_enabled=True):
        pods = self.get_cilium_agent_pods(cache_enabled=cache_enabled)
        if pods is None:
            return None
        
        pod_map = {}
        for pod in pods:
            pod_map[pod['host_name']] = pod['name']

        return pod_map
    
    def get_any_cilium_agent_pod_name(self, cache_enabled=True):
        pods = self.get_cilium_agent_pods(cache_enabled=cache_enabled)
        if pods is None:
            return None
        
        for pod in pods:
            if pod['running']:
                return pod['name']
            
        return None
    
    def get_cilium_agent_pods_name(self, cache_enabled=True):
        pods = self.get_cilium_agent_pods(cache_enabled=cache_enabled)
        if pods is None:
            return None
        
        names = []
        for pod in pods:
            names.append(pod['name'])

        return names

    def get_cilium_agent_pods(self, return_mo=False, cache_enabled=False):
        pods = self.get_pods(
            namespace=self.cilium_namespace,
            return_mo=return_mo,
            cache_enabled=cache_enabled
        )
        if pods is None:
            return None
        
        cilium_pods = []
        for pod in pods:
            if not self.is_pod_cilium_agent(pod=pod):
                continue
            cilium_pods.append(pod)

        return cilium_pods
    
    def get_cilium_agent_pods_image(self, cache_enabled=True):
        pods = self.get_cilium_agent_pods(
            return_mo=True,
            cache_enabled=cache_enabled
        )
        if pods is None:
            return None
        
        image = {}
        for pod in pods:
            pod_name = filter_helper.get(pod, 'metadata:name')
            containers_mo = filter_helper.get(pod, 'spec:containers')
            if containers_mo is None:
                continue
            for container_mo in containers_mo:
                cname = filter_helper.get(container_mo, 'name')
                if cname is None:
                    continue

                if cname != 'cilium-agent':
                    continue

                image[pod_name] = filter_helper.get(container_mo, 'image')

        return image
    
    def is_cilium_agent_pod_image_hash(self, image_hash, cache_enabled=True):
        image = self.get_cilium_agent_pods_image(cache_enabled=cache_enabled)
        if image is None:
            return False
        
        for pod in image:
            pod_image_hash = image[pod].split(':')[1].split('@')[0]
            if pod_image_hash != image_hash:
                return False
            
        return True

    def get_cilium_agent_db(self, db_name, name=None, cache_enabled=True, cast_json=False):
        if name is None:
            name = self.get_any_cilium_agent_pod_name(cache_enabled=cache_enabled)
        
        if name is None:
            return None
        
        if cast_json:
            content = self.get_pod_exec(
                self.cilium_namespace,
                name,
                ['cilium', 'shell', 'db/show', '%s -f json' % (db_name)]
            )
            try:
                output = json.loads(filter_helper.json_fixup(content))
            except BaseException:
                self.log.error('get_cilium_agent_db', str(db_name))
                self.log.error('get_cilium_agent_db', str(content))
                self.log.error('get_cilium_agent_db', traceback.format_exc())
                output = None
        else:
            output = self.get_pod_exec(
                self.cilium_namespace,
                name,
                'cilium shell db/show %s' % (db_name)
            )

        return output
    
    def get_cilium_agent_dbs(self, db_names, name=None, cache_enabled=True, cast_json=False):
        if name is None:
            name = self.get_any_cilium_agent_pod_name(cache_enabled=cache_enabled)
        
        if name is None:
            return None
        
        response = {}
        for db_name in db_names:
            response[db_name] = self.get_cilium_agent_db(
                db_name,
                name=name,
                cast_json=cast_json
            )

        return response

    def get_cilium_agent_status(self, name=None, cache_enabled=True):
        if name is not None:
            names = [name]
        else:
            names = self.get_cilium_agent_pods_name(cache_enabled=cache_enabled)
        
        if names is None:
            return None
        
        status = []

        for name in names:
            content = self.get_pod_exec(
                self.cilium_namespace,
                name,
                ['cilium', 'status', '-o', 'json']
            )
            try:
                output = json.loads(filter_helper.json_fixup(content))
            except BaseException:
                self.log.error('get_cilium_agent_status', str(name))
                self.log.error('get_cilium_agent_db', str(content))
                self.log.error('get_cilium_agent_db', traceback.format_exc())
                continue

            output[0]['agent'] = name
            status.append(output[0])

        return status

    def get_cilium_agent_logs(self, agent=None, cache_enabled=False):
        pods = self.get_cilium_agent_pods(cache_enabled=cache_enabled)
        if pods is None:
            return None
        
        target_pods = []
        for pod in pods:
            if agent is not None and pod['name'] != agent:
                continue

            target_pods.append(pod)

        for pod in target_pods:
            pod['logs'] = self.get_pod_log_mo(
                pod['namespace'],
                pod['name'],
                cache_enabled=False
            )
            
        return target_pods
    