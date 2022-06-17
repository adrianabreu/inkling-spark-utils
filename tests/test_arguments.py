import pytest
from datetime import datetime
from inklings_spark_utils.arguments import process_etl_arguments

def test_process_etl_arguments_when_valid_date_are_supplied():
    args=["-start_date","2022-06-15","-end_date","2022-06-16"]
    parsed_args = process_etl_arguments(args)

    assert parsed_args.start_date == datetime(2022,6,15)
    assert parsed_args.end_date == datetime(2022,6,16)
    
def test_process_etl_arguments_when_invalid_date_are_supplied():
    args=["-start_date","2022-15-15","-end_date","06-06-2022"]
    with pytest.raises(ValueError):
        process_etl_arguments(args)
    