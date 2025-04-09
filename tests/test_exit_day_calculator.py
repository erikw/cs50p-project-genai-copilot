import pytest
from datetime import datetime, timedelta
from visa_tool.exit_day_calculator import calculate_exit_day

def test_calculate_exit_day_valid():
    entry_date = datetime(2023, 1, 1)
    valid_days = 30
    expected_exit_date = entry_date + timedelta(days=valid_days)
    assert calculate_exit_day(entry_date, valid_days) == expected_exit_date

def test_calculate_exit_day_zero_days():
    entry_date = datetime(2023, 1, 1)
    valid_days = 0
    expected_exit_date = entry_date
    assert calculate_exit_day(entry_date, valid_days) == expected_exit_date

def test_calculate_exit_day_negative_days():
    entry_date = datetime(2023, 1, 1)
    valid_days = -5
    expected_exit_date = entry_date + timedelta(days=valid_days)
    assert calculate_exit_day(entry_date, valid_days) == expected_exit_date

def test_calculate_exit_day_edge_case():
    entry_date = datetime(2023, 12, 31)
    valid_days = 1
    expected_exit_date = datetime(2024, 1, 1)
    assert calculate_exit_day(entry_date, valid_days) == expected_exit_date