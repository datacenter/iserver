def fixup_clife_url(registry, version):
    if 'isovalent' in registry:
        url = 'https://%s/artifactory/archive/clife-manifests/clife-v%s.tar.gz' % (
            registry,
            version
        )
    else:
        url = 'https://%s/artifactory/isovalent-iep-generic/clife-manifests/clife-v%s.tar.gz' % (
            registry,
            version
        )
    return url


def fixup_tetragon_url(registry):
    if 'isovalent' in registry:
        url = '%s/tetragon-operator-index:v0.0.1' % (registry)
    else:
        url = '%s/isovalent-iep-docker-local/tetragon-operator-index:v0.0.1' % (registry)
    return url