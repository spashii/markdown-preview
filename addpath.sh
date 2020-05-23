#!/bin/bash
path=pwd
export abc=$PATH:path/geckodriver
echo export PATH=$abc>>/home/$USER/.bashrc
# echo $path