import google
import csv
import sys
from firebase_utils import get_reference_collection


def csv_writer(file, fields):
    """Generate CSV writer"""
    return csv.DictWriter(file, fields)


def export_to_csv(db: google.cloud.firestore_v1.client.Client, id_coll: str):
    """
    Export data from table to local .csv

    :param db: google.cloud.firestore_v1.client.Client
        cLient to communicate with server
    :param id_coll: str
        Name of collection to be exported
    :param local_file_name: str
        Name of local file name
    """

    coll_ref = get_reference_collection(db, id_coll)
    docs = coll_ref.stream()
    #for doc in docs:




