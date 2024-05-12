import price_info

def test_total_cost_shopping():
    price_list={'apple' : 1., 'orange':2}
    quantity_list= {'apple': 1, 'orange':2}
    total_cost = 0
    x = 0
    test = 5
    for key in price_list.keys():
        if key in quantity_list:
            total_cost = quantity_list[key]*price_list[key] 
            x += total_cost 

    assert(test== x) 

def test_cost_of_fruits():
    fruits = "apple"
    quantity = 10
    actual_res = price_info.cost_of_fruits(fruits, quantity)
    test = 12
    assert(test == actual_res)





