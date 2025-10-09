import numpy as np
from scipy import fftpack, linalg, interpolate, signal, optimize, integrate
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Q1
data = np.random.rand(10)
mean_value = np.mean(data)
median_value = np.median(data)
variance_value = np.var(data)
print("Q1:")
print("Data:", data)
print("Mean:", mean_value)
print("Median:", median_value)
print("Variance:", variance_value)

# Q2
arr_2d = np.random.rand(4, 4)
fft_result = fftpack.fft2(arr_2d)
print("\nQ2:")
print("Original Array:\n", arr_2d)
print("FFT Result:\n", fft_result)

# Q3
mat = np.array([[2, 1], [5, 3]])
det_val = linalg.det(mat)
inv_mat = linalg.inv(mat)
eig_vals, eig_vecs = linalg.eig(mat)
print("\nQ3:")
print("Matrix:\n", mat)
print("Determinant:", det_val)
print("Inverse:\n", inv_mat)
print("Eigenvalues:", eig_vals)

# Q4
x_points = np.linspace(0, 10, 10)
y_points = np.sin(x_points)
f_interp = interpolate.interp1d(x_points, y_points, kind='cubic')
x_new = np.linspace(0, 10, 100)
y_new = f_interp(x_new)
plt.plot(x_points, y_points, 'o', label='Original')
plt.plot(x_new, y_new, '-', label='Interpolated')
plt.title("Q4 Interpolation")
plt.legend()
plt.show()

# Q5
t = np.linspace(0, 1, 500)
sig = np.sin(2 * np.pi * 50 * t) + np.sin(2 * np.pi * 120 * t)
filtered = signal.medfilt(sig, kernel_size=5)
plt.plot(t, sig, label='Original Signal')
plt.plot(t, filtered, label='Filtered Signal')
plt.legend()
plt.title("Q5 Signal Filtering")
plt.show()

# Q6
sales = np.random.randint(1000, 5000, (4, 12))
total_sales = np.sum(sales)
avg_sales = np.mean(sales)
max_month = np.argmax(np.sum(sales, axis=0)) + 1
min_month = np.argmin(np.sum(sales, axis=0)) + 1
print("\nQ6:")
print("Total Sales:", total_sales)
print("Average Sales:", avg_sales)
print("Best Month:", max_month)
print("Worst Month:", min_month)

# Q7
students = ["Arin", "Aditya", "Chirag", "Gurleen", "Kunal"]
marks = np.array([
    [85, 78, 92, 88],
    [79, 82, 74, 90],
    [90, 85, 89, 92],
    [66, 75, 80, 78],
    [70, 68, 75, 85]
])
total_marks = np.sum(marks, axis=1)
avg_marks = np.mean(marks, axis=1)
best_student = students[np.argmax(total_marks)]
worst_student = students[np.argmin(total_marks)]
print("\nQ7:")
print("Total Marks:", total_marks)
print("Average Marks:", avg_marks)
print("Best Student:", best_student)
print("Worst Student:", worst_student)

# Q8
time = np.array([0, 1, 2, 3, 4, 5])
velocity = np.array([2, 3.1, 7.9, 18.2, 34.3, 56.2])

def func(t, a, b, c):
    return a*t**2 + b*t + c

popt, _ = curve_fit(func, time, velocity)
a, b, c = popt
print("\nQ8:")
print("a, b, c =", a, b, c)

# Q9 (same as Q7 but with plots)
plt.bar(students, total_marks)
plt.title("Q9 - Student Total Marks")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()

# Q10 (curve fit with plot)
t_new = np.linspace(0, 5, 100)
v_fit = func(t_new, a, b, c)
plt.scatter(time, velocity, color='red', label='Data')
plt.plot(t_new, v_fit, label='Fitted Curve')
plt.title("Q10 Curve Fitting")
plt.legend()
plt.show()

# Q11
years = np.array([2000, 2005, 2010, 2015, 2020])
pop = np.array([50, 55, 70, 80, 90])
corr = np.corrcoef(years, pop)[0, 1]
f = interpolate.interp1d(years, pop)
pop_2008 = f(2008)
print("\nQ11:")
print("Correlation Coefficient:", corr)
print("Estimated Population in 2008:", pop_2008)
plt.plot(years, pop, 'o-', label='Population Data')
plt.axvline(2008, color='r', linestyle='--', label='2008')
plt.legend()
plt.title("Q11 Interpolation")
plt.show()

# Q12
x = np.linspace(-3, 3, 100)
p = 3*x**3 - 5*x**2 + 2*x - 8
roots = np.roots([3, -5, 2, -8])
print("\nQ12:")
print("Roots:", roots)
plt.plot(x, p, label='p(x)')
plt.scatter(roots, np.zeros_like(roots), color='red', label='Roots')
plt.title("Q12 Polynomial Roots")
plt.legend()
plt.show()

# Q13
import time
sizes = [200, 400, 600, 800, 1000]
times = []
for s in sizes:
    text = "a" * (s * 1024 * 1024)
    start = time.time()
    text.upper()
    end = time.time()
    times.append(end - start)
print("\nQ13:")
print("Times for file sizes:", times)
plt.plot(sizes, times, 'o-')
plt.title("Q13 Time vs File Size")
plt.xlabel("Size (MB)")
plt.ylabel("Time (s)")
plt.show()

# Q14
def f(x):
    return x**4 - 3*x**3 + 2
res = optimize.minimize(f, x0=0)
x_min = res.x[0]
y_min = res.fun
print("\nQ14:")
print("Local Min at x =", x_min, "y =", y_min)
x_vals = np.linspace(-2, 3, 100)
plt.plot(x_vals, f(x_vals))
plt.scatter(x_min, y_min, color='red', label='Min Point')
plt.legend()
plt.title("Q14 Local Minima")
plt.show()

# Q15
def model(theta, t):
    theta1, theta2 = theta
    dtheta1 = theta2
    dtheta2 = -0.2*theta2 - np.sin(theta1)
    return [dtheta1, dtheta2]

t_vals = np.linspace(0, 20, 200)
init = [1, 0]
sol = integrate.odeint(model, init, t_vals)
theta_vals = sol[:, 0]
max_disp = np.max(theta_vals)
max_time = t_vals[np.argmax(theta_vals)]
print("\nQ15:")
print("Max Displacement:", max_disp)
print("Time of Max:", max_time)
plt.plot(t_vals, theta_vals)
plt.title("Q15 Damped Motion")
plt.xlabel("Time")
plt.ylabel("Theta(t)")
plt.show()
