# Theoretical Orientation and Research Attitudes in Psychotherapy

The aim of this project is to study the relationship between theoretical orientations in psychotherapy (e.g., psychoanalysis, cognitive-behavioral therapy) and the use of scientific evidence and research attitudes by psychotherapists. 

The project seeks to determine whether certain orientations (such as psychoanalysis) rely less on scientific evidence compared to others (such as cognitive behavioral therapy). This hypothesis is tested using MANOVA, corrected with Tukey post-hoc analyses, to assess differences across theoretical orientations.

## Main Findings 

- As expected, cognitive-behavioral therapies (TCC) demonstrate a stronger reliance on empirical, evidence-based practices compared to eclectic and psychoanalytic orientations.

Psychoanalytic practitioners differ significantly from TCC and eclectic practitioners in several areas:

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
│   │   ├── exploratory_analysis.ipynb    # Exploratory data analysis and visualizations
│   │   ├── statistical_analysis.ipynb    # Statistical analysis, including MANOVA and Tukey tests
│   │
│   ├── data_featuring/
│       ├── data_cleaning.ipynb           # Data cleaning and preprocessing steps
│       ├── data_featuring.ipynb          # Feature extraction and selection
│
├── utils/
│   └── utils.py                    # Utility functions for data loading, preprocessing, etc.
│
├── .gitignore
│
├── original_analysis_gyani.ipynb   # First analyses conducted 
│
└── README.md                       # Project documentation and organization
```