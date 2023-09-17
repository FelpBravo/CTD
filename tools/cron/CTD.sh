#!/usr/bin/bash

echo "Activando entorno virtual"
source /previred/CTD/.env/bin/activate

echo "Dirijiendo a directorio /previred/CTD"
cd /previred/CTD

echo "Iniciando script CTD Cuprum"
python3 main.py

echo "Desactivando entorno virtual"
deactivate
