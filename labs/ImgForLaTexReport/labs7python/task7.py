def task7():
    incidents = [
        {"id": 101, "staff": 4},
        {"id": 102, "staff": 12},
        {"id": 103, "staff": 7},
        {"id": 104, "staff": 20}
    ]

    sorted_incidents = sorted(incidents, key=lambda x: x["staff"], reverse=True)
    
    top3 = sorted_incidents[:3]
    
    print(top3)
