import streamlit as st
from PIL import Image
import pytesseract
import re
import sqlite3
import pandas as pd
import plotly.express as px

# Tesseract Path
pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)

# Database Connection
conn = sqlite3.connect(
    "expenses.db",
    check_same_thread=False
)

cursor = conn.cursor()

# Create Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS expenses(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    merchant TEXT,
    amount REAL,
    date TEXT,
    category TEXT
)
""")

conn.commit()

# Categorization Function
def categorize(text):

    text = text.lower()

    if (
        "domino" in text
        or "pizza" in text
    ):
        return "Food"

    elif (
        "uber" in text
        or "ola" in text
        or "taxi" in text
    ):
        return "Travel"

    elif "amazon" in text:
        return "Shopping"

    else:
        return "Others"

# Title
st.title("Intelligent Expense Categorizer")

# Upload Receipt
uploaded_file = st.file_uploader(
    "Upload Receipt",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:

    # Open Image
    image = Image.open(uploaded_file)

    st.image(image, width=300)

    # Convert Image to Grayscale
    gray_image = image.convert("L")

    # OCR Configuration
    custom_config = r'--oem 3 --psm 11'

    # OCR Text
    text = pytesseract.image_to_string(
        gray_image,
        config=custom_config
    )

    # Show OCR Text
    st.subheader("Extracted Text")

    st.text(text)

    # Split Lines
    lines = text.split("\n")

    # Merchant Detection
    merchant = "Unknown"

    for line in lines:

        line = line.strip()

        if (
            line != ""
            and "amount" not in line.lower()
            and "date" not in line.lower()
            and len(line) < 20
        ):

            merchant = line
            break

    # Amount Detection
    amount_match = re.search(
        r'\d+\.\d{2}',
        text
    )

    if amount_match:

        amount = float(
            amount_match.group()
        )

    else:

        amount = 0

    # Date Detection
    date_match = re.search(
        r'\d{4}-\d{2}-\d{2}',
        text
    )

    if date_match:

        date = date_match.group()

    else:

        date = "Unknown"

    # Category Detection
    category = categorize(text)

    # Expense Details
    st.subheader("Expense Details")

    # Editable Fields

    merchant = st.text_input(
        "Merchant",
        merchant
    )

    amount = st.number_input(
        "Amount",
        value=float(amount)
    )

    date = st.text_input(
        "Date",
        date
    )

    category = st.selectbox(
        "Category",
        [
            "Food",
            "Travel",
            "Shopping",
            "Others"
        ],
        index=[
            "Food",
            "Travel",
            "Shopping",
            "Others"
        ].index(category)
    )

    # Save Expense
    if st.button("Save Expense"):

        cursor.execute("""
        INSERT INTO expenses
        (merchant, amount, date, category)
        VALUES (?, ?, ?, ?)
        """, (
            merchant,
            amount,
            date,
            category
        ))

        conn.commit()

        st.success("Expense Saved Successfully")

# Dashboard
st.header("Dashboard")

cursor.execute(
    "SELECT * FROM expenses"
)

data = cursor.fetchall()

if len(data) > 0:

    df = pd.DataFrame(
        data,
        columns=[
            "ID",
            "Merchant",
            "Amount",
            "Date",
            "Category"
        ]
    )

    # Show Table
    st.dataframe(df)

    # Category Summary
    summary = (
        df.groupby("Category")["Amount"]
        .sum()
        .reset_index()
    )

    # Pie Chart
    fig = px.pie(
        summary,
        names="Category",
        values="Amount",
        title="Expenses by Category"
    )

    st.plotly_chart(fig)

    # Insight
    highest = summary.loc[
        summary["Amount"].idxmax()
    ]

    st.info(
        f"Highest spending category: "
        f"{highest['Category']} ₹{highest['Amount']}"
    )