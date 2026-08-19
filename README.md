# AI Agent Evaluation Benchmark: High-Stakes Data Curation & Validation

## 📌 Project Overview
This repository serves as a professional-grade benchmark for evaluating the accuracy, reasoning, and reconciliation capabilities of frontier AI agents. 

In high-stakes, audit-sensitive environments—such as financial services and healthcare—AI systems often struggle with "silent errors" like digit transpositions and data truncations. This project provides a structured framework to test if an AI can detect, flag, and correct these errors against a defined "Ground Truth" dataset.

## 🎯 Role-Specific Objectives (micro1)
This project was designed to meet the rigorous standards of a **Data Entry Keyer** and **AI Data Trainer**, specifically focusing on:
- **Accuracy Discipline:** Zero-tolerance approach to data discrepancies.
- **Error Detection:** Identifying complex malformed records, including silent truncations.
- **Format Reconciliation:** Standardizing disparate data types (dates, currency, zip codes) into audit-ready formats.
- **Rubric Authoring:** A comprehensive 35+ criteria evaluation framework for AI output assessment.

## 📂 Repository Structure
- **`/data/ground_truth/`**: The "Gold Standard" dataset—exactly how the data should look after perfect processing.
- **`/data/corrupted_tasks/`**: The "Dirty" dataset—contains intentional, high-difficulty errors (transpositions, format inconsistencies, and truncations) designed to challenge AI models.
- **`/scripts/`**: A Python-based automation script used to programmatically generate benchmarks and inject specific error types.
- **`/rubrics/`**: The core evaluation document containing over 35 specific grading criteria to measure AI performance.

## 🛠 Technical Workflow
1. **Data Curation:** Designed a synthetic Mortgage Audit dataset mimicking real-world regulated environments.
2. **Error Engineering:** Used Python (Pandas) to inject "Silent Truncations" (names cut off mid-string) and "Digit Transpositions" (swapping numbers in currency fields), which are traditionally difficult for LLMs to detect.
3. **Reconciliation Logic:** Defined strict standards for ISO 8601 date compliance and currency normalization.
4. **Evaluation:** Authored a 35-point grading rubric that scores an AI agent not just on its final output, but on its **reasoning** and **transparency** in reporting changes.

## 📋 Evaluation Criteria Examples
The included rubric assesses AI agents on:
- **Detection of Silent Truncation:** Identifying if "Nathaniel Richardson" was incorrectly keyed as "Nathaniel Richar".
- **Currency Integrity:** Flagging a $45,000 variance caused by a digit swap ($450,250 vs $405,250).
- **Format Normalization:** Converting `15-Jan-24` and `01/12/2024` into a unified `YYYY-MM-DD` format.
- **Scientific Notation Recovery:** Correcting zip codes that were corrupted into scientific notation (e.g., `8.02E+04`).

## 🚀 About the Author
I am a Data Validation and AI Training specialist focused on building the human intelligence layer for frontier AI. I specialize in creating complex evaluation tasks that ensure AI agents perform with the precision required for audit-sensitive industries.

---
*This project is part of a portfolio to showcase my abilities.*
