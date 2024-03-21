# defining the exceptions class

#sys is the system for us to interact with the system
import sys

# making a parent class

class customexception(Exception):

    def __init__(self,error_message,error_details:sys):
        self.error_message=error_message
        _,_,exc_tb=error_details.exc_info() #to collect execution details 
        self.lineno=exc_tb.tb_lineno
        self.file_name=exc_tb.tb_frame.f_code.co_filename

    def __str__(self):
        return "Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
    {self.file_name,self.lineno,str(self.error_message)})


#executing this module in standalone
    
if __name__== '__main__':
    try:
        pass
    except Exception as e:
        raise customexception(e,sys)
