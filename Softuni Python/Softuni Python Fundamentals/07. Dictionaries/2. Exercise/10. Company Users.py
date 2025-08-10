companies = {}

while True:
    company_info = input()

    if company_info == "End":
        for company in companies:
            print(f'{companies[company]["name"]}')
            print("\n".join([f'-- {emploee}' for emploee in companies[company]["staff"]]))
        break

    company_name, employee_id = company_info.split(" -> ")

    if company_name not in companies:
        companies[company_name] = {
            "name": company_name,
            "staff": []
        }
    if employee_id not in companies[company_name]["staff"]:
        companies[company_name]["staff"].append(employee_id)



