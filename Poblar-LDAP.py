#!/usr/bin/env python
# -*- coding: utf-8 -*-


import ldap
from ldap import modlist
import getpass
from json import loads

# Values #
#user = 'admin'
conection = "ldap://localhost:389/"
dom = 'dc=example,dc=org'
uidNumberInitial = 2000
gidNumber = 2000
# Values #

user = raw_input('Introduce el usuario LDAP: ')
passwd = getpass.getpass('Contraseña del usuario %s LDAP: ' % user)

# JSON
f = open(clase.json,'r')
content = f.read()
f.close()
json_humans = loads(content)
list_humans = json_humans[alumnos]

