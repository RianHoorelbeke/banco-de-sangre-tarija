import pandas as pd
import google
from write_data import add_document_with_id


def convert_xlsx_to_csv(file_name: str):
    """
    Import local .xlsx file and output to .csv

    :param file_name: str
        Name of local .xlsx
    """

    read_file = pd.read_excel(file_name)
    file_name = file_name.replace(".xlsx", ".csv")
    read_file.to_csv(file_name, index=None, header=True)

def _import_csv_to_df (file_name: str):
    """
    Import local csv and convert to dataframe

    :param file_name: str
        Name of local .csv file

    :return: DataFrame object with records of csv
    """

    return pd.read_csv(file_name, keep_default_na=False)


def _convert_df_to_dict (df: pd.DataFrame):
    """
    Import local csv and convert to dataframe

    :param df: pd.DataFrame
        Dataframe to convert to dictionary

    :return: Dictionary object with records of DataFrame
    """

    return df.to_dict(orient='records')


def import_csv_to_collection(file_name: str, coll_ref: google.cloud.firestore_v1.collection.CollectionReference):
    """
    Import local csv to firebase

    :param file_name: str
        Name of local csv file with .csv

    :param coll_ref: google.cloud.firestore_v1.collection.CollectionReference
        Reference to collection where documents will be added

    """

    df = _import_csv_to_df(file_name)
    df['apto para donar'] = df['apto para donar'].apply(
        lambda x: 1 if x == 'Si' else 0)
    df['apto para donar'] = df['apto para donar'].astype('bool')

    df['fecha de nacimiento'] = pd.to_datetime(df['fecha de nacimiento'])
    df['fecha de nacimiento'] = df['fecha de nacimiento'].apply(lambda x: x.date())

    df['fecha de registro'] = pd.to_datetime(df['fecha de registro'])
    df['fecha de registro'] = df['fecha de registro'].apply(lambda x: x.date())

    df['ultima donacion'] = pd.to_datetime(df['ultima donacion'])
    df['ultima donacion'] = df['ultima donacion'].apply(lambda x: x.date())

    df['voluntario'] = True
    df['rechazado'] = False

    df = df.drop('ultima donacion', axis=1)
    df = df.drop('rechazo', axis=1)

    df = df.astype({"nombre": "string", "apellidos": "string", "sexo": "string", "grupo sanguineo": "string",
                    "tipo de donante": "string", "correo electronico": "string",
                    "direccion": "string", "ciudad": "string", "departamento": "string", "fecha de nacimiento": "datetime64[ns]", "fecha de registro": "datetime64[ns]"})

    print(df.dtypes)

    list_dict = _convert_df_to_dict(df)
    i=1
    for field_values in list_dict:
        add_document_with_id(coll_ref, str(i), field_values)
        i = i + 1



