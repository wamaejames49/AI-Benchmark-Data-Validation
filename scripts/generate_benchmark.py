import pandas as pd

def generate_benchmark_errors():
    """
    Simulates high-stakes data entry errors for AI agent evaluation.
    Includes: Silent truncation, Transpositions, and Format Inconsistencies.
    """
    # Load Clean Data
    df = pd.read_csv('../data/ground_truth/mortgage_audit_clean.csv')
    
    # 1. Silent Truncation (Name cut off)
    df.at[0, 'borrower_name'] = "Nathaniel Richar" # Removed 'dson'
    
    # 2. Digit Transposition (High Risk Audit Error)
    df.at[0, 'loan_amount'] = 405250.00 # Swapped 50 with 05
    
    # 3. Format Inconsistency (Date formats)
    df.at[0, 'closing_date'] = "01/12/2024"
    df.at[2, 'closing_date'] = "15-Jan-24"
    
    # 4. Data Loss (Missing SSN)
    df.at[2, 'ssn_mask'] = ""
    
    # 5. Scientific Notation Error (Common in spreadsheet exports)
    df.at[5, 'property_zip'] = "8.02E+04"
    
    # 6. Leading Zero Loss (Common CSV error)
    df.at[8, 'property_zip'] = "2108" # Should be 02108
    
    # Save the corrupted file
    df.to_csv('../data/corrupted_tasks/mortgage_audit_dirty.csv', index=False)
    print("AI Benchmark Dataset successfully created with 6 high-stakes error types.")

if __name__ == "__main__":
    generate_benchmark_errors()
