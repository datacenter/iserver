#!/bin/bash

exit_on_error() {
    exit_code=$1
    if [ $exit_code -ne 0 ]; then
        exit $exit_code
    fi
}

cd /root

echo Create namespace ${NAMESPACE}
kubectl create namespace ${NAMESPACE}
exit_on_error $?

echo Helm install
helm install --debug ${POD} ${CHART} --namespace ${NAMESPACE} --set iwoServerVersion=${SERVER} --set collectorImage.tag=${COLLECTOR} --set targetName=${TARGET}
exit_on_error $?

sleep 5

echo Get IWO POD names
PODS=`kubectl get pods --namespace ${NAMESPACE} -o 'jsonpath={..metadata.name}'`
arrPODS=(${PODS})
for arrPOD in "${arrPODS[@]}"
do
    echo $arrPOD
done

echo Initial PODs state
kubectl get pods --namespace ${NAMESPACE}

echo Wait for IWO pods running state
for arrPOD in "${arrPODS[@]}"
do
    while [[ $(kubectl get pod ${arrPOD} --namespace ${NAMESPACE} -o 'jsonpath={..status.conditions[?(@.type=="Ready")].status}') != "True" ]]; do
        sleep 1
    done
done

echo Ready PODs state
kubectl get pods --namespace ${NAMESPACE}

echo Configure port forwarding
kubectl -n ${NAMESPACE} port-forward ${arrPODS[0]} 9110 &

sleep 5

HTTP_PROXY_ENABLED="${HTTP_PROXY_ENABLED}"
if [ $HTTP_PROXY_ENABLED = "True" ]; then
    echo Configure HTTP Proxy
    curl -XPUT http://localhost:9110/HttpProxies -d '{"ProxyType":"Manual", "ProxyHost":"${HTTP_PROXY_SERVER}", "ProxyPort":${HTTP_PROXY_PORT}}'
    exit_on_error $?
fi

sleep 5

echo Get Device Identifiers
curl -s http://localhost:9110/DeviceIdentifiers -o /tmp/iwo_device_identifiers
exit_on_error $?
cat /tmp/iwo_device_identifiers
echo

echo Get Security Tokens
curl -s http://localhost:9110/SecurityTokens -o /tmp/iwo_security_tokens
exit_on_error $?
cat /tmp/iwo_security_tokens
echo

exit 0