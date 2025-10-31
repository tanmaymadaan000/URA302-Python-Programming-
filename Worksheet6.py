# q1.1
import pandas as pd
print("pandas version:", pd.__version__)
print()

# q1.2
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
cities = ["New York", "Los Angeles", "Chicago"]
df = pd.DataFrame({
    "Name": names,
    "Age": ages,
    "City": cities
})
print(df)
print()

# q2.1
s1 = pd.Series([100, 200, 300, 400, 500])
print(s1)
print()

# q2.2
print(s1.iloc[1])
print(s1.iloc[3])
print()

# q2.3
s2 = pd.Series([10, 20, 30, 40, 50])
print(s1 + s2)
print()

# q3.1
print(df[["Name", "City"]])
print()

# q3.2
salaries = [50000, 60000, 70000]
df["Salary"] = salaries
print(df)
print()

# q3.3
print(df["Age"].mean())
print(df["Salary"].sum())
print()

# q4.1
data = {
    "A": [10, 20, 30],
    "B": [40, 50, 60],
    "C": [70, 80, 90]
}
df2 = pd.DataFrame(data)
print(df2)
print()

# q4.2
print(df2.describe())
print()

# q5.1
data = {
    "Name": ["Ravi", "Neha", "Aman", "Simran"],
    "Marks": [85, 90, 75, 95],
    "Subject": ["Math", "Science", "English", "Math"]
}
df3 = pd.DataFrame(data)
print(df3)
print()

# q5.2
print(df3[df3["Marks"] > 80])
print()

# q5.3
print(df3["Marks"].mean())
print()

# q6.1
df3.to_csv("student_data.csv", index=False)
print("CSV file saved!")
print()

# q6.2
read_df = pd.read_csv("student_data.csv")
print(read_df)
print()

# q7.1
print(read_df.sort_values("Marks"))
print()

# q7.2
print(read_df.sort_values("Marks", ascending=False))
print()

# q8.1
print(read_df["Subject"].value_counts())
print()

# q8.2
print(read_df.groupby("Subject")["Marks"].mean())
print()

# q9.1
print(read_df.iloc[0])
print()

# q9.2
print(read_df.iloc[1:3])
print()

# q10.1
print(read_df.head(2))
print()

# q10.2
print(read_df.tail(2))
print()
