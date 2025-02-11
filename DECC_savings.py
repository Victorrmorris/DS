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
savings_per_month = 194.49
savings_per_year = 194.49 * 12

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
st.markdown("[What if I change to nearest $5 round-up and transfer that total each month to a HYSA with 3.80% APY?](#)", unsafe_allow_html=True)
user_query = st.text_area("Ask me anything about your finances!")

if user_query:
    if "nearest $5 round-up" in user_query.lower() or "3.80% APY" in user_query.lower():
        new_savings_per_month = 250.00  # Dummy new savings amount with $5 round-up
        new_savings_per_year = new_savings_per_month * 12
        apy = 0.038
        estimated_interest = new_savings_per_year * apy
        total_with_interest = new_savings_per_year + estimated_interest

        st.write("### Adjusted Round-Up Savings Calculation")
        st.write(f"If you switch to rounding up to the nearest $5 and deposit monthly into a 3.80% APY savings account, your new estimated monthly savings would be ${new_savings_per_month:,.2f}.")
        st.write(f"This would total ${new_savings_per_year:,.2f} annually before interest.")
        st.write(f"With a 3.80% APY, your estimated total savings including interest after one year would be approximately ${total_with_interest:,.2f}.")
    elif "round-up" in user_query.lower() or "transfer rule" in user_query.lower():
        st.write("### Automatic Transfer Rule")
        st.write("If you round up $150.00 or more per month, it gets automatically transferred to AMEX high-yield savings.")
        st.write("Based on your current savings of $194.49 per month, you are on track to transfer your savings efficiently.")
    else:
        st.write("I'm here to help! Try asking about your savings, transfer rules, or financial insights.")

# Automatic Savings Rule
st.subheader("Automatic Transfer Rule")
st.write(f"Your pooled savings of ${savings_per_month:,.2f} is automatically transferred to {high_yield_account} to maximize your returns.")

st.success(f"Your savings automation is active and running smoothly! Your projected yearly savings is ${savings_per_year:,.2f}.")
