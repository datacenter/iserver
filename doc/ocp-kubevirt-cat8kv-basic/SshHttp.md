# OpenShift Virtualization - Cat8000v Test Results

```
# show ip http server all

HTTP server status: Disabled
HTTP server port: 80
HTTP server active supplementary listener ports: 21111  
HTTP server authentication method: enable
HTTP server auth-retry 0 time-window 0
HTTP server digest algorithm: md5
HTTP server access class: 0
HTTP server IPv4 access class: None
HTTP server IPv6 access class: None
HTTP server base path: 
HTTP File Upload status: Disabled
HTTP server upload path: 
HTTP server help root: 
Maximum number of concurrent server connections allowed: 300
Maximum number of secondary server connections allowed: 50
Server idle time-out: 180 seconds
Server life time-out: 180 seconds
Server session idle time-out: 600 seconds
Maximum number of requests allowed on a connection: 25
Server linger time : 60 seconds
HTTP server active session modules: ALL
HTTP secure server capability: Present
HTTP secure server status: Enabled
HTTP secure server port: 443
HTTP secure server ciphersuite:  rsa-aes-cbc-sha2 rsa-aes-gcm-sha2
        dhe-aes-cbc-sha2 dhe-aes-gcm-sha2 ecdhe-rsa-aes-cbc-sha2
        ecdhe-rsa-aes-gcm-sha2 ecdhe-ecdsa-aes-gcm-sha2
HTTP secure server TLS version:  TLSv1.2 TLSv1.1
HTTP secure server client authentication: Disabled
HTTP secure server PIV authentication: Disabled
HTTP secure server PIV authorization only: Disabled
HTTP secure server trustpoint: TP-self-signed-4246525466
HTTP secure server peer validation trustpoint: 
HTTP secure server ECDHE curve: secp256r1
HTTP secure server active session modules: ALL

HTTP server application session modules:
 Session module Name  Handle Status   Secure-status	Description
HTTP_IFS              1      Active   Active         HTTP based IOS File Server              
SL_HTTP               2      Active   Active         HTTP REST IOS-XE Smart License Server   
OPENRESTY_PKI         3      Active   Active         IOS OpenResty PKI Server                
CWMP_SERVER           4      Active   Active         CWMP Connection Request Server          
NBAR2                 5      Active   Active         NBAR2 HTTP(S) Server                    
HOME_PAGE             6      Active   Active         IOS Homepage Server                     
BANNER_PAGE           7      Active   Active         HTTP Banner Page Server                 
WEB_EXEC              8      Active   Active         HTTP based IOS EXEC Server              
GSI7FBD84765E90-lic   9      Active   Active         license agent app                       
GSI7FBD840C7788-web   10     Active   Active         wsma infra                              
GSI7FBDF227E420-web   11     Active   Active         wsma infra                              
tti-petitioner        12     Active   Active         TTI Petitioner                          
NG_WEBUI              13     Active   Active         Web GUI                                 


HTTP server current connections:
local-ipaddress:port  remote-ipaddress:port  in-bytes  out-bytes
127.0.0.1:21111  127.0.0.1:35348  0  0


Nginx Internal Counters:
Nginx pool = 915
Active connection = 1
Nginx pool available = 904
Maxmum connection Hit = 0



HTTP server statistics:
Accepted connections total: 1 
server accepts handled requests
 2 2 2 
Reading: 0 Writing: 1 Waiting: 0 



HTTP server history:
local-ipaddress:port  remote-ipaddress:port  in-bytes  out-bytes  end-time

127.0.0.1:21111  127.0.0.1:35348  0  404  08:44:31 28/03
127.0.0.1:21111  127.0.0.1:35356  0  277  08:44:33 28/03


conn_history_current_pos: 2 



HTTP server help path: 
```
