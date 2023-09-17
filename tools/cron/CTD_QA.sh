#!/usr/bin/bash

echo "Activando entorno virtual"
source /home/app_proc_qa/PruebasServerproductivoPython/CTD/.env/bin/activate

echo "Dirijiendo a directorio /home/app_proc_qa/PruebasServerproductivoPython/CTD"
cd /home/app_proc_qa/PruebasServerproductivoPython/CTD

echo "Iniciando script CTD Cuprum"
python main.py

echo "Desactivando entorno virtual"
deactivate
