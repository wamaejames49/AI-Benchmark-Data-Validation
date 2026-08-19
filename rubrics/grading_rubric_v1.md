AI Agent Grading Rubric: Mortgage Audit Data Reconciliation
Total Points: 100 | Passing Score: 100 (Zero Tolerance Domain)
I. Accuracy & Error Detection (40 Points)
Silent Truncation: Did the agent identify the truncated name "Nathaniel Richar"?
Silent Truncation: Did the agent identify the truncated name "Maria Garcia-Lope"?
Digit Transposition: Did the agent flag the $45,000 difference in Loan 88201?
Digit Transposition: Did the agent flag the $72,000 difference in Loan 88207?
Missing Fields: Did the agent flag the null SSN mask in Row 3?
Value Preservation: Did the agent keep the hyphen in "Sterling-Archer"?
Value Preservation: Did the agent keep the apostrophe in "D'Souza"?
Value Preservation: Did the agent keep the period in "Robert J. Miller"?
Status Accuracy: Did the agent expand "PEND" to "PENDING"?
Status Accuracy: Did the agent expand "APPROV" to "APPROVED"?
II. Format Reconciliation (30 Points)
Date Standard: Are all dates converted to ISO 8601 (YYYY-MM-DD)?
Date Detection: Did the agent correctly parse "15-Jan-24"?
Date Detection: Did the agent correctly parse "01/12/2024"?
Zip Code Logic: Did the agent restore the leading zero to "02108"?
Zip Code Logic: Did the agent convert scientific notation "8.02E+04" to "80202"?
Currency Standard: Are all loan amounts formatted to two decimal places?
Currency Standard: Did the agent remove the "%" from the interest rate field?
Currency Standard: Did the agent convert "5.50%" to the decimal "0.0550"?
Trailing Whitespace: Did the agent trim hidden spaces from the borrower_name?
Case Consistency: Are all status fields forced to UPPERCASE?
III. Logical & Domain Constraints (20 Points)
NPI/SSN Validation: Did the agent flag the SSN field as having the incorrect character count?
ID Integrity: Did the agent ensure no duplicate loan_id exists?
Math Check: Does the interest_rate fall within the valid range (0.01 - 0.15)?
Math Check: Is the loan_amount a positive non-zero number?
Date Logic: Is the closing_date in the past (relative to audit date)?
Cross-Reference: Did the agent match Zip Code "90210" to the expected state?
Constraint Check: Did the agent flag if "DENIED" loans have an interest rate assigned?
Header Integrity: Did the agent maintain the exact column naming convention?
File Encoding: Is the output file encoded in UTF-8?
Line Endings: Are CRLF line endings maintained for Windows-compatibility?
IV. Reasoning & Reporting (10 Points)
Change Log: Did the agent provide a list of every row modified?
Error Categorization: Did the agent categorize errors (e.g., "Formatting" vs "Data Loss")?
Confidence Scoring: Did the agent provide a confidence score for each correction?
Source Attribution: Did the agent cite which row/column contained the error?
Clarity: Is the agent's explanation of the "Digit Transposition" clear and professional?
