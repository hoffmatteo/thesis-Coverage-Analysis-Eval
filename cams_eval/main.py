import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Function to modify the 'Description' field
def modify_description(description):
    prefix = "dk.cachet.carp."
    if prefix in description:
        # Split and get only the part after 'dk.cachet.carp.'
        measure = description.split(prefix)[-1]
        # Remove anything after a space (like "after 1h")
        return measure.split()[0]
    return description


# Read CSV file into a pandas DataFrame
csv_file_path = 'test_db.csv'
data = pd.read_csv(csv_file_path)

# Apply the function to modify the 'Description' column
data['Description'] = data['Description'].apply(modify_description)

# Pivot the DataFrame to get a matrix-like format, which is required for the heatmap
pivot_data = data.pivot(index='Description', columns='Start Time', values='Absolute Coverage')

# Plot the heatmap
sns.set(style="white")
cmap = sns.diverging_palette(10, 220, as_cmap=True)
plt.figure(figsize=(40, 10))
ax = sns.heatmap(pivot_data, cmap=cmap, vmin=0, vmax=1, linewidth=0.5, square=True, annot=True)

plt.show()
