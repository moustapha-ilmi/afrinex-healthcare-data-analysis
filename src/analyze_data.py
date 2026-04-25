import pandas as pd
import matplotlib.pyplot as plt
import os

df = pd.read_csv("data/raw/clinic_visits.csv")

os.makedirs("visuals", exist_ok=True)

# 1. Patients by department
department_counts = df["department"].value_counts()

department_counts.plot(kind="bar", figsize=(8, 5))
plt.title("Patients by Department")
plt.xlabel("Department")
plt.ylabel("Number of Patients")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig("visuals/patients_by_department.png")
plt.show()

# 2. Average wait time by department
completed_df = df[df["status"] == "Completed"]

avg_wait = completed_df.groupby("department")["wait_time_minutes"].mean().sort_values()

avg_wait.plot(kind="bar", figsize=(8, 5))
plt.title("Average Wait Time by Department")
plt.xlabel("Department")
plt.ylabel("Average Wait Time (Minutes)")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig("visuals/avg_wait_by_department.png")
plt.show()

# 3. Appointment status
status_counts = df["status"].value_counts()

status_counts.plot(kind="pie", autopct="%1.1f%%", figsize=(6, 6))
plt.title("Appointment Status Distribution")
plt.ylabel("")
plt.tight_layout()
plt.savefig("visuals/status_distribution.png")
plt.show()

print("Charts created successfully in the visuals folder.")