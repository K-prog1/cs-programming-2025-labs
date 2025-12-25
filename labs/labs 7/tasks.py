import re
def task1():
    objects = [
    ("Containment Cell A", 4),
    ("Archive Vault", 1),
    ("Bio Lab Sector", 3),
    ("Observation Wing", 2)
    ]
    print(sorted(objects, key= lambda x: x[1]))

def task2():
    staff_shifts = [
    {"name": "Dr. Shaw", "shift_cost": 120, "shifts": 15},
    {"name": "Agent Torres", "shift_cost": 90, "shifts": 22},
    {"name": "Researcher Hall", "shift_cost": 150, "shifts": 10}
    ]
    shift_costs = list(map(lambda x: x["shift_cost"], staff_shifts))
    print(shift_costs)
    print(f"Максимум: {max(shift_costs)}")

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

    print(a)


def task4():
    zones = [
    {"zone": "Sector-12", "active_from": 8, "active_to": 18},
    {"zone": "Deep Storage", "active_from": 0, "active_to": 24},
    {"zone": "Research Wing", "active_from": 9, "active_to": 17}
    ]
    a = list(filter(lambda x: x["zone"] if x["active_from"]>=8 and x["active_to"]<= 18 else False, zones))

    print(a)

def task5():
    reports = [
    {"author": "Dr. Moss", "text": "Analysis completed. Reference: http://external-archive.net"},
    {"author": "Agent Lee", "text": "Incident resolved without escalation."},
    {"author": "Dr. Patel", "text": "Supplementary data available at https://secure-research.org"},
    {"author": "Supervisor Kane", "text": "No anomalies detected during inspection."},
    {"author": "Researcher Bloom", "text": "Extended observations uploaded to http://research-notes.lab"},
    {"author": "Agent Novak", "text": "Perimeter secured. No external interference observed."},
    {"author": "Dr. Hargreeve", "text": "Full containment log stored at https://internal-db.scp"},
    {"author": "Technician Moore", "text": "Routine maintenance completed successfully."},
    {"author": "Dr. Alvarez", "text": "Cross-reference materials: http://crosslink.foundation"},
    {"author": "Security Officer Tan", "text": "Shift completed without incidents."},
    {"author": "Analyst Wright", "text": "Statistical model published at https://analysis-hub.org"},
    {"author": "Dr. Kowalski", "text": "Behavioral deviations documented internally."},
    {"author": "Agent Fischer", "text": "Additional footage archived: http://video-storage.sec"},
    {"author": "Senior Researcher Hall", "text": "All test results verified and approved."},
    {"author": "Operations Lead Grant", "text": "Emergency protocol draft shared via https://ops-share.scp"}
    ]
    

    a = list(map(
        lambda r: {"author": r["author"], "text": re.sub(r'https?://\S+', '[ДАННЫЕ УДАЛЕНЫ]', r["text"])},
        filter(lambda r: 'http://' in r["text"] or 'https://' in r["text"], reports)
    ))
    print(a)

def task6():
    scp_objects = [
        {"scp": "SCP-096", "class": "Euclid"},
        {"scp": "SCP-173", "class": "Euclid"},
        {"scp": "SCP-055", "class": "Keter"},
        {"scp": "SCP-999", "class": "Safe"},
        {"scp": "SCP-3001", "class": "Keter"}
    ]

    high_risk = list(filter(lambda x: x["class"] != "Safe", scp_objects))
    
    print(high_risk)

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

def task8():
    protocols = [
    ("Lockdown", 5),
    ("Evacuation", 4),
    ("Data Wipe", 3),
    ("Routine Scan", 1)
    ]

    result = list(map(lambda x: f"Protocol {x[0]} - Criticality {x[1]}", protocols))
    print(result)


def task9():
    shifts = [6, 12, 8, 24, 10, 4]

    valid_shifts = list(filter(lambda x: 8 <= x <= 12, shifts))
    print(valid_shifts)

def task10():
    
    evaluations = [
        {"name": "Agent Cole", "score": 78},
        {"name": "Dr. Weiss", "score": 92},
        {"name": "Technician Moore", "score": 61},
        {"name": "Researcher Lin", "score": 88}
    ]

    best = max(evaluations, key=lambda x: x["score"])
    print(best)

