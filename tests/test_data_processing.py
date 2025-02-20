import pytest
from src.data_processing import load_data, clean_data, transform_data

def test_load_data():
    # Assuming load_data returns a DataFrame
    df = load_data('path/to/data.csv')
    assert df is not None
    assert not df.empty

def test_clean_data():
    # Assuming clean_data takes a DataFrame and returns a cleaned DataFrame
    df = load_data('path/to/data.csv')
    cleaned_df = clean_data(df)
    assert 'column_with_nan' not in cleaned_df.columns  # Example check for NaN removal

def test_transform_data():
    # Assuming transform_data takes a DataFrame and returns a transformed DataFrame
    df = load_data('path/to/data.csv')
    transformed_df = transform_data(df)
    assert 'transformed_column' in transformed_df.columns  # Example check for transformation