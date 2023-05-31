#!/bin/bash

calicoctl patch bgpconfiguration default -p '{"spec": {"prefixAdvertisements": [{"cidr": "172.70.66.66/32", "communities": ["1:128"]},{"cidr": "172.70.66.67/32", "communities": ["1:128"]}]}}'
