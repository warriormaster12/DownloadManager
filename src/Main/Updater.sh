#! /bin/bash 

check_updates='git pull'

cd 

if [ ! -d "DownloadManager" ]; then
  git clone https://github.com/warriormaster12/DownloadManager.git
else
  cd DownloadManager && echo check_updates
fi 

