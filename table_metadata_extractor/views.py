from django.http import JsonResponse
from sqlalchemy import create_engine, inspect

def table_metadata_view(request):
    connection_string = request.GET.get('connection_string')

    if not connection_string:
        return JsonResponse({'error': 'No connection string provided'})

    try:
        engine = create_engine(connection_string)
        inspector = inspect(engine)
        tables = inspector.get_table_names()

        table_metadata_list = []
        for table_name in tables:
            columns = inspector.get_columns(table_name)
            num_rows = 0
            schema = ''
            database = ''

            column_metadata_list = [
                {"name": column['name'], "type": str(column['type'])} for column in columns
            ]

            table_metadata = {
                "columns": column_metadata_list,
                "num_rows": num_rows,
                "schema": schema,
                "database": database
            }

            table_metadata_list.append(table_metadata)

        return JsonResponse({'tables': table_metadata_list})

    except Exception as e:
        return JsonResponse({'error': str(e)})
