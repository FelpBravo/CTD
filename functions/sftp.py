import pysftp
from config.log import logger
import config.config as constant
import traceback

cnopts= pysftp.CnOpts()
cnopts.hostkeys= None 

def connect(rutaLocal, rutaRemota) :
    logger(f'SFTP Depositando archivos en casilla "{constant.host}"')
    
    estado = True
    
    try:
        with pysftp.Connection(host=constant.host, username=constant.username, password=constant.password, port=constant.port, cnopts=cnopts) as sftp:
            sftp.put(rutaLocal, rutaRemota)
            sftp.close()
    
    except Exception as e:
        logger("EXCEPTION_SFTP: " + str(e) + str(traceback.format_exc(limit=1)))
        estado = False
        
    finally:
        return estado
    
        
        
