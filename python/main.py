from firebase_utils import connect_firebase, get_reference_collection, get_reference_document
from read_data import query_where, query_order_by, print_query_results
from write_data import add_document, add_document_with_id, update_document
from upload_data import import_csv_to_collection, convert_xlsx_to_csv
from google_bigquery import update_routine


if __name__ == '__main__':

    routine_body = "TIMESTAMP_MILLIS(\nSAFE_CAST(JSON_EXTRACT(json, '$._seconds') AS INT64) * 1000 + 7200000 + SAFE_CAST(\nSAFE_CAST(JSON_EXTRACT(json, '$._nanoseconds') AS INT64) / 1E6 AS INT64))"
    routine_id = "banco-de-sangre-tarija.firestore_fact_donantes.firestoreTimestamp"
    update_routine(routine_id, routine_body)

    # convert_xlsx_to_csv("donantes.xlsx")

    # Connect with database
    # google.cloud.firestore_v1.client.Client object to communicate with database
    db = connect_firebase()

    # --------------------------------------------------------------------------------

    # export_to_csv(db,'fact_donantes', 'test.csv')

    # Get reference to collection

    # Get reference to collection of donantes
    donantes_ref = get_reference_collection(db, "fact_donantes")

    # -----------------------------------------------------------------------------------

    # Upload data

    # Upload data using csv
    file_name = "donantes.csv"
    import_csv_to_collection(file_name, donantes_ref)

    # -----------------------------------------------------------------------------------

    # Get reference to a document (=donante1) from the collection (=donantes)
    donante1_ref = get_reference_document(db, "fact_donantes","1")

    # -----------------------------------------------------------------------------------

    # Read data

    # Query where name = Rian
    query_results = query_where(donantes_ref, "nombre", "==", "Valeria", 1)
    print("Results of query: select * from donantes where nombre = Valeria")
    print_query_results(query_results)

    # Query order by name
    query_results = query_order_by(donantes_ref, "id", "ASCENDING", 50)
    print("Results of query: select * from donantes order by nombre ascending")
    print_query_results(query_results)

    # -----------------------------------------------------------------------------------

    # Write data

    # Add document with random ID
    field_values = {"nombre": "Rian", "edad": 29}
    add_document(donantes_ref, field_values)

    # Add document with ID
    id_doc = "rhoorel"
    add_document_with_id(donantes_ref, id_doc, field_values)

    # Update document using reference
    doc_ref = get_reference_document(db,"donantes", "rhoorel")
    field_updates = {"nombre": "otro_nombre", "edad": 24}
    update_document(doc_ref, field_updates)

