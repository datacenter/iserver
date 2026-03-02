import json
from lib import output_helper
from lib.workflow.ocp_task import common
from lib.workflow.ocp_ai_operator import task as task_ai
from lib.workflow.ocp_cert_manager import task as task_cert_manager
from lib.workflow.ocp_cilium_bgp import task as task_cilium_bgp
from lib.workflow.ocp_cilium_cni import image_task as task_cilium_image
from lib.workflow.ocp_cilium_inb import task as task_cilium_inb
from lib.workflow.ocp_cilium_mesh import task as task_cilium_mesh
from lib.workflow.ocp_cilium_pnet import task as task_cilium_pnet
from lib.workflow.ocp_cilium_timescape import task as task_cilium_timescape
from lib.workflow.ocp_cli import task as task_cli
from lib.workflow.ocp_web_terminal_operator import task as task_cli_web
from lib.workflow.ocp_cnv_operator import task as task_cnv
from lib.workflow.ocp_gpu_operator import task as task_gpu
from lib.workflow.ocp_grafana_operator import task as task_grafana
from lib.workflow.ocp_identity import task as task_identity
from lib.workflow.ocp_imm import task as task_imm
from lib.workflow.ocp_iotel import task as task_iotel
from lib.workflow.ocp_local_storage_operator import task as task_lso
from lib.workflow.ocp_lvm_operator import task as task_lvm
from lib.workflow.ocp_minio_operator import task as task_minio
from lib.workflow.ocp_mtv_operator import task as task_mtv
from lib.workflow.ocp_nfd_operator import task as task_nfd
from lib.workflow.ocp_nfs_helm import task as task_nfs
from lib.workflow.ocp_nim_operator import task as task_nim
from lib.workflow.ocp_nmstate_operator import task as task_nmstate
from lib.workflow.ocp_odf_operator import task as task_odf
from lib.workflow.ocp_portworx_operator import task as task_portworx
from lib.workflow.ocp_prometheus import task as task_prometheus
from lib.workflow.ocp_serverless_operator import task as task_serverless
from lib.workflow.ocp_service_mesh_operator import task as task_service_mesh
from lib.workflow.ocp_sriov_operator import task as task_sriov
from lib.workflow.ocp_ssh import task as task_ssh
from lib.workflow.ocp_splunk_operator import task as task_splunk
from lib.workflow.ocp_tetragon_operator import task as task_tetragon
from lib.workflow.ocp_trident_operator import task as task_trident
from lib.workflow.ocp_vast_operator import task as task_vast
from lib.workflow.k8s import task as task_k8s


