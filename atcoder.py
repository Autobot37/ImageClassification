import json
import matplotlib.pyplot as plt

# Load JSON data from file
with open('problem-models.json', 'r') as file:
    data = json.load(file)

# Extract difficulty values
difficulties = [val.get('difficulty', 0) for key, val in data.items()]

# Calculate frequency in 10 interval bins
interval_width = 10
min_difficulty = min(difficulties)
max_difficulty = max(difficulties)
num_bins = (max_difficulty - min_difficulty) // interval_width + 1
bins = [min_difficulty + i * interval_width for i in range(num_bins)]
frequency = [0] * num_bins

for difficulty in difficulties:
    bin_index = (difficulty - min_difficulty) // interval_width
    frequency[bin_index] += 1

a = 400
b = 2400
# Calculate average frequency within the specified range
start_bin_index = (a - min_difficulty) // interval_width
end_bin_index = (b - min_difficulty) // interval_width + 1
average_frequency = (sum(frequency[start_bin_index:end_bin_index])-250) / ((b - a) // interval_width + 1)

# Plotting
plt.figure(figsize=(10*2, 6*2))
plt.bar(bins, frequency, width=interval_width, align='edge', edgecolor='black')
plt.title('Frequency of Difficulties in 10 Interval Bins')
plt.xlabel('Difficulty')
plt.ylabel('Frequency')
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Annotate average frequency on the plot
plt.annotate(f'Average Frequency: {average_frequency:.2f}',
             xy=(0.5, 0.9),
             xycoords='axes fraction',
             fontsize=12,
             ha='center')

# Set x-axis and y-axis limits
plt.ylim(0, 20)
plt.xlim(a, b)

plt.show()
