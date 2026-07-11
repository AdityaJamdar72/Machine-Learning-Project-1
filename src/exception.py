import sys

def error_message_detail(error, error_details: sys):
    #error ---------> tells current exception 

    _, _, exc_tb = error_details.exc_info() #return information about current exception and it can be sys.error_details

    file_name = exc_tb.tb_frame.f_code.co_filename

    error_message = (
        "The error occurred in python script [{0}] "
        "line number [{1}] "
        "error message [{2}]"
    ).format(
        file_name,
        exc_tb.tb_lineno,
        str(error)
    )

    return error_message


class CustomException(Exception):
    def __init__(self, error, error_details: sys):
        super().__init__(error)
        self.error_message = error_message_detail(error, error_details)

    def __str__(self):
        return self.error_message
    



    # it is just understanding the code who try to read what we acutually implemented 
    '''
    when error occur suppose 10/o is exception occur the python return lots of values 
    for exc_info() return (type,value,traceback ) the first two value ignored by using _,_
    and exc_tb stores traceback of exception 
     '''