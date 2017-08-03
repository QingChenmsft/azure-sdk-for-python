# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator 1.2.2.0
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ClusterUpdateParameters(Model):
    """Cluster update request.

    :param reliability_level: This level is used to set the number of replicas
     of the system services. Possible values include: 'Bronze', 'Silver',
     'Gold'
    :type reliability_level: str or :class:`enum
     <azure.mgmt.servicefabric.models.enum>`
    :param upgrade_mode: Cluster upgrade mode indicates if fabric upgrade is
     initiated automatically by the system or not. Possible values include:
     'Automatic', 'Manual'
    :type upgrade_mode: str or :class:`enum
     <azure.mgmt.servicefabric.models.enum>`
    :param cluster_code_version: The ServiceFabric code version, if set it,
     please make sure you have set upgradeMode to Manual, otherwise ,it will
     fail, if you are using PUT new cluster, you can get the version by using
     ClusterVersions_List, if you are updating existing cluster, you can get
     the availableClusterVersions from Clusters_Get
    :type cluster_code_version: str
    :param certificate: This primay certificate will be used as cluster node
     to node security, SSL certificate for cluster management endpoint and
     default admin client, the certificate should exist in the virtual machine
     scale sets or Azure key vault, before you add it. It will override
     original value
    :type certificate: :class:`CertificateDescription
     <azure.mgmt.servicefabric.models.CertificateDescription>`
    :param client_certificate_thumbprints: The client thumbprint details, it
     is used for client access for cluster operation, it will override existing
     collection
    :type client_certificate_thumbprints: list of
     :class:`ClientCertificateThumbprint
     <azure.mgmt.servicefabric.models.ClientCertificateThumbprint>`
    :param client_certificate_common_names: List of client certificates to
     whitelist based on common names.
    :type client_certificate_common_names: list of
     :class:`ClientCertificateCommonName
     <azure.mgmt.servicefabric.models.ClientCertificateCommonName>`
    :param fabric_settings: List of custom fabric settings to configure the
     cluster, Note, it will overwrite existing collection
    :type fabric_settings: list of :class:`SettingsSectionDescription
     <azure.mgmt.servicefabric.models.SettingsSectionDescription>`
    :param reverse_proxy_certificate: Certificate for the reverse proxy
    :type reverse_proxy_certificate: :class:`CertificateDescription
     <azure.mgmt.servicefabric.models.CertificateDescription>`
    :param node_types: The list of nodetypes that make up the cluster, it will
     override
    :type node_types: list of :class:`NodeTypeDescription
     <azure.mgmt.servicefabric.models.NodeTypeDescription>`
    :param upgrade_description: The policy to use when upgrading the cluster.
    :type upgrade_description: :class:`ClusterUpgradePolicy
     <azure.mgmt.servicefabric.models.ClusterUpgradePolicy>`
    :param tags: Cluster update parameters
    :type tags: dict
    """

    _attribute_map = {
        'reliability_level': {'key': 'properties.reliabilityLevel', 'type': 'str'},
        'upgrade_mode': {'key': 'properties.upgradeMode', 'type': 'str'},
        'cluster_code_version': {'key': 'properties.clusterCodeVersion', 'type': 'str'},
        'certificate': {'key': 'properties.certificate', 'type': 'CertificateDescription'},
        'client_certificate_thumbprints': {'key': 'properties.clientCertificateThumbprints', 'type': '[ClientCertificateThumbprint]'},
        'client_certificate_common_names': {'key': 'properties.clientCertificateCommonNames', 'type': '[ClientCertificateCommonName]'},
        'fabric_settings': {'key': 'properties.fabricSettings', 'type': '[SettingsSectionDescription]'},
        'reverse_proxy_certificate': {'key': 'properties.reverseProxyCertificate', 'type': 'CertificateDescription'},
        'node_types': {'key': 'properties.nodeTypes', 'type': '[NodeTypeDescription]'},
        'upgrade_description': {'key': 'properties.upgradeDescription', 'type': 'ClusterUpgradePolicy'},
        'tags': {'key': 'tags', 'type': '{str}'},
    }

    def __init__(self, reliability_level=None, upgrade_mode=None, cluster_code_version=None, certificate=None, client_certificate_thumbprints=None, client_certificate_common_names=None, fabric_settings=None, reverse_proxy_certificate=None, node_types=None, upgrade_description=None, tags=None):
        self.reliability_level = reliability_level
        self.upgrade_mode = upgrade_mode
        self.cluster_code_version = cluster_code_version
        self.certificate = certificate
        self.client_certificate_thumbprints = client_certificate_thumbprints
        self.client_certificate_common_names = client_certificate_common_names
        self.fabric_settings = fabric_settings
        self.reverse_proxy_certificate = reverse_proxy_certificate
        self.node_types = node_types
        self.upgrade_description = upgrade_description
        self.tags = tags