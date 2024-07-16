import streamlit as st
import pandas as pd
import requests
st.sidebar.title("APPS")
st.title("Agri-link Software")
b = st.sidebar.button("Price Manager")
c = st.sidebar.button("Farm Manager")
d = st.sidebar.button("Weather")
e = st.sidebar.button('Back to Home Screen')

st.markdown("""
    <style>
        h1 {
            font-size: 40px
        }
    </style>
""", unsafe_allow_html=True)
def home():

    st.write("Imagine a comprehensive website designed to empower agricultural professionals with a suite of essential tools. This platform integrates apps tailored specifically for livestock managers, offering functionalities such as real-time health monitoring, feeding schedules, and breeding insights. For farm managers, the site provides tools for crop rotation planning, equipment maintenance scheduling, and yield forecasting. Additionally, there's a price observer app that tracks market trends, helping users make informed decisions on buying and selling agricultural products. The weather assistant app offers localized forecasts, alerts for severe weather conditions, and recommendations for optimal planting and harvesting times. Together, these apps form a unified digital ecosystem that enhances efficiency, productivity, and decision-making across various aspects of agricultural management.")
    
    st.subheader("Livestock Management")
    st.write(
        "A livestock manager app is a digital tool tailored for professionals involved in animal husbandry. It provides essential features such as real-time health monitoring, tracking of feeding schedules, and management of breeding cycles. This app helps livestock managers ensure the well-being of their animals by enabling them to monitor parameters like weight, vaccination schedules, and reproductive health. Additionally, it may offer insights into optimal nutrition and environmental conditions, thereby enhancing productivity and welfare in livestock operations.")
    st.subheader("Farm Management")
    st.write(
        "A farm manager app serves as a comprehensive digital assistant for agricultural professionals overseeing farm operations. It includes functionalities such as crop rotation planning, inventory management for seeds and fertilizers, equipment maintenance scheduling, and workforce management. This tool aids farm managers in optimizing resources, improving efficiency, and maximizing yields. It may also provide analytics and reports on crop health, soil conditions, and yield forecasts, empowering managers to make informed decisions for sustainable farming practices.")
    st.subheader("Weather Assistant")
    st.write(
        "A weather assistant app is a crucial tool for agricultural decision-making, providing localized weather forecasts, alerts for severe weather events, and climate data analysis. It helps agricultural professionals plan planting and harvesting schedules, irrigation timings, and pest management strategies based on weather patterns. The app may also offer historical weather data, long-term climate predictions, and agronomic recommendations tailored to specific geographic locations. By leveraging accurate weather information, the weather assistant app enables users to mitigate risks, optimize resource use, and enhance overall farm productivity and resilience to weather-related challenges.")

    st.subheader("Price Observer")
    st.write(
        "A price observer app is designed for agricultural professionals and traders to monitor market trends and prices of agricultural commodities. It provides real-time updates on commodity prices, historical data analysis, and price forecasts. This tool enables users to track market fluctuations, identify price trends, and make informed decisions on buying and selling agricultural products. By offering insights into market dynamics and competitor pricing, the price observer app helps users optimize their procurement and sales strategies to maximize profitability.")
def ad():
    farm_data = {
        'Farm Name': ['Farm A', 'Farm B', 'Farm C'],
        'Location': ['Location A', 'Location B', 'Location C'],
        'Crop': ['Wheat', 'Corn', 'Soybean'],
        'Livestock': ['Cattle', 'Pigs', 'Chickens'],
        'Area (acres)': [100, 200, 150]
    }

    df = pd.DataFrame(farm_data)

    def main():
        st.title('Farm Management App')

    # Sidebar with options
        st.sidebar.title('Menu')
        page = st.sidebar.radio('Select a page', ['Home', 'Crop Management', 'Livestock Tracking',  'Tasks'])

        if page == 'Home':
            st.subheader('Farm Overview')
            st.write(df)  # Display farm data

        elif page == 'Crop Management':
            st.subheader('Crop Management')
            st.write('Select a crop to manage:')

            selected_crop = st.selectbox('Select Crop', df['Crop'].unique())
            crop_info = df[df['Crop'] == selected_crop].iloc[0]

            st.write(f"**Crop Name:** {crop_info['Crop']}")
            st.write(f"**Farm Name:** {crop_info['Farm Name']}")
            st.write(f"**Location:** {crop_info['Location']}")
            st.write(f"**Area (acres):** {crop_info['Area (acres)']}")

        elif page == 'Livestock Tracking':
            st.subheader('Livestock Tracking')
            st.write('Select a livestock to track:')

            selected_livestock = st.selectbox('Select Livestock', df['Livestock'].unique())
            livestock_info = df[df['Livestock'] == selected_livestock].iloc[0]

            st.write(f"**Livestock Type:** {livestock_info['Livestock']}")
            st.write(f"**Farm Name:** {livestock_info['Farm Name']}")
            st.write(f"**Location:** {livestock_info['Location']}")
            st.write(f"**Area (acres):** {livestock_info['Area (acres)']}")


        elif page == 'Tasks':
            st.subheader('Task Management')
            st.write('Manage your farm tasks here.')

            task = st.text_area('Enter a new task')
            if st.button('Add Task'):
                st.write(f'New task added: {task}')
    
    if __name__ == "__main__":
        main()
