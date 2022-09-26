import google


def add_document(coll_ref: google.cloud.firestore_v1.collection.CollectionReference, field_values: dict):
    """
    add new document to collection with random document ID

    :param coll_ref: google.cloud.firestore_v1.collection.CollectionReference
        reference to collection where new document should be added
    :param field_values: dict
        ej. field_values = {"nombre": "Rian", edad: 29}
    """

    coll_ref.add(field_values)


def add_document_with_id(coll_ref: google.cloud.firestore_v1.collection.CollectionReference, id_doc: str, field_values: dict):
    """
    add new document to collection with specific document ID

    :param coll_ref: google.cloud.firestore_v1.collection.CollectionReference
        reference to collection where new document should be added
    :param id_doc: str
        id of new document
    :param field_values: dict
        ej. field_values = {"nombre": "Rian", edad: 29}
    """

    coll_ref.document(id_doc).set(field_values)


def update_document(doc_ref: google.cloud.firestore_v1.document.DocumentReference, field_updates: dict):
    """
    Update field values of a document

    :param doc_ref: google.cloud.firestore_v1.document.DocumentReference
        reference to document to be updated
    :param field_updates: dict
        ej. field_updates = {"nombre": "Rian", edad: 29}
    """

    doc_ref.update(field_updates)


