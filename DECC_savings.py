import streamlit as st
import pandas as pd
import numpy as np
import random

# App Configuration
st.set_page_config(page_title="DECC Savings Dashboard", layout="wide", initial_sidebar_state='expanded')

# Dummy Data
accounts = [
    {"name": "USAA Checking", "balance": 4500.13},
    {"name": "AMEX Savings", "balance": 20348.05},
    {"name": "Germany Checking", "balance": 233.81},
    {"name": "Wise", "balance": 198.76},
    {"name": "Greenlight (Kids)", "balance": 300.00},
]

total_balance = sum(acc["balance"] for acc in accounts)

# Round-up Savings Calculation
transactions = [random.uniform(1.50, 98.99) for _ in range(50)]  # Simulated transactions
round_up_savings = sum([np.ceil(t) - t for t in transactions])
savings_per_month = round_up_savings + random.uniform(50, 100)
savings_per_year = savings_per_month * 12

# Auto-transfer pooled savings
high_yield_account = "AMEX Savings"

# Sidebar Navigation
st.sidebar.title("DECC Navigation")
st.sidebar.header("Accounts & Insights")
st.sidebar.write("- Home")
st.sidebar.write("- Linked Accounts")
st.sidebar.write("- Automated Savings")
st.sidebar.write("- Transactions")

st.sidebar.header("Tools")
st.sidebar.write("- Currency Converter")
st.sidebar.write("- Subscription Manager")
st.sidebar.write("- Budget Manager")
st.sidebar.write("- Credit Builder")
st.sidebar.write("- AI Assistant")

# Main Content
st.title("DECC Financial Overview")

# Account Balance Section
st.subheader("All Accounts Balance")
st.metric("Total Balance", f"${total_balance:,.2f}")

# Savings Section
st.subheader("All Accounts Automatic Savings")
st.metric("Monthly Savings", f"${savings_per_month:,.2f}")
st.metric("Yearly Savings Estimate", f"${savings_per_year:,.2f}")

# Savings Insights
st.info(f"At this pace, you will save ${savings_per_year:,.2f} this year. Consider optimizing subscriptions and discretionary spending to boost savings.")

# AI Financial Assistant
st.subheader("AI Financial Assistant")
st.text_area("Ask me anything about your finances!")

# Automatic Savings Rule
st.subheader("Automatic Transfer Rule")
st.write(f"Your pooled savings of ${savings_per_month:,.2f} is automatically transferred to {high_yield_account} to maximize your returns.")

st.success(f"Your savings automation is active and running smoothly! Your projected yearly savings is ${savings_per_year:,.2f}.")
