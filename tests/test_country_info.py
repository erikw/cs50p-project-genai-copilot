import pytest
from visa_tool.country_info import CountryInfo

def test_get_visa_info_valid_country():
    country_info = CountryInfo()
    result = country_info.get_visa_info("Canada")
    assert result is not None
    assert "visa requirements" in result

def test_get_visa_info_invalid_country():
    country_info = CountryInfo()
    result = country_info.get_visa_info("InvalidCountry")
    assert result is None

def test_get_visa_info_case_insensitivity():
    country_info = CountryInfo()
    result = country_info.get_visa_info("canada")
    assert result is not None
    assert "visa requirements" in result

def test_get_visa_info_empty_country_name():
    country_info = CountryInfo()
    result = country_info.get_visa_info("")
    assert result is None