import pandas as pd

# Create a sample DataFrame
data = {'A': [1, 2, 3],
        'B': [4, 5, 6],
        'C': [7, 8, 9]}

df = pd.DataFrame(data)

# Define a function to make a cell bold
def make_bold(val):
    return 'font-weight: bold'

# Apply the styling to a specific cell
styled_df = df.style.map(lambda x: make_bold(x) if x == 5 else '')

# Display the styled DataFrame
styled_df.to_excel("test_panda.xlsx", index = False, header = True)