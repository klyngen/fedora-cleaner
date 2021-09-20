#!/usr/bin/bash

INSTALL_LOCATION='/usr/bin/fedora-cleaner'

if [[$1 == 'uninstall']]
then
  echo "Removing $FILE_LOCATION"
  sudo rm $INSTALL_LOCATION
else
  echo "installing script to $INSTALL_LOCATION \n Run ./install.sh uninstall to remove script"
  chmod +x cleaner.py
  sudo cp cleaner.py $INSTALL_LOCATION
fi




