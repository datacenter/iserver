from lib import log_helper

from lib.k8s.api import K8sApi
from lib.k8s.common import K8sCommon

from lib.k8s.alert_manager.main import K8sAlertManager
from lib.k8s.alert_manager_config.main import K8sAlertManagerConfig
from lib.k8s.cluster_operator.main import K8sClusterOperator
from lib.k8s.cluster_quota.main import K8sClusterQuota
from lib.k8s.cluster_role_binding.main import K8sClusterRoleBinding
from lib.k8s.cluster_service_version.main import K8sClusterServiceVersion
from lib.k8s.cni.main import K8sCni
from lib.k8s.config_map.main import K8sConfigMap
from lib.k8s.custom_resource_definition.main import K8sCustomResourceDefinition
from lib.k8s.daemon_set.main import K8sDaemonSet
from lib.k8s.data_volume.main import K8sDataVolume
from lib.k8s.deployment.main import K8sDeployment
from lib.k8s.deployment_config.main import K8sDeploymentConfig
from lib.k8s.egress_ip.main import K8sEgressIp
from lib.k8s.egress_router.main import K8sEgressRouter
from lib.k8s.endpoint.main import K8sEndpoint
from lib.k8s.event.main import K8sEvent
from lib.k8s.ingress.main import K8sIngress
from lib.k8s.kubevirt.main import K8sKubevirt
from lib.k8s.limit.main import K8sLimit
from lib.k8s.machine_config.main import K8sMachineConfig
from lib.k8s.machine_config_pool.main import K8sMachineConfigPool
from lib.k8s.namespace.main import K8sNamespace
from lib.k8s.network_attachment_definition.main import K8sNetworkAttachmentDefinition
from lib.k8s.node.main import K8sNode
from lib.k8s.node_network_configuration_enactment.main import K8sNodeNetworkConfigurationEnactment
from lib.k8s.node_network_configuration_policy.main import K8sNodeNetworkConfigurationPolicy
from lib.k8s.node_network_state.main import K8sNodeNetworkState
from lib.k8s.operator_group.main import K8sOperatorGroup
from lib.k8s.performance_profile.main import K8sPerformanceProfile
from lib.k8s.pod.main import K8sPod
from lib.k8s.pod_monitor.main import K8sPodMonitor
from lib.k8s.priority_class.main import K8sPriorityClass
from lib.k8s.probe.main import K8sProbe
from lib.k8s.profile.main import K8sProfile
from lib.k8s.prometheus.main import K8sPrometheus
from lib.k8s.prometheus_rule.main import K8sPrometheusRule
from lib.k8s.pv.main import K8sPv
from lib.k8s.pvc.main import K8sPvc
from lib.k8s.replication_controller.main import K8sReplicationController
from lib.k8s.replica_set.main import K8sReplicaSet
from lib.k8s.resource_quota.main import K8sResourceQuota
from lib.k8s.role_binding.main import K8sRoleBinding
from lib.k8s.route.main import K8sRoute
from lib.k8s.secret.main import K8sSecret
from lib.k8s.security_context_constraint.main import K8sSecurityContextConstraint
from lib.k8s.service.main import K8sService
from lib.k8s.service_account.main import K8sServiceAccount
from lib.k8s.service_monitor.main import K8sServiceMonitor
from lib.k8s.sriov_network.main import K8sSriovNetwork
from lib.k8s.sriov_network_node_policy.main import K8sSriovNetworkNodePolicy
from lib.k8s.sriov_network_node_state.main import K8sSriovNetworkNodeState
from lib.k8s.stateful_set.main import K8sStatefulSet
from lib.k8s.storage_class.main import K8sStorageClass
from lib.k8s.subscription.main import K8sSubscription
from lib.k8s.thanos_ruler.main import K8sThanosRuler
from lib.k8s.tuned.main import K8sTuned
from lib.k8s.version.main import K8sVersion
from lib.k8s.virtual_machine.main import K8sVirtualMachine
from lib.k8s.virtual_machine_clone.main import K8sVirtualMachineClone
from lib.k8s.virtual_machine_cluster_instance_type.main import K8sVirtualMachineClusterInstanceType
from lib.k8s.virtual_machine_cluster_preference.main import K8sVirtualMachineClusterPreference
from lib.k8s.virtual_machine_export.main import K8sVirtualMachineExport
from lib.k8s.virtual_machine_instance.main import K8sVirtualMachineInstance
from lib.k8s.virtual_machine_instance_migration.main import K8sVirtualMachineInstanceMigration
from lib.k8s.virtual_machine_instance_preset.main import K8sVirtualMachineInstancePreset
from lib.k8s.virtual_machine_instance_replica_set.main import K8sVirtualMachineInstanceReplicaSet
from lib.k8s.virtual_machine_preference.main import K8sVirtualMachinePreference
from lib.k8s.virtual_machine_restore.main import K8sVirtualMachineRestore
from lib.k8s.virtual_machine_snapshot.main import K8sVirtualMachineSnapshot
from lib.k8s.virtual_machine_snapshot_content.main import K8sVirtualMachineSnapshotContent
from lib.k8s.volume_attachment.main import K8sVolumeAttachment
from lib.k8s.volume_snapshot.main import K8sVolumeSnapshot
from lib.k8s.volume_snapshot_class.main import K8sVolumeSnapshotClass
from lib.k8s.volume_snapshot_content.main import K8sVolumeSnapshotContent


