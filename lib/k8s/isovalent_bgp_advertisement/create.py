import yaml
import json
from lib import ip_helper
from menu.common import get_confirmation


class K8sIsovalentBGPAdvertisementCreate():
    def __init__(self):
        pass

    def get_isovalent_bgp_community(self, community):
        communities = {}
        for item in community:
            if len(item.split(':')) == 1:
                if 'wellKnown' not in communities:
                    communities['wellKnown'] = []
                
                communities['wellKnown'].append(item)

            if len(item.split(':')) == 2:
                if 'standard' not in communities:
                    communities['standard'] = []
                
                communities['standard'].append(item)

            if len(item.split(':')) == 3:
                if 'large' not in communities:
                    communities['large'] = []
                
                communities['large'].append(item)

        return communities

    def get_isovalent_bgp_advertisement_body_pod(
            self, 
            name,
            label,
            settings
        ):
        body = {}
        body['apiVersion'] = 'isovalent.com/v1'
        body['kind'] = 'IsovalentBGPAdvertisement'
        body['metadata'] = {}
        body['metadata']['name'] = name
        body['metadata']['labels'] = {}
        for key in label:
            body['metadata']['labels'][key] = label[key]

        body['spec'] = {}
        body['spec']['advertisements'] = []

        advertisement_mo = {}
        advertisement_mo['advertisementType'] = 'PodCIDR'

        if len(settings['community']) > 0:
            advertisement_mo['attributes'] = {}
            advertisement_mo['attributes']['communities'] = self.get_isovalent_bgp_community(settings['community'])

        body['spec']['advertisements'].append(
            advertisement_mo
        )

        return body

    def create_isovalent_bgp_advertisement_pod(
            self, 
            name, 
            label,
            settings,
            confirmation=False, 
            my_output=None, 
            wait=True
        ):
        if my_output is None:
            confirmation = False

        if my_output is not None:
            my_output.default('Create BGP Advertisement for POD subnets', before_newline=True, underline=True)
            my_output.default('- name: %s' % (name))

        current_resource = self.get_isovalent_bgp_advertisement(name, return_mo=True, cache_enabled=False)
        if current_resource is not None:
            if my_output is not None:
                my_output.default('BGP advertisement found and will be updated', before_newline=True)
        else:
            if my_output is not None:
                my_output.default('BGP advertisement not found and will be created', before_newline=True)

        body = self.get_isovalent_bgp_advertisement_body_pod(
            name,
            label,
            settings
        )
        if my_output is not None:
            my_output.default(yaml.dump(body), before_newline=True, wrap='~~~')

        if confirmation:
            if not get_confirmation():
                return False

        if current_resource is None:
            if not self.create_resource(body):
                if my_output is not None:
                    my_output.error('REST API failed')
                return False
        else:
            body['metadata']['resourceVersion'] = current_resource['metadata']['resourceVersion']
            if not self.replace_resource(body):
                if my_output is not None:
                    my_output.error('REST API failed')
                return False

        if my_output is not None:
            if current_resource is None:
                my_output.default('BGP advertisement created', before_newline=True, after_newline=True)
            else:
                my_output.default('BGP advertisement updated', before_newline=True, after_newline=True)

        if not wait or current_resource is not None:
            return True
        
        if my_output is not None:
            my_output.default('Wait for crd...')
    
        if not self.wait_isovalent_bgp_advertisement(name):
            if my_output is not None:
                my_output.error('Timed out')
            return False

        return True    

    def get_isovalent_bgp_advertisement_body_service(
            self, 
            name,
            label,
            settings,
            service_type
        ):
        body = {}
        body['apiVersion'] = 'isovalent.com/v1'
        body['kind'] = 'IsovalentBGPAdvertisement'
        body['metadata'] = {}
        body['metadata']['name'] = name
        body['metadata']['labels'] = {}
        for key in label:
            body['metadata']['labels'][key] = label[key]

        body['spec'] = {}
        body['spec']['advertisements'] = []

        advertisement_mo = {}
        advertisement_mo['advertisementType'] = 'Service'

        advertisement_mo['service'] = {}
        advertisement_mo['service']['addresses'] = [service_type]

        if len(settings['community']) > 0:
            advertisement_mo['attributes'] = {}
            advertisement_mo['attributes']['communities'] = self.get_isovalent_bgp_community(settings['community'])

        if len(settings['selector']) > 0:
            advertisement_mo['selector'] = {}
            advertisement_mo['selector']['matchExpressions'] = []  
            for item in settings['selector']:
                advertisement_mo['selector']['matchExpressions'].append(
                    item
                )

        if settings['aggregatev4'] is not None:
            advertisement_mo['service']['aggregationLengthIPv4'] = settings['aggregatev4']

        if settings['aggregatev6'] is not None:
            advertisement_mo['service']['aggregationLengthIPv6'] = settings['aggregatev6']

        body['spec']['advertisements'].append(
            advertisement_mo
        )

        return body

    def create_isovalent_bgp_advertisement_service(
            self, 
            name, 
            label,
            settings,
            service_type,
            confirmation=False, 
            my_output=None, 
            wait=True
        ):
        if my_output is None:
            confirmation = False

        if my_output is not None:
            my_output.default('Create BGP Advertisement for service %s' % (service_type), before_newline=True, underline=True)
            my_output.default('- name: %s' % (name))

        current_resource = self.get_isovalent_bgp_advertisement(name, return_mo=True, cache_enabled=False)
        if current_resource is not None:
            if my_output is not None:
                my_output.default('BGP advertisement found and will be updated', before_newline=True)
        else:
            if my_output is not None:
                my_output.default('BGP advertisement not found and will be created', before_newline=True)

        body = self.get_isovalent_bgp_advertisement_body_service(
            name,
            label,
            settings,
            service_type
        )
        if my_output is not None:
            my_output.default(yaml.dump(body), before_newline=True, wrap='~~~')

        if confirmation:
            if not get_confirmation():
                return False

        if current_resource is None:
            if not self.create_resource(body):
                if my_output is not None:
                    my_output.error('REST API failed')
                return False
        else:
            body['metadata']['resourceVersion'] = current_resource['metadata']['resourceVersion']
            if not self.replace_resource(body):
                if my_output is not None:
                    my_output.error('REST API failed')
                return False

        if my_output is not None:
            if current_resource is None:
                my_output.default('BGP advertisement created', before_newline=True, after_newline=True)
            else:
                my_output.default('BGP advertisement updated', before_newline=True, after_newline=True)

        if not wait or current_resource is not None:
            return True
        
        if my_output is not None:
            my_output.default('Wait for crd...')
    
        if not self.wait_isovalent_bgp_advertisement(name):
            if my_output is not None:
                my_output.error('Timed out')
            return False

        return True    

    def create_isovalent_bgp_advertisement(
            self, 
            name, 
            label,
            pod,
            cluster,
            lb,
            ext,
            egw,
            confirmation=False, 
            my_output=None, 
            wait=True
        ):
        if pod['enabled']:
            success = self.create_isovalent_bgp_advertisement_pod(
                '%s-pod' % (name), 
                label,
                pod,
                confirmation=confirmation, 
                my_output=my_output, 
                wait=wait
            )
            if not success:
                return False

        if cluster['enabled']:
            success = self.create_isovalent_bgp_advertisement_service(
                '%s-cluster' % (name), 
                label,
                cluster,
                'ClusterIP',
                confirmation=confirmation, 
                my_output=my_output, 
                wait=wait
            )
            if not success:
                return False
            
        if lb['enabled']:
            success = self.create_isovalent_bgp_advertisement_service(
                '%s-lb' % (name), 
                label,
                lb,
                'LoadBalancerIP',
                confirmation=confirmation, 
                my_output=my_output, 
                wait=wait
            )
            if not success:
                return False
            
        if ext['enabled']:
            success = self.create_isovalent_bgp_advertisement_service(
                '%s-ext' % (name), 
                label,
                ext,
                'ExternalIP',
                confirmation=confirmation, 
                my_output=my_output, 
                wait=wait
            )
            if not success:
                return False

        if egw['enabled']:
            success = self.create_isovalent_bgp_advertisement_service(
                '%s-egw' % (name), 
                label,
                ext,
                'EgressGateway',
                confirmation=confirmation, 
                my_output=my_output, 
                wait=wait
            )
            if not success:
                return False

        return True