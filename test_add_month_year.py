import pytest
import pandas as pd
from pandas.testing import assert_frame_equal 
import add_month_year


def test_add_month_year_process_file():
	test_data = add_month_year.process_file()
	expected_result = pd.read_csv('sampleoutput.csv')
	expected_result['Day'] = pd.to_datetime(expected_result['Day'])
	expected_result['Month_Year'] = expected_result['Day'].dt.to_period('M')

	assert_frame_equal(test_data,expected_result, check_dtype = False), 'The processor does not produce the expected result'
