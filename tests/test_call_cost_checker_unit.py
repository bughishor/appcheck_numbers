from call_cost_checker import call_cost_checker
from tests_data import *


def test_file_path_requirements():
    assert call_cost_checker.check_file_path_given(TEST_FILE_BROKEN_MIN) is False
    assert call_cost_checker.check_file_path_given(TEST_FILE_OK) is True


def test_file_path_broken():
    assert call_cost_checker.open_call_log_file(TEST_FILE_BROKEN_PATH) is False


def test_strip_phone_number():
    assert call_cost_checker.strip_non_numeric(TEST_PHONE_NUMBER_WRONG_INPUT) == TEST_PHONE_NUMBER_CORRECT_INPUT


def test_call_is_cheap():
    assert call_cost_checker.call_is_at_night(TEST_CALL_TIME_CHEAP) is True


def test_call_is_normal_price():
    assert call_cost_checker.call_is_at_night(TEST_CALL_TIME_NORMAL) is False

