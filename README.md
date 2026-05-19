# Intelligent Expense Categorizer using OCR

## Overview

Intelligent Expense Categorizer is a Python-based application that automates receipt scanning and expense tracking using OCR (Optical Character Recognition).

Users can upload receipt images, and the system automatically:

* Extracts text using Tesseract OCR
* Detects merchant name, amount, and date
* Categorizes expenses intelligently
* Stores records in SQLite database
* Displays expense analytics using charts and dashboards

---

# Features

* Receipt image upload
* OCR-based text extraction
* Automatic expense categorization
* SQLite database storage
* Interactive dashboard
* Pie chart visualization
* Expense insights

---

# Technologies Used

* Python
* Streamlit
* pytesseract
* Pillow
* SQLite
* Pandas
* Plotly

---

# Project Architecture

```text
Receipt Upload
      ↓
OCR Processing
      ↓
Text Extraction
      ↓
Expense Categorization
      ↓
SQLite Database Storage
      ↓
Dashboard Visualization
```

---

# Categorization Logic

The application uses keyword-based categorization.

## Food

* Domino
* Pizza
* Burger
* Zomato
* Swiggy

## Travel

* Uber
* Ola
* Taxi

## Shopping

* Amazon

If no keywords match, the expense is categorized as:

* Others

---

# Database Structure

Table: expenses

| Column   | Type    |
| -------- | ------- |
| id       | INTEGER |
| merchant | TEXT    |
| amount   | REAL    |
| date     | TEXT    |
| category | TEXT    |

---

# Installation

## 1. Clone Repository

```bash
git clone <repository-link>
```

---

## 2. Install Dependencies

```bash
pip install streamlit pytesseract pillow pandas plotly
```

---

## 3. Install Tesseract OCR

Download and install Tesseract OCR on Windows.

Default installation path:

```text
C:\Program Files\Tesseract-OCR\tesseract.exe
```

---

# Run the Application

```bash
streamlit run app.py
```

---

# How It Works

1. User uploads receipt image
2. OCR extracts text from receipt
3. System detects:

   * Merchant
   * Amount
   * Date
4. Expense is automatically categorized
5. Data is stored in SQLite database
6. Dashboard displays analytics and charts

---

# Dashboard Features

* Expense table
* Category-wise summary
* Pie chart visualization
* Highest spending category insight

---

# Future Enhancements

* AI-based categorization
* Multi-language OCR
* Monthly expense reports
* User authentication
* Cloud database integration

---

# Conclusion

This project demonstrates how OCR and intelligent categorization can simplify expense tracking and automate receipt management using lightweight Python technologies.
