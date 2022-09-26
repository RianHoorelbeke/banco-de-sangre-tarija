from firebase_admin import firestore, credentials, initialize_app
import google


def connect_firebase():
    """
    Connect with firebase donantes-bancodesangre-tarija

    :return: google.cloud.firestore_v1.client.Client object for database
    """

    cred = credentials.Certificate("donantes-bancodesangre-tarija-firebase-adminsdk-f0rlm-c85336ad82.json")

    initialize_app(cred,{'databaseURL': 'https://banco-de-sangre-tarija.firebaseio.com/'})
    db = firestore.client()
    return db


def get_reference_collection(db: google.cloud.firestore_v1.client.Client, id_coll: str):
    """
    Get reference to collection using its ID

    :param db: google.cloud.firestore_v1.client.Client
        cLient to comunicate with server
    :param id_coll: str
        id of collection

    :return: google.cloud.firestore_v1.collection.CollectionReference object to collection
    """

    coll_ref = db.collection(id_coll)
    return coll_ref


def get_reference_document(db: google.cloud.firestore_v1.client.Client, id_coll: str, id_doc: str):

    """
    Get reference to document using ID of collection and document

    :param id_coll: str
        id of collection
    :param id_doc: str
        id of document
    :param db: google.cloud.firestore_v1.client.Client
        cLient to comunicate with server


    :return: google.cloud.firestore_v1.document.DocumentReference object to document
    """

    doc_ref = db.collection(id_coll).document(id_doc)
    return doc_ref


def print_collection(coll_ref: google.cloud.firestore_v1.collection.CollectionReference):
    """
    Print all documents of a collection

    :param coll_ref: google.cloud.firestore_v1.collection.CollectionReference
        Reference to collection of documents that will be printed
    """

    docs = coll_ref.stream()
    for doc in docs:
        print(f'{doc.id} ==> {doc.to_dict()}')
