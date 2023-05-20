from functions import from_json_data, get_iso_date, format_data

list_of_operations = from_json_data()
list_executed = [operation for operation in list_of_operations if operation and operation['state'] == 'EXECUTED']

sorted_executed_list = sorted(list_executed, key=get_iso_date, reverse=True)
for operation in sorted_executed_list[:5]:
    print(format_data(operation))
    print()