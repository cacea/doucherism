#!/bin/bash

echo 'After script'

file="/etc/apt/sources.list.d/heroku.list"
if [ -f "$file" ]
then
	echo "$file found. There is no need to install this, but we will update Heroku Toolbelt"
	apt-get update
	apt-get install -y heroku-toolbelt
else
	echo "$file not found. We will begin the installation of Heroku Toolbelt now"
	wget -qO- https://toolbelt.heroku.com/install-ubuntu.sh | sh
fi
