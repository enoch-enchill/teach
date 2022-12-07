import matplotlib.pyplot as plt
import numpy as np


def readData(file_path):
    f = open(file_path, 'r')
    lines = f.readlines()
    f.close()
    return lines


def cleanData(data):
    scores = []
    for line in data:
        score = float((line.strip().split(",")[1]).strip())
        scores.append(score)
    return np.array(scores)


def plotGraph(x, y, z):
        
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    ax.scatter(x, y, z, marker='^')
    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')

    plt.show()

print("Reading files....")
x_data = readData("src\casia_far_labels_scores.txt")
y_data = readData("src\glint_far_labels_scores.txt")
z_data = readData("src\ms1_far_labels_scores.txt")

x_array = cleanData(x_data)
y_array = cleanData(y_data)
z_array = cleanData(z_data)

print(len(x_array), len(y_array), len(z_array))
print("Plotting graph")
# plotGraph(x_array, y_array, z_array)
print("Done...!")