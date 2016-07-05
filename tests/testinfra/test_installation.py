"""
Role tests
"""
import pytest

pytestmark = pytest.mark.docker_images('infopen/ubuntu-trusty-ssh')


def test_packages(Package):
    """
    Tests about packages installed
    """

    packages = ['python-apt-common', 'python-apt', 'openjdk-7-jre']

    for package in packages:
        assert Package(package).is_installed is True
