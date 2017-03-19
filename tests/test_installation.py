"""
Role tests
"""

from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner('.molecule/ansible_inventory').get_hosts('all')


def test_repository_file(Package, SystemInfo):
    """
    Test community repository file permissions
    """

    jre_package_name = ''

    if SystemInfo.distribution in ['debian', 'ubuntu']:
        if SystemInfo.release == '16.04':
            jre_package_name = 'openjdk-9-jre'
        else:
            jre_package_name = 'openjdk-7-jre'

    packages = ['python-apt-common', 'python-apt', jre_package_name]

    for package in packages:
        assert Package(package).is_installed is True
