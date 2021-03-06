#!/usr/bin/python3

import json
import argparse
import re
import couchdb

""" This is a simple script to add a ssh_authorized key file to a REST API.

This script was created for use with Puppet. We use a REST API backend (CouchDB) for Hiera and this is used to streamline emails with SSH keys into CouchDB.

Example:
	parse.ssh.keys.py --file <insert file name>
"""

# Static variables
url='http://domain.com:5984/'
database="my_database"
document="my_document"
couch = couchdb.Server(url)
db = couch[database]
doc = db[document]

parser = argparse.ArgumentParser(description='This is a simple script to add a ssh_authorized key file to a REST API')
parser.add_argument('-f','--file', help='The file to be parsed. This file can contain multiple SSH keys.', required=True)
args = parser.parse_args();
file = args.file
type = re.compile(r"(\w+-\w+) (\S+) (\S+)")

with open(file) as f:
	for row in f:
		if row.strip() == '':
			continue
		result = type.match(row)
		ssh_key_type = result.group(1)
		ssh_key_comment = result.group(3)
		ssh_key = result.group(2)

		ssh_key_name = input("Please enter a title for " + ssh_key_comment + ": [" + ssh_key_comment + "] ")
		if ssh_key_name == "":
			ssh_key_name = ssh_key_comment
		ssh_key_user = input("Which user should this be applied to? [root] ")
		if ssh_key_user == "":
			ssh_key_user = "root"

		doc = db[document]
		doc["ssh_key_" + ssh_key_name] = {
			ssh_key_name: {
				'ensure':  'present', 
				'type': ssh_key_type,
				'name': ssh_key_name,
				'key': ssh_key,
				'user': ssh_key_user 
			}
		}

		db.save(doc)
		print(doc["ssh_key_" + ssh_key_name])
