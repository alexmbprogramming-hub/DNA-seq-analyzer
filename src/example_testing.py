from sequence import Sequence 
import streamlit as st

import pandas as pd

sequence_string = "actgactgactgactgactgactgactgactgactgactgactgactgactg"

sequence = Sequence("example", sequence_string)

print("Hello we are trying this thing")

print(sequence.full_data_list())

data = {
    "name": [sequence.name],
    "sequence": [sequence.sequence],
    "How many A": [sequence.how_many_A()],
    "How many T": [sequence.how_many_T()],
    "How many G": [sequence.how_many_G()],
    "How many C": [sequence.how_many_C()],
    "Percentage of Purines (A and T)": [sequence.percentage_purines()],
    "Percentage of Pirimidines (C and G)": [sequence.percentage_pirimidines()]
}

df = pd.DataFrame(data)
print(df)

st.title("This is an example of data")

st.subheader("We have the next sequence:")

st.dataframe(df)

st.write("The complementary sequence is the next one:")
st.write(sequence.complementary_string())
st.markdown("**A little reminder:** when a sequence has the complementary if this sequence goes 5' to 3' the other sequence goes 3' to 5' so when we get the complementary one we have to take into account that it is in the oposite direction")