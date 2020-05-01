#!/bin/sh

ssh-keygen -t rsa -b 4096 -C "akamlani@gmail.com"
eval "$(ssh-agent -s)"
ssh-add -K ~/.ssh/id_rsa
pbcopy < ~/.ssh/id_rsa.pub
