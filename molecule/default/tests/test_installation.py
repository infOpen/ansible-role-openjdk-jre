"""
Role tests
"""

import os
import pytest

from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize('name,codenames', [
    ('python-apt-common', None),
    ('python-apt', None),
    ('openjdk-7-jre', ['jessie', 'trusty']),
    ('openjdk-9-jre', ['xenial']),
])
def test_repository_file(host, name, codenames):
    """
    Test packages installed
    """

    if host.system_info.distribution not in ['debian', 'ubuntu']:
        pytest.skip('{} ({}) distribution not managed'.format(
            host.system_info.distribution, host.system_info.release))

    if codenames and host.system_info.codename.lower() not in codenames:
        pytest.skip('{} package not used with {} ({})'.format(
            name, host.system_info.distribution, host.system_info.codename))

    assert host.package(name).is_installed
