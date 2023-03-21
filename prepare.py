import pandas as pd
from sklearn.model_selection import train_test_split

def clean_telco(df):
    '''Prepares acquired teclo data for exploration'''
    df.columns = df.columns.str.lower()
    df.drop_duplicates(inplace=True)
    df.dropna(inplace=True)
    df = df[df.total_charges!=' ']
    df.total_charges = pd.to_numeric(df['total_charges'], errors='coerce')
    df['churn_encoded'] = df.churn.map({'Yes': 1, 'No': 0})
    df.drop(columns=['customer_id','payment_type_id', 'internet_service_type_id','contract_type_id', 'churn'], inplace=True)
    df['payment_type'] = df['payment_type'].str.replace(' (automatic)', '', regex=False)

    
    return df

def dem_dummies(df):
    # Get all categorical columns
    categorical_cols = df.select_dtypes(include=['object']).columns.tolist()

    # Create dummy variables for each categorical column
    for col in categorical_cols:
        dummies = pd.get_dummies(df[col], prefix=col, drop_first=True)
        df = pd.concat([df, dummies], axis=1)
        df.drop(col, axis=1, inplace=True)

    return df


def generate_data_dictionary(data):
    # Get variable names and data types
    var_names = data.columns.tolist()
    var_types = data.dtypes.tolist()

    # Get variable descriptions
    var_desc = []
    for col in var_names:
        var_desc.append(input("Enter description for " + col + ": "))

    # Create the data dictionary as a dataframe
    data_dict = pd.DataFrame({'Column Name': var_names, 'Data Type': var_types, 'Column Description': var_desc})

    return data_dict


def train_validate_test_split(df, target):
    '''
    Takes in a data frame and the target variable column  and returns
    train (65%), validate (20%), and test (15%) data frames.
    '''
    train, test = train_test_split(df,test_size = 0.15, stratify = df[target], random_state=27)
    train, validate = train_test_split(train, test_size = 0.235, stratify = train[target],random_state=27)
    
    return train, validate, test
