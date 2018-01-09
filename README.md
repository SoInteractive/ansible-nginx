<a href="https://www.nginx.com/">
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Nginx_logo.svg/2000px-Nginx_logo.svg.png" alt="nginx logo" title="nginx" align="right" height="60" />
</a>

Ansible Role: nginx
===================

[![Build Status](https://travis-ci.org/SoInteractive/ansible-nginx.svg?branch=master)](https://travis-ci.org/SoInteractive/ansible-nginx) [![License: MIT](https://img.shields.io/badge/license-MIT%20License-brightgreen.svg)](https://opensource.org/licenses/MIT) [![Ansible Role](https://img.shields.io/badge/ansible%20role-SoInteractive.nginx-blue.svg)](https://galaxy.ansible.com/SoInteractive/nginx/)  [![GitHub tag](https://img.shields.io/github/tag/sointeractive/ansible-nginx.svg)](https://github.com/SoInteractive/ansible-nginx/tags) [![Twitter URL](https://img.shields.io/twitter/follow/sointeractive.svg?style=social&label=Follow%20%40SoInteractive)](https://twitter.com/sointeractive)

This role will install and configure nginx and its sites. It supports SSL/TLS termination and letsencrypt autorenewal directory.

Disclaimer
----------

Ideas taken from https://github.com/jdauphant/ansible-role-nginx

Requirements
------------

When using metrics exporter, golang should be installed on deployer host. Also systemd is currently needed.

Let's encrypt
-------------

This role can automatically generate letencrypt certificates. To do this you need an email previously used for some let's encrypt certificate and set some variables:
- `nginx_letsencrypt_email`
- use `server_name` directive in `nginx_sites` for sites which need certificate.

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
