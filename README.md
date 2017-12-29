# openjdk-jre

[![Build Status](https://img.shields.io/travis/infOpen/ansible-role-openjdk-jre/master.svg?label=travis_master)](https://travis-ci.org/infOpen/ansible-role-openjdk-jre)
[![Build Status](https://img.shields.io/travis/infOpen/ansible-role-openjdk-jre/develop.svg?label=travis_develop)](https://travis-ci.org/infOpen/ansible-role-openjdk-jre)
[![Updates](https://pyup.io/repos/github/infOpen/ansible-role-openjdk-jre/shield.svg)](https://pyup.io/repos/github/infOpen/ansible-role-openjdk-jre/)
[![Python 3](https://pyup.io/repos/github/infOpen/ansible-role-openjdk-jre/python-3-shield.svg)](https://pyup.io/repos/github/infOpen/ansible-role-openjdk-jre/)
[![Ansible Role](https://img.shields.io/ansible/role/10569.svg)](https://galaxy.ansible.com/infOpen/openjdk-jre/)

Install openjdk-jre package.

## Requirements

This role requires Ansible 2.2 or higher,
and platform requirements are listed in the metadata file.

## Testing

This role use [Molecule](https://github.com/metacloud/molecule/) to run tests.

Local and Travis tests run tests on Docker by default.
See molecule documentation to use other backend.

Currently, tests are done on:
- Debian Jessie
- Ubuntu Trusty
- Ubuntu Xenial

and use:
- Ansible 2.2.x
- Ansible 2.3.x
- Ansible 2.4.x

### Running tests

#### Using Docker driver

```
$ tox
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
- http://www.infopen.pro
- a.chaussier [at] infopen.pro
