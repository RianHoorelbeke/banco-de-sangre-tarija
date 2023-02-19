from google.cloud import bigquery


def update_routine(routine_id: str, routine_body: str):

    client = bigquery.Client()
    routine = client.get_routine(routine_id)

    routine.body = routine_body

    client.update_routine(
        routine,
        [
            "body",
            "arguments",
            "language",
            "type_",
            "return_type",
        ],
    )