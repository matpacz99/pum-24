import streamlit as st
import pandas as pd
import pickle
import Featurizer
st.title('☆Solubility predictor☆')

st.write("This app takes a SMILES string and returns it's predicted solubility")

with open('variables.pkl', 'rb') as file:
    featurizer_class = pickle.load(file)
    svr = pickle.load(file)

smiles = st.text_input('Enter SMILES', '')

# add a button
if st.button('START'): # this executes when the button is clicked

    if not smiles:
        st.write('Enter SMILES')
        st.stop()
        
    X = featurizer_class.featurize(smiles)
    sol_pred = svr.predict(X)
    st.write("The predicted solubility is {}".format(sol_pred))
