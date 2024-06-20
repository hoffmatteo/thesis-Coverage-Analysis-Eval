import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# for each deployment: coverage for each data stream per timebox, heatmap
def deployment_coverage():
    # Load the CSV file
    csv_file_path = './test_survey.csv'
    data = pd.read_csv(csv_file_path)

    unique_deployments = data['Deployment IDs'].unique()
    for deployment in unique_deployments:
        deployment_data = data[data['Deployment IDs'] == deployment]

        sns.set(style="white")
        cmap = sns.diverging_palette(10, 220, as_cmap=True)
        pivot_data = deployment_data.pivot(index='Description', columns='Start Time', values='Time Coverage')
        plt.figure(figsize=(15, 10))
        ax = sns.heatmap(pivot_data, cmap=cmap, vmin=0, vmax=1, linewidth=0.5, square=True, annot=True)

        plt.title(f'Coverage for each Data Stream for Deployment ID {deployment}')
        plt.tight_layout()
        plt.xticks(rotation=45)
        plt.yticks(rotation=0)

        plt.show()


deployment_coverage()
