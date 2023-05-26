# Redfish Endpoint Type

Generic (--type generic) is the default endpoint following standard Redfish authentication and session management rules.

Authentication Request
- https://<endpoint-ip>/redfish/v1/SessionService/Sessions
- JSON payload
    - UserName
    - Password (plain-text)

Authentication Response
- Session-ID is in Location header
- Authentication Token in X-Auth-Token header

Get request
- https://<endpoint-ip>/redfish/v1/<URI>

Disconnect
- https://<endpoint-ip>/redfish/v1/SessionService/Sessions/<session-id>
- header with X-Auth-Token

Notes:
- Deep commands run through entire API tree, with no URI exclusions.
- No predefined template supported.
