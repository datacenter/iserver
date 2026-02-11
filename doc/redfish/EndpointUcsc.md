# UCS Rack Standalone Redfish Endpoint Type

[[Next]](./EndpointFi.md) [[Back]](./README.md)

Endpoint:
- UCS rack standalone server
- not connected to Fabric Interconnect
- redfish-enabled
- the IP address and credentials below are the same as IMC address and credentials of the server

```
# iserver get redfish uri \
    --type ucsc \
    --ip 10.10.10.10 \
    --username admin \
    --password secret \
    --uri Systems
```

## Authentication Request

Web-based authentication request with username/password authentication requesting new session

```
POST https://10.10.10.10:443/redfish/v1/SessionService/Sessions
Data {'Username': 'admin', 'Password': 'secret'}
```

Expected Authentication Response of 2xx with the following headers:
- Session-ID is in Location header
- Authentication Token in X-Auth-Token header

## GET API

```
GET https://10.10.10.10:443/redfish/v1/Systems
Headers {'X-Auth-Token': 'Token-value'}
```

## Disconnect

```
DELETE https://10.10.10.10:443/redfish/v1/SessionService/Sessions/Session-ID-value
Headers {'X-Auth-Token': 'Token-value'}
```

[[Back]](./README.md)