import streamlit as st
import pandas as pd
import numpy as np

# Mock data
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [24, 30, 22, 35],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}

df = pd.DataFrame(data)

# Title
st.title('Dashboard')

# Display the DataFrame
st.write('### Mock Data', df)

# Add a simple plot
st.line_chart(df['Age'])