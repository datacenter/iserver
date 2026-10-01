import yaml
from lib import filter_helper


def base():
    return """
apiVersion: kubevirt.io/v1
kind: VirtualMachine
metadata:
  name: ${NAME}
  namespace: ${NAMESPACE}
  labels:
    app: ${NAME}
spec:
  dataVolumeTemplates:
    - apiVersion: cdi.kubevirt.io/v1beta1
      kind: DataVolume
      metadata:
        name: ${NAME}
        namespace: ${NAMESPACE}
      spec:
        pvc:
          accessModes:
            - ReadWriteOnce
          resources:
            requests:
              storage: 500Mi
          volumeMode: Filesystem
        source:
          registry:
            url: "docker://quay.io/kubevirt/cirros-container-disk-demo"
  runStrategy: Always
  template:
    metadata:
      labels:
        kubevirt.io/domain: ${NAME}
    spec:
      domain:
        cpu:
          cores: ${CORE}
          sockets: ${SOCKET}
          threads: ${THREAD}
        devices:
          disks:
          - disk:
              bus: virtio
            name: rootdisk
          interfaces:
          - masquerade: {}
            name: default
          rng: {}
        resources:
          requests:
            memory: ${MEMORY}Gi
      evictionStrategy: LiveMigrate
      hostname: ${NAME}
      networks:
      - name: default
        pod: {}
      volumes:
        - dataVolume:
            name: ${NAME}
          name: rootdisk
    """

def get(params, my_output):
    metadata = {}
    metadata['dv'] = dict(namespace=params['namespace'], name=params['name'])

    content = filter_helper.replace_attributes(base(), params['variables'])
    leftover = filter_helper.get_content_attributes(content)
    if len(leftover) > 0:
       my_output.error('Not all variables replaced: %s' % (', '.join(leftover)))
       return None, None
    
    try:
        content = yaml.safe_load(content)
    except BaseException:
        my_output.error('Template load failed')
        return None, None
    
    return content, metadata