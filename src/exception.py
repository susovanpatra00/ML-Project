import sys
from src.logger import logging

def error_message_detail(error, error_detail:sys):
    _,_,exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    error_message = "Error occured in python name [{0}]  line number [{1}] error message [{2}]".format(
        file_name, line_number, str(error)
    )
    return error_message


class CustomException(Exception):
    def __int__(self, error_message, error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail = error_detail)

    def __str__(self):
        return self.error_message
    

if __name__ == "__main__":
    try:
        a = 1/0
    except Exception as e:
        logging.info("Divide by Zero error")
        raise CustomException(e, sys)



# The sys module in Python is a part of the standard library that provides access to some variables used or 
# maintained by the Python interpreter and functions that interact strongly with the interpreter. It is used to 
# manipulate Python runtime environment.
    

# sys.exc_info() is a function in the sys module of Python, which returns a tuple of three values that give 
# information about the exception that is currently being handled. This function is useful primarily in 
# exception handling blocks. The information it provides is especially helpful for logging and for creating 
# custom error messages.
# The tuple returned by sys.exc_info() contains the following three values: 
#   1. Exception Type       2. Exception Value      3. Traceback Object