def validate(tasks, cluster_name, cluster_settings=None, k8s_handler=None, confirmation=True):
    if not isinstance(tasks, list):
        return None, 'tasks list required'
    
    for task in tasks:
        if not isinstance(task, dict):
            return None, 'tasks list of dict required'

    # cni
    # server
    supported_tasks = common.get_supported_tasks()
    new_tasks = []

    for task in tasks:
        for task_name in task:
            if task_name not in supported_tasks:
                return None, 'Unsupported task: %s' % (task_name)

            if task_name == 'cli':
                new_task, error = task_cli.validate_create(
                    task[task_name],
                    cluster_name,
                    confirmation,
                    cluster_settings=cluster_settings,
                    k8s_handler=k8s_handler
                )
                if new_task is None:
                    return None, 'Task cli: %s' % (error)

                new_tasks.append(
                    dict(cli=new_task)
                )

            if task_name == 'cli-web':
                new_task, error = task_cli_web.validate_create(
                    task[task_name],
                    cluster_name,
                    confirmation,
                    cluster_settings=cluster_settings,
                    k8s_handler=k8s_handler
                )
                if new_task is None:
                    return None, 'Task cli-web: %s' % (error)

                task_def = {}
                task_def['cli-web'] = new_task
                new_tasks.append(
                    task_def
                )

            if task_name == 'gpu':
                new_task, error = task_gpu.validate_create(
                    task[task_name],
                    cluster_name,
                    confirmation,
                    cluster_settings=cluster_settings,
                    k8s_handler=k8s_handler
                )
                if new_task is None:
                    return None, 'Task gpu: %s' % (error)

                new_tasks.append(
                    dict(gpu=new_task)
                )

            if task_name == 'serverless':
                new_task, error = task_serverless.validate_create(
                    task[task_name],
                    cluster_name,
                    confirmation,
                    cluster_settings=cluster_settings,
                    k8s_handler=k8s_handler
                )
                if new_task is None:
                    return None, 'Task serverless: %s' % (error)

                new_tasks.append(
                    dict(serverless=new_task)
                )

            if task_name == 'service-mesh':
                new_task, error = task_service_mesh.validate_create(
                    task[task_name],
                    cluster_name,
                    confirmation,
                    cluster_settings=cluster_settings,
                    k8s_handler=k8s_handler
                )
                if new_task is None:
                    return None, 'Task service-mesh: %s' % (error)
                
                task_def = {}
                task_def['service-mesh'] = new_task
                new_tasks.append(
                    task_def
                )

            if task_name == 'ai':
                new_task, error = task_ai.validate_create(
                    task[task_name],
                    cluster_name,
                    confirmation,
                    cluster_settings=cluster_settings,
                    k8s_handler=k8s_handler
                )
                if new_task is None:
                    return None, 'Task ai: %s' % (error)

                new_tasks.append(
                    dict(ai=new_task)
                )

            if task_name == 'nim':
                new_task, error = task_nim.validate_create(
                    task[task_name],
                    cluster_name,
                    confirmation,
                    cluster_settings=cluster_settings,
                    k8s_handler=k8s_handler
                )
                if new_task is None:
                    return None, 'Task nim: %s' % (error)

                new_tasks.append(
                    dict(nim=new_task)
                )

            if task_name == 'grafana':
                new_task, error = task_grafana.validate_create(
                    task[task_name],
                    cluster_name,
                    confirmation,
                    cluster_settings=cluster_settings,
                    k8s_handler=k8s_handler
                )
                if new_task is None:
                    return None, 'Task grafana: %s' % (error)

                new_tasks.append(
                    dict(grafana=new_task)
                )

            if task_name == 'prometheus':
                new_task, error = task_prometheus.validate_create(
                    task[task_name],
                    cluster_name,
                    confirmation,
                    cluster_settings=cluster_settings,
                    k8s_handler=k8s_handler
                )
                if new_task is None:
                    return None, 'Task prometheus: %s' % (error)

                new_tasks.append(
                    dict(prometheus=new_task)
                )

            if task_name == 'identity':
                new_task, error = task_identity.validate_create(
                    task[task_name],
                    cluster_name,
                    confirmation,
                    cluster_settings=cluster_settings,
                    k8s_handler=k8s_handler
                )
                if new_task is None:
                    return None, 'Task identity: %s' % (error)

                new_tasks.append(
                    dict(identity=new_task)
                )

            if task_name == 'imm':
                new_task, error = task_imm.validate_create(
                    task[task_name],
                    cluster_name,
                    confirmation,
                    cluster_settings=cluster_settings,
                    k8s_handler=k8s_handler
                )
                if new_task is None:
                    return None, 'Task imm: %s' % (error)

                new_tasks.append(
                    dict(imm=new_task)
                )

            if task_name == 'iotel':
                new_task, error = task_iotel.validate_create(
                    task[task_name],
                    cluster_name,
                    confirmation,
                    cluster_settings=cluster_settings,
                    k8s_handler=k8s_handler
                )
                if new_task is None:
                    return None, 'Task iotel: %s' % (error)

                new_tasks.append(
                    dict(iotel=new_task)
                )

            if task_name == 'lso':
                new_task, error = task_lso.validate_create(
                    task[task_name],
                    cluster_name,
                    confirmation,
                    cluster_settings=cluster_settings,
                    k8s_handler=k8s_handler
                )
                if new_task is None:
                    return None, 'Task lso: %s' % (error)

                new_tasks.append(
                    dict(lso=new_task)
                )

            if task_name == 'lvm':
                new_task, error = task_lvm.validate_create(
                    task[task_name],
                    cluster_name,
                    confirmation,
                    cluster_settings=cluster_settings,
                    k8s_handler=k8s_handler
                )
                if new_task is None:
                    return None, 'Task lvm: %s' % (error)

                new_tasks.append(
                    dict(lvm=new_task)
                )

            if task_name == 'minio':
                new_task, error = task_minio.validate_create(
                    task[task_name],
                    cluster_name,
                    confirmation,
                    cluster_settings=cluster_settings,
                    k8s_handler=k8s_handler
                )
                if new_task is None:
                    return None, 'Task minio: %s' % (error)

                new_tasks.append(
                    dict(minio=new_task)
                )

            if task_name == 'portworx':
                new_task, error = task_portworx.validate_create(
                    task[task_name],
                    cluster_name,
                    confirmation,
                    cluster_settings=cluster_settings,
                    k8s_handler=k8s_handler
                )
                if new_task is None:
                    return None, 'Task portworx: %s' % (error)

                new_tasks.append(
                    dict(portworx=new_task)
                )

            if task_name == 'vast':
                new_task, error = task_vast.validate_create(
                    task[task_name],
                    cluster_name,
                    confirmation,
                    cluster_settings=cluster_settings,
                    k8s_handler=k8s_handler
                )
                if new_task is None:
                    return None, 'Task vast: %s' % (error)

                new_tasks.append(
                    dict(vast=new_task)
                )

            if task_name == 'nfd':
                new_task, error = task_nfd.validate_create(
                    task[task_name],
                    cluster_name,
                    confirmation,
                    cluster_settings=cluster_settings,
                    k8s_handler=k8s_handler
                )
                if new_task is None:
                    return None, 'Task nfd: %s' % (error)

                new_tasks.append(
                    dict(nfd=new_task)
                )

            if task_name == 'nfs':
                new_task, error = task_nfs.validate_create(
                    task[task_name],
                    cluster_name,
                    confirmation,
                    cluster_settings=cluster_settings,
                    k8s_handler=k8s_handler
                )
                if new_task is None:
                    return None, 'Task nfs: %s' % (error)

                new_tasks.append(
                    dict(nfs=new_task)
                )

            if task_name == 'nmstate':
                new_task, error = task_nmstate.validate_create(
                    task[task_name],
                    cluster_name,
                    confirmation,
                    cluster_settings=cluster_settings,
                    k8s_handler=k8s_handler
                )
                if new_task is None:
                    return None, 'Task nmstate: %s' % (error)

                new_tasks.append(
                    dict(nmstate=new_task)
                )

            if task_name == 'odf':
                new_task, error = task_odf.validate_create(
                    task[task_name],
                    cluster_name,
                    confirmation,
                    cluster_settings=cluster_settings,
                    k8s_handler=k8s_handler
                )
                if new_task is None:
                    return None, 'Task odf: %s' % (error)

                new_tasks.append(
                    dict(odf=new_task)
                )

            if task_name == 'cnv':
                new_task, error = task_cnv.validate_create(
                    task[task_name],
                    cluster_name,
                    confirmation,
                    cluster_settings=cluster_settings,
                    k8s_handler=k8s_handler
                )
                if new_task is None:
                    return None, 'Task cnv: %s' % (error)

                new_tasks.append(
                    dict(cnv=new_task)
                )

            if task_name == 'mtv':
                new_task, error = task_mtv.validate_create(
                    task[task_name],
                    cluster_name,
                    confirmation,
                    cluster_settings=cluster_settings,
                    k8s_handler=k8s_handler
                )
                if new_task is None:
                    return None, 'Task mtv: %s' % (error)

                new_tasks.append(
                    dict(mtv=new_task)
                )

            if task_name == 'sriov':
                new_task, error = task_sriov.validate_create(
                    task[task_name],
                    cluster_name,
                    confirmation,
                    cluster_settings=cluster_settings,
                    k8s_handler=k8s_handler
                )
                if new_task is None:
                    return None, 'Task sriov: %s' % (error)

                new_tasks.append(
                    dict(sriov=new_task)
                )

            if task_name == 'ssh':
                new_task, error = task_ssh.validate_create(
                    task[task_name],
                    cluster_name,
                    confirmation,
                    cluster_settings=cluster_settings,
                    k8s_handler=k8s_handler
                )
                if new_task is None:
                    return None, 'Task ssh: %s' % (error)

                new_tasks.append(
                    dict(ssh=new_task)
                )

            if task_name == 'splunk':
                new_task, error = task_splunk.validate_create(
                    task[task_name],
                    cluster_name,
                    confirmation,
                    cluster_settings=cluster_settings,
                    k8s_handler=k8s_handler
                )
                if new_task is None:
                    return None, 'Task splunk: %s' % (error)

                new_tasks.append(
                    dict(splunk=new_task)
                )

            if task_name == 'tetragon':
                new_task, error = task_tetragon.validate_create(
                    task[task_name],
                    cluster_name,
                    confirmation,
                    cluster_settings=cluster_settings,
                    k8s_handler=k8s_handler
                )
                if new_task is None:
                    return None, 'Task tetragon: %s' % (error)

                new_tasks.append(
                    dict(tetragon=new_task)
                )

            if task_name == 'trident':
                new_task, error = task_trident.validate_create(
                    task[task_name],
                    cluster_name,
                    confirmation,
                    cluster_settings=cluster_settings,
                    k8s_handler=k8s_handler
                )
                if new_task is None:
                    return None, 'Task trident: %s' % (error)

                new_tasks.append(
                    dict(trident=new_task)
                )

            if task_name == 'cert-manager':
                new_task, error = task_cert_manager.validate_create(
                    task[task_name],
                    cluster_name,
                    confirmation,
                    cluster_settings=cluster_settings,
                    k8s_handler=k8s_handler
                )
                if new_task is None:
                    return None, 'Task cert-manager: %s' % (error)

                task_def = {}
                task_def['cert-manager'] = new_task
                new_tasks.append(
                    task_def
                )

            if task_name == 'cilium-image':
                new_task, error = task_cilium_image.validate_create(
                    task[task_name],
                    cluster_name,
                    confirmation,
                    cluster_settings=cluster_settings,
                    k8s_handler=k8s_handler
                )
                if new_task is None:
                    return None, 'Task cilium-image: %s' % (error)

                task_def = {}
                task_def['cilium-image'] = new_task
                new_tasks.append(
                    task_def
                )

            if task_name == 'cilium-bgp':
                new_task, error = task_cilium_bgp.validate_create(
                    task[task_name],
                    cluster_name,
                    confirmation,
                    cluster_settings=cluster_settings,
                    k8s_handler=k8s_handler
                )
                if new_task is None:
                    return None, 'Task cilium-bgp: %s' % (error)

                task_def = {}
                task_def['cilium-bgp'] = new_task
                new_tasks.append(
                    task_def
                )

            if task_name == 'cilium-timescape':
                new_task, error = task_cilium_timescape.validate_create(
                    task[task_name],
                    cluster_name,
                    confirmation,
                    cluster_settings=cluster_settings,
                    k8s_handler=k8s_handler
                )
                if new_task is None:
                    return None, 'Task cilium-timescape: %s' % (error)

                task_def = {}
                task_def['cilium-timescape'] = new_task
                new_tasks.append(
                    task_def
                )

            if task_name == 'cilium-mesh':
                new_task, error = task_cilium_mesh.validate_create(
                    task[task_name],
                    cluster_name,
                    confirmation,
                    cluster_settings=cluster_settings,
                    k8s_handler=k8s_handler
                )
                if new_task is None:
                    return None, 'Task cilium-mesh: %s' % (error)

                task_def = {}
                task_def['cilium-mesh'] = new_task
                new_tasks.append(
                    task_def
                )

            if task_name == 'cilium-pnet':
                new_task, error = task_cilium_pnet.validate_create(
                    task[task_name],
                    cluster_name,
                    confirmation,
                    cluster_settings=cluster_settings,
                    k8s_handler=k8s_handler
                )
                if new_task is None:
                    return None, 'Task cilium-pnet: %s' % (error)

                task_def = {}
                task_def['cilium-pnet'] = new_task
                new_tasks.append(
                    task_def
                )

            if task_name == 'cilium-inb':
                new_task, error = task_cilium_inb.validate_create(
                    task[task_name],
                    cluster_name,
                    confirmation,
                    cluster_settings=cluster_settings,
                    k8s_handler=k8s_handler
                )
                if new_task is None:
                    return None, 'Task cilium-inb: %s' % (error)

                task_def = {}
                task_def['cilium-inb'] = new_task
                new_tasks.append(
                    task_def
                )

            if task_name == 'k8s':
                new_task, error = task_k8s.validate_create(
                    task[task_name],
                    cluster_name,
                    confirmation,
                    cluster_settings=cluster_settings,
                    k8s_handler=k8s_handler
                )
                if new_task is None:
                    return None, 'Task k8s: %s' % (error)

                task_def = {}
                task_def['k8s'] = new_task
                new_tasks.append(
                    task_def
                )

    return new_tasks, None


