#!/bin/bash

echo Command Executes is ifconfig.
ifconfig
if [$? -eq 0]
then
   echo "exit code is 0 so sucess"
else
   echo exit code was $? so not sucess
fi
echo Command Executes is ifconfig.
ifconfig
if [$? -eq 0]
then
   echo "exit code is 0 so sucess"
else
   echo exit code was $? so not sucess
fi