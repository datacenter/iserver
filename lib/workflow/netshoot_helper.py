import os
import yaml
from lib import filter_helper


def is_netshoots(params):
    pods = get_netshoots(params)
    if pods is None:
        return False
    return True


def get_netshoots(params):
    namespace = os.environ.get('NAMESPACE')
    if namespace is None:
        namespace = 'default'
    name = 'cd-netshoot'

    netshoots = params['k8s_handler'].get_daemon_set_resources(namespace, name, cache_enabled=False, brief=False)
    pods = filter_helper.get(netshoots, 'pod')
    if pods is None:
        return None

    info = {}
    for pod in pods:
        info[pod['host_name']] = dict(namespace=pod['namespace'], name=pod['name'])
    
    return info


def create_netshoots(params, my_output=None):
    namespace = os.environ.get('NAMESPACE')
    if namespace is None:
        namespace = 'default'
    name = 'cd-netshoot'

    body = """apiVersion: apps/v1
kind: DaemonSet
metadata:
  namespace: %s
  name: %s
spec:
  selector:
    matchLabels:
      name: cd-netshoot
  template:
    metadata:
      labels:
        name: cd-netshoot
    spec:
      hostNetwork: true
      containers:
      - name: netshoot
        image: nicolaka/netshoot:latest
        command:
        - sleep
        - infinite
      securityContext:
        runAsUser: 0
        capabilities:
          add: ["IPC_LOCK","SYS_RESOURCE","NET_RAW", "NET_ADMIN"]
""" % (namespace, name)

    if my_output is not None:
        my_output.default('Deploy netshoot daemonset with host networking', underline=True)
        my_output.default(body, wrap='~~~')

    if params['k8s_handler'].is_daemon_set(namespace, name, cache_enabled=False):
        if my_output is not None:
            my_output.default('DaemonSet already exists')
        if not params['k8s_handler'].is_daemon_set_ready(namespace, name, cache_enabled=True):
            if my_output is not None:
                my_output.error('DaemonSet not ready')
            return None

        params['netshoot'] = get_netshoots(params)
        params['netshoot_created'] = False
    else:
        success, _ = params['k8s_handler'].create_resource(yaml.safe_load(body), my_output=my_output)
        if not success:
            if my_output is not None:
                my_output.error('DaemonSet create REST API failed')
            return None

        if my_output is not None:
            my_output.default('DaemonSet created')

        success = params['k8s_handler'].wait_daemon_set_ready_state(namespace, name, max_time=600, my_output=my_output)
        if not success:
            return None

        params['netshoot'] = get_netshoots(params)
        params['netshoot_created'] = True

    if my_output is not None:
        my_output.default('Netshoots')
        for hostname in params['netshoot']:
            my_output.default('- %s: %s/%s' % (hostname, params['netshoot'][hostname]['namespace'], params['netshoot'][hostname]['name']))

    return params


def delete_netshoots(params, my_output=None):
    namespace = os.environ.get('NAMESPACE')
    if namespace is None:
        namespace = 'default'
    name = 'cd-netshoot'

    if my_output is not None:
        my_output.default('Undeploy netshoot daemonset with host networking: %s/%s' % (namespace, name), underline=True)

    if not params['k8s_handler'].is_daemon_set(namespace, name, cache_enabled=False):
        if my_output is not None:
            my_output.default('DaemonSet already deleted')
        return True
    
    success, _ = params['k8s_handler'].delete_resource('DaemonSet', 'apps/v1', name, namespace=namespace)
    if not success:
        if my_output is not None:
            my_output.error('DaemonSet delete REST API failed')
        return False

    success = params['k8s_handler'].wait_no_daemon_set(namespace, name, max_time=180, prompt='DaemonSet', my_output=my_output)
    if not success:
        return False
    
    return True


def get_netshoot_cli(params, cli, node_name=None, container=None):
    if 'netshoot' not in params or params['netshoot'] is None:
        return None

    output = {}

    for node in params['netshoot']:
        if node_name is not None and node_name != node:
            continue

        output[node] = params['k8s_handler'].get_pod_exec(
            params['netshoot'][node]['namespace'],
            params['netshoot'][node]['name'],
            cli.split(' '),
            container=container
        )            

    return output


def run_netshoot_cli(params, commands, node_name=None, container=None, my_output=None, always_delete=False):
    if 'netshoot' not in params:
        params = create_netshoots(params, my_output=my_output)
        if params is None:
            return None

    output = {}
    for cli in commands:
        output[cli['key']] = get_netshoot_cli(params, cli['cmd'], node_name=node_name, container=container)

    if params['netshoot_created'] and not always_delete or always_delete:
        delete_netshoots(params, my_output=my_output)

    return output    