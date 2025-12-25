def task8():
    protocols = [
    ("Lockdown", 5),
    ("Evacuation", 4),
    ("Data Wipe", 3),
    ("Routine Scan", 1)
    ]

    result = list(map(lambda x: f"Protocol {x[0]} - Criticality {x[1]}", protocols))
    print(result)