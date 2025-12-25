def task2():
    staff_shifts = [
    {"name": "Dr. Shaw", "shift_cost": 120, "shifts": 15},
    {"name": "Agent Torres", "shift_cost": 90, "shifts": 22},
    {"name": "Researcher Hall", "shift_cost": 150, "shifts": 10}
    ]
    shift_costs = list(map(lambda x: x["shift_cost"], staff_shifts))
    print(shift_costs)
    print(f"Максимум: {max(shift_costs)}")