class K8s(
        K8sApi,
        K8sCommon,
        K8sAlertManager,
        K8sAlertManagerConfig,
        K8sClusterOperator,
        K8sClusterQuota,
        K8sClusterRoleBinding,
        K8sClusterServiceVersion,
        K8sCni,
        K8sConfigMap,
        K8sCustomResourceDefinition,
        K8sDaemonSet,
        K8sDataVolume,
        K8sDeployment,
        K8sDeploymentConfig,
        K8sEgressIp,
        K8sEgressRouter,
        K8sEndpoint,
        K8sEvent,
        K8sIngress,
        K8sKubevirt,
        K8sLimit,
        K8sMachineConfig,
        K8sMachineConfigPool,
        K8sNamespace,
        K8sNetworkAttachmentDefinition,
        K8sNode,
        K8sNodeNetworkConfigurationEnactment,
        K8sNodeNetworkConfigurationPolicy,
        K8sNodeNetworkState,
        K8sOperatorGroup,
        K8sPerformanceProfile,
        K8sPod,
        K8sPodMonitor,
        K8sPriorityClass,
        K8sProbe,
        K8sProfile,
        K8sPrometheus,
        K8sPrometheusRule,
        K8sPv,
        K8sPvc,
        K8sReplicaSet,
        K8sReplicationController,
        K8sResourceQuota,
        K8sRoleBinding,
        K8sRoute,
        K8sSecret,
        K8sSecurityContextConstraint,
        K8sService,
        K8sServiceAccount,
        K8sServiceMonitor,
        K8sSriovNetwork,
        K8sSriovNetworkNodePolicy,
        K8sSriovNetworkNodeState,
        K8sStatefulSet,
        K8sStorageClass,
        K8sSubscription,
        K8sThanosRuler,
        K8sTuned,
        K8sVersion,
        K8sVirtualMachine,
        K8sVirtualMachineClone,
        K8sVirtualMachineClusterInstanceType,
        K8sVirtualMachineClusterPreference,
        K8sVirtualMachineExport,
        K8sVirtualMachineInstance,
        K8sVirtualMachineInstanceMigration,
        K8sVirtualMachineInstancePreset,
        K8sVirtualMachineInstanceReplicaSet,
        K8sVirtualMachinePreference,
        K8sVirtualMachineRestore,
        K8sVirtualMachineSnapshot,
        K8sVirtualMachineSnapshotContent,
        K8sVolumeAttachment,
        K8sVolumeSnapshot,
        K8sVolumeSnapshotClass,
        K8sVolumeSnapshotContent
        ):
    def __init__(self, kubeconfig_filename, cluster_type='standard', verbose=False, debug=False, log_id=None):
        K8sApi.__init__(self, kubeconfig_filename, cluster_type=cluster_type)
        K8sCommon.__init__(self)

        K8sAlertManager.__init__(self)
        K8sAlertManagerConfig.__init__(self)
        K8sClusterOperator.__init__(self)
        K8sClusterQuota.__init__(self)
        K8sClusterRoleBinding.__init__(self)
        K8sClusterServiceVersion.__init__(self)
        K8sCni.__init__(self)
        K8sConfigMap.__init__(self)
        K8sCustomResourceDefinition.__init__(self)
        K8sDaemonSet.__init__(self)
        K8sDataVolume.__init__(self)
        K8sDeployment.__init__(self)
        K8sDeploymentConfig.__init__(self)
        K8sEgressIp.__init__(self)
        K8sEgressRouter.__init__(self)
        K8sEndpoint.__init__(self)
        K8sEvent.__init__(self)
        K8sIngress.__init__(self)
        K8sKubevirt.__init__(self)
        K8sLimit.__init__(self)
        K8sMachineConfig.__init__(self)
        K8sMachineConfigPool.__init__(self)
        K8sNamespace.__init__(self)
        K8sNetworkAttachmentDefinition.__init__(self)
        K8sNode.__init__(self)
        K8sNodeNetworkConfigurationEnactment.__init__(self)
        K8sNodeNetworkConfigurationPolicy.__init__(self)
        K8sNodeNetworkState.__init__(self)
        K8sOperatorGroup.__init__(self)
        K8sPerformanceProfile.__init__(self)
        K8sPod.__init__(self)
        K8sPodMonitor.__init__(self)
        K8sPriorityClass.__init__(self)
        K8sProbe.__init__(self)
        K8sProfile.__init__(self)
        K8sPrometheus.__init__(self)
        K8sPrometheusRule.__init__(self)
        K8sPv.__init__(self)
        K8sPvc.__init__(self)
        K8sReplicaSet.__init__(self)
        K8sReplicationController.__init__(self)
        K8sResourceQuota.__init__(self)
        K8sRoleBinding.__init__(self)
        K8sRoute.__init__(self)
        K8sSecret.__init__(self)
        K8sSecurityContextConstraint.__init__(self)
        K8sService.__init__(self)
        K8sServiceAccount.__init__(self)
        K8sServiceMonitor.__init__(self)
        K8sSriovNetwork.__init__(self)
        K8sSriovNetworkNodePolicy.__init__(self)
        K8sSriovNetworkNodeState.__init__(self)
        K8sStatefulSet.__init__(self)
        K8sStorageClass.__init__(self)
        K8sSubscription.__init__(self)
        K8sThanosRuler.__init__(self)
        K8sTuned.__init__(self)
        K8sVersion.__init__(self)
        K8sVirtualMachine.__init__(self)
        K8sVirtualMachineClone.__init__(self)
        K8sVirtualMachineClusterInstanceType.__init__(self)
        K8sVirtualMachineClusterPreference.__init__(self)
        K8sVirtualMachineExport.__init__(self)
        K8sVirtualMachineInstance.__init__(self)
        K8sVirtualMachineInstanceMigration.__init__(self)
        K8sVirtualMachineInstancePreset.__init__(self)
        K8sVirtualMachineInstanceReplicaSet.__init__(self)
        K8sVirtualMachinePreference.__init__(self)
        K8sVirtualMachineRestore.__init__(self)
        K8sVirtualMachineSnapshot.__init__(self)
        K8sVirtualMachineSnapshotContent.__init__(self)
        K8sVolumeAttachment.__init__(self)
        K8sVolumeSnapshot.__init__(self)
        K8sVolumeSnapshotClass.__init__(self)
        K8sVolumeSnapshotContent.__init__(self)

        self.verbose = verbose
        self.debug = debug
        self.log_id = log_id
        self.log = log_helper.Log(log_id=log_id)
