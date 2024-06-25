import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
def split_description(description, max_length=50):
    words = description.split()
    if len(description) > max_length:
        midpoint = (len(words) // 2) - 1
        description = ' '.join(words[:midpoint]) + '\n' + ' '.join(words[midpoint:])
    return description


# for each deployment: coverage for each data stream per timebox, heatmap
def deployment_coverage():
    # Load the CSV file
    csv_file_path = './test_survey.csv'
    data = pd.read_csv(csv_file_path)
    data['Description'] = data['Description'].apply(split_description)


    unique_deployments = data['Deployment IDs'].unique()
    for deployment in unique_deployments:
        deployment_data = data[data['Deployment IDs'] == deployment]

        sns.set(style="white")
        cmap = sns.diverging_palette(10, 220, as_cmap=True)
        pivot_data = deployment_data.pivot(index='Description', columns='Start Time', values='Expectation Coverage')
        plt.figure(figsize=(15, 10))
        ax = sns.heatmap(pivot_data, cmap=cmap, vmin=0, vmax=1, linewidth=0.5, square=True, annot=True)

        plt.title(f'Coverage for each Data Stream for Deployment ID {deployment}')
        plt.tight_layout()
        plt.xticks(rotation=45)
        plt.yticks(rotation=0)

        plt.show()


deployment_coverage()
