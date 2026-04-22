class K8sAuthenticationInfo():
    def __init__(self):
        self.authentication = None

    def get_authentication_info(self, managed_object):
        info = self.get_base_info(
            managed_object
        )
        info['spec'] = self.get(managed_object, 'spec')
        info['status'] = self.get(managed_object, 'status')
        info['logLevel'] = self.get(managed_object, 'spec:logLevel', on_error='Normal', on_none='Normal')
        
        condition_map = {}
        condition_map['UnsupportedConfigOverridesUpgradeable'] = 'True'
        condition_map['ManagementStateDegraded'] = 'False'
        condition_map['WebhookAuthenticatorCertApprover_OpenShiftAuthenticatorDegraded'] = 'False'
        condition_map['OAuthClientsController_SwitchedControllerDegraded'] = 'False'
        condition_map['WebhookAuthenticatorControllerDegraded'] = 'False'
        condition_map['ReadyIngressNodesAvailable'] = 'True'
        condition_map['APIServicesAvailable'] = 'True'
        condition_map['APIServicesDegraded'] = 'False'
        condition_map['EncryptionMigrationControllerDegraded'] = 'False'
        condition_map['EncryptionMigrationControllerProgressing'] = 'False'
        condition_map['EncryptionPruneControllerDegraded'] = 'False'
        condition_map['EncryptionKeyControllerDegraded'] = 'False'
        condition_map['EncryptionStateControllerDegraded'] = 'False'
        condition_map['OAuthAPIServerConfigObservationDegraded'] = 'False'
        condition_map['RevisionControllerDegraded'] = 'False'
        condition_map['OAuthServerServiceEndpointAccessibleControllerAvailable'] = 'True'
        condition_map['OAuthServerServiceEndpointAccessibleControllerDegraded'] = 'False'
        condition_map['OAuthServiceDegraded'] = 'False'
        condition_map['SystemServiceCAConfigDegraded'] = 'False'
        condition_map['APIServerDeploymentAvailable'] = 'True'
        condition_map['APIServerDeploymentDegraded'] = 'False'
        condition_map['APIServerDeploymentProgressing'] = 'False'
        condition_map['APIServerWorkloadDegraded'] = 'False'
        condition_map['ExternalOIDCControllerDegraded'] = 'False'
        condition_map['OAuthServerServiceEndpointsEndpointAccessibleControllerAvailable'] = 'True'
        condition_map['OAuthServerServiceEndpointsEndpointAccessibleControllerDegraded'] = 'False'
        condition_map['ResourceSyncControllerDegraded'] = 'False'
        condition_map['IngressStateEndpointsDegraded'] = 'False'
        condition_map['IngressStatePodsDegraded'] = 'False'
        condition_map['AuditPolicyDegraded'] = 'False'
        condition_map['RouterCertsDegraded'] = 'False'
        condition_map['RouterCertsDomainValidationControllerDegraded'] = 'False'
        condition_map['OAuthServerConfigObservationDegraded'] = 'False'
        condition_map['AuthenticatorCertKeyProgressing'] = 'False'
        condition_map['APIServerStaticResourcesDegraded'] = 'False'
        condition_map['OpenshiftAuthenticationStaticResourcesDegraded'] = 'False'
        condition_map['OAuthServerRouteEndpointAccessibleControllerAvailable'] = 'True'
        condition_map['WellKnownAvailable'] = 'True'
        condition_map['WellKnownReadyControllerProgressing'] = 'False'
        condition_map['OAuthClientsControllerDegraded'] = 'False'
        condition_map['WellKnownReadyControllerDegraded'] = 'False'
        condition_map['CustomRouteControllerDegraded'] = 'False'
        condition_map['OAuthServerDeploymentAvailable'] = 'True'
        condition_map['OAuthServerDeploymentDegraded'] = 'False'
        condition_map['OAuthServerDeploymentProgressing'] = 'False'
        condition_map['OAuthServerWorkloadDegraded'] = 'False'
        condition_map['AuthConfigDegraded'] = 'False'
        condition_map['IngressConfigDegraded'] = 'False'
        condition_map['OAuthSystemMetadataDegraded'] = 'False'
        condition_map['OAuthConfigDegraded'] = 'False'
        condition_map['OAuthConfigIngressDegraded'] = 'False'
        condition_map['OAuthConfigRouteDegraded'] = 'False'
        condition_map['OAuthConfigServiceDegraded'] = 'False'
        condition_map['OAuthSessionSecretDegraded'] = 'False'
        condition_map['OAuthServerRouteEndpointAccessibleControllerDegraded'] = 'False'
        condition_map['ProxyConfigControllerDegraded'] = 'False'

        info['error_conditions'] = []
        condition_mos = self.get(managed_object, 'status:conditions', on_error=[], on_none=[])
        for condition_mo in condition_mos:
            condition_type = self.get(condition_mo, 'type', on_error='', on_none='')
            condition_status = self.get(condition_mo, 'status', on_error='', on_none='')
            if condition_type not in condition_map:
                continue

            if condition_map[condition_type].lower() == condition_status.lower():
                continue

            info['error_conditions'].append(
                condition_type
            )

        info['error_conditionsT'] = ','.join(info['error_conditions'])
        if len(info['error_conditionsT']) == 0:
            info['error_conditionsT'] = '---'
            
        return info

    def get_authentications(self, object_filter=None, return_mo=False, cache_enabled=True):
        infos = self.get_infos(
            'authentication', 
            object_filter=object_filter, 
            return_mo=return_mo, 
            cache_enabled=cache_enabled
        )
        return infos

    def get_authentication(self, name, return_mo=False, cache_enabled=True, optimized=True):
        return self.get_info(
            'authentication', 
            name,
            return_mo=return_mo, 
            cache_enabled=cache_enabled,
            optimized=optimized
        )

    def is_authentication(self, name, cache_enabled=True, optimized=True):
        if self.get_authentication(name, cache_enabled=cache_enabled, optimized=optimized) is None:
            return False
        return True
