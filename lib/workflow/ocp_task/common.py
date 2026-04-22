def get_task_map():
    fmap = {}
    fmap['ai'] = 'ocp_ai_operator'
    fmap['cert-manager'] = 'ocp_cert_manager'
    fmap['cilium-bgp'] = 'ocp_cilium_bgp'
    fmap['cilium-image'] = 'ocp_cilium_cni'
    fmap['cilium-inb'] = 'ocp_cilium_inb'
    fmap['cilium-mesh'] = 'ocp_cilium_mesh'
    fmap['cilium-pnet'] = 'ocp_cilium_pnet'
    fmap['cilium-timescape'] = 'ocp_cilium_timescape'
    fmap['cli'] = 'ocp_cli'
    fmap['cli-web'] = 'ocp_web_terminal_operator'
    fmap['cnv'] = 'ocp_cnv_operator'
    fmap['gpu'] = 'ocp_gpu_operator'
    fmap['grafana'] = 'ocp_grafana_operator'
    fmap['identity'] = 'ocp_identity'
    fmap['imm'] = 'ocp_imm'
    fmap['intersight'] = 'ocp_intersight_operator'
    fmap['iotel'] = 'ocp_iotel'
    fmap['k8s'] = 'k8s'
    fmap['lso'] = 'ocp_local_storage_operator'
    fmap['lvm'] = 'ocp_lvm_operator'
    fmap['minio'] = 'ocp_minio_operator'
    fmap['nfd'] = 'ocp_nfd_operator'
    fmap['nfs'] = 'ocp_nfs_helm'
    fmap['nim'] = 'ocp_nim_operator'
    fmap['nmstate'] = 'ocp_nmstate_operator'
    fmap['ocp-proxy'] = 'ocp_proxy'
    fmap['ovn-bgp'] = 'ocp_ovn_bgp'
    fmap['odf'] = 'ocp_odf_operator'
    fmap['portworx'] = 'ocp_portworx_operator'
    fmap['prometheus'] = 'ocp_prometheus'
    fmap['serverless'] = 'ocp_serverless_operator'
    fmap['service-mesh'] = 'ocp_service_mesh_operator'
    fmap['vast'] = 'ocp_vast_operator'
    fmap['mtv'] = 'ocp_mtv_operator'
    fmap['splunk'] = 'ocp_splunk_operator'
    fmap['sriov'] = 'ocp_sriov_operator'
    fmap['ssh'] = 'ocp_ssh'
    fmap['tetragon'] = 'ocp_tetragon_operator'
    fmap['trident'] = 'ocp_trident_operator'
    return fmap


def get_no_delete_task():
    task = [
        'cli',
        'cilium-image'
    ]
    return task
