from datetime import datetime

def validate_input(input, input_format):
    if input:
        try:
            res = bool(datetime.strptime(input, input_format))
            return res
        except ValueError:
            return False
    else:
        return True