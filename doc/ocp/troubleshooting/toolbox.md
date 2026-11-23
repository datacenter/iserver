# toolbox

```
$ sudo su –
# export HTTPS_PROXY=http://proxy.domain.com:80
# podman login registry.redhat.io
Username: your-user
Password:
Login Succeeded!

# podman pull registry.redhat.io/rhel9/support-tools:latest
Trying to pull registry.redhat.io/rhel9/support-tools:latest...
Getting image source signatures
Checking if image destination supports signatures
Copying blob 1153e061da4e done
Copying blob e8a06b74363b done
Copying config c8e694579b done
Writing manifest to image destination
Storing signatures
C8e694579bc61bcd3f742db0d517bb9ab14005b07784a71b08f7d82f3ea2b4a7

# exit

$ toolbox
Checking if there is a newer version of registry.redhat.io/rhel9/support-tools available...
FATA[0060] Error parsing image name "docker://registry.redhat.io/rhel9/support-tools": pinging container registry registry.redhat.io: Get "https://registry.redhat.io/v2/": dial tcp 104.123.92.36:443: i/o timeout
Error inspecting registry.redhat.io/rhel9/support-tools via skopeo
Spawning a container 'toolbox-core' with image 'registry.redhat.io/rhel9/support-tools'
Detected RUN label in the container image. Using that as the default...
69301eb03e39b2bc08dbecd8fdf10e47724b53fdf786754268e1915d8781733c
toolbox-core
Container started successfully. To exit, type 'exit'.
[root@ocp-bm1-1 /]# 
```