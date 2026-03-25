import pandas as pd

def calculate_epigenetic_risk(lifestyle_data, genetic_features):
    """
    Applies a weighted predictive method to estimate risk 
    based on the interaction of Hardware (DNA) and Software (Lifestyle).
    """
    # 1. Define Weights (Data Science Approach)
    weights = {
        'stress_level': 0.35,
        'avg_sleep_hours': -0.25, # More sleep reduces risk
        'activity_impact': {'Low': 25, 'Moderate': 10, 'High': 0}
    }
    
    # 2. Calculate interaction score
    # If DNA has high GC content (CpG Island), it's more sensitive to stress
    sensitivity_multiplier = 1.5 if genetic_features['is_cpg_island'] else 1.0
    
    base_risk = (lifestyle_data['stress_level'] * weights['stress_level'] * 10)
    sleep_penalty = (8 - lifestyle_data['avg_sleep_hours']) * 5
    activity_penalty = weights['activity_impact'][lifestyle_data['physical_activity']]
    
    total_score = (base_risk + sleep_penalty + activity_penalty) * sensitivity_multiplier
    
    # 3. Requirement: Use Pandas for Data Analysis
    results_df = pd.DataFrame([{
        'Metric': 'Epigenetic Risk Index',
        'Score': round(total_score, 2),
        'Analysis': 'High Risk' if total_score > 50 else 'Stable Expression'
    }])
    
    return results_df