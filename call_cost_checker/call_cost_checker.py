import csv
import re
import dateutil.parser


def check_file_path_given(file_path):
    """
    Checking input file path for length to determine if it was provided or not
    We're assuming a minimum length of 5 chars for provided path (x.csv)
    """

    if len(file_path) > 4:
        return True
    else:
        return False


def strip_non_numeric(text_input):
    """
    To avoid any CSV reading errors, we're stripping expected numeric inputs from all non-necessary characters
    :param text_input: phone number
    :return: stripped phone number
    """
    return re.sub('[^0-9]', '', text_input)


def call_is_international(string_input):
    """
    Decide whether call is international or not
    :param string_input: the phone number
    :return: True/False
    """

    is_international = False

    if string_input[0] == '+' and string_input[1:3] != '44':
        is_international = True

    if string_input[0:2] == '00' and string_input[2:4] != '44':
        is_international = True

    return is_international


def simplify_number(string_input):
    """
    Remove leading +44 or 0044 from UK numbers
    :param string_input: the phone number
    :return: simplified phone number
    """

    if string_input[0:3] == '+44':
        return string_input.replace('+44', '0')

    if string_input[0:4] == '0044':
        return string_input.replace('0044', '0')

    return string_input


def call_is_landline(string_input):
    """
    Decide if the call is landline
    :param string_input: the phone number
    :return: True/False
    """

    if string_input[0:2] in ['01', '02']:
        return True

    return False


def call_is_mobile(string_input):
    """
    Decide if a call is to a mobile number
    :param string_input: the phone number
    :return: True/False
    """

    if string_input[0:2] == '07':
        if string_input[2] == 6 and string_input[0:5] != '07624':
            return False
        return True

    return False


def call_is_toll_free(string_input):
    """
    Decide if the call was made to a toll free number
    :param string_input: the phone number
    :return: True/False
    """

    if string_input[0:3] == '080':
        return True

    return False


def call_is_at_night(string_input):
    """
    Transforming dates from ISO to readable format in python and decide if call is cheaper
    :param string_input: Call start time
    :return: True/False
    """
    call_time = dateutil.parser.parse(string_input).hour

    if 21 > call_time > 7:
        return False
    else:
        return True


def open_call_log_file(file_path):
    """
    Trying to open the file located at provided path
    :param file_path: file path
    :return: False if file is not present or dict containing input if present
    """
    try:
        with open(file_path, mode='r') as call_log:
            reader = csv.reader(call_log)

            for row in reader:
                phone_number = strip_non_numeric(row[0])
                is_international = call_is_international(phone_number)

                if not is_international:
                    phone_number = simplify_number(phone_number)

                    is_landline = call_is_landline(phone_number)
                    is_mobile = call_is_mobile(phone_number)
                    is_toll_free = call_is_toll_free(phone_number)

                is_at_night = call_is_at_night(row[1])

    except FileNotFoundError:
        return False


def find_most_expensive_number(call_log_file_path):
    if check_file_path_given(call_log_file_path) is False:
        return "File path not provided"

    if open_call_log_file(call_log_file_path) is False:
        return None

    json_result = True

    return json_result


find_most_expensive_number('../call_log_example.csv')
