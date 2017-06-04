![Logo](https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Nginx_logo.svg/2000px-Nginx_logo.svg.png)

Ansible Role: nginx
===================

[![Build Status](https://ci.devops.sosoftware.pl/buildStatus/icon?job=SoInteractive/nginx/master)](https://ci.devops.sosoftware.pl/job/SoInteractive/nginx/master) [![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT) [![Ansible Role](https://img.shields.io/ansible/role/18219.svg)](https://galaxy.ansible.com/SoInteractive/nginx/) [![Twitter URL](https://img.shields.io/twitter/follow/sointeractive.svg?style=social&label=Follow%20%40SoInteractive)](https://twitter.com/sointeractive)

This role will install and configure nginx and its sites. It supports SSL/TLS termination and letsencrypt autorenewal directory.

Disclaimer
----------
Ideas taken from https://github.com/jdauphant/ansible-role-nginx

Examples
--------

Use it in a playbook as follows:
```yaml
- hosts: all
  become: true
  roles:
    - SoInteractive.nginx
  
```

Whenever needed, you can pass `nginx_dh_remove_old=true` to ansible-playbook 
execution to remove previous Diffie-Hellman parameters

Have a look at the [defaults/main.yml](defaults/main.yml) for role variables
that can be overridden.

TODO
----

- CentOS 7 support
