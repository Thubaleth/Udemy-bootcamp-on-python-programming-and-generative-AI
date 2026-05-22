"""
Analyze store sales.

sales = {
    "Monday": [120, 300, 250],
    "Tuesday": [500, 100, 400],
    "Wednesday": [150, 200, 100]
}

Requirements:
- Calculate daily totals
- Find highest sales day
- Find average sales
- Display summary statistics
"""

sales = {
    "Monday": [120, 300, 250],
    "Tuesday": [500, 100, 400],
    "Wednesday": [150, 200, 100]
}
def analyze_store_sales():
      biggest = 0
      day = ""
      avg_list = []
      daily_totals = {}
      for days,amount in sales.items():
        tot_of_day = sum(amount)
        daily_totals[day] = tot_of_day

        avg_list.append(tot_of_day)
        if tot_of_day > biggest:
            biggest = tot_of_day
            day = days
      average_sales = sum(daily_totals.values()) / len(daily_totals)
    
      return (
        f"Daily totals: {daily_totals}\n"
        f"Highest sales day: {day} ({biggest})\n"
        f"Average sales: {average_sales}"
        )

        

print(analyze_store_sales)

