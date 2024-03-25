import pandas as pd
import matplotlib.pyplot as plt
import sys


if len(sys.argv) < 2:
    print("Missing filename :(")
    exit(1)


file_name = sys.argv[1]

data = pd.read_csv(f'data\\{file_name}.txt', sep='\s+', header=None)

series_names = ["X-Achse", "Y-Achse", "Z-Achse"]

for col in data.columns:
    plt.plot(data[col], label=series_names[col], linewidth=0.5)

plt.xlabel("Index")
plt.ylabel("Value")
plt.title("Line Graph of Each Series")
plt.legend()

plt.savefig(f"export\\{file_name}.png", dpi=300)
plt.show()