def da():
    def get_city(state):
        state_to_city = {
            "Andhra Pradesh": "Visakhapatnam",
            "Tamil Nadu": "Chennai",
            "Kerala": "Thiruvananthapuram",
            "Karnataka": "Bangalore",
        }
        return state_to_city.get(state, state)
    def get_weather(city, api_key):
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=imperial"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            weather_description = data['weather'][0]['description']
            temperature_fahrenheit = data['main']['temp']
            temperature_celsius = int((temperature_fahrenheit - 32) * 0.5555555)
            weather_info = f"The weather in {city} is currently {weather_description} with a temperature of {temperature_celsius}°C."
            return weather_info, temperature_celsius
        else:
            return "Sorry, I couldn't get the weather information. Please try again later.", None

    def get_crop_recommendation(month, terrain, temperature_celsius):
        month = month.lower()
        terrain = terrain.lower()
        if month in ["march", "april"] and terrain in ["plain", "plateau"]:
            return "The conditions are suitable for planting zaid crops."
        elif month in ["october", "december"]:
            if terrain == "plain" and 25 < temperature_celsius < 30:
                return "The conditions are suitable for successfully planting rabi crops."
            elif terrain == "plateau" and 25 < temperature_celsius < 30:
                return "You can plant rabi crops, but you should take extremely good care."
            elif terrain == "mountain" and 25 < temperature_celsius < 30:
                return "It is going to be very hard to farm."
            else:
                return "The conditions are not suitable for planting rabi crops."
        elif month in ["september", "october"]:
            if terrain == "plain" and 20 < temperature_celsius < 25:
                return "The conditions are suitable for successfully planting kharif crops, and the plain terrain makes it easier."
            elif terrain == "plateau" and 20 < temperature_celsius < 25:
                return "You can plant kharif crops, but it would take effort."
            elif terrain == "mountain" and 20 < temperature_celsius < 25:
                return "The conditions are good for planting kharif crops, but it is going to be very hard to farm."
            else:
                return "The conditions are not suitable for planting kharif crops."
        else:
            return "The current month is not suitable for planting either rabi or kharif crops based on the given conditions."

    def main():
        st.title("Crop Recommendation Based on Weather and Terrain")
    
        st.write("Enter the details below to get crop recommendations based on the weather and terrain conditions.")

        state = st.selectbox("Select your state:", ["Andhra Pradesh", "Tamil Nadu", "Kerala", "Karnataka"])
        terrain = st.selectbox("Select your terrain:", ["Plain", "Plateau", "Mountain"])
        month = st.selectbox("Select the month:", ["March", "April", "September", "October", "November", "December"])
    
        if st.button("Get Recommendation"):
            api_key = "5cfb38f8a25bdae00a1f5984e6644063"
            city = get_city(state)
            weather_info, temperature_celsius = get_weather(city, api_key)

            if temperature_celsius is not None:
                crop_info = get_crop_recommendation(month, terrain, temperature_celsius)
                st.success(f"Weather Info: {weather_info}")
                st.success(f"Crop Recommendation: {crop_info}")
            else:
                st.error("Could not retrieve weather information.")
    if _name_ == "_main_":
        main()
def dad():
    st.write('work in progress')
if 'page' not in st.session_state:
    st.session_state.page = 'home'
if c:
    st.session_state.page = 'farm'
if d:
    st.session_state.page = 'weather'
if b:
    st.session_state.page = 'price'

if st.session_state.page == 'home':
    home()
elif st.session_state.page == 'farm':
    ad()
elif st.session_state.page == 'weather':
    da()
elif st.session_state.page == 'price':
    dad()
if e:
        st.session_state.page = 'home'
        st.experimental_rerun()
if c:
    audio_file = open("da.wav", "rb")
    audio_bytes = audio_file.read()
    st.audio(audio_bytes, format="audio/wav")
