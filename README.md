Install and configure nginx
===========================

This role will install and configure nginx and its sites. It supports SSL/TLS
termination and letsencrypt autorenewal directory.


Disclaimer
----------
Some ideas taken from: https://github.com/jdauphant/ansible-role-nginx

Requirements
------------

None

Examples
--------

Use it in a playbook as follows, assuming you already have docker setup:
```yaml
- hosts: all
  become: true
  roles:
    - users
  
```
Whenever needed, you can pass `nginx_dh_remove_old=true` to ansible-playbook 
execution to remove previous Diffie-Hellman parameters

Have a look at the [defaults/main.yml](defaults/main.yml) for role variables
that can be overridden.
