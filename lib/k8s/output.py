from lib import output_helper

from lib.k8s.alert_manager.output import K8sAlertManagerOutput
from lib.k8s.alert_manager_config.output import K8sAlertManagerConfigOutput
from lib.k8s.cluster_operator.output import K8sClusterOperatorOutput
from lib.k8s.cluster_quota.output import K8sClusterQuotaOutput
from lib.k8s.cluster_role_binding.output import K8sClusterRoleBindingOutput
from lib.k8s.cluster_service_version.output import K8sClusterServiceVersionOutput
from lib.k8s.cni.output import K8sCniOutput
from lib.k8s.config_map.output import K8sConfigMapOutput
from lib.k8s.custom_resource_definition.output import K8sCustomResourceDefinitionOutput
from lib.k8s.daemon_set.output import K8sDaemonSetOutput
from lib.k8s.data_volume.output import K8sDataVolumeOutput
from lib.k8s.deployment.output import K8sDeploymentOutput
from lib.k8s.deployment_config.output import K8sDeploymentConfigOutput
from lib.k8s.egress_ip.output import K8sEgressIpOutput
from lib.k8s.egress_router.output import K8sEgressRouterOutput
from lib.k8s.endpoint.output import K8sEndpointOutput
from lib.k8s.event.output import K8sEventOutput
from lib.k8s.ingress.output import K8sIngressOutput
from lib.k8s.kubevirt.output import K8sKubevirtOutput
from lib.k8s.limit.output import K8sLimitOutput
from lib.k8s.machine_config.output import K8sMachineConfigOutput
from lib.k8s.machine_config_pool.output import K8sMachineConfigPoolOutput
from lib.k8s.namespace.output import K8sNamespaceOutput
from lib.k8s.network_attachment_definition.output import K8sNetworkAttachmentDefinitionOutput
from lib.k8s.node.output import K8sNodeOutput
from lib.k8s.node_network_configuration_enactment.output import K8sNodeNetworkConfigurationEnactmentOutput
from lib.k8s.node_network_configuration_policy.output import K8sNodeNetworkConfigurationPolicyOutput
from lib.k8s.node_network_state.output import K8sNodeNetworkStateOutput
from lib.k8s.operator_group.output import K8sOperatorGroupOutput
from lib.k8s.performance_profile.output import K8sPerformanceProfileOutput
from lib.k8s.pod.output import K8sPodOutput
from lib.k8s.pod_monitor.output import K8sPodMonitorOutput
from lib.k8s.priority_class.output import K8sPriorityClassOutput
from lib.k8s.probe.output import K8sProbeOutput
from lib.k8s.profile.output import K8sProfileOutput
from lib.k8s.prometheus.output import K8sPrometheusOutput
from lib.k8s.prometheus_rule.output import K8sPrometheusRuleOutput
from lib.k8s.pv.output import K8sPvOutput
from lib.k8s.pvc.output import K8sPvcOutput
from lib.k8s.replica_set.output import K8sReplicaSetOutput
from lib.k8s.replication_controller.output import K8sReplicationControllerOutput
from lib.k8s.resource_quota.output import K8sResourceQuotaOutput
from lib.k8s.role_binding.output import K8sRoleBindingOutput
from lib.k8s.route.output import K8sRouteOutput
from lib.k8s.secret.output import K8sSecretOutput
from lib.k8s.security_context_constraint.output import K8sSecurityContextConstraintOutput
from lib.k8s.service.output import K8sServiceOutput
from lib.k8s.service_account.output import K8sServiceAccountOutput
from lib.k8s.service_monitor.output import K8sServiceMonitorOutput
from lib.k8s.sriov_network.output import K8sSriovNetworkOutput
from lib.k8s.sriov_network_node_policy.output import K8sSriovNetworkNodePolicyOutput
from lib.k8s.sriov_network_node_state.output import K8sSriovNetworkNodeStateOutput
from lib.k8s.stateful_set.output import K8sStatefulSetOutput
from lib.k8s.storage_class.output import K8sStorageClassOutput
from lib.k8s.subscription.output import K8sSubscriptionOutput
from lib.k8s.thanos_ruler.output import K8sThanosRulerOutput
from lib.k8s.tuned.output import K8sTunedOutput
from lib.k8s.version.output import K8sVersionOutput
from lib.k8s.virtual_machine.output import K8sVirtualMachineOutput
from lib.k8s.virtual_machine_clone.output import K8sVirtualMachineCloneOutput
from lib.k8s.virtual_machine_cluster_instance_type.output import K8sVirtualMachineClusterInstanceTypeOutput
from lib.k8s.virtual_machine_cluster_preference.output import K8sVirtualMachineClusterPreferenceOutput
from lib.k8s.virtual_machine_export.output import K8sVirtualMachineExportOutput
from lib.k8s.virtual_machine_instance.output import K8sVirtualMachineInstanceOutput
from lib.k8s.virtual_machine_instance_migration.output import K8sVirtualMachineInstanceMigrationOutput
from lib.k8s.virtual_machine_instance_preset.output import K8sVirtualMachineInstancePresetOutput
from lib.k8s.virtual_machine_instance_replica_set.output import K8sVirtualMachineInstanceReplicaSetOutput
from lib.k8s.virtual_machine_preference.output import K8sVirtualMachinePreferenceOutput
from lib.k8s.virtual_machine_restore.output import K8sVirtualMachineRestoreOutput
from lib.k8s.virtual_machine_snapshot.output import K8sVirtualMachineSnapshotOutput
from lib.k8s.virtual_machine_snapshot_content.output import K8sVirtualMachineSnapshotContentOutput
from lib.k8s.volume_attachment.output import K8sVolumeAttachmentOutput
from lib.k8s.volume_snapshot.output import K8sVolumeSnapshotOutput
from lib.k8s.volume_snapshot_class.output import K8sVolumeSnapshotClassOutput
from lib.k8s.volume_snapshot_content.output import K8sVolumeSnapshotContentOutput


