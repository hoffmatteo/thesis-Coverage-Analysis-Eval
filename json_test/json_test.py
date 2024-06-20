import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# give overall study coverage for each timebox, scatter plot
def overall_study_coverage():
    # Load the new CSV file
    file_path_study = './test_study.csv'
    data_study = pd.read_csv(file_path_study)

    # Convert 'Start Time' to datetime
    data_study['Start Time'] = pd.to_datetime(data_study['Start Time'])

    # Plot the line chart for Time Coverage over Start Time
    plt.figure(figsize=(14, 7))
    plt.plot(data_study['Start Time'], data_study['Time Coverage'], marker='o', linestyle='-', color='b')

    plt.title('Time Coverage over Start Time for the entire study')
    plt.xlabel('Start Time')
    plt.ylabel('Time Coverage')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.show()


# give coverage for each data stream for each timebox over all deployments --> heatmap
def overall_deployment_coverage():
    csv_file_path = './test_deployments.csv'

    # Read CSV file into a pandas DataFrame
    data = pd.read_csv(csv_file_path)

    # Pivot the DataFrame to get a matrix-like format, which is required for the heatmap

    sns.set(style="white")
    cmap = sns.diverging_palette(10, 220, as_cmap=True)
    pivot_data = data.pivot(index='Description', columns='Start Time', values='Time Coverage')
    plt.figure(figsize=(15, 10))
    ax = sns.heatmap(pivot_data, cmap=cmap, vmin=0, vmax=1, linewidth=0.5, square=True, annot=True)
    plt.tight_layout()
    plt.xticks(rotation=45)
    plt.yticks(rotation=0)
    plt.title('Time Coverage for each Data Stream over all Deployments')

    plt.show()


# for each deployment: coverage for each data stream per timebox, heatmap
def deployment_coverage():
    # Load the CSV file
    csv_file_path = './test_datastreams.csv'
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


overall_study_coverage()
