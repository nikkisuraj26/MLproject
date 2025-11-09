# for exception handling and sh
import sys # sys module has info about the exception that occurred
from src.logger import logging
def error_message_detail(error, error_detail:sys):
    filename= exc_tb.tb_frame.f_code.co_filename
    _,_,exc_tb = error_detail.exc_info() # exc_info() returns a tuple of 3 values, not interested in first two info only in tb
    error_message="Error occurred in python script name [{0}] line number [{1}] error message [{2}]".format(
        filename, exc_tb.tb_lineno,str(error))
    return error_message

class CustomException(Exception):
    def __init__(self,error_message, error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_detail)
    def __str__(self):
        return self.error_messageHyH