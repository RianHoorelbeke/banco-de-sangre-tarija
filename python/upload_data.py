import pandas as pd
import google
import datetime
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

    return pd.read_csv(file_name)


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
    df = df.astype({"id": "int64", "nombre" : "str", "apellidos": "str", "sexo": "str", "grupo sanguineo" : "str", "tipo de donante": "str", "fecha de nacimiento": "str","peso": "int", "altura": "int", "nr. de donaciones": "int", "ultima donacion": "str","rechazo": "str", "apto para donar": "str", "correo electronico": "str", "nr. de telefono": "int64", "nr. de carnet": "int64", "direccion": "str", "ciudad": "str", "departamento": "str", "fecha de registro": "str"})
    list_dict = _convert_df_to_dict(df)
    i=1
    for field_values in list_dict:
        add_document_with_id(coll_ref, "donante" + str(i), field_values)
        i = i + 1



