# Proyecto CTD (Cuprum Traspasados Diarios)

El proyecto CTD (Cuprum Traspasados Diarios) es un proceso automatizado que se ejecuta en el sistema operativo Linux a través de un cronjob. Su principal objetivo es procesar archivos de traspasos diarios, realizar validaciones, consultas SQL, limpieza de datos, y generar informes. Este proceso incluye la transferencia de archivos a través de SFTP y el envío de correos electrónicos con informes a instituciones específicas.

## Ejecución Programada

El proyecto se ejecuta en función de un cronjob en Linux. Este cronjob se configura para que el proceso se ejecute en días hábiles específicos, asegurándose de que las operaciones se realicen en los momentos adecuados. La programación también considera un período de tiempo predefinido para el procesamiento de datos.

## Proceso Detallado

El proceso se divide en varias etapas clave:

1. **Inserción de Bitácora**: Al inicio del proceso, se registra una entrada en la bitácora para rastrear la ejecución y los posibles errores.

2. **Procesamiento de Datos**: Se realizan consultas SQL en la base de datos utilizando un procedimiento almacenado específico. Los datos resultantes se almacenan en un DataFrame para su posterior procesamiento.

3. **Generación de Archivo de Salida**: Los datos procesados se exportan a un archivo CSV local en la ubicación especificada.

4. **Compresión de Archivo**: El archivo CSV se comprime en formato ZIP para facilitar la transferencia y el almacenamiento.

5. **Transferencia a SFTP**: El archivo comprimido se transfiere a través de SFTP a una ubicación remota.

6. **Envío de Correo Electrónico**: Se envía un correo electrónico que contiene un informe del proceso a la institución correspondiente.

## 
Nota Importante: Los archivos sensibles no han sido subidos al repositorio o han sido ocultados por razones de seguridad.

Estos archivos contienen información confidencial, como contraseñas o claves de acceso, y no deben estar disponibles públicamente en un repositorio de código abierto.
