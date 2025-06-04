import logging
import os
from datetime import datetime

Log_F = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log" 

path_logf = os.path.join(os.getcwd(), 'log') 

os.makedirs(path_logf, exist_ok= True) 

path_log_file = os.path.join(path_logf, Log_F) 

logging.basicConfig(
    
    filename= path_log_file, 
    
    format= "[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s", 
  
    level = logging.INFO, 
    
)
