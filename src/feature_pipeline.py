import pandas as pd

def preprocess_input(df):

    # 1. yes/no → 1/0
    binary_cols = [
        "mainroad", "guestroom", "basement",
        "hotwaterheating", "airconditioning", "prefarea"
    ]

    for col in binary_cols:
        df[col] = df[col].map({"yes": 1, "no": 0})

    # 2. One-hot encoding
    df = pd.get_dummies(df, columns=["furnishingstatus"], drop_first=True)

    # 3. Ensure ALL required columns exist (VERY IMPORTANT)
    required_cols = [
        'area', 'bedrooms', 'bathrooms', 'stories',
        'mainroad', 'guestroom', 'basement',
        'hotwaterheating', 'airconditioning',
        'parking', 'prefarea',
        'furnishingstatus_semi-furnished',
        'furnishingstatus_unfurnished'
    ]

    for col in required_cols:
        if col not in df.columns:
            df[col] = 0

    df = df[required_cols]

    return df