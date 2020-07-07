# openjdk-jre

[![CI](https://github.com/infOpen/ansible-role-openjdk-jre/workflows/CI/badge.svg)](https://github.com/infOpen/ansible-role-openjdk-jre/actions)
[![Mergify Status][mergify-status]][mergify]
[![Updates](https://pyup.io/repos/github/infOpen/ansible-role-openjdk-jre/shield.svg)](https://pyup.io/repos/github/infOpen/ansible-role-openjdk-jre/)
[![Python 3](https://pyup.io/repos/github/infOpen/ansible-role-openjdk-jre/python-3-shield.svg)](https://pyup.io/repos/github/infOpen/ansible-role-openjdk-jre/)
[![Ansible Role](https://img.shields.io/ansible/role/10569.svg)](https://galaxy.ansible.com/infOpen/openjdk-jre/)

Install openjdk-jre package.

## Requirements

This role requires Ansible 2.8 or higher,
and platform requirements are listed in the metadata file.

## Testing

This role use [Molecule](https://github.com/ansible-community/molecule) to run tests.

Local and Github Actions tests run tests on Docker by default.
See molecule documentation to use other backend.

Currently, tests are done on:
- CentOS 7
- CentOS 8
- Debian Buster
- Debian Stretch
- Ubuntu Bionic
- Ubuntu Focal

and use:
- Ansible 2.8.x
- Ansible 2.9.x

### Running tests

#### Using Docker driver

```
$ tox
```

You can also configure molecule options and molecule command using environment variables:
* `MOLECULE_OPTIONS` Default: "--debug"
* `MOLECULE_COMMAND` Default: "test"

```
$ MOLECULE_OPTIONS='' MOLECULE_COMMAND=converge tox
```

## Role Variables

### Default role variables

``` yaml
# Defaults vars file for openjdk-jre role

# Specific Debian family settings
openjdk_jre_apt_update_cache: True
openjdk_jre_apt_cache_valid_time: 3600

# General settings
openjdk_jre_version: "{{ _openjdk_jre_version }}"
openjdk_jre_packages: "{{ _openjdk_jre_packages }}"
```

## Dependencies

None

## Example Playbook

``` yaml
- hosts: servers
  roles:
    - { role: infOpen.openjdk-jre }
```

## License

MIT

## Author Information

Alexandre Chaussier (for Infopen company)
- https://www.infopen.pro
- a.chaussier [at] infopen.pro

[mergify]: https://mergify.io
[mergify-status]: https://img.shields.io/endpoint.svg?url=https://gh.mergify.io/badges/infOpen/ansible-role-openjdk-jre&style=flat
