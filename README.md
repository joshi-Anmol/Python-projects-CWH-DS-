# Coders of Bangalore – Instagram Data Analysis

## 📌 Problem Statement

You are given a raw text dump of Instagram profile data (followers of OpenAI).  
The data is **unstructured** and stored in a text file.

Your task is to process this raw data and answer the following questions:

1. Who has the **maximum number of posts**?
2. Who has the **maximum number of followers**?
3. Who **follows the maximum number of people**?
4. How many **categories of pages** exist (e.g., Digital Creator, Non-profit, etc.) and how many profiles fall under each?

This project focuses on **data cleaning, parsing unstructured text, and logical analysis using Python**.

---

---

## 🧠 Approach & Logic

### 1. Data Collection
- Raw Instagram data is read from `final_datadump.txt`.
- Each profile is separated by **two newline characters (`\n\n`)**.

### 2. Data Cleaning
- Empty or invalid chunks are removed.
- Numeric values like `K` and `M` are converted into integers.

### 3. Data Parsing
Each profile is parsed to extract:
- Username
- Number of posts
- Number of followers
- Number of following
- Page category

Each profile is stored as a **Python dictionary**.

---

## 🧾 Parsed Data Format

```json
{
  "user_name": "example_user",
  "no_of_post": 120,
  "no_of_followers": 45000,
  "no_of_following": 300,
  "type_of_page": "Digital Creator"
}



