import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Statistical Plots & Distribution Analysis")

# sample data
data = [10, 20, 20, 30, 30, 30, 40, 50, 60, 60, 70]
df = pd.DataFrame(data, columns=["Values"])

st.subheader("Data")
st.write(df)

# Histogram
st.subheader("Histogram")
fig1 = plt.figure()
plt.hist(df["Values"], bins=5)
st.pyplot(fig1)

# Boxplot
st.subheader("Box Plot")
fig2 = plt.figure()
sns.boxplot(x=df["Values"])
st.pyplot(fig2)

# Distribution curve
st.subheader("Distribution")
fig3 = plt.figure()
sns.histplot(df["Values"], kde=True)
st.pyplot(fig3)