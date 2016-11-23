#!/bin/bash
ldapsearch -x -h localhost -b dc=barney,dc=jlramirez,dc=gonzalonazareno,dc=org "(&(objectClass=posixAccount)(uid=$1))" sshPublicKey | sed -n '/^ /{H;d};/sshPublicKey:/x;$g;s/\n *//g;s/sshPublicKey: //gp'
