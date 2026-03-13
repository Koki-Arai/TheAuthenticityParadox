import pandas as pd
import numpy as np
from scipy import stats
import statsmodels.api as sm
from statsmodels.stats.multicomp import pairwise_tukeyhsd

def run_analysis():
    # Load data (skipping label rows 1-4 based on CSV structure)
    df_raw = pd.read_csv('data/consumer_data.csv', encoding='utf-8')
    df = df_raw.iloc[5:].reset_index(drop=True)
    
    # 1. Variable Preparation
    df['purchase'] = (df['q3'].astype(str).str.strip().str[0] == '1').astype(int)
    df['awareness'] = pd.to_numeric(df['sc2ac'], errors='coerce')
    df['concern'] = 5 - pd.to_numeric(df['q4'], errors='coerce') 
    df['pricetol'] = pd.to_numeric(df['q5'], errors='coerce')
    df['age'] = pd.to_numeric(df['年齢'], errors='coerce')
    df['agedummy'] = (df['age'] < 40).astype(int)

    # 2. Analysis 1: Awareness-Adoption Paradox
    df['awarenesscat'] = pd.cut(df['awareness'], bins=[0,1,3,5,7], 
                                labels=['Not aware','Somewhat aware','Very aware','Completely aware'])
    ct1 = pd.crosstab(df['awarenesscat'], df['purchase'])
    print("--- Analysis 1: Chi-square Results ---")
    chi2, p, _, _ = stats.chi2_contingency(ct1)
    print(f"Chi2: {chi2:.2f}, p: {p:.4f}")

    # 3. Analysis 3: ANOVA for Price Tolerance
    print("\n--- Analysis 3: ANOVA Results ---")
    groups = [df[df['q4'].astype(float)==c]['pricetol'].dropna() for c in [1,2,3,4]]
    f_stat, p_val = stats.f_oneway(*groups)
    print(f"F-stat: {f_stat:.2f}, p: {p_val:.4f}")

if __name__ == "__main__":
    run_analysis()