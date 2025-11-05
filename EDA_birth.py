
import pandas as pd
import numpy as np
import statsmodels.formula.api as smf
import pingouin as pg
import seaborn as sns
import matplotlib.pyplot as plt

nchs = pd.read_csv('NCHS_-_U.S._and_State_Trends_on_Teen_Births.csv')
nchs = nchs.rename(columns={
    'State': 'state',
    'State Rate': 'teen_birth_rate',   
    'Age Group (Years)': 'age_group',
    'Year': 'year'
})


policy = pd.read_csv('Sex_Policies.csv')
# Standardize column names
policy.columns = [c.strip() for c in policy.columns]

# Rename for convenience
policy = policy.rename(columns={
    "Jurisdiction": "state",
    "Sex ed mandated": "sex_mand",
    "HIV ed mandated": "hiv_mand",
    "Ed must be medically accurate": "accurate",
    "Ed must be age-appropriate": "ageapp",
    "Ed must include abstinence": "abstinence",
    "Ed must include contraception": "contraception",
    "Ed must cover consent": "consent",
    "Ed must include sexual orientation and gender identity": "sogi",
    "Ed must cover healthy relationships": "relationships"
})

# use only columns with yes or no answers
policy = policy[['state', 'sex_mand', 'hiv_mand', 'ageapp','contraception', 'consent', 'relationships']]

# Filter for age group 15–19 and year 2019
nchs = nchs[(nchs["age_group"] == "15-19 years") & (nchs["year"] == 2019)].copy()     
nchs = nchs[['state', 'teen_birth_rate']]

nchs = nchs.groupby('state', as_index=False)['teen_birth_rate'].mean()
merged = pd.merge(nchs, policy, on="state", how="inner")

# Force teen_birth_rate to numeric
merged["teen_birth_rate"] = pd.to_numeric(merged["teen_birth_rate"], errors="coerce")

# Drop rows with missing numeric values
merged = merged.dropna(subset=["teen_birth_rate"])




policy_cols = ["sex_mand","hiv_mand",
               "contraception","consent","relationships"]


summary_table = {}
for col in policy_cols:
    if col in merged.columns:
        means = merged.groupby(col)["teen_birth_rate"].mean()
        summary_table[col] = means.round(2).to_dict()

# Create a table
summary_df = pd.DataFrame(summary_table).T
summary_df.columns = ["No Policy (0)", "Policy Present (1)"]
summary_df.index.name = "Policy Feature"
summary_df = summary_df.sort_index()

'''print("\nAverage Teen Birth Rate by Policy Feature (2019):\n")
print(summary_df)'''


plot_df = summary_df.reset_index().melt(
    id_vars="Policy Feature",
    var_name="Policy Status",
    value_name="Average Teen Birth Rate"
)

# Set up style
sns.set(style="whitegrid")
plt.figure(figsize=(10,6))

# Create grouped barplot
sns.barplot(
    data=plot_df,
    x="Policy Feature",
    y="Average Teen Birth Rate",
    hue="Policy Status",
    palette=["#E57373", "#64B5F6"]
)

# Customize
plt.title("Average Teen Birth Rate by Policy Feature (2019)", fontsize=14, pad=15)
plt.xticks(rotation=45, ha="right")
plt.xlabel("")
plt.ylabel("Average Births per 1,000 Females (Ages 15–19)")
plt.legend(title="")
plt.tight_layout()

plt.show()