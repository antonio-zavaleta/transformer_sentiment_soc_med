def load_data(file_path):
    import pandas as pd
    return pd.read_csv(file_path)

def clean_data(df):
    df = df.dropna()  # Remove missing values
    df = df.reset_index(drop=True)  # Reset index after dropping
    return df

def transform_data(df):
    # Example transformation: Convert categorical variables to dummy/indicator variables
    return pd.get_dummies(df, drop_first=True)

def save_data(df, file_path):
    df.to_csv(file_path, index=False)