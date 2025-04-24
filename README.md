# Theoretical Orientation and Research Attitudes in Psychotherapy

In this project, we studied the relationship between theoretical orientations in psychotherapy (e.g., psychoanalysis, cognitive-behavioral therapy, etc.) and the use of scientific evidence and research attitudes by psychotherapists. 

Our objective was to determine whether certain orientations (such as psychoanalysis) rely less or more on scientific evidence compared to others (such as cognitive behavioral therapy). This hypothesis was tested using MANCOVA (corrected with Tukey post-hoc analyses), PCA, cluster, and multinomial logistic regression analysis, to assess differences across theoretical orientations.

## Main Findings 

- Sources such as books, supervision, and peer discussion were more commonly used than empirical research across all orientations; however, CBT practitioners used outcome measures and clinical guidelines significantly more often than psychoanalysts.
- Cluster analysis revealed four therapist profiles that differed by age and workload. Younger (mainly CBT) therapists were more open to research, while older (mainly psychoanalytic) therapists were more conservative.
- A research-practice gap persists in Argentine psychotherapy.

Additionally, psychoanalytic practitioners differ significantly from TCC and eclectic practitioners in several areas:

- Less engagement with evidence-based practices: They show significantly less use of outcome measures, lower openness to researcher-developed therapies, and less interest in learning or applying evidence-based treatments.
- Lower reliance on supervision and external evidence requirements: Psychoanalytic practitioners report relying less on supervision and do not emphasize the need for their supervisors to require evidence-based practices.
- More individual-focused approach: Psychoanalysts tend to focus more on individualized treatment approaches, as opposed to manualized or standardized therapies.

## Repository Structure
===

```
project_root/
│
├── data/
│   ├── featured_data.csv           # Final dataset with selected features for analysis
│   ├── preprocessed_data.csv       # Cleaned and preprocessed dataset
│   ├── raw_data.csv                # Original, raw dataset
│
├── notebooks/
│   ├── analysis/
│   │   ├── cluster_analysis.ipynb    # PCA and cluster data analysis and visualizations
│   │   ├── statistical_analysis.ipynb    # Statistical analysis, including MANCOVA and Tukey tests
│   │
│   ├── data_featuring/
│       ├── data_cleaning.ipynb           # Data cleaning and preprocessing steps
│       ├── data_featuring.ipynb          # Feature extraction and selection
│
├── utils/
│   └── utils.py                    # Utility functions for data loading, preprocessing, data featuring, plots, etc.
│
├── .gitignore
│
└── README.md                       # Project documentation and organization
```