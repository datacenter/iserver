from lib import output_helper

from lib.k8s.aaq.output import K8sAaqOutput
from lib.k8s.admin_job.output import K8sAdminJobOutput
from lib.k8s.alert_manager.output import K8sAlertManagerOutput
from lib.k8s.alert_manager_config.output import K8sAlertManagerConfigOutput
from lib.k8s.alert_rule.output import K8sAlertRuleOutput
from lib.k8s.auth.output import K8sAuthOutput
from lib.k8s.authentication.output import K8sAuthenticationOutput
from lib.k8s.bare_metal_host.output import K8sBareMetalHostOutput
from lib.k8s.build_config.output import K8sBuildConfigOutput
from lib.k8s.catalog_source.output import K8sCatalogSourceOutput
from lib.k8s.cdi.output import K8sCdiOutput
from lib.k8s.cdi_config.output import K8sCdiConfigOutput
from lib.k8s.ceph_block_pool.output import K8sCephBlockPoolOutput
from lib.k8s.ceph_block_pool_rados_namespace.output import K8sCephBlockPoolRadosNamespaceOutput
from lib.k8s.ceph_bucket_notification.output import K8sCephBucketNotificationOutput
from lib.k8s.ceph_bucket_topic.output import K8sCephBucketTopicOutput
from lib.k8s.ceph_client.output import K8sCephClientOutput
from lib.k8s.ceph_client_profile.output import K8sCephClientProfileOutput
from lib.k8s.ceph_client_profile_mapping.output import K8sCephClientProfileMappingOutput
from lib.k8s.ceph_cluster.output import K8sCephClusterOutput
from lib.k8s.ceph_connection.output import K8sCephConnectionOutput
from lib.k8s.ceph_cosi_driver.output import K8sCephCosiDriverOutput
from lib.k8s.ceph_driver.output import K8sCephDriverOutput
from lib.k8s.ceph_filesystem.output import K8sCephFilesystemOutput
from lib.k8s.ceph_filesystem_mirror.output import K8sCephFilesystemMirrorOutput
from lib.k8s.ceph_filesystem_subvolume_group.output import K8sCephFilesystemSubVolumeGroupOutput
from lib.k8s.ceph_nfs.output import K8sCephNfsOutput
from lib.k8s.ceph_object_realm.output import K8sCephObjectRealmOutput
from lib.k8s.ceph_object_store.output import K8sCephObjectStoreOutput
from lib.k8s.ceph_object_store_user.output import K8sCephObjectStoreUserOutput
from lib.k8s.ceph_object_zone.output import K8sCephObjectZoneOutput
from lib.k8s.ceph_object_zone_group.output import K8sCephObjectZoneGroupOutput
from lib.k8s.ceph_operator_config.output import K8sCephOperatorConfigOutput
from lib.k8s.ceph_rdb_mirror.output import K8sCephRdbMirrorOutput
from lib.k8s.certificate.output import K8sCertificateOutput
from lib.k8s.cilium_config.output import K8sCiliumConfigOutput
from lib.k8s.cilium_load_balancer_ip_pool.output import CiliumLoadBalancerIpPoolOutput
from lib.k8s.cluster_operator.output import K8sClusterOperatorOutput
from lib.k8s.cluster_policy.output import K8sClusterPolicyOutput
from lib.k8s.cluster_quota.output import K8sClusterQuotaOutput
from lib.k8s.cluster_role.output import K8sClusterRoleOutput
from lib.k8s.cluster_role_binding.output import K8sClusterRoleBindingOutput
from lib.k8s.cluster_service_version.output import K8sClusterServiceVersionOutput
from lib.k8s.cluster_version.output import K8sClusterVersionOutput
from lib.k8s.clusterwide_private_network.output import K8sClusterwidePrivateNetworkOutput
from lib.k8s.cni.output import K8sCniOutput
from lib.k8s.config_map.output import K8sConfigMapOutput
from lib.k8s.cron_job.output import K8sCronJobOutput
from lib.k8s.custom_resource_definition.output import K8sCustomResourceDefinitionOutput
from lib.k8s.daemon_set.output import K8sDaemonSetOutput
from lib.k8s.data_import_cron.output import K8sDataImportCronOutput
from lib.k8s.data_science_cluster.output import K8sDataScienceClusterOutput
from lib.k8s.data_science_cluster_initialization.output import K8sDataScienceClusterInitializationOutput
from lib.k8s.data_source.output import K8sDataSourceOutput
from lib.k8s.data_volume.output import K8sDataVolumeOutput
from lib.k8s.deployment.output import K8sDeploymentOutput
from lib.k8s.deployment_config.output import K8sDeploymentConfigOutput
from lib.k8s.dev_workspace.output import K8sDevWorkspaceOutput
from lib.k8s.dev_workspace_template.output import K8sDevWorkspaceTemplateOutput
from lib.k8s.dns.output import K8sDnsOutput
from lib.k8s.egress_ip.output import K8sEgressIpOutput
from lib.k8s.egress_router.output import K8sEgressRouterOutput
from lib.k8s.endpoint.output import K8sEndpointOutput
from lib.k8s.event.output import K8sEventOutput
from lib.k8s.forklift_controller.output import K8sForkliftControllerOutput
from lib.k8s.grafana.output import K8sGrafanaOutput
from lib.k8s.grafana_alert_rule_group.output import K8sGrafanaAlertRuleGroupOutput
from lib.k8s.grafana_contact_point.output import K8sGrafanaContactPointOutput
from lib.k8s.grafana_dashboard.output import K8sGrafanaDashboardOutput
from lib.k8s.grafana_datasource.output import K8sGrafanaDatasourceOutput
from lib.k8s.grafana_folder.output import K8sGrafanaFolderOutput
from lib.k8s.grafana_library_panel.output import K8sGrafanaLibraryPanelOutput
from lib.k8s.grafana_mute_timing.output import K8sGrafanaMuteTimingOutput
from lib.k8s.grafana_notification_policy.output import K8sGrafanaNotificationPolicyOutput
from lib.k8s.grafana_notification_policy_route.output import K8sGrafanaNotificationPolicyRouteOutput
from lib.k8s.grafana_notification_template.output import K8sGrafanaNotificationTemplateOutput
from lib.k8s.group.output import K8sGroupOutput
from lib.k8s.hook.output import K8sHookOutput
from lib.k8s.host.output import K8sHostOutput
from lib.k8s.host_path_provisioner.output import K8sHostPathProvisionerOutput
from lib.k8s.hyperconverged.output import K8sHyperConvergedOutput
from lib.k8s.identity.output import K8sIdentityOutput
from lib.k8s.image_stream.output import K8sImageStreamOutput
from lib.k8s.ingress.output import K8sIngressOutput
from lib.k8s.installplan.output import K8sInstallplanOutput
from lib.k8s.isovalent_bgp_advertisement.output import K8sIsovalentBGPAdvertisementOutput
from lib.k8s.isovalent_bgp_cluster_config.output import K8sIsovalentBGPClusterConfigOutput
from lib.k8s.isovalent_bgp_node_config.output import K8sIsovalentBGPNodeConfigOutput
from lib.k8s.isovalent_bgp_peer_config.output import K8sIsovalentBGPPeerConfigOutput
from lib.k8s.issuer.output import K8sIssuerOutput
from lib.k8s.job.output import K8sJobOutput
from lib.k8s.knative_eventing.output import K8sKnativeEventingOutput
from lib.k8s.knative_serving.output import K8sKnativeServingOutput
from lib.k8s.knative_kafka.output import K8sKnativeKafkaOutput
from lib.k8s.kubevirt.output import K8sKubevirtOutput
from lib.k8s.lease.output import K8sLeaseOutput
from lib.k8s.limit.output import K8sLimitOutput
from lib.k8s.local_volume.output import K8sLocalVolumeOutput
from lib.k8s.local_volume_set.output import K8sLocalVolumeSetOutput
from lib.k8s.local_volume_discovery.output import K8sLocalVolumeDiscoveryOutput
from lib.k8s.local_volume_discovery_result.output import K8sLocalVolumeDiscoveryResultOutput
from lib.k8s.logical_volume.output import K8sLogicalVolumeOutput
from lib.k8s.lvm_cluster.output import K8sLvmClusterOutput
from lib.k8s.machine_config.output import K8sMachineConfigOutput
from lib.k8s.machine_config_pool.output import K8sMachineConfigPoolOutput
from lib.k8s.migration.output import K8sMigrationOutput
from lib.k8s.migration_policy.output import K8sMigrationPolicyOutput
from lib.k8s.mutating_webhook.output import K8sMutatingWebhookOutput
from lib.k8s.namespace.output import K8sNamespaceOutput
from lib.k8s.nemo_customizer.output import K8sNemoCustomizerOutput
from lib.k8s.nemo_datastore.output import K8sNemoDatastoreOutput
from lib.k8s.nemo_entitystore.output import K8sNemoEntitystoreOutput
from lib.k8s.nemo_evaluator.output import K8sNemoEvaluatorOutput
from lib.k8s.nemo_guardrail.output import K8sNemoGuardrailOutput
from lib.k8s.network.output import K8sNetworkOutput
from lib.k8s.network_addons_config.output import K8sNetworkAddonsConfigOutput
from lib.k8s.network_attachment_definition.output import K8sNetworkAttachmentDefinitionOutput
from lib.k8s.network_map.output import K8sNetworkMapOutput
from lib.k8s.network_operator.output import K8sNetworkOperatorOutput
from lib.k8s.nim_build.output import K8sNimBuildOutput
from lib.k8s.nim_cache.output import K8sNimCacheOutput
from lib.k8s.nim_pipeline.output import K8sNimPipelineOutput
from lib.k8s.nim_service.output import K8sNimServiceOutput
from lib.k8s.nmstate.output import K8sNmstateOutput
from lib.k8s.node.output import K8sNodeOutput
from lib.k8s.node_feature.output import K8sNodeFeatureOutput
from lib.k8s.node_feature_discovery.output import K8sNodeFeatureDiscoveryOutput
from lib.k8s.node_network_configuration_enactment.output import K8sNodeNetworkConfigurationEnactmentOutput
from lib.k8s.node_network_configuration_policy.output import K8sNodeNetworkConfigurationPolicyOutput
from lib.k8s.node_network_state.output import K8sNodeNetworkStateOutput
from lib.k8s.oauth.output import K8sOAuthOutput
from lib.k8s.object_store.output import K8sObjectStoreOutput
from lib.k8s.object_transfer.output import K8sObjectTransferOutput
from lib.k8s.ocs_initialization.output import K8sOcsInitializationOutput
from lib.k8s.openstack_volume_populator.output import K8sOpenstackVolumePopulatorOutput
from lib.k8s.operator_group.output import K8sOperatorGroupOutput
from lib.k8s.ovirt_volume_populator.output import K8sOvirtVolumePopulatorOutput
from lib.k8s.package.output import K8sPackageOutput
from lib.k8s.performance_profile.output import K8sPerformanceProfileOutput
from lib.k8s.plan.output import K8sPlanOutput
from lib.k8s.pod.output import K8sPodOutput
from lib.k8s.pod_info.output import K8sPodInfoOutput
from lib.k8s.pod_monitor.output import K8sPodMonitorOutput
from lib.k8s.policy_binding.output import K8sPolicyBindingOutput
from lib.k8s.portworx_storage_cluster.output import K8sPortworxStorageClusterOutput
from lib.k8s.portworx_storage_node.output import K8sPortworxStorageNodeOutput
from lib.k8s.priority_class.output import K8sPriorityClassOutput
from lib.k8s.private_network_endpoint_slice.output import K8sPrivateNetworkEndpointSliceOutput
from lib.k8s.private_network_external_endpoint.output import K8sPrivateNetworkExternalEndpointOutput
from lib.k8s.probe.output import K8sProbeOutput
from lib.k8s.profile.output import K8sProfileOutput
from lib.k8s.prometheus.output import K8sPrometheusOutput
from lib.k8s.prometheus_rule.output import K8sPrometheusRuleOutput
from lib.k8s.prometheus_target.output import K8sPrometheusTargetOutput
from lib.k8s.provider.output import K8sProviderOutput
from lib.k8s.proxy.output import K8sProxyOutput
from lib.k8s.pv.output import K8sPvOutput
from lib.k8s.pvc.output import K8sPvcOutput
from lib.k8s.replica_set.output import K8sReplicaSetOutput
from lib.k8s.replication_controller.output import K8sReplicationControllerOutput
from lib.k8s.resource_quota.output import K8sResourceQuotaOutput
from lib.k8s.role.output import K8sRoleOutput
from lib.k8s.role_binding.output import K8sRoleBindingOutput
from lib.k8s.route.output import K8sRouteOutput
from lib.k8s.sandbox_policy.output import K8sSandboxPolicyOutput
from lib.k8s.sandbox_policy_namespaced.output import K8sSandboxPolicyNamespacedOutput
from lib.k8s.secret.output import K8sSecretOutput
from lib.k8s.security_context_constraint.output import K8sSecurityContextConstraintOutput
from lib.k8s.service.output import K8sServiceOutput
from lib.k8s.service_account.output import K8sServiceAccountOutput
from lib.k8s.service_mesh_control_plane.output import K8sServiceMeshControlPlaneOutput
from lib.k8s.service_mesh_member_roll.output import K8sServiceMeshMemberRollOutput
from lib.k8s.service_mesh_member.output import K8sServiceMeshMemberOutput
from lib.k8s.service_monitor.output import K8sServiceMonitorOutput
from lib.k8s.splunk_cluster_manager.output import K8sSplunkClusterManagerOutput
from lib.k8s.splunk_cluster_master.output import K8sSplunkClusterMasterOutput
from lib.k8s.splunk_indexer_cluster.output import K8sSplunkIndexerClusterOutput
from lib.k8s.splunk_license_manager.output import K8sSplunkLicenseManagerOutput
from lib.k8s.splunk_license_master.output import K8sSplunkLicenseMasterOutput
from lib.k8s.splunk_monitoring_console.output import K8sSplunkMonitoringConsoleOutput
from lib.k8s.splunk_search_head_cluster.output import K8sSplunkSearchHeadClusterOutput
from lib.k8s.splunk_standalone.output import K8sSplunkStandaloneOutput
from lib.k8s.sriov_network.output import K8sSriovNetworkOutput
from lib.k8s.sriov_network_node_policy.output import K8sSriovNetworkNodePolicyOutput
from lib.k8s.sriov_network_node_state.output import K8sSriovNetworkNodeStateOutput
from lib.k8s.sriov_operator_config.output import K8sSriovOperatorConfigOutput
from lib.k8s.ssp.output import K8sSspOutput
from lib.k8s.stateful_set.output import K8sStatefulSetOutput
from lib.k8s.storage_claim.output import K8sStorageClaimOutput
from lib.k8s.storage_class.output import K8sStorageClassOutput
from lib.k8s.storage_client.output import K8sStorageClientOutput
from lib.k8s.storage_cluster.output import K8sStorageClusterOutput
from lib.k8s.storage_cluster_peer.output import K8sStorageClusterPeerOutput
from lib.k8s.storage_consumer.output import K8sStorageConsumerOutput
from lib.k8s.storage_map.output import K8sStorageMapOutput
from lib.k8s.storage_profile.output import K8sStorageProfileOutput
from lib.k8s.storage_request.output import K8sStorageRequestOutput
from lib.k8s.storage_system.output import K8sStorageSystemOutput
from lib.k8s.subscription.output import K8sSubscriptionOutput
from lib.k8s.tetragon_network_policy.output import K8sTetragonNetworkPolicyOutput
from lib.k8s.tetragon_network_policy_namespaced.output import K8sTetragonNetworkPolicyNamespacedOutput
from lib.k8s.thanos_ruler.output import K8sThanosRulerOutput
from lib.k8s.tracing_policy.output import K8sTracingPolicyOutput
from lib.k8s.tracing_policy_namespaced.output import K8sTracingPolicyNamespacedOutput
from lib.k8s.tuned.output import K8sTunedOutput
from lib.k8s.upload_token_request.output import K8sUploadTokenRequestOutput
from lib.k8s.user.output import K8sUserOutput
from lib.k8s.vast_cluster.output import K8sVastClusterOutput
from lib.k8s.vast_driver.output import K8sVastDriverOutput
from lib.k8s.vast_storage.output import K8sVastStorageOutput
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
from lib.k8s.virtual_machine_pool.output import K8sVirtualMachinePoolOutput
from lib.k8s.virtual_machine_preference.output import K8sVirtualMachinePreferenceOutput
from lib.k8s.virtual_machine_restore.output import K8sVirtualMachineRestoreOutput
from lib.k8s.virtual_machine_snapshot.output import K8sVirtualMachineSnapshotOutput
from lib.k8s.virtual_machine_snapshot_content.output import K8sVirtualMachineSnapshotContentOutput
from lib.k8s.volume_attachment.output import K8sVolumeAttachmentOutput
from lib.k8s.volume_clone_source.output import K8sVolumeCloneSourceOutput
from lib.k8s.volume_import_source.output import K8sVolumeImportSourceOutput
from lib.k8s.volume_upload_source.output import K8sVolumeUploadSourceOutput
from lib.k8s.volume_snapshot.output import K8sVolumeSnapshotOutput
from lib.k8s.volume_snapshot_class.output import K8sVolumeSnapshotClassOutput
from lib.k8s.volume_snapshot_content.output import K8sVolumeSnapshotContentOutput


class K8sOutput(
    K8sAaqOutput,
    K8sAdminJobOutput,
    K8sAlertManagerOutput,
    K8sAlertManagerConfigOutput,
    K8sAlertRuleOutput,
    K8sAuthOutput,
    K8sAuthenticationOutput,
    K8sBareMetalHostOutput,
    K8sBuildConfigOutput,
    K8sCatalogSourceOutput,
    K8sCdiOutput,
    K8sCdiConfigOutput,
    K8sCephBlockPoolOutput,
    K8sCephBlockPoolRadosNamespaceOutput,
    K8sCephBucketNotificationOutput,
    K8sCephBucketTopicOutput,
    K8sCephClientOutput,
    K8sCephClientProfileOutput,
    K8sCephClientProfileMappingOutput,
    K8sCephClusterOutput,
    K8sCephConnectionOutput,
    K8sCephCosiDriverOutput,
    K8sCephDriverOutput,
    K8sCephFilesystemOutput,
    K8sCephFilesystemMirrorOutput,
    K8sCephFilesystemSubVolumeGroupOutput,
    K8sCephNfsOutput,
    K8sCephObjectRealmOutput,
    K8sCephObjectStoreOutput,
    K8sCephObjectStoreUserOutput,
    K8sCephObjectZoneOutput,
    K8sCephObjectZoneGroupOutput,
    K8sCephOperatorConfigOutput,
    K8sCephRdbMirrorOutput,
    K8sCertificateOutput,
    K8sCiliumConfigOutput,
    CiliumLoadBalancerIpPoolOutput,
    K8sClusterOperatorOutput,
    K8sClusterPolicyOutput,
    K8sClusterQuotaOutput,
    K8sClusterRoleOutput,
    K8sClusterRoleBindingOutput,
    K8sClusterServiceVersionOutput,
    K8sClusterVersionOutput,
    K8sClusterwidePrivateNetworkOutput,
    K8sCniOutput,
    K8sConfigMapOutput,
    K8sCronJobOutput,
    K8sCustomResourceDefinitionOutput,
    K8sDaemonSetOutput,
    K8sDataImportCronOutput,
    K8sDataScienceClusterOutput,
    K8sDataScienceClusterInitializationOutput,
    K8sDataSourceOutput,
    K8sDataVolumeOutput,
    K8sDeploymentOutput,
    K8sDeploymentConfigOutput,
    K8sDevWorkspaceOutput,
    K8sDevWorkspaceTemplateOutput,
    K8sDnsOutput,
    K8sEgressIpOutput,
    K8sEgressRouterOutput,
    K8sEndpointOutput,
    K8sEventOutput,
    K8sForkliftControllerOutput,
    K8sGrafanaOutput,
    K8sGrafanaAlertRuleGroupOutput,
    K8sGrafanaContactPointOutput,
    K8sGrafanaDashboardOutput,
    K8sGrafanaDatasourceOutput,
    K8sGrafanaFolderOutput,
    K8sGrafanaLibraryPanelOutput,
    K8sGrafanaMuteTimingOutput,
    K8sGrafanaNotificationPolicyOutput,
    K8sGrafanaNotificationPolicyRouteOutput,
    K8sGrafanaNotificationTemplateOutput,
    K8sGroupOutput,
    K8sHookOutput,
    K8sHostOutput,
    K8sHostPathProvisionerOutput,
    K8sHyperConvergedOutput,
    K8sIdentityOutput,
    K8sImageStreamOutput,
    K8sIngressOutput,
    K8sInstallplanOutput,
    K8sIsovalentBGPAdvertisementOutput,
    K8sIsovalentBGPClusterConfigOutput,
    K8sIsovalentBGPNodeConfigOutput,
    K8sIsovalentBGPPeerConfigOutput,
    K8sIssuerOutput,
    K8sJobOutput,
    K8sKnativeEventingOutput,
    K8sKnativeServingOutput,
    K8sKnativeKafkaOutput,
    K8sKubevirtOutput,
    K8sLeaseOutput,
    K8sLimitOutput,
    K8sLocalVolumeOutput,
    K8sLocalVolumeSetOutput,
    K8sLocalVolumeDiscoveryOutput,
    K8sLocalVolumeDiscoveryResultOutput,
    K8sLogicalVolumeOutput,
    K8sLvmClusterOutput,
    K8sMachineConfigOutput,
    K8sMachineConfigPoolOutput,
    K8sMigrationOutput,
    K8sMigrationPolicyOutput,
    K8sMutatingWebhookOutput,
    K8sNamespaceOutput,
    K8sNemoCustomizerOutput,
    K8sNemoDatastoreOutput,
    K8sNemoEntitystoreOutput,
    K8sNemoEvaluatorOutput,
    K8sNemoGuardrailOutput,
    K8sNetworkOutput,
    K8sNetworkAddonsConfigOutput,
    K8sNetworkAttachmentDefinitionOutput,
    K8sNetworkMapOutput,
    K8sNetworkOperatorOutput,
    K8sNimBuildOutput,
    K8sNimCacheOutput,
    K8sNimPipelineOutput,
    K8sNimServiceOutput,
    K8sNmstateOutput,
    K8sNodeOutput,
    K8sNodeFeatureOutput,
    K8sNodeFeatureDiscoveryOutput,
    K8sNodeNetworkConfigurationEnactmentOutput,
    K8sNodeNetworkConfigurationPolicyOutput,
    K8sNodeNetworkStateOutput,
    K8sOAuthOutput,
    K8sObjectStoreOutput,
    K8sObjectTransferOutput,
    K8sOcsInitializationOutput,
    K8sOpenstackVolumePopulatorOutput,
    K8sOperatorGroupOutput,
    K8sOvirtVolumePopulatorOutput,
    K8sPackageOutput,
    K8sPerformanceProfileOutput,
    K8sPlanOutput,
    K8sPodOutput,
    K8sPodInfoOutput,
    K8sPodMonitorOutput,
    K8sPolicyBindingOutput,
    K8sPortworxStorageClusterOutput,
    K8sPortworxStorageNodeOutput,
    K8sPriorityClassOutput,
    K8sPrivateNetworkEndpointSliceOutput,
    K8sPrivateNetworkExternalEndpointOutput,
    K8sProbeOutput,
    K8sProfileOutput,
    K8sPrometheusOutput,
    K8sPrometheusRuleOutput,
    K8sPrometheusTargetOutput,
    K8sProviderOutput,
    K8sProxyOutput,
    K8sPvOutput,
    K8sPvcOutput,
    K8sReplicaSetOutput,
    K8sReplicationControllerOutput,
    K8sResourceQuotaOutput,
    K8sRoleOutput,
    K8sRoleBindingOutput,
    K8sRouteOutput,
    K8sSandboxPolicyOutput,
    K8sSandboxPolicyNamespacedOutput,
    K8sSecretOutput,
    K8sSecurityContextConstraintOutput,
    K8sServiceOutput,
    K8sServiceAccountOutput,
    K8sServiceMeshControlPlaneOutput,
    K8sServiceMeshMemberRollOutput,
    K8sServiceMeshMemberOutput,
    K8sServiceMonitorOutput,
    K8sSplunkClusterManagerOutput,
    K8sSplunkClusterMasterOutput,
    K8sSplunkIndexerClusterOutput,
    K8sSplunkLicenseManagerOutput,
    K8sSplunkLicenseMasterOutput,
    K8sSplunkMonitoringConsoleOutput,
    K8sSplunkSearchHeadClusterOutput,
    K8sSplunkStandaloneOutput,
    K8sSriovNetworkOutput,
    K8sSriovNetworkNodePolicyOutput,
    K8sSriovNetworkNodeStateOutput,
    K8sSriovOperatorConfigOutput,
    K8sSspOutput,
    K8sStatefulSetOutput,
    K8sStorageClaimOutput,
    K8sStorageClassOutput,
    K8sStorageClientOutput,
    K8sStorageClusterOutput,
    K8sStorageClusterPeerOutput,
    K8sStorageConsumerOutput,
    K8sStorageMapOutput,
    K8sStorageProfileOutput,
    K8sStorageRequestOutput,
    K8sStorageSystemOutput,
    K8sSubscriptionOutput,
    K8sTetragonNetworkPolicyOutput,
    K8sTetragonNetworkPolicyNamespacedOutput,
    K8sThanosRulerOutput,
    K8sTracingPolicyOutput,
    K8sTracingPolicyNamespacedOutput,
    K8sTunedOutput,
    K8sUploadTokenRequestOutput,
    K8sUserOutput,
    K8sVastClusterOutput,
    K8sVastDriverOutput,
    K8sVastStorageOutput,
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
    K8sVirtualMachinePoolOutput,
    K8sVirtualMachinePreferenceOutput,
    K8sVirtualMachineRestoreOutput,
    K8sVirtualMachineSnapshotOutput,
    K8sVirtualMachineSnapshotContentOutput,
    K8sVolumeAttachmentOutput,
    K8sVolumeCloneSourceOutput,
    K8sVolumeImportSourceOutput,
    K8sVolumeUploadSourceOutput,
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

        K8sAaqOutput.__init__(self)
        K8sAdminJobOutput.__init__(self)
        K8sAlertManagerOutput.__init__(self)
        K8sAlertManagerConfigOutput.__init__(self)
        K8sAlertRuleOutput.__init__(self)
        K8sAuthOutput.__init__(self)
        K8sAuthenticationOutput.__init__(self)
        K8sBareMetalHostOutput.__init__(self)
        K8sBuildConfigOutput.__init__(self)
        K8sCatalogSourceOutput.__init__(self)
        K8sCdiOutput.__init__(self)
        K8sCdiConfigOutput.__init__(self)
        K8sCephBlockPoolOutput.__init__(self)
        K8sCephBlockPoolRadosNamespaceOutput.__init__(self)
        K8sCephBucketNotificationOutput.__init__(self)
        K8sCephBucketTopicOutput.__init__(self)
        K8sCephClientOutput.__init__(self)
        K8sCephClientProfileOutput.__init__(self)
        K8sCephClientProfileMappingOutput.__init__(self)
        K8sCephClusterOutput.__init__(self)
        K8sCephConnectionOutput.__init__(self)
        K8sCephCosiDriverOutput.__init__(self)
        K8sCephDriverOutput.__init__(self)
        K8sCephFilesystemOutput.__init__(self)
        K8sCephFilesystemMirrorOutput.__init__(self)
        K8sCephFilesystemSubVolumeGroupOutput.__init__(self)
        K8sCephNfsOutput.__init__(self)
        K8sCephObjectRealmOutput.__init__(self)
        K8sCephObjectStoreOutput.__init__(self)
        K8sCephObjectStoreUserOutput.__init__(self)
        K8sCephObjectZoneOutput.__init__(self)
        K8sCephObjectZoneGroupOutput.__init__(self)
        K8sCephOperatorConfigOutput.__init__(self)
        K8sCephRdbMirrorOutput.__init__(self)
        K8sCertificateOutput.__init__(self)
        K8sCiliumConfigOutput.__init__(self)
        CiliumLoadBalancerIpPoolOutput.__init__(self)
        K8sClusterOperatorOutput.__init__(self)
        K8sClusterPolicyOutput.__init__(self)
        K8sClusterQuotaOutput.__init__(self)
        K8sClusterRoleBindingOutput.__init__(self)
        K8sClusterServiceVersionOutput.__init__(self)
        K8sClusterVersionOutput.__init__(self)
        K8sClusterwidePrivateNetworkOutput.__init__(self)
        K8sCniOutput.__init__(self)
        K8sConfigMapOutput.__init__(self)
        K8sCronJobOutput.__init__(self)
        K8sCustomResourceDefinitionOutput.__init__(self)
        K8sDaemonSetOutput.__init__(self)
        K8sDataImportCronOutput.__init__(self)
        K8sDataScienceClusterOutput.__init__(self)
        K8sDataScienceClusterInitializationOutput.__init__(self)
        K8sDataSourceOutput.__init__(self)
        K8sDataVolumeOutput.__init__(self)
        K8sDeploymentOutput.__init__(self)
        K8sDeploymentConfigOutput.__init__(self)
        K8sDevWorkspaceOutput.__init__(self)
        K8sDevWorkspaceTemplateOutput.__init__(self)
        K8sDnsOutput.__init__(self)
        K8sEgressIpOutput.__init__(self)
        K8sEgressRouterOutput.__init__(self)
        K8sEndpointOutput.__init__(self)
        K8sEventOutput.__init__(self)
        K8sForkliftControllerOutput.__init__(self)
        K8sGrafanaOutput.__init__(self)
        K8sGrafanaDashboardOutput.__init__(self)
        K8sGrafanaDatasourceOutput.__init__(self)
        K8sGroupOutput.__init__(self)
        K8sHookOutput.__init__(self)
        K8sHostOutput.__init__(self)
        K8sHostPathProvisionerOutput.__init__(self)
        K8sHyperConvergedOutput.__init__(self)
        K8sIdentityOutput.__init__(self)
        K8sImageStreamOutput.__init__(self)
        K8sIngressOutput.__init__(self)
        K8sInstallplanOutput.__init__(self)
        K8sIsovalentBGPAdvertisementOutput.__init__(self)
        K8sIsovalentBGPClusterConfigOutput.__init__(self)
        K8sIsovalentBGPNodeConfigOutput.__init__(self)
        K8sIsovalentBGPPeerConfigOutput.__init__(self)
        K8sIssuerOutput.__init__(self)
        K8sJobOutput.__init__(self)
        K8sKnativeEventingOutput.__init__(self)
        K8sKnativeServingOutput.__init__(self)
        K8sKnativeKafkaOutput.__init__(self)
        K8sKubevirtOutput.__init__(self)
        K8sLeaseOutput.__init__(self)
        K8sLimitOutput.__init__(self)
        K8sLocalVolumeOutput.__init__(self)
        K8sLocalVolumeSetOutput.__init__(self)
        K8sLocalVolumeDiscoveryOutput.__init__(self)
        K8sLocalVolumeDiscoveryResultOutput.__init__(self)
        K8sLogicalVolumeOutput.__init__(self)
        K8sLvmClusterOutput.__init__(self)
        K8sMachineConfigOutput.__init__(self)
        K8sMachineConfigPoolOutput.__init__(self)
        K8sMigrationOutput.__init__(self)
        K8sMigrationPolicyOutput.__init__(self)
        K8sMutatingWebhookOutput.__init__(self)
        K8sNamespaceOutput.__init__(self)
        K8sNemoCustomizerOutput.__init__(self)
        K8sNemoDatastoreOutput.__init__(self)
        K8sNemoEntitystoreOutput.__init__(self)
        K8sNemoEvaluatorOutput.__init__(self)
        K8sNemoGuardrailOutput.__init__(self)
        K8sNetworkOutput.__init__(self)
        K8sNetworkAddonsConfigOutput.__init__(self)
        K8sNetworkAttachmentDefinitionOutput.__init__(self)
        K8sNetworkMapOutput.__init__(self)
        K8sNetworkOperatorOutput.__init__(self)
        K8sNimBuildOutput.__init__(self)
        K8sNimCacheOutput.__init__(self)
        K8sNimPipelineOutput.__init__(self)
        K8sNimServiceOutput.__init__(self)
        K8sNmstateOutput.__init__(self)
        K8sNodeOutput.__init__(self)
        K8sNodeFeatureOutput.__init__(self)
        K8sNodeFeatureDiscoveryOutput.__init__(self)
        K8sNodeNetworkConfigurationEnactmentOutput.__init__(self)
        K8sNodeNetworkConfigurationPolicyOutput.__init__(self)
        K8sNodeNetworkStateOutput.__init__(self)
        K8sOAuthOutput.__init__(self)
        K8sObjectStoreOutput.__init__(self)
        K8sObjectTransferOutput.__init__(self)
        K8sOcsInitializationOutput.__init__(self)
        K8sOpenstackVolumePopulatorOutput.__init__(self)
        K8sOperatorGroupOutput.__init__(self)
        K8sOvirtVolumePopulatorOutput.__init__(self)
        K8sPackageOutput.__init__(self)
        K8sPerformanceProfileOutput.__init__(self)
        K8sPlanOutput.__init__(self)
        K8sPodOutput.__init__(self)
        K8sPodInfoOutput.__init__(self)
        K8sPodMonitorOutput.__init__(self)
        K8sPolicyBindingOutput.__init__(self)
        K8sPortworxStorageClusterOutput.__init__(self)
        K8sPortworxStorageNodeOutput.__init__(self)
        K8sPriorityClassOutput.__init__(self)
        K8sPrivateNetworkEndpointSliceOutput.__init__(self)
        K8sPrivateNetworkExternalEndpointOutput.__init__(self)
        K8sProbeOutput.__init__(self)
        K8sProfileOutput.__init__(self)
        K8sPrometheusOutput.__init__(self)
        K8sPrometheusRuleOutput.__init__(self)
        K8sPrometheusTargetOutput.__init__(self)
        K8sProviderOutput.__init__(self)
        K8sProxyOutput.__init__(self)
        K8sPvOutput.__init__(self)
        K8sPvcOutput.__init__(self)
        K8sReplicaSetOutput.__init__(self)
        K8sReplicationControllerOutput.__init__(self)
        K8sResourceQuotaOutput.__init__(self)
        K8sRoleBindingOutput.__init__(self)
        K8sRouteOutput.__init__(self)
        K8sSandboxPolicyOutput.__init__(self)
        K8sSandboxPolicyNamespacedOutput.__init__(self)
        K8sSecretOutput.__init__(self)
        K8sSecurityContextConstraintOutput.__init__(self)
        K8sServiceMeshControlPlaneOutput.__init__(self)
        K8sServiceMeshMemberRollOutput.__init__(self)
        K8sServiceMeshMemberOutput.__init__(self)
        K8sServiceOutput.__init__(self)
        K8sServiceMonitorOutput.__init__(self)
        K8sServiceMonitorOutput.__init__(self)
        K8sSplunkClusterManagerOutput.__init__(self)
        K8sSplunkClusterMasterOutput.__init__(self)
        K8sSplunkIndexerClusterOutput.__init__(self)
        K8sSplunkLicenseManagerOutput.__init__(self)
        K8sSplunkLicenseMasterOutput.__init__(self)
        K8sSplunkMonitoringConsoleOutput.__init__(self)
        K8sSplunkSearchHeadClusterOutput.__init__(self)
        K8sSplunkStandaloneOutput.__init__(self)
        K8sSriovNetworkOutput.__init__(self)
        K8sSriovNetworkNodePolicyOutput.__init__(self)
        K8sSriovNetworkNodeStateOutput.__init__(self)
        K8sSriovOperatorConfigOutput.__init__(self)
        K8sSspOutput.__init__(self)
        K8sStatefulSetOutput.__init__(self)
        K8sStorageClaimOutput.__init__(self)
        K8sStorageClassOutput.__init__(self)
        K8sStorageClientOutput.__init__(self)
        K8sStorageClusterOutput.__init__(self)
        K8sStorageClusterPeerOutput.__init__(self)
        K8sStorageConsumerOutput.__init__(self)
        K8sStorageMapOutput.__init__(self)
        K8sStorageProfileOutput.__init__(self)
        K8sStorageRequestOutput.__init__(self)
        K8sStorageSystemOutput.__init__(self)
        K8sSubscriptionOutput.__init__(self)
        K8sTetragonNetworkPolicyOutput.__init__(self)
        K8sTetragonNetworkPolicyNamespacedOutput.__init__(self)
        K8sThanosRulerOutput.__init__(self)
        K8sTracingPolicyOutput.__init__(self)
        K8sTracingPolicyNamespacedOutput.__init__(self)
        K8sTunedOutput.__init__(self)
        K8sUploadTokenRequestOutput.__init__(self)
        K8sUserOutput.__init__(self)
        K8sVastClusterOutput.__init__(self)
        K8sVastDriverOutput.__init__(self)
        K8sVastStorageOutput.__init__(self)
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
        K8sVirtualMachinePoolOutput.__init__(self)
        K8sVirtualMachinePreferenceOutput.__init__(self)
        K8sVirtualMachineRestoreOutput.__init__(self)
        K8sVirtualMachineSnapshotOutput.__init__(self)
        K8sVirtualMachineSnapshotContentOutput.__init__(self)
        K8sVolumeAttachmentOutput.__init__(self)
        K8sVolumeCloneSourceOutput.__init__(self)
        K8sVolumeImportSourceOutput.__init__(self)
        K8sVolumeUploadSourceOutput.__init__(self)
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
