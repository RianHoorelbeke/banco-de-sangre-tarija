import google


def query_where(coll_ref: google.cloud.firestore_v1.collection.CollectionReference, document_key: str, operator: str, condition: str or int, limit: int = 100):
    """
    Get results from query with where statement

    :param coll_ref: google.cloud.firestore_v1.collection.CollectionReference
        reference to collection
    :param document_key: str
        ej. nombre, edad
    :param operator: str
        ej. "==" or ">="
    :param condition: str
        ej. "Rian" or 29
    :param limit: int
        limit for number of results, default = 100

    :return: google.cloud.firestore_v1.base_document.DocumentSnapshot object
        Results of query with condition
    """

    return coll_ref.where(document_key, operator, condition).limit(limit).get()


def query_order_by(coll_ref: google.cloud.firestore_v1.collection.CollectionReference, document_key: str, direction: str = 'DESCENDING', limit: int = 100):
    """
    Get results from query to order by document key

    :param coll_ref: google.cloud.firestore_v1.collection.CollectionReference
        reference to collection
    :param document_key: str
        ej. nombre, edad
    :param direction: str
        ej. "DESCENDING" or "ASCENDING", default = "DESCENDING"
    :param limit: int
        limit for number of results, default = 100

    :return: Results of ordered query
    """

    return coll_ref.order_by(document_key, direction=direction).limit(limit).get()


def print_query_results(results: list):
    """
    Print results from query

    :param results: google.cloud.firestore_v1.base_document.DocumentSnapshot object
    """

    for doc in results:
        print(doc.id, doc.to_dict())