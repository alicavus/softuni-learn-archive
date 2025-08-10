def evaluate_data(data_type: str, data_value: str) -> str:
    output = ''
    match data_type:
        case "int":
            output = int(data_value) * 2
        case "real":
            output = f'{float(data_value) * 1.5:.2f}'
        case 'string':
            output = f'${data_value}$'
    print(output)

evaluate_data(input(), input())