Bill_Amount = float(input("Enter the bill amount:"))
Number_of_people = int(input("Enter the number of people:"))
Tip_percentage = int(input("Enter the tip percentage (10,12,15):"))
Tip_Amount = (Bill_Amount * Tip_percentage) / 100
Total_Amount = Bill_Amount + Tip_Amount
Amount_per_person = Total_Amount / Number_of_people
print(f"Each person should pay: {Amount_per_person:.2f}")