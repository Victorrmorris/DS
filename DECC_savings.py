import streamlit as st
import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt

# App Configuration
st.set_page_config(page_title="DECC Savings Dashboard", layout="wide", initial_sidebar_state='expanded')

# Dummy Data
accounts = [
    {"name": "USAA Checking", "balance": 4500.13, "savings": 75},
    {"name": "Germany Checking", "balance": 233.81, "savings": 30},
    {"name": "Wise", "balance": 198.76, "savings": 60},
    {"name": "Greenlight (Kids)", "balance": 300.00, "savings": 25},
]

total_balance = sum(acc["balance"] for acc in accounts)
savings_per_month = sum(acc["savings"] for acc in accounts)
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

# Bar Chart for Savings Distribution
fig, ax = plt.subplots()
account_names = [acc["name"] for acc in accounts]
savings_values = [acc["savings"] for acc in accounts]
ax.bar(account_names, savings_values, color=["blue", "lightblue", "green", "lightgreen"])
ax.set_ylabel("Savings ($)")
ax.set_title("Automatic savings from all accounts")
st.pyplot(fig)

# Savings Insights
st.info(f"At this pace, you will save ${savings_per_year:,.2f} this year. Consider optimizing subscriptions and discretionary spending to boost savings.")

# AI Financial Assistant
st.subheader("AI Financial Assistant")
st.text_area("Ask me anything about your finances!")

# Automatic Savings Rule
st.subheader("Automatic Transfer Rule")
st.write(f"Your pooled savings of ${savings_per_month:,.2f} is automatically transferred to {high_yield_account} to maximize your returns.")

st.success(f"Your savings automation is active and running smoothly! Your projected yearly savings is ${savings_per_year:,.2f}.")
