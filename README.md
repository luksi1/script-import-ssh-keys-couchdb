# script-import-ssh-keys-couchdb
Import SSH keys from authorized_keys (or a file with the same syntax) into CouchDB as key/value pairs. Value is an object with type,comment and key.

## Description
This is a simple Python script to import SSH keys into CouchDB. This script was intended for use with Puppet and Hiera + CouchDB. This script streamlines the process of importing SSH keys from, for instance, emails. 

## Use case
This was created for use with the "http" backend for Hiera.

You can find the Hiera backend here: https://github.com/crayfishx/hiera-http

## Configuration
Change the variable "url", "database" and "document" to match your environment.

## Dependencies
 - python 3
 - argparse
 - re
 - couchdb

## Options
 - file TheNameOfYourFileToImport (required)

## Examples
parse.ssh.keys.py --file MyFile

## Notes
 - This script has only been run with Python 3 on Ubuntu 14.04.

## Author
Luke Simmons
