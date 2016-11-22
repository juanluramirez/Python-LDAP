#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf8')

import os
import getpass
import json

password = getpass.getpass("Contraseña del usuario admin LDAP:  ")

# Lectura del fichero JSON
fichero_json = open("clase.json")
alumnos = json.load(fichero_json)


for i in alumnos["personas"]:
	del_usuarios = 'ldapdelete -x -D "cn=admin,dc=barney,dc=jlramirez,dc=gonzalonazareno,dc=org" -h localhost -p 389 -w %s "uid=%s,ou=People,dc=barney,dc=jlramirez,dc=gonzalonazareno,dc=org"' % (password,str(i["usuario"]))
	os.system(rm_usuarios)

for i in alumnos["computers"]:
	del_ordenadores = 'ldapdelete -x -D "cn=admin,dc=barney,dc=jlramirez,dc=gonzalonazareno,dc=org" -h localhost -p 389 -w %s "uid=%s,ou=computers,dc=barney,dc=jlramirez,dc=gonzalonazareno,dc=org"' % (password,str(i["ipv4"]))
	os.system(rm_ordenadores)

print "Usuarios eliminados correctamente"
print "Ordenadores eliminados correctamente"
