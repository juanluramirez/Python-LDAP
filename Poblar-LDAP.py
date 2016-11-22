#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ldap
from ldap import modlist
import getpass
from json import loads

# Values #
conection = "ldap://172.22.200.151:389/"
file_name = 'clase.json'
dom = 'dc=barney,dc=jlramirez,dc=gonzalonazareno,dc=org'
uidNumberInitial = 2000
gidNumber = 2000


user = 'admin'
passwd = getpass.getpass('Contraseña del usuario %s LDAP: ' % user)

# Carga fichero JSON
f = open(file_name,'r')
content = f.read()
f.close()
json_humans = loads(content)

# Poblar LDAP
try:
	bind = "cn=%s,%s" % (user, dom)
	l = ldap.initialize(conection)
	l.simple_bind_s(bind,passwd)

	for i in json_humans['personas']:
		nombre = i['nombre'].encode('utf8')
		apellidos = i['apellidos'].encode('utf8')
		uid = str(i['usuario'])
		attrs = {}
		dn = "cn=%s,%s" % (uid, dom)
		attrs['objectClass'] = ['top', 'posixAccount', 'inetOrgPerson', 'ldapPublicKey']
		attrs['uid'] = uid
		attrs['cn'] = nombre
		attrs['sn'] = apellidos
		attrs['mail'] = str(i['correo'])
		attrs['uidNumber'] = str(uidNumberInitial)
		attrs['gidNumber'] = str(gidNumber)
		attrs['homeDirectory'] = '/home/%s' % uid
		attrs['loginShell'] = '/bin/bash'
		attrs['sshPublicKey'] = str(i['clave'])
		ldif = modlist.addModlist(attrs)
		l.add_s(dn,ldif)
		uidNumberInitial += 1
		print 'Usuario %s insertado.' % uid 

	l.unbind_s()
