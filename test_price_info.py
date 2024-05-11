
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

def test_cost_of_fruits():
    price_list={'apple' : 1., 'orange':2}
    quantity_list= {'apple': 1, 'orange':2}
    fruits = 0
    for key in price_list.keys():
        if fruits == quantity_list[key]: 
            cost = fruits*price_list[key]



