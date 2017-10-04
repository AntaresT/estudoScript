#!/bin/bash
if ["$1" == ""]
then
echo "Usage: 'nmapScan.sh' [xxx.xxx.xxx.xxx/xx]"
else
nmap -F -O -oG scanOs.txt $1 | grep "Running: " > /home/antares/Documentos/Estudos/Scripts/scanOs.txt; echo "$(cat /home/antares/Documentos/Estudos/Scripts/scanOs.txt | grep Linux | wc -l):Linux"; echo "$(cat /home/antares/Documentos/Estudos/Scripts/scanOs.txt | grep Windows | wc -l):Windows"
fi 

