# RunIt - Web Server Check

[[Back]](../BareMetalCluster.md) [[Next]](./example_redfish_check.md) [[Prev]](./example_openshift_api_check.md)

Workflow
- check web server http access
- prepare test file 
- download test file via http
- delete test file

> [!NOTE]
> Workflow differences for local vs. remote web server

```
Check web server
----------------
Web server is local
Upload directory found: /home/cisco/image
Check local web server http access...
- http get [http://10.10.10.10:8080] with timeout [5 seconds] and ssl-check [True]
- prepare local file for download: /home/cisco/image/76e85fe7-532f-434d-b13f-5e89b445e1c1
- http get [http://10.10.10.10:8080/76e85fe7-532f-434d-b13f-5e89b445e1c1] with timeout [5 seconds] and ssl-check [True]
Test file uploaded locally to web server and then downloaded successfully via http
```

[[Back]](../BareMetalCluster.md) [[Next]](./example_redfish_check.md) [[Prev]](./example_openshift_api_check.md)