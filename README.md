# openjdk-jre

[![Build Status](https://travis-ci.org/infOpen/ansible-role-openjdk-jre.svg?branch=master)](https://travis-ci.org/infOpen/ansible-role-openjdk-jre)

Install openjdk-jre package.

## Requirements

This role requires Ansible 1.4 or higher, and platform requirements are listed
in the metadata file.

## Testing

This role use [Molecule](https://github.com/metacloud/molecule/) to run tests.

Locally, you can run tests on Docker (default driver) or Vagrant.
Travis run tests using Docker driver only.

Currently, tests are done on:
- Debian Jessie
- Ubuntu Trusty
- Ubuntu Xenial
and use:
- Ansible 2.0.x
- Ansible 2.1.x
- Ansible 2.2.x

### Running tests

#### Using Docker driver

```
$ tox
```

#### Using Vagrant driver

```
$ MOLECULE_DRIVER=vagrant tox
```

## Role Variables

Follow the possible variables with their default values

```
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

```
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
