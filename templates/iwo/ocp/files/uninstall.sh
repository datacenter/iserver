#!/bin/bash

exit_on_error() {
    exit_code=$1
    if [ $exit_code -ne 0 ]; then
        exit $exit_code
    fi
}

echo Helm delete
helm delete -n ${NAMESPACE} ${POD}

echo Namespace delete
kubectl delete namespace ${NAMESPACE}

exit 0