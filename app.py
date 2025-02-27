import streamlit as st
import requests

# Set the title for your app
st.title("Currency Converter")

# User inputs
amount = st.number_input("Enter the amount:", value=1.0)
from_currency = st.selectbox("From Currency:", ["USD", "EUR", "GBP", "JPY", "INR" , "CAD" , "PKR"])
to_currency = st.selectbox("To Currency:", ["USD", "EUR", "GBP", "JPY", "INR" , "CAD" , "PKR" ])

# When the user clicks the Convert button
if st.button("Convert"):
    # Api key should be in the api_key variable in env file
    api_key = "8dafe8403db3f711747f4da9"
    
    url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}?apikey={api_key}"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Ensure we notice bad responses
        data = response.json()
        
        # Get the conversion rate for the target currency
        rate = data['rates'].get(to_currency)
        if rate:
            converted_amount = amount * rate
            st.success(f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}")
        else:
            st.error("Conversion rate not available for the selected currency.")
    except Exception as e:
        st.error("Error fetching exchange rates. Please try again later.")
        st.error(e)
