import numpy as np

# === Project 1 ===
data = np.genfromtxt("sensor_data.csv", delimiter=",", skip_header=1)

temperature = data[:,1]
distance = data[:,2]
battery = data[:,3]
humidity = data[:,4]

below30 = np.sum(battery < 30)
index = np.argmax(temperature)

with open("Result_1.csv", "w") as d:
    d.write(f"Temperature mean: {np.mean(temperature)}\n")
    d.write(f"Distance mean: {np.mean(distance)}\n")
    d.write(f"Battery mean: {np.mean(battery)}\n")
    d.write(f"Humidity mean: {np.mean(humidity)}\n")
    d.write("\n")

    d.write(f"Min Temperature: {np.min(temperature)}\n")
    d.write(f"Min Distance: {np.min(distance)}\n")
    d.write(f"Min Battery: {np.min(battery)}\n")
    d.write(f"Min Humidity: {np.min(humidity)}\n")
    d.write("\n")

    d.write(f"Max Temperature: {np.max(temperature)}\n")
    d.write(f"Max Distance: {np.max(distance)}\n")
    d.write(f"Max Battery: {np.max(battery)}\n")
    d.write(f"Max Humidity: {np.max(humidity)}\n")
    d.write("\n")

    d.write(f"Time when temp was highest: {data[index,0]}\n")
    d.write(f"Count Battery < 30: {below30}\n")

# === Project 2 ===
path = np.genfromtxt("robot_path.csv", delimiter=",", skip_header=1)

diff = np.diff(path, axis=0)
step_dist = np.linalg.norm(diff, axis=1)
total_dist = np.sum(step_dist)

dist_origin = np.linalg.norm(path, axis=1)
farthest = path[np.argmax(dist_origin)]

unique = np.unique(path, axis=0)
revisit = len(unique) != len(path)

with open("Result_2.csv", "w") as d:
    d.write(f"Total Distance: {total_dist}\n")
    d.write(f"Farthest Point: {farthest}\n")
    d.write(f"Revisited: {revisit}\n")
