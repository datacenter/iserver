# Standard Redfish Endpoint

Standard (--type standard) is the default endpoint following standard Redfish authentication and session management rules.

## Authentication Request

Web-based authentication request with username/password authentication requesting new session
- https://<endpoint-ip>/redfish/v1/SessionService/Sessions
- JSON payload
    - UserName
    - Password (plain-text)

## Authentication Response

Expected Authentication Response of 2xx with the following headers:
- Session-ID is in Location header
- Authentication Token in X-Auth-Token header

## Sending Redfish GET API

Get request must be sent to properly formatted URL i.e. https://<endpoint-ip>/redfish/v1/<URI> with HTTP headers including X-Auth-Token value based on authentication.

## Redfish session disconnect

Being a good citizen means disconnecting the Redfish session when it is not needed by sending HTTP Delete request:
- https://<endpoint-ip>/redfish/v1/SessionService/Sessions/<session-id>
- header with X-Auth-Token

## Notes

- Deep commands run through entire API tree, with no URI exclusions. It may impact the execution time.
- No predefined template supported.
