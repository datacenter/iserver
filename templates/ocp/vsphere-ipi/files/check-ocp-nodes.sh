#!/bin/bash

export KUBECONFIG=/root/install/auth/kubeconfig
oc get nodes

exit $?