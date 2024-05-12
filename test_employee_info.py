import employee_info

employee_data = [
    {"name": "John", "age": 30, "department": "Sales", "salary": 50000},
    {"name": "Jane", "age": 25, "department": "Marketing", "salary": 60000},
    {"name": "Mary", "age": 23, "department": "Marketing", "salary": 56000},
    {"name": "Chloe",  "age": 35, "department": "Engineering", "salary": 70000},
    {"name": "Mike", "age": 32, "department": "Engineering", "salary": 65000},
    {"name": "Peter", "age": 40, "department": "Sales", "salary": 60000}
]

def test_get_employees_by_age_range():
    lower_limit = 20
    upper_limit = 25
    test_res = []
    
    for item in employee_data:
        if int(item["age"]) > int(lower_limit) and int(item["age"]) < int(upper_limit):
            test_res.append(item)
    
    actual_res = employee_info.get_employees_by_age_range(lower_limit, upper_limit)

    assert(test_res == actual_res)

def test_get_employees_by_age_range():
    result = []
    input_arr = [ {"name " : "John ", "age" : "22"}, 
             {"name " : "may ", "age" : "24"} ]
    test = str("john" , "may")
    for item in input_arr:
        if int(item["age"]) > int(20) and int(item["age"]) < int(30):
            result.append(item)
    print (result)

    assert (result == test)

def test_get_employees_by_dept():
    result = []
    department = "Sales"
  
    for item in employee_data: 
        if "Sales" == item["department"] :
            result.append(item)

    actual_res = employee_info.get_employees_by_dept(department)
    assert (result == actual_res)