def run(tasks, cluster_name, confirmation=True, cluster_settings=None, k8s_handler=None, validate_only=False, break_on_error=True, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    my_output.default('OpenShift Workflow - Create Tasks', before_newline=True, after_newline=True, double_underline=True)

    my_output.default('Validate Input', underline=True)
    resolved_tasks, error = validate(
        tasks,
        cluster_name,
        cluster_settings=cluster_settings,
        k8s_handler=k8s_handler,
        confirmation=confirmation
    )
    if resolved_tasks is None:
        my_output.error(error)    
        return False
    
    if validate_only:
        my_output.default(json.dumps(resolved_tasks, indent=4))
        return True

    my_output.default('Completed', after_newline=True)

    success = True
    supported_tasks = common.get_supported_tasks()
    for task in tasks:
        for task_name in task:
            if task_name not in supported_tasks:
                return None, 'Unsupported task: %s' % (task_name)

            if task_name == 'cli':
                task_success = task_cli.run(
                    task[task_name],
                    log_id=log_id
                )
                if break_on_error:
                    return False
                
                success = success and task_success

            if task_name == 'cli-web':
                task_success = task_cli_web.run(
                    task[task_name],
                    log_id=log_id
                )
                if break_on_error:
                    return False
                
                success = success and task_success

            if task_name == 'gpu':
                task_success = task_gpu.run(
                    task[task_name],
                    log_id=log_id
                )
                if break_on_error:
                    return False
                
                success = success and task_success

            if task_name == 'serverless':
                task_success = task_serverless.run(
                    task[task_name],
                    log_id=log_id
                )
                if break_on_error:
                    return False
                
                success = success and task_success

            if task_name == 'service-mesh':
                task_success = task_service_mesh.run(
                    task[task_name],
                    log_id=log_id
                )
                if break_on_error:
                    return False
                
                success = success and task_success

            if task_name == 'ai':
                task_success = task_ai.run(
                    task[task_name],
                    log_id=log_id
                )
                if break_on_error:
                    return False
                
                success = success and task_success

            if task_name == 'nim':
                task_success = task_nim.run(
                    task[task_name],
                    log_id=log_id
                )
                if break_on_error:
                    return False
                
                success = success and task_success

            if task_name == 'grafana':
                task_success = task_grafana.run(
                    task[task_name],
                    log_id=log_id
                )
                if break_on_error:
                    return False
                
                success = success and task_success

            if task_name == 'prometheus':
                task_success = task_prometheus.run(
                    task[task_name],
                    log_id=log_id
                )
                if break_on_error:
                    return False
                
                success = success and task_success

            if task_name == 'identity':
                task_success = task_identity.run(
                    task[task_name],
                    log_id=log_id
                )
                if break_on_error:
                    return False
                
                success = success and task_success

            if task_name == 'imm':
                task_success = task_imm.run(
                    task[task_name],
                    log_id=log_id
                )
                if break_on_error:
                    return False
                
                success = success and task_success

            if task_name == 'iotel':
                task_success = task_iotel.run(
                    task[task_name],
                    log_id=log_id
                )
                if break_on_error:
                    return False
                
                success = success and task_success

            if task_name == 'lso':
                task_success = task_lso.run(
                    task[task_name],
                    log_id=log_id
                )
                if break_on_error:
                    return False
                
                success = success and task_success

            if task_name == 'lvm':
                task_success = task_lvm.run(
                    task[task_name],
                    log_id=log_id
                )
                if break_on_error:
                    return False
                
                success = success and task_success

            if task_name == 'minio':
                task_success = task_minio.run(
                    task[task_name],
                    log_id=log_id
                )
                if break_on_error:
                    return False
                
                success = success and task_success

            if task_name == 'portworx':
                task_success = task_portworx.run(
                    task[task_name],
                    log_id=log_id
                )
                if break_on_error:
                    return False
                
                success = success and task_success

            if task_name == 'vast':
                task_success = task_vast.run(
                    task[task_name],
                    log_id=log_id
                )
                if break_on_error:
                    return False
                
                success = success and task_success

            if task_name == 'nfd':
                task_success = task_nfd.run(
                    task[task_name],
                    log_id=log_id
                )
                if break_on_error:
                    return False
                
                success = success and task_success

            if task_name == 'nfs':
                task_success = task_nfs.run(
                    task[task_name],
                    log_id=log_id
                )
                if break_on_error:
                    return False
                
                success = success and task_success

            if task_name == 'nmstate':
                task_success = task_nmstate.run(
                    task[task_name],
                    log_id=log_id
                )
                if break_on_error:
                    return False
                
                success = success and task_success

            if task_name == 'odf':
                task_success = task_odf.run(
                    task[task_name],
                    log_id=log_id
                )
                if break_on_error:
                    return False
                
                success = success and task_success

            if task_name == 'cnv':
                task_success = task_cnv.run(
                    task[task_name],
                    log_id=log_id
                )
                if break_on_error:
                    return False
                
                success = success and task_success

            if task_name == 'mtv':
                task_success = task_mtv.run(
                    task[task_name],
                    log_id=log_id
                )
                if break_on_error:
                    return False
                
                success = success and task_success

            if task_name == 'sriov':
                task_success = task_sriov.run(
                    task[task_name],
                    log_id=log_id
                )
                if break_on_error:
                    return False
                
                success = success and task_success

            if task_name == 'ssh':
                task_success = task_ssh.run(
                    task[task_name],
                    log_id=log_id
                )
                if break_on_error:
                    return False
                
                success = success and task_success

            if task_name == 'splunk':
                task_success = task_splunk.run(
                    task[task_name],
                    log_id=log_id
                )
                if break_on_error:
                    return False
                
                success = success and task_success

            if task_name == 'tetragon':
                task_success = task_tetragon.run(
                    task[task_name],
                    log_id=log_id
                )
                if break_on_error:
                    return False
                
                success = success and task_success

            if task_name == 'trident':
                task_success = task_trident.run(
                    task[task_name],
                    log_id=log_id
                )
                if break_on_error:
                    return False
                
                success = success and task_success

            if task_name == 'cert-manager':
                task_success = task_cert_manager.run(
                    task[task_name],
                    log_id=log_id
                )
                if break_on_error:
                    return False
                
                success = success and task_success

            if task_name == 'cilium-image':
                task_success = task_cilium_image.run(
                    task[task_name],
                    log_id=log_id
                )
                if break_on_error:
                    return False
                
                success = success and task_success

            if task_name == 'cilium-bgp':
                task_success = task_cilium_bgp.run(
                    task[task_name],
                    log_id=log_id
                )
                if break_on_error:
                    return False
                
                success = success and task_success

            if task_name == 'cilium-timescape':
                task_success = task_cilium_timescape.run(
                    task[task_name],
                    log_id=log_id
                )
                if break_on_error:
                    return False
                
                success = success and task_success

            if task_name == 'cilium-mesh':
                task_success = task_cilium_mesh.run(
                    task[task_name],
                    log_id=log_id
                )
                if break_on_error:
                    return False
                
                success = success and task_success

            if task_name == 'cilium-pnet':
                task_success = task_cilium_pnet.run(
                    task[task_name],
                    log_id=log_id
                )
                if break_on_error:
                    return False
                
                success = success and task_success
                
            if task_name == 'cilium-inb':
                task_success = task_cilium_inb.run(
                    task[task_name],
                    log_id=log_id
                )
                if break_on_error:
                    return False
                
                success = success and task_success

            if task_name == 'k8s':
                task_success = task_k8s.run(
                    task[task_name],
                    log_id=log_id
                )
                if break_on_error:
                    return False
                
                success = success and task_success

    return success