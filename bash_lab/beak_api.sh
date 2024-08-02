#!/bin/bash

var=0
while true;
do
	$((var++))
	curl -s "http://getalien.tech/api/v1/users" 1>/dev/null
	if [[ $($var % 100) -eq 0 ]]
	then
		printf ".";
	fi
	if [[ $var -eq 10000 ]]
	then
		exit;
	fi
done
