days = int(input())
plunder_per_day = float(input())
expected_plunder = float(input())

total_plunder = 0.0

for day in range(1, days+1):
    total_plunder += plunder_per_day

    if not day % 3:
        total_plunder += plunder_per_day * 0.5
    
    if not day % 5:
        total_plunder *= 0.7
    

print(f"Ahoy! {total_plunder:.2f} plunder gained." if total_plunder >= expected_plunder else f"Collected only {total_plunder/expected_plunder * 100:.2f}% of the plunder.")
    
