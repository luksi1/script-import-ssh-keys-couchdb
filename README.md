# script-import-ssh-keys-couchdb
Import SSH keys from authorized_keys (or a file with the same syntax) into CouchDB as key/value pairs. Value is an object with type,comment and key.

## Description
This is a simple Python script to import SSH keys into CouchDB. This script was intended for use with Puppet and Hiera + CouchDB. This script streamlines the process of importing SSH keys from, for instance, emails. 

## Use case
This was created for use with the "http" backend for Hiera, using CouchDB.

You can find the Hiera backend here: https://github.com/crayfishx/hiera-http

## Author
Luke Simmons
