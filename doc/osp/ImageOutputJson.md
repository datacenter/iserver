# Image

## Default output

```
# iserver get osp img --cluster pod1 -o json

Cluster: pod1
[
    {
        "__Output": {
            "status": "Green"
        },
        "name": "esc-5.10",
        "disk_format": "qcow2",
        "container_format": "bare",
        "visibility": "public",
        "size": 1467678720,
        "sizeT": "1,467,678,720",
        "virtual_size": null,
        "status": "active",
        "checksum": "8024dd4edff3b5facd633580f1710f75",
        "protected": false,
        "protectedTick": "\u2717",
        "min_ram": 0,
        "min_disk": 0,
        "owner": "2cced286b74c45ea95c83cc2e5d3b413",
        "os_hidden": false,
        "os_hash_algo": "sha512",
        "os_hash_value": "19f0f5d3ecd21016d1448f7410e2c5df6626f2ac8c31f80d9d3464f29a51e4398f903b534715815f146a46bf2772548241869cc141044e997cdad04f32efc1fa",
        "id": "3bfe62d8-7f36-480f-a6f2-a3e17731c3c6",
        "updated_at": "2023-11-16T16:56:47Z",
        "created_at": "2023-11-16T16:56:04Z",
        "locations": [
            {
                "url": "rbd://a68d132c-d6a2-40c9-ac38-8060e13736b1/images/3bfe62d8-7f36-480f-a6f2-a3e17731c3c6/snap",
                "metadata": {}
            }
        ],
        "file": "/v2/images/3bfe62d8-7f36-480f-a6f2-a3e17731c3c6/file"
    },
    {
        "__Output": {
            "status": "Green"
        },
        "name": "migrate-81288fe18055",
        "disk_format": "qcow2",
        "container_format": "bare",
        "visibility": "private",
        "size": 216596480,
        "sizeT": "216,596,480",
        "virtual_size": null,
        "status": "active",
        "checksum": "bf3e50a15fd2fd5caf9835d21f88162c",
        "protected": false,
        "protectedTick": "\u2717",
        "min_ram": 0,
        "min_disk": 20,
        "owner": "2cced286b74c45ea95c83cc2e5d3b413",
        "os_hidden": false,
        "os_hash_algo": "sha512",
        "os_hash_value": "0a032247ee406e246b0c1034031eed5799fb8522d86bf76f41be518ddf4d0287a57c209fc285040b09a178a3dfea3427147ce855b13eb22746675536ac87f387",
        "id": "a26714e1-bd0c-4dbf-a1a6-3124959327ea",
        "updated_at": "2023-11-02T22:34:10Z",
        "created_at": "2023-11-02T22:34:02Z",
        "locations": [
            {
                "url": "rbd://a68d132c-d6a2-40c9-ac38-8060e13736b1/images/a26714e1-bd0c-4dbf-a1a6-3124959327ea/snap",
                "metadata": {}
            }
        ],
        "file": "/v2/images/a26714e1-bd0c-4dbf-a1a6-3124959327ea/file"
    },
    {
        "__Output": {
            "status": "Green"
        },
        "name": "7d8bb8b5-f286-4466-a583-b493b3084efe",
        "disk_format": "raw",
        "container_format": "bare",
        "visibility": "private",
        "size": 17179869184,
        "sizeT": "17,179,869,184",
        "virtual_size": null,
        "status": "active",
        "checksum": "d4a7872bebf404b37a8776cf14062531",
        "protected": false,
        "protectedTick": "\u2717",
        "min_ram": 0,
        "min_disk": 0,
        "owner": "2cced286b74c45ea95c83cc2e5d3b413",
        "os_hidden": false,
        "os_hash_algo": "sha512",
        "os_hash_value": "b86a0e28936e4b0653dbb847b4c08d54e469ac3bedaf0e7bf6ce2036344825f32cb9ec659bc396c24d5416d677d86596da4709e749db157f304252eb67c02a1d",
        "id": "ae125e9e-3b85-4d23-99f9-0320db76adb5",
        "updated_at": "2023-11-02T08:40:40Z",
        "created_at": "2023-11-02T08:30:54Z",
        "locations": [
            {
                "url": "rbd://a68d132c-d6a2-40c9-ac38-8060e13736b1/images/ae125e9e-3b85-4d23-99f9-0320db76adb5/snap",
                "metadata": {}
            }
        ],
        "file": "/v2/images/ae125e9e-3b85-4d23-99f9-0320db76adb5/file"
    },
    {
        "__Output": {
            "status": "Green"
        },
        "name": "final-before-migration-c8kv-orange",
        "disk_format": "qcow2",
        "container_format": "bare",
        "visibility": "private",
        "size": 2343763968,
        "sizeT": "2,343,763,968",
        "virtual_size": null,
        "status": "active",
        "checksum": "ad42e085b954f5a2214c71c38e2f05ca",
        "protected": false,
        "protectedTick": "\u2717",
        "min_ram": 0,
        "min_disk": 0,
        "owner": "2cced286b74c45ea95c83cc2e5d3b413",
        "os_hidden": false,
        "os_hash_algo": "sha512",
        "os_hash_value": "be8f23500174cf880897c3989a839e8c76f29901f05ac705803771616b20c86a340c232d351dabd0d61efd062e7b8c45978fc21da37a741b693a01d9ba769743",
        "id": "924cb554-021a-49a3-9786-7e5a18efc882",
        "updated_at": "2023-11-01T21:03:20Z",
        "created_at": "2023-11-01T20:55:01Z",
        "locations": [
            {
                "url": "rbd://a68d132c-d6a2-40c9-ac38-8060e13736b1/images/924cb554-021a-49a3-9786-7e5a18efc882/snap",
                "metadata": {}
            }
        ],
        "file": "/v2/images/924cb554-021a-49a3-9786-7e5a18efc882/file"
    },
    {
        "__Output": {
            "status": "Green"
        },
        "name": "my-cirros",
        "disk_format": "qcow2",
        "container_format": "bare",
        "visibility": "private",
        "size": 26351104,
        "sizeT": "26,351,104",
        "virtual_size": null,
        "status": "active",
        "checksum": "acbba3dc308c003078ff3af371827a4e",
        "protected": false,
        "protectedTick": "\u2717",
        "min_ram": 0,
        "min_disk": 0,
        "owner": "2cced286b74c45ea95c83cc2e5d3b413",
        "os_hidden": false,
        "os_hash_algo": "sha512",
        "os_hash_value": "7c758ebcda726e688fca49b7b7ff334c125f0da25e912c9896904c5c6b54063b612225f5cfd0e543f18dffd68ed69c2987a4806959b0c40e8fce2442faf68548",
        "id": "e0840683-9c42-46d1-b19d-13f560333448",
        "updated_at": "2023-10-30T22:10:43Z",
        "created_at": "2023-10-30T22:09:13Z",
        "locations": [
            {
                "url": "rbd://a68d132c-d6a2-40c9-ac38-8060e13736b1/images/e0840683-9c42-46d1-b19d-13f560333448/snap",
                "metadata": {}
            }
        ],
        "file": "/v2/images/e0840683-9c42-46d1-b19d-13f560333448/file"
    },
    {
        "__Output": {
            "status": "Green"
        },
        "name": "cirros",
        "disk_format": "qcow2",
        "container_format": "bare",
        "visibility": "public",
        "size": 16338944,
        "sizeT": "16,338,944",
        "virtual_size": null,
        "status": "active",
        "checksum": "1d3062cd89af34e419f7100277f38b2b",
        "protected": false,
        "protectedTick": "\u2717",
        "min_ram": 0,
        "min_disk": 0,
        "owner": "2cced286b74c45ea95c83cc2e5d3b413",
        "os_hidden": false,
        "os_hash_algo": "sha512",
        "os_hash_value": "553d220ed58cfee7dafe003c446a9f197ab5edf8ffc09396c74187cf83873c877e7ae041cb80f3b91489acf687183adcd689b53b38e3ddd22e627e7f98a09c46",
        "id": "f59b504b-42b7-415f-b34a-72dd53043bc0",
        "updated_at": "2023-10-30T15:04:42Z",
        "created_at": "2023-10-30T15:04:41Z",
        "locations": [
            {
                "url": "rbd://a68d132c-d6a2-40c9-ac38-8060e13736b1/images/f59b504b-42b7-415f-b34a-72dd53043bc0/snap",
                "metadata": {}
            }
        ],
        "file": "/v2/images/f59b504b-42b7-415f-b34a-72dd53043bc0/file"
    },
    {
        "__Output": {
            "status": "Green"
        },
        "name": "rcm-21.28.m15",
        "disk_format": "qcow2",
        "container_format": "bare",
        "visibility": "public",
        "size": 4415356928,
        "sizeT": "4,415,356,928",
        "virtual_size": null,
        "status": "active",
        "checksum": "209e798809cc6e09fc8d07f632cf09d6",
        "protected": false,
        "protectedTick": "\u2717",
        "min_ram": 0,
        "min_disk": 0,
        "owner": "2cced286b74c45ea95c83cc2e5d3b413",
        "os_hidden": false,
        "os_hash_algo": "sha512",
        "os_hash_value": "7c669543928982342bfa3d0cd73e72e5d29ce661410807db25cdbc0788bf26733136f8665c7309ea0ef68b75bebf67f49f6a1471704e312ead41cdbd0bcba6db",
        "id": "8dece690-5977-4a30-a3cb-91f914135ae8",
        "updated_at": "2023-10-25T13:35:36Z",
        "created_at": "2023-10-25T13:33:40Z",
        "locations": [
            {
                "url": "rbd://a68d132c-d6a2-40c9-ac38-8060e13736b1/images/8dece690-5977-4a30-a3cb-91f914135ae8/snap",
                "metadata": {}
            }
        ],
        "file": "/v2/images/8dece690-5977-4a30-a3cb-91f914135ae8/file"
    },
    {
        "__Output": {
            "status": "Green"
        },
        "name": "esc-6.0",
        "disk_format": "qcow2",
        "container_format": "bare",
        "visibility": "public",
        "size": 2036203520,
        "sizeT": "2,036,203,520",
        "virtual_size": null,
        "status": "active",
        "checksum": "24e27098c80de99b112a574a62f1a259",
        "protected": false,
        "protectedTick": "\u2717",
        "min_ram": 0,
        "min_disk": 0,
        "owner": "05b8e996f0654e4491d2e925a91c6250",
        "os_hidden": false,
        "os_hash_algo": "sha512",
        "os_hash_value": "cc1af6af22b3cc674d4b59489704dd43353e5beb266f4077066213a7fcded426b524fc74e30209591ca2f270584a4a7455127c88270564f13143730f9543d959",
        "id": "25c65eef-fa83-481e-a04a-9c1a81a54ccd",
        "updated_at": "2023-10-25T11:05:35Z",
        "created_at": "2023-10-25T11:04:48Z",
        "locations": [
            {
                "url": "rbd://a68d132c-d6a2-40c9-ac38-8060e13736b1/images/25c65eef-fa83-481e-a04a-9c1a81a54ccd/snap",
                "metadata": {}
            }
        ],
        "file": "/v2/images/25c65eef-fa83-481e-a04a-9c1a81a54ccd/file"
    },
    {
        "__Output": {
            "status": "Green"
        },
        "name": "qvpc-di-xf-21.28.m15",
        "disk_format": "qcow2",
        "container_format": "bare",
        "visibility": "public",
        "size": 201064448,
        "sizeT": "201,064,448",
        "virtual_size": null,
        "status": "active",
        "checksum": "d040fa8919c009318c600486f9057b77",
        "protected": false,
        "protectedTick": "\u2717",
        "min_ram": 0,
        "min_disk": 0,
        "owner": "2cced286b74c45ea95c83cc2e5d3b413",
        "os_hidden": false,
        "os_hash_algo": "sha512",
        "os_hash_value": "96039bd30f1fdf93455a54a395f6a5fbc7d594b66fbd914da9589653cbda0a425ddc7ee25c986e95ef38d134e79aa48eb75ebcdee3c497011e130cd105a72e0c",
        "id": "defbeda5-b6fe-43f8-8ecf-dc0b772d032a",
        "updated_at": "2023-10-25T10:04:21Z",
        "created_at": "2023-10-25T10:04:17Z",
        "locations": [
            {
                "url": "rbd://a68d132c-d6a2-40c9-ac38-8060e13736b1/images/defbeda5-b6fe-43f8-8ecf-dc0b772d032a/snap",
                "metadata": {}
            }
        ],
        "file": "/v2/images/defbeda5-b6fe-43f8-8ecf-dc0b772d032a/file"
    },
    {
        "__Output": {
            "status": "Green"
        },
        "name": "qvpc-di-cf-21.28.m15",
        "disk_format": "qcow2",
        "container_format": "bare",
        "visibility": "public",
        "size": 209125376,
        "sizeT": "209,125,376",
        "virtual_size": null,
        "status": "active",
        "checksum": "5ce4a218e2394987b4b48e2782f613f9",
        "protected": false,
        "protectedTick": "\u2717",
        "min_ram": 0,
        "min_disk": 0,
        "owner": "2cced286b74c45ea95c83cc2e5d3b413",
        "os_hidden": false,
        "os_hash_algo": "sha512",
        "os_hash_value": "f45a30c980e78c7268f8ae7df0bc519ecbfb6bd9023f6020145c19b017944328c85367eff00d2782e32418cdff4840007fd3037be4efc17137ef23abd1aea7fe",
        "id": "1bc2eff3-64b4-46eb-8d85-ea288f2793b7",
        "updated_at": "2023-10-25T10:04:05Z",
        "created_at": "2023-10-25T10:03:48Z",
        "locations": [
            {
                "url": "rbd://a68d132c-d6a2-40c9-ac38-8060e13736b1/images/1bc2eff3-64b4-46eb-8d85-ea288f2793b7/snap",
                "metadata": {}
            }
        ],
        "file": "/v2/images/1bc2eff3-64b4-46eb-8d85-ea288f2793b7/file"
    },
    {
        "__Output": {
            "status": "Green"
        },
        "name": "qvpc-si-21.28.m15",
        "disk_format": "qcow2",
        "container_format": "bare",
        "visibility": "public",
        "size": 210370560,
        "sizeT": "210,370,560",
        "virtual_size": null,
        "status": "active",
        "checksum": "55e8916d3911570596ba35cd9aff8357",
        "protected": false,
        "protectedTick": "\u2717",
        "min_ram": 0,
        "min_disk": 0,
        "owner": "2cced286b74c45ea95c83cc2e5d3b413",
        "os_hidden": false,
        "os_hash_algo": "sha512",
        "os_hash_value": "dc73e525d600c472521ea1d6a520815900b4ed720fb4ac4b177df1134508582c54c89dc723c6e6ba435f8438344aeff25fdb40f21e27c7eddbbe2b2bd76549e9",
        "id": "fd4c408c-8860-4111-8ec0-dba64266cdbf",
        "updated_at": "2023-10-25T10:03:24Z",
        "created_at": "2023-10-25T10:03:19Z",
        "locations": [
            {
                "url": "rbd://a68d132c-d6a2-40c9-ac38-8060e13736b1/images/fd4c408c-8860-4111-8ec0-dba64266cdbf/snap",
                "metadata": {}
            }
        ],
        "file": "/v2/images/fd4c408c-8860-4111-8ec0-dba64266cdbf/file"
    },
    {
        "__Output": {
            "status": "Green"
        },
        "name": "image-SDWAN-C8KV01",
        "disk_format": "qcow2",
        "container_format": "bare",
        "visibility": "private",
        "size": 2436956160,
        "sizeT": "2,436,956,160",
        "virtual_size": null,
        "status": "active",
        "checksum": "2d29dd6799f105375eb3ef06184a8bc0",
        "protected": false,
        "protectedTick": "\u2717",
        "min_ram": 0,
        "min_disk": 0,
        "owner": "9b50a8dba82f4c14802c4554482882b8",
        "os_hidden": false,
        "os_hash_algo": "sha512",
        "os_hash_value": "980d97aab820a843991a0428be655513d5547bd5037efc002ebc33ce527b186f5f4d9f5cb35efa3a030bb17670aac24ed91d6d985a4dd28361494ff891547554",
        "id": "9095f375-3afa-46d7-9cce-a0c2a3cd0736",
        "updated_at": "2023-10-23T15:17:32Z",
        "created_at": "2023-10-23T15:16:29Z",
        "locations": [
            {
                "url": "rbd://a68d132c-d6a2-40c9-ac38-8060e13736b1/images/9095f375-3afa-46d7-9cce-a0c2a3cd0736/snap",
                "metadata": {}
            }
        ],
        "file": "/v2/images/9095f375-3afa-46d7-9cce-a0c2a3cd0736/file"
    },
    {
        "__Output": {
            "status": "Green"
        },
        "name": "c8000v_17_09_01a_16G_vga",
        "disk_format": "qcow2",
        "container_format": "bare",
        "visibility": "public",
        "size": 1860567040,
        "sizeT": "1,860,567,040",
        "virtual_size": null,
        "status": "active",
        "checksum": "3836e1c924e21eb55b54397fef415c42",
        "protected": false,
        "protectedTick": "\u2717",
        "min_ram": 0,
        "min_disk": 0,
        "owner": "2cced286b74c45ea95c83cc2e5d3b413",
        "os_hidden": false,
        "os_hash_algo": "sha512",
        "os_hash_value": "ae47ace93c6b0699f99ead5bca646b7be098ff991ba901cb3b1dde2b83ca272aa88898ef06d12c81c60135968d106cae96f0772f31dcbf9d59f3a990dbbdad7a",
        "id": "06e5174d-124d-444d-9aca-8e2e82218865",
        "updated_at": "2023-10-16T15:22:37Z",
        "created_at": "2023-10-16T15:21:58Z",
        "locations": [
            {
                "url": "rbd://a68d132c-d6a2-40c9-ac38-8060e13736b1/images/06e5174d-124d-444d-9aca-8e2e82218865/snap",
                "metadata": {}
            }
        ],
        "file": "/v2/images/06e5174d-124d-444d-9aca-8e2e82218865/file"
    },
    {
        "__Output": {
            "status": "Green"
        },
        "name": "rcm-21.28.2",
        "disk_format": "qcow2",
        "container_format": "bare",
        "visibility": "public",
        "size": 4064215040,
        "sizeT": "4,064,215,040",
        "virtual_size": null,
        "status": "active",
        "checksum": "14617b2ec8249200dd458f6228b0ce1b",
        "protected": false,
        "protectedTick": "\u2717",
        "min_ram": 0,
        "min_disk": 0,
        "owner": "05b8e996f0654e4491d2e925a91c6250",
        "os_hidden": false,
        "os_hash_algo": "sha512",
        "os_hash_value": "6fd472d139c7c8552b7664c6ac077515f5b9f1b2ffafad4ba60ae2c05da6a849c172d33c8205ceb7827be77ab20b7026a783168887926848004a799e5cf0a95a",
        "id": "cf4ca9a7-df96-4676-9ed3-e0b81f38bf64",
        "updated_at": "2022-12-20T13:31:17Z",
        "created_at": "2022-12-20T13:29:55Z",
        "locations": [
            {
                "url": "rbd://a68d132c-d6a2-40c9-ac38-8060e13736b1/images/cf4ca9a7-df96-4676-9ed3-e0b81f38bf64/snap",
                "metadata": {}
            }
        ],
        "file": "/v2/images/cf4ca9a7-df96-4676-9ed3-e0b81f38bf64/file"
    },
    {
        "__Output": {
            "status": "Green"
        },
        "name": "qvpc-si-21.28.h0",
        "disk_format": "qcow2",
        "container_format": "bare",
        "visibility": "public",
        "size": 223150080,
        "sizeT": "223,150,080",
        "virtual_size": null,
        "status": "active",
        "checksum": "dd7dc7d10849d777cdabf22d34894599",
        "protected": false,
        "protectedTick": "\u2717",
        "min_ram": 0,
        "min_disk": 0,
        "owner": "05b8e996f0654e4491d2e925a91c6250",
        "os_hidden": false,
        "os_hash_algo": "sha512",
        "os_hash_value": "e2bf14d237a41ec07c19b7efdb5aee8940e38c9a5d3609b54d0d151d5f627dfd53c6f525b34b778e59d8af7765d5cc94b56c18340312e88026a3ed98730e0768",
        "id": "69c7b87a-a951-46c6-b9de-0b2cffddd11c",
        "updated_at": "2022-12-20T13:15:11Z",
        "created_at": "2022-12-20T13:15:07Z",
        "locations": [
            {
                "url": "rbd://a68d132c-d6a2-40c9-ac38-8060e13736b1/images/69c7b87a-a951-46c6-b9de-0b2cffddd11c/snap",
                "metadata": {}
            }
        ],
        "file": "/v2/images/69c7b87a-a951-46c6-b9de-0b2cffddd11c/file"
    },
    {
        "__Output": {
            "status": "Green"
        },
        "name": "qvpc-si-21.28.2",
        "disk_format": "qcow2",
        "container_format": "bare",
        "visibility": "public",
        "size": 212074496,
        "sizeT": "212,074,496",
        "virtual_size": null,
        "status": "active",
        "checksum": "4858ef8e164ac5fe3c8df7265122fadd",
        "protected": false,
        "protectedTick": "\u2717",
        "min_ram": 0,
        "min_disk": 0,
        "owner": "05b8e996f0654e4491d2e925a91c6250",
        "os_hidden": false,
        "os_hash_algo": "sha512",
        "os_hash_value": "48994ebdac2a4235d7a1b09ffb0b392d43e54744006cf424e2fe64b4456eb62e182184b99da0e62e6f2495d7b9c4e6f2a95a50cb66210f29800958ca3320feb1",
        "id": "20f03ddd-8b1f-4846-a4af-bd3d982c2a5c",
        "updated_at": "2022-12-20T13:14:53Z",
        "created_at": "2022-12-20T13:14:48Z",
        "locations": [
            {
                "url": "rbd://a68d132c-d6a2-40c9-ac38-8060e13736b1/images/20f03ddd-8b1f-4846-a4af-bd3d982c2a5c/snap",
                "metadata": {}
            }
        ],
        "file": "/v2/images/20f03ddd-8b1f-4846-a4af-bd3d982c2a5c/file"
    },
    {
        "__Output": {
            "status": "Green"
        },
        "name": "qvpc-di-cf-21.28.2",
        "disk_format": "qcow2",
        "container_format": "bare",
        "visibility": "public",
        "size": 210894848,
        "sizeT": "210,894,848",
        "virtual_size": null,
        "status": "active",
        "checksum": "0bd42ab4e337ed927639bafe778afca1",
        "protected": false,
        "protectedTick": "\u2717",
        "min_ram": 0,
        "min_disk": 0,
        "owner": "05b8e996f0654e4491d2e925a91c6250",
        "os_hidden": false,
        "os_hash_algo": "sha512",
        "os_hash_value": "092674eed61bd55cb2ccadfb9ceb07f2ca1b3a9029862e72027380c8e0d316b9a0e102314d021e6f461fc37ee95441921ef979e8e8026d517325fc7aef2dcdd4",
        "id": "4ccad0e8-821e-4b3f-8465-66abd2ff449e",
        "updated_at": "2022-12-20T13:14:28Z",
        "created_at": "2022-12-20T13:14:23Z",
        "locations": [
            {
                "url": "rbd://a68d132c-d6a2-40c9-ac38-8060e13736b1/images/4ccad0e8-821e-4b3f-8465-66abd2ff449e/snap",
                "metadata": {}
            }
        ],
        "file": "/v2/images/4ccad0e8-821e-4b3f-8465-66abd2ff449e/file"
    },
    {
        "__Output": {
            "status": "Green"
        },
        "name": "qvpc-di-xf-21.28.2",
        "disk_format": "qcow2",
        "container_format": "bare",
        "visibility": "public",
        "size": 202833920,
        "sizeT": "202,833,920",
        "virtual_size": null,
        "status": "active",
        "checksum": "63d734d4d329406f8910c226784c02f0",
        "protected": false,
        "protectedTick": "\u2717",
        "min_ram": 0,
        "min_disk": 0,
        "owner": "05b8e996f0654e4491d2e925a91c6250",
        "os_hidden": false,
        "os_hash_algo": "sha512",
        "os_hash_value": "89b93414b36c61853e8ec059baa0de136f8facbf34f35e40113bada4abc39b98398eed9b9ac08e170ff6e4127a53163e45f31fa803304d57773b75c28f67af3a",
        "id": "8b9edb94-63dd-4a5a-8871-4d9d61b0cae3",
        "updated_at": "2022-12-20T13:14:09Z",
        "created_at": "2022-12-20T13:14:03Z",
        "locations": [
            {
                "url": "rbd://a68d132c-d6a2-40c9-ac38-8060e13736b1/images/8b9edb94-63dd-4a5a-8871-4d9d61b0cae3/snap",
                "metadata": {}
            }
        ],
        "file": "/v2/images/8b9edb94-63dd-4a5a-8871-4d9d61b0cae3/file"
    },
    {
        "__Output": {
            "status": "Green"
        },
        "name": "smi-install-disk.20211122",
        "disk_format": "raw",
        "container_format": "bare",
        "visibility": "public",
        "size": 443547648,
        "sizeT": "443,547,648",
        "virtual_size": null,
        "status": "active",
        "checksum": "5c076926d5c741e57a1b64cfe222dd72",
        "protected": false,
        "protectedTick": "\u2717",
        "min_ram": 0,
        "min_disk": 0,
        "owner": "05b8e996f0654e4491d2e925a91c6250",
        "os_hidden": false,
        "os_hash_algo": "sha512",
        "os_hash_value": "020f810236e291f0b19f17da22e2b2a13a020e98d32110f4567a660c15f01777371ef5fda636896a6c62207a8364315ac21ee85669661bf9c4bd4987518dbe67",
        "id": "dba69f93-008e-4cf6-9774-685897e08550",
        "updated_at": "2022-08-15T10:43:24Z",
        "created_at": "2022-08-15T10:43:13Z",
        "locations": [
            {
                "url": "rbd://a68d132c-d6a2-40c9-ac38-8060e13736b1/images/dba69f93-008e-4cf6-9774-685897e08550/snap",
                "metadata": {}
            }
        ],
        "file": "/v2/images/dba69f93-008e-4cf6-9774-685897e08550/file"
    },
    {
        "__Output": {
            "status": "Green"
        },
        "name": "qvpc-di-xf-21.27.1",
        "disk_format": "qcow2",
        "container_format": "bare",
        "visibility": "public",
        "size": 201392128,
        "sizeT": "201,392,128",
        "virtual_size": null,
        "status": "active",
        "checksum": "cd2b564b606bd46a3d2e7b2060a72225",
        "protected": false,
        "protectedTick": "\u2717",
        "min_ram": 0,
        "min_disk": 0,
        "owner": "05b8e996f0654e4491d2e925a91c6250",
        "os_hidden": false,
        "os_hash_algo": "sha512",
        "os_hash_value": "aa8d68a52e0ac5bdfc56c9e82d983472cc82411a82786ac0084c80f996a18b66df2c7a9dd6f40d0ea597a85120004bd59be747f6961a0dc05c9ba0226027fdc4",
        "id": "7c299f8a-a8b8-4090-ac3f-d78ef1d5c77a",
        "updated_at": "2022-08-04T16:37:30Z",
        "created_at": "2022-08-04T16:37:25Z",
        "locations": [
            {
                "url": "rbd://a68d132c-d6a2-40c9-ac38-8060e13736b1/images/7c299f8a-a8b8-4090-ac3f-d78ef1d5c77a/snap",
                "metadata": {}
            }
        ],
        "file": "/v2/images/7c299f8a-a8b8-4090-ac3f-d78ef1d5c77a/file"
    },
    {
        "__Output": {
            "status": "Green"
        },
        "name": "qvpc-di-cf-21.27.1",
        "disk_format": "qcow2",
        "container_format": "bare",
        "visibility": "public",
        "size": 209518592,
        "sizeT": "209,518,592",
        "virtual_size": null,
        "status": "active",
        "checksum": "e0892942de2fb8f6fc47b72150c7e307",
        "protected": false,
        "protectedTick": "\u2717",
        "min_ram": 0,
        "min_disk": 0,
        "owner": "05b8e996f0654e4491d2e925a91c6250",
        "os_hidden": false,
        "os_hash_algo": "sha512",
        "os_hash_value": "d3a5452ff00f77f5d2971871005701491e949b3779071b21bab607cd0243c9718ea6260dc18195337d4d5fe34000a8fbab0b72544e7fabe868a01831b2a0c8ee",
        "id": "9a0384ca-801f-4c5f-97b1-cd48b18ec365",
        "updated_at": "2022-08-04T16:37:23Z",
        "created_at": "2022-08-04T16:37:18Z",
        "locations": [
            {
                "url": "rbd://a68d132c-d6a2-40c9-ac38-8060e13736b1/images/9a0384ca-801f-4c5f-97b1-cd48b18ec365/snap",
                "metadata": {}
            }
        ],
        "file": "/v2/images/9a0384ca-801f-4c5f-97b1-cd48b18ec365/file"
    },
    {
        "__Output": {
            "status": "Green"
        },
        "name": "qvpc-si-21.27.h0",
        "disk_format": "qcow2",
        "container_format": "bare",
        "visibility": "public",
        "size": 221839360,
        "sizeT": "221,839,360",
        "virtual_size": null,
        "status": "active",
        "checksum": "5c4eb0fb4fbd048fa01b4b91707ed20e",
        "protected": false,
        "protectedTick": "\u2717",
        "min_ram": 0,
        "min_disk": 0,
        "owner": "05b8e996f0654e4491d2e925a91c6250",
        "os_hidden": false,
        "os_hash_algo": "sha512",
        "os_hash_value": "389bc62177c4db6508e512429b86784b463ee24afe0ec230660c2d174d50b48b8ad22978bed89ea10835b1b6cd1beea77260f0122147b5b99d71ccd9ef8c4801",
        "id": "5b7446f5-882b-4639-86a6-43b5b4b0b9de",
        "updated_at": "2022-08-04T16:36:33Z",
        "created_at": "2022-08-04T16:36:28Z",
        "locations": [
            {
                "url": "rbd://a68d132c-d6a2-40c9-ac38-8060e13736b1/images/5b7446f5-882b-4639-86a6-43b5b4b0b9de/snap",
                "metadata": {}
            }
        ],
        "file": "/v2/images/5b7446f5-882b-4639-86a6-43b5b4b0b9de/file"
    },
    {
        "__Output": {
            "status": "Green"
        },
        "name": "rcm-21.27.1",
        "disk_format": "qcow2",
        "container_format": "bare",
        "visibility": "public",
        "size": 3726704640,
        "sizeT": "3,726,704,640",
        "virtual_size": null,
        "status": "active",
        "checksum": "904d622f8c15e3e41200de718d509559",
        "protected": false,
        "protectedTick": "\u2717",
        "min_ram": 0,
        "min_disk": 0,
        "owner": "05b8e996f0654e4491d2e925a91c6250",
        "os_hidden": false,
        "os_hash_algo": "sha512",
        "os_hash_value": "e74f61554f788f35d0e6b2f8d0c25b27e2176ae28cb3c255873d9c23ae191a3ef2a6476e97c52b9f0693a0c35617cdd0473fa886b7bf9d470f341284360dbf02",
        "id": "f463944b-ad54-494a-b841-0b5f0f66291c",
        "updated_at": "2022-08-04T16:36:26Z",
        "created_at": "2022-08-04T16:35:09Z",
        "locations": [
            {
                "url": "rbd://a68d132c-d6a2-40c9-ac38-8060e13736b1/images/f463944b-ad54-494a-b841-0b5f0f66291c/snap",
                "metadata": {}
            }
        ],
        "file": "/v2/images/f463944b-ad54-494a-b841-0b5f0f66291c/file"
    },
    {
        "__Output": {
            "status": "Green"
        },
        "name": "portal-snapshot-20220802",
        "disk_format": "qcow2",
        "container_format": "bare",
        "visibility": "public",
        "size": 80702210048,
        "sizeT": "80,702,210,048",
        "virtual_size": null,
        "status": "active",
        "checksum": "06668115973408eaf8950f2d0eeff560",
        "protected": false,
        "protectedTick": "\u2717",
        "min_ram": 0,
        "min_disk": 0,
        "owner": "05b8e996f0654e4491d2e925a91c6250",
        "os_hidden": false,
        "os_hash_algo": "sha512",
        "os_hash_value": "86819cd81df75e97e98a0ff891e7cc39a7a214a9fee56b5fc8fb1c666b0f2e9ded66b85962580a55a52b1896606f1bae85d2de915a5aa1294b0fdff9b8fcc620",
        "id": "f7ba2608-75f2-4a4a-b6e7-41566665f52f",
        "updated_at": "2022-08-04T11:59:34Z",
        "created_at": "2022-08-04T11:32:08Z",
        "locations": [
            {
                "url": "rbd://a68d132c-d6a2-40c9-ac38-8060e13736b1/images/f7ba2608-75f2-4a4a-b6e7-41566665f52f/snap",
                "metadata": {}
            }
        ],
        "file": "/v2/images/f7ba2608-75f2-4a4a-b6e7-41566665f52f/file"
    },
    {
        "__Output": {
            "status": "Green"
        },
        "name": "lattice-snapshot-20220802",
        "disk_format": "qcow2",
        "container_format": "bare",
        "visibility": "public",
        "size": 23308992512,
        "sizeT": "23,308,992,512",
        "virtual_size": null,
        "status": "active",
        "checksum": "114e9ea949c75b47e937b80a3a85f05c",
        "protected": false,
        "protectedTick": "\u2717",
        "min_ram": 0,
        "min_disk": 0,
        "owner": "05b8e996f0654e4491d2e925a91c6250",
        "os_hidden": false,
        "os_hash_algo": "sha512",
        "os_hash_value": "2e59e984b157533dbed16c95e099d80b7be5ed89cb74e2fd089182a21181dca9d9b4a307780092ea44f1c02e538ffbc890c0f00277701bb5094b7696221470a8",
        "id": "407ac7cc-2757-4fe3-abf5-9a29925aa639",
        "updated_at": "2022-08-04T11:24:40Z",
        "created_at": "2022-08-04T11:16:34Z",
        "locations": [
            {
                "url": "rbd://a68d132c-d6a2-40c9-ac38-8060e13736b1/images/407ac7cc-2757-4fe3-abf5-9a29925aa639/snap",
                "metadata": {}
            }
        ],
        "file": "/v2/images/407ac7cc-2757-4fe3-abf5-9a29925aa639/file"
    },
    {
        "__Output": {
            "status": "Green"
        },
        "name": "ubuntu-1804-i386",
        "disk_format": "qcow2",
        "container_format": "bare",
        "visibility": "public",
        "size": 351797248,
        "sizeT": "351,797,248",
        "virtual_size": null,
        "status": "active",
        "checksum": "cec3dec44f5437a087b70403df7e6487",
        "protected": false,
        "protectedTick": "\u2717",
        "min_ram": 0,
        "min_disk": 0,
        "owner": "05b8e996f0654e4491d2e925a91c6250",
        "os_hidden": false,
        "os_hash_algo": "sha512",
        "os_hash_value": "e379b78914b68ac5bc8e31e244c675c23fab25400a09944af60fbd1d4d9f1192e01b3686ae6de4188ed82d721de5053dd6ba348be5d9376c3a0048c4b8b8cb34",
        "id": "b659442c-b5e8-4bdf-a15e-a6c43695c317",
        "updated_at": "2022-08-04T11:03:55Z",
        "created_at": "2022-08-04T11:03:43Z",
        "locations": [
            {
                "url": "rbd://a68d132c-d6a2-40c9-ac38-8060e13736b1/images/b659442c-b5e8-4bdf-a15e-a6c43695c317/snap",
                "metadata": {}
            }
        ],
        "file": "/v2/images/b659442c-b5e8-4bdf-a15e-a6c43695c317/file"
    },
    {
        "__Output": {
            "status": "Green"
        },
        "name": "ubuntu-2204-amd64",
        "disk_format": "qcow2",
        "container_format": "bare",
        "visibility": "public",
        "size": 624361472,
        "sizeT": "624,361,472",
        "virtual_size": null,
        "status": "active",
        "checksum": "2454ccb3b986448911f6b5e99ca7d9c7",
        "protected": false,
        "protectedTick": "\u2717",
        "min_ram": 0,
        "min_disk": 0,
        "owner": "05b8e996f0654e4491d2e925a91c6250",
        "os_hidden": false,
        "os_hash_algo": "sha512",
        "os_hash_value": "6c9100e4fae15aab30b471daafa3850b80f6d75c9b730a038bd5f1a300ab6e3583ec4ad8716657ec434c88adbb102457e3a2346345e20ce7bec506adf7510164",
        "id": "273bf614-2aba-4f4f-8f0f-5c782dc90b40",
        "updated_at": "2022-08-04T11:03:39Z",
        "created_at": "2022-08-04T11:03:27Z",
        "locations": [
            {
                "url": "rbd://a68d132c-d6a2-40c9-ac38-8060e13736b1/images/273bf614-2aba-4f4f-8f0f-5c782dc90b40/snap",
                "metadata": {}
            }
        ],
        "file": "/v2/images/273bf614-2aba-4f4f-8f0f-5c782dc90b40/file"
    },
    {
        "__Output": {
            "status": "Green"
        },
        "name": "qvpc-si-21.27.1",
        "disk_format": "qcow2",
        "container_format": "bare",
        "visibility": "public",
        "size": 210763776,
        "sizeT": "210,763,776",
        "virtual_size": null,
        "status": "active",
        "checksum": "d1f670c32c80d1282e5b24d6b190aab4",
        "protected": false,
        "protectedTick": "\u2717",
        "min_ram": 0,
        "min_disk": 0,
        "owner": "05b8e996f0654e4491d2e925a91c6250",
        "os_hidden": false,
        "os_hash_algo": "sha512",
        "os_hash_value": "ac3db7604e896339284c8ac6fe568c4b3923f7a3ae80b54c8392d18461d2aab9967fabf0be0dd676c36656f691685c791fd5b2b7eef280fd158549d8b61e97f5",
        "id": "7de8f319-097f-44da-ae3f-42229d6102e6",
        "updated_at": "2022-08-04T11:01:54Z",
        "created_at": "2022-08-04T11:01:49Z",
        "locations": [
            {
                "url": "rbd://a68d132c-d6a2-40c9-ac38-8060e13736b1/images/7de8f319-097f-44da-ae3f-42229d6102e6/snap",
                "metadata": {}
            }
        ],
        "file": "/v2/images/7de8f319-097f-44da-ae3f-42229d6102e6/file"
    },
    {
        "__Output": {
            "status": "Green"
        },
        "name": "esc-5.6",
        "disk_format": "qcow2",
        "container_format": "bare",
        "visibility": "public",
        "size": 1451753472,
        "sizeT": "1,451,753,472",
        "virtual_size": null,
        "status": "active",
        "checksum": "67c062ee700b9ccf6bb2adb7e9be52b9",
        "protected": false,
        "protectedTick": "\u2717",
        "min_ram": 0,
        "min_disk": 0,
        "owner": "05b8e996f0654e4491d2e925a91c6250",
        "os_hidden": false,
        "os_hash_algo": "sha512",
        "os_hash_value": "ffbc995d43e7b9ee50a491a04d11d0c97cbd98e444e3d2f119d657223a97c484f90ca93aaec80aea31cdc6860b47827cd1b0c83cb71bb77d000d787b19ab831c",
        "id": "969f3733-a8a7-4af1-89f7-8cc44b683550",
        "updated_at": "2022-08-04T11:01:20Z",
        "created_at": "2022-08-04T11:00:47Z",
        "locations": [
            {
                "url": "rbd://a68d132c-d6a2-40c9-ac38-8060e13736b1/images/969f3733-a8a7-4af1-89f7-8cc44b683550/snap",
                "metadata": {}
            }
        ],
        "file": "/v2/images/969f3733-a8a7-4af1-89f7-8cc44b683550/file"
    },
    {
        "__Output": {
            "status": "Green"
        },
        "name": "RHEL-guest-image",
        "disk_format": "qcow2",
        "container_format": "bare",
        "visibility": "shared",
        "size": 1196818432,
        "sizeT": "1,196,818,432",
        "virtual_size": null,
        "status": "active",
        "checksum": "f0b3efae6e9eb9e2d500ed78b2544755",
        "protected": false,
        "protectedTick": "\u2717",
        "min_ram": 0,
        "min_disk": 0,
        "owner": "2cced286b74c45ea95c83cc2e5d3b413",
        "os_hidden": false,
        "os_hash_algo": "sha512",
        "os_hash_value": "9c623218a59799bc6f6b200028122d84fbfd10995a1f56338420ac0607a091e6238d16a8d9e67c8a2f05ea61c1bec7ae45c3164a6adf8606055de862dc1b2620",
        "id": "199c6764-3d9b-41f0-941c-61a9aa785e23",
        "updated_at": "2022-08-03T15:50:27Z",
        "created_at": "2022-08-03T15:50:01Z",
        "locations": [
            {
                "url": "rbd://a68d132c-d6a2-40c9-ac38-8060e13736b1/images/199c6764-3d9b-41f0-941c-61a9aa785e23/snap",
                "metadata": {}
            }
        ],
        "file": "/v2/images/199c6764-3d9b-41f0-941c-61a9aa785e23/file"
    }
]
```

Developer

```
# iserver get osp img --cluster pod1 -o json

{
    "duration": 3747,
    "osp": {
        "read": true,
        "success": 1,
        "failed": 0,
        "mo": 1,
        "mo_time": 0,
        "total_time": 0
    },
    "error": {
        "read": false,
        "lines": 0
    },
    "info": {
        "read": false,
        "lines": 0
    },
    "debug": {
        "read": true,
        "lines": 3
    },
    "cache_hits": 0
}

Log: osp
---------

2023-11-19 12:22:56.314063	True	0	get	images
```

[[Back]](./ImageGet.md)