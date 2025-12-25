def task3():
    personnel = [
    {"name": "Dr. Klein", "clearance": 2},
    {"name": "Agent Brooks", "clearance": 4},
    {"name": "Technician Reed", "clearance": 1}
    ]
    a = list(map(lambda x: { "name": x["name"],
                "clearance": x["clearance"],
                "category":(

     'Top secret' if 4 == x["clearance"] else 'Confidental' if 2 == x['clearance'] else 'Restricted')}, personnel))
