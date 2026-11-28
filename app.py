# import streamlit as st
# import requests

# st.set_page_config(page_title="Wine Quality Prediction")

# st.title("🍷 Wine Quality Prediction")

# fixed_acidity = st.number_input("Fixed Acidity", value=7.4)
# volatile_acidity = st.number_input("Volatile Acidity", value=0.7)
# citric_acid = st.number_input("Citric Acid", value=0.0)
# residual_sugar = st.number_input("Residual Sugar", value=1.9)
# chlorides = st.number_input("Chlorides", value=0.076)
# free_sulfur_dioxide = st.number_input("Free Sulfur Dioxide", value=11.0)
# total_sulfur_dioxide = st.number_input("Total Sulfur Dioxide", value=34.0)
# density = st.number_input("Density", value=0.9978)
# pH = st.number_input("pH", value=3.51)
# sulphates = st.number_input("Sulphates", value=0.56)
# alcohol = st.number_input("Alcohol", value=9.4)

# if st.button("Predict"):

#     payload = {
#         "fixed_acidity": fixed_acidity,
#         "volatile_acidity": volatile_acidity,
#         "citric_acid": citric_acid,
#         "residual_sugar": residual_sugar,
#         "chlorides": chlorides,
#         "free_sulfur_dioxide": free_sulfur_dioxide,
#         "total_sulfur_dioxide": total_sulfur_dioxide,
#         "density": density,
#         "pH": pH,
#         "sulphates": sulphates,
#         "alcohol": alcohol
#     }

#     response = requests.post(
#         "http://127.0.0.1:8000/predict",
#         json=payload
#     )

#     if response.status_code == 200:
#         prediction = response.json()["prediction"]
#         st.success(f"Predicted Quality: {prediction}")
#     else:
#         st.error("Prediction failed")





import streamlit as st
import requests

# Page configuration
st.set_page_config(
    page_title="Wine Quality Predictor",
    page_icon="🍷",
    layout="centered"
)

# Custom styling
st.markdown("""
<style>
.stApp {
    background-color: #160D12;
    color: white;
}

h1 {
    color: #E8B4C0 !important;
    text-align: center;
}

.subtitle {
    text-align: center;
    color: #BFAAB1;
    margin-bottom: 30px;
}

.stButton button {
    background-color: #922F50;
    color: white;
    border-radius: 10px;
    width: 100%;
    height: 45px;
    font-weight: bold;
}

.stButton button:hover {
    background-color: #B74768;
    color: white;
}

div[data-testid="stNumberInput"] input {
    background-color: #281A22;
    color: white;
}
</style>
""", unsafe_allow_html=True)


# Header
st.title("🍷 Wine Quality Predictor")

st.markdown(
    '<p class="subtitle">AI-powered wine quality prediction</p>',
    unsafe_allow_html=True
)

st.divider()

# Input fields
st.subheader("Enter Wine Properties")

col1, col2 = st.columns(2)

with col1:
    fixed_acidity = st.number_input("Fixed Acidity", value=7.4)
    volatile_acidity = st.number_input("Volatile Acidity", value=0.7)
    citric_acid = st.number_input("Citric Acid", value=0.0)
    residual_sugar = st.number_input("Residual Sugar", value=1.9)
    chlorides = st.number_input("Chlorides", value=0.076)
    free_sulfur_dioxide = st.number_input(
        "Free Sulfur Dioxide", value=11.0
    )

with col2:
    total_sulfur_dioxide = st.number_input(
        "Total Sulfur Dioxide", value=34.0
    )
    density = st.number_input("Density", value=0.9978)
    pH = st.number_input("pH", value=3.51)
    sulphates = st.number_input("Sulphates", value=0.56)
    alcohol = st.number_input("Alcohol", value=9.4)

st.divider()

# Prediction
if st.button("🔍 Predict Wine Quality"):

    if free_sulfur_dioxide > total_sulfur_dioxide:
        st.warning("Free sulfur dioxide cannot exceed total sulfur dioxide.")

    else:
        payload = {
            "fixed_acidity": fixed_acidity,
            "volatile_acidity": volatile_acidity,
            "citric_acid": citric_acid,
            "residual_sugar": residual_sugar,
            "chlorides": chlorides,
            "free_sulfur_dioxide": free_sulfur_dioxide,
            "total_sulfur_dioxide": total_sulfur_dioxide,
            "density": density,
            "pH": pH,
            "sulphates": sulphates,
            "alcohol": alcohol
        }

        try:
            with st.spinner("Predicting wine quality..."):
                response = requests.post(
                    "http://127.0.0.1:8000/predict",
                    json=payload,
                    timeout=15
                )

            if response.status_code == 200:
                prediction = response.json()["prediction"]

                st.success("Prediction Completed!")

                st.markdown(
                    f"""
                    <div style="
                        background: #281A22;
                        padding: 25px;
                        border-radius: 15px;
                        text-align: center;
                        border: 1px solid #922F50;
                    ">
                        <h3 style="color: #E8B4C0;">
                            Predicted Wine Quality
                        </h3>
                        <h1 style="color: #E8B4C0; font-size: 55px;">
                            {prediction}
                        </h1>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            else:
                st.error("Prediction failed. Check your API.")

        except requests.exceptions.ConnectionError:
            st.error("Cannot connect to the backend. Start your FastAPI server.")

        except requests.exceptions.RequestException as e:
            st.error(f"Request error: {e}")

        except (ValueError, KeyError):
            st.error("Invalid response received from the API.")

# Footer
st.markdown("---")
st.caption("🍷 Wine Quality Predictor | Powered by Machine Learning")