class K8sOutput(
    K8sAlertManagerOutput,
    K8sAlertManagerConfigOutput,
    K8sClusterOperatorOutput,
    K8sClusterQuotaOutput,
    K8sClusterRoleBindingOutput,
    K8sClusterServiceVersionOutput,
    K8sCniOutput,
    K8sConfigMapOutput,
    K8sCustomResourceDefinitionOutput,
    K8sDaemonSetOutput,
    K8sDataVolumeOutput,
    K8sDeploymentOutput,
    K8sDeploymentConfigOutput,
    K8sEgressIpOutput,
    K8sEgressRouterOutput,
    K8sEndpointOutput,
    K8sEventOutput,
    K8sIngressOutput,
    K8sKubevirtOutput,
    K8sLimitOutput,
    K8sMachineConfigOutput,
    K8sMachineConfigPoolOutput,
    K8sNamespaceOutput,
    K8sNetworkAttachmentDefinitionOutput,
    K8sNodeOutput,
    K8sNodeNetworkConfigurationEnactmentOutput,
    K8sNodeNetworkConfigurationPolicyOutput,
    K8sNodeNetworkStateOutput,
    K8sOperatorGroupOutput,
    K8sPerformanceProfileOutput,
    K8sPodOutput,
    K8sPodMonitorOutput,
    K8sPriorityClassOutput,
    K8sProbeOutput,
    K8sProfileOutput,
    K8sPrometheusOutput,
    K8sPrometheusRuleOutput,
    K8sPvOutput,
    K8sPvcOutput,
    K8sReplicaSetOutput,
    K8sReplicationControllerOutput,
    K8sResourceQuotaOutput,
    K8sRoleBindingOutput,
    K8sRouteOutput,
    K8sSecretOutput,
    K8sSecurityContextConstraintOutput,
    K8sServiceOutput,
    K8sServiceAccountOutput,
    K8sServiceMonitorOutput,
    K8sSriovNetworkOutput,
    K8sSriovNetworkNodePolicyOutput,
    K8sSriovNetworkNodeStateOutput,
    K8sStatefulSetOutput,
    K8sStorageClassOutput,
    K8sSubscriptionOutput,
    K8sThanosRulerOutput,
    K8sTunedOutput,
    K8sVersionOutput,
    K8sVirtualMachineOutput,
    K8sVirtualMachineCloneOutput,
    K8sVirtualMachineClusterInstanceTypeOutput,
    K8sVirtualMachineClusterPreferenceOutput,
    K8sVirtualMachineExportOutput,
    K8sVirtualMachineInstanceOutput,
    K8sVirtualMachineInstanceMigrationOutput,
    K8sVirtualMachineInstancePresetOutput,
    K8sVirtualMachineInstanceReplicaSetOutput,
    K8sVirtualMachinePreferenceOutput,
    K8sVirtualMachineRestoreOutput,
    K8sVirtualMachineSnapshotOutput,
    K8sVirtualMachineSnapshotContentOutput,
    K8sVolumeAttachmentOutput,
    K8sVolumeSnapshotOutput,
    K8sVolumeSnapshotClassOutput,
    K8sVolumeSnapshotContentOutput
    ):
    def __init__(self, verbose=False, debug=False, log_id=None):
        self.my_output = output_helper.OutputHelper(
            log_id=log_id,
            verbose=verbose,
            debug=debug
        )

        K8sAlertManagerOutput.__init__(self)
        K8sAlertManagerConfigOutput.__init__(self)
        K8sClusterOperatorOutput.__init__(self)
        K8sClusterQuotaOutput.__init__(self)
        K8sClusterRoleBindingOutput.__init__(self)
        K8sClusterServiceVersionOutput.__init__(self)
        K8sCniOutput.__init__(self)
        K8sConfigMapOutput.__init__(self)
        K8sCustomResourceDefinitionOutput.__init__(self)
        K8sDaemonSetOutput.__init__(self)
        K8sDataVolumeOutput.__init__(self)
        K8sDeploymentOutput.__init__(self)
        K8sDeploymentConfigOutput.__init__(self)
        K8sEgressIpOutput.__init__(self)
        K8sEgressRouterOutput.__init__(self)
        K8sEndpointOutput.__init__(self)
        K8sEventOutput.__init__(self)
        K8sIngressOutput.__init__(self)
        K8sKubevirtOutput.__init__(self)
        K8sLimitOutput.__init__(self)
        K8sMachineConfigOutput.__init__(self)
        K8sMachineConfigPoolOutput.__init__(self)
        K8sNamespaceOutput.__init__(self)
        K8sNetworkAttachmentDefinitionOutput.__init__(self)
        K8sNodeOutput.__init__(self)
        K8sNodeNetworkConfigurationEnactmentOutput.__init__(self)
        K8sNodeNetworkConfigurationPolicyOutput.__init__(self)
        K8sNodeNetworkStateOutput.__init__(self)
        K8sOperatorGroupOutput.__init__(self)
        K8sPerformanceProfileOutput.__init__(self)
        K8sPodOutput.__init__(self)
        K8sPodMonitorOutput.__init__(self)
        K8sPriorityClassOutput.__init__(self)
        K8sProbeOutput.__init__(self)
        K8sProfileOutput.__init__(self)
        K8sPrometheusOutput.__init__(self)
        K8sPrometheusRuleOutput.__init__(self)
        K8sPvOutput.__init__(self)
        K8sPvcOutput.__init__(self)
        K8sReplicaSetOutput.__init__(self)
        K8sReplicationControllerOutput.__init__(self)
        K8sResourceQuotaOutput.__init__(self)
        K8sRoleBindingOutput.__init__(self)
        K8sRouteOutput.__init__(self)
        K8sSecretOutput.__init__(self)
        K8sSecurityContextConstraintOutput.__init__(self)
        K8sServiceOutput.__init__(self)
        K8sServiceMonitorOutput.__init__(self)
        K8sServiceMonitorOutput.__init__(self)
        K8sSriovNetworkOutput.__init__(self)
        K8sSriovNetworkNodePolicyOutput.__init__(self)
        K8sSriovNetworkNodeStateOutput.__init__(self)
        K8sStatefulSetOutput.__init__(self)
        K8sStorageClassOutput.__init__(self)
        K8sSubscriptionOutput.__init__(self)
        K8sThanosRulerOutput.__init__(self)
        K8sTunedOutput.__init__(self)
        K8sVersionOutput.__init__(self)
        K8sVirtualMachineOutput.__init__(self)
        K8sVirtualMachineCloneOutput.__init__(self)
        K8sVirtualMachineClusterInstanceTypeOutput.__init__(self)
        K8sVirtualMachineClusterPreferenceOutput.__init__(self)
        K8sVirtualMachineExportOutput.__init__(self)
        K8sVirtualMachineInstanceOutput.__init__(self)
        K8sVirtualMachineInstanceMigrationOutput.__init__(self)
        K8sVirtualMachineInstancePresetOutput.__init__(self)
        K8sVirtualMachineInstanceReplicaSetOutput.__init__(self)
        K8sVirtualMachinePreferenceOutput.__init__(self)
        K8sVirtualMachineRestoreOutput.__init__(self)
        K8sVirtualMachineSnapshotOutput.__init__(self)
        K8sVirtualMachineSnapshotContentOutput.__init__(self)
        K8sVolumeAttachmentOutput.__init__(self)
        K8sVolumeSnapshotOutput.__init__(self)
        K8sVolumeSnapshotClassOutput.__init__(self)
        K8sVolumeSnapshotContentOutput.__init__(self)

    def get_namespace_name(self, namespace, name):
        namespace_nameT = []
        namespace_nameT.append(
            namespace
        )
        namespace_nameT.append(
            name
        )
        return namespace_nameT

    def add_namespace_name(self, values):
        for value in values:
            value['namespace_nameT'] = self.get_namespace_name(
                value['namespace'],
                value['name']
            )
        return values

    def print_clusters(self, clusters, title=False):
        if title:
            self.my_output.default(
                'Cluster [#%s]' % (len(clusters)),
                underline=True,
                before_newline=True
            )

        if len(clusters) == 0:
            self.my_output.default('None')
            return

        order = [
            'name',
            'defaultTick',
            'type',
            'virtctl.description',
            'helm.description',
            'tools.description',
            'apiTick'
        ]

        headers = [
            'Cluster Name',
            'Default',
            'Type',
            'OCP Virtctl',
            'OCP Helm',
            'OCP Tools',
            'API'
        ]

        self.my_output.my_table(
            clusters,
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            row_separator=False,
            remove_empty_columns=True,
            table=True
        )

    def print_clusters_kubeconfig(self, clusters, title=False):
        if title:
            self.my_output.default(
                'Kubeconfig [#%s]' % (len(clusters)),
                underline=True,
                before_newline=True
            )

        if len(clusters) == 0:
            self.my_output.default('None')
            return

        order = [
            'name',
            'kubeconfigFilename',
            'isKubeconfigFileTick',
            'apiFqdn',
            'apiVip',
            'kubeApiTick'
        ]

        headers = [
            'Cluster Name',
            'Kubeconfig',
            'IsFile',
            'API FQDN',
            'API VIP',
            'K8s API'
        ]

        self.my_output.my_table(
            clusters,
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            remove_empty_columns=True,
            table=True
        )
