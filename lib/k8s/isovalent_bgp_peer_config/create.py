import yaml
import json
from lib import ip_helper
from menu.common import get_confirmation


class K8sIsovalentBGPPeerConfigCreate():
    def __init__(self):
        pass

    def get_isovalent_bgp_peer_config_body(
            self, 
            name,
            label,
            address_family,
            retry,
            hold,
            keepalive,
            multihop,
            graceful,
            restart,
            port,
            secret,
            bfd
        ):
        body = {}
        body['apiVersion'] = 'isovalent.com/v1'
        body['kind'] = 'IsovalentBGPPeerConfig'
        body['metadata'] = {}
        body['metadata']['name'] = name
        body['spec'] = {}

        body['spec']['families'] = []
        for item in address_family:
            if item == 'v4':
                family_mo = {}
                family_mo['afi'] = 'ipv4'
                family_mo['safi'] = 'unicast'
                family_mo['advertisements'] = {}
                family_mo['advertisements']['matchLabels'] = {}
                for key in label:
                    family_mo['advertisements']['matchLabels'][key] = label[key]
                body['spec']['families'].append(
                    family_mo
                )

            if item == 'v6':
                family_mo = {}
                family_mo['afi'] = 'ipv6'
                family_mo['safi'] = 'unicast'
                family_mo['advertisements'] = {}
                family_mo['advertisements']['matchLabels'] = {}
                for key in label:
                    family_mo['advertisements']['matchLabels'][key] = label[key]
                body['spec']['families'].append(
                    family_mo
                )

            if item == 'vpn':
                family_mo = {}
                family_mo['afi'] = 'ipv4'
                family_mo['safi'] = 'mpls_vpn'
                family_mo['advertisements'] = {}
                family_mo['advertisements']['matchLabels'] = {}
                for key in label:
                    family_mo['advertisements']['matchLabels'][key] = label[key]
                body['spec']['families'].append(
                    family_mo
                )

        body['spec']['timers'] = {}
        body['spec']['timers']['connectRetryTimeSeconds'] = retry
        body['spec']['timers']['holdTimeSeconds'] = hold
        body['spec']['timers']['keepAliveTimeSeconds'] = keepalive
        body['spec']['ebgpMultihop'] = multihop

        if not graceful and restart > 0:
            body['spec']['gracefulRestart'] = {}
            body['spec']['gracefulRestart']['enabled'] = False

        if graceful:
            body['spec']['gracefulRestart'] = {}
            body['spec']['gracefulRestart']['enabled'] = True
            if restart > 0:
                body['spec']['gracefulRestart']['restartTimeSeconds'] = restart

        body['spec']['transport'] = {}
        body['spec']['transport']['peerPort'] = port

        if secret is not None:
            body['spec']['authSecretRef'] = secret

        if bfd is not None:
            body['spec']['bfdProfileRef'] = bfd

        return body

    def create_isovalent_bgp_peer_config(
            self, 
            name, 
            label,
            address_family,
            retry,
            hold,
            keepalive,
            multihop,
            graceful,
            restart,
            port,
            secret,
            bfd,
            confirmation=False, 
            my_output=None, 
            wait=True
        ):
        if my_output is None:
            confirmation = False

        if my_output is not None:
            my_output.default('Create BGP Peer Config', before_newline=True, underline=True)
            my_output.default('- name: %s' % (name))

        current_peer_config = self.get_isovalent_bgp_peer_config(name, return_mo=True, cache_enabled=False)
        if current_peer_config is not None:
            if my_output is not None:
                my_output.default('BGP peer configuration found and will be updated', before_newline=True)
        else:
            if my_output is not None:
                my_output.default('BGP peer configuration not found and will be created', before_newline=True)

        body = self.get_isovalent_bgp_peer_config_body(
            name,
            label,
            address_family,
            retry,
            hold,
            keepalive,
            multihop,
            graceful,
            restart,
            port,
            secret,
            bfd
        )
        if my_output is not None:
            my_output.default(yaml.dump(body), before_newline=True, wrap='~~~')

        if confirmation:
            if not get_confirmation():
                return False

        if current_peer_config is None:
            if not self.create_resource(body):
                if my_output is not None:
                    my_output.error('REST API failed')
                return False

        if current_peer_config is not None:
            body['metadata']['resourceVersion'] = current_peer_config['metadata']['resourceVersion']
            if not self.replace_resource(body):
                if my_output is not None:
                    my_output.error('REST API failed')
                return False

        if my_output is not None:
            my_output.default('BGP peer configuration created', before_newline=True, after_newline=True)

        if not wait:
            return True
        
        if my_output is not None:
            my_output.default('Wait for crd...')
    
        if not self.wait_isovalent_bgp_peer_config(name):
            if my_output is not None:
                my_output.error('Timed out')
            return False

        return True    
