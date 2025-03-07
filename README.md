📌 README.md for Wildfire Weather Dashboard
md
Copy
Edit
# 🔥 Wildfire Weather Dashboard  

### **Real-time wildfire weather analysis & risk assessment powered by Python, Streamlit, and Power BI**  

![Dashboard Screenshot](assets/dashboard_screenshot.png)  

## 📌 Overview  
The **Wildfire Weather Dashboard** is a **real-time data analytics** tool that helps **monitor wildfire risks** using live weather data, Fire Weather Index (FWI) calculations, and interactive visualizations. It integrates **Streamlit for live updates** and **Power BI for advanced analytics**.

## 🚀 Features  
✅ **Fetch live weather data** (temperature, humidity, wind speed, precipitation)  
✅ **Automated Fire Weather Index (FWI) calculation**  
✅ **Interactive dashboard with Streamlit** (real-time updates)  
✅ **Power BI integration** (geospatial heatmaps & wildfire risk visualization)  
✅ **Daily automated updates via GitHub Actions**  

---

## 📂 Project Structure  

wildfire_weather_dashboard/ │── data/
│ ├── raw/ # Unprocessed weather data │ ├── processed/ # Cleaned and formatted data │ ├── fwi_calculations/ # Fire Weather Index results │── scripts/
│ ├── fetch_weather.py # Fetch real-time weather data │ ├── process_data.py # Clean and preprocess data │ ├── fwi_calculator.py # Compute Fire Weather Index │── app/
│ ├── dashboard.py # Main Streamlit dashboard │ ├── assets/ # Images, logos, icons for UI │── powerbi/
│ ├── wildfire_dashboard.pbix # Power BI report file │── logs/ # Log files for debugging │── .github/workflows/
│ ├── update_data.yml # GitHub Actions for automation │── config.toml # Streamlit UI customization │── requirements.txt # Python dependencies │── README.md # Project documentation │── .gitignore # Ignore unnecessary files

yaml
Copy
Edit

---

## 📥 Installation & Setup  

### **🔹 Prerequisites**  
Ensure you have installed:  
- **Python 3.9+**  
- **Power BI Desktop**  
- **VS Code (Optional, for editing)**  

### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/yourusername/wildfire_weather_dashboard.git
cd wildfire_weather_dashboard
2️⃣ Create & Activate Virtual Environment
bash
Copy
Edit
python -m venv venv
source venv/Scripts/activate  # On Windows
# source venv/bin/activate  # On Mac/Linux
3️⃣ Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
4️⃣ Run the Streamlit Dashboard
bash
Copy
Edit
streamlit run app/dashboard.py
✅ Now your dashboard will open in your browser!

⚙️ How It Works
1️⃣ Fetch Real-Time Weather Data
The fetch_weather.py script retrieves wildfire-relevant weather data from Open-Meteo API:

python
Copy
Edit
response = requests.get("https://api.open-meteo.com/v1/forecast", params={ ... })
df.to_csv("data/raw/weather_data.csv", index=False)
2️⃣ Clean & Process Data
The process_data.py script formats and renames the data for easier analysis.

python
Copy
Edit
df.rename(columns={"temperature_2m": "Temperature (°C)", ...}, inplace=True)
3️⃣ Calculate Fire Weather Index (FWI)
The fwi_calculator.py script computes the Fire Weather Index:

python
Copy
Edit
df['FWI'] = (df['Temperature (°C)'] * 0.3) + (df['Wind Speed (km/h)'] * 0.2) - (df['Humidity (%)'] * 0.1) + (df['Precipitation (mm)'] * 0.05)
✅ The results are saved in data/fwi_calculations/fwi_results.csv.

4️⃣ Display Interactive Dashboard (Streamlit)
The dashboard visualizes real-time weather trends and FWI scores:

python
Copy
Edit
fig1 = px.line(df_fwi_filtered, x="time", y=["Temperature (°C)", "Wind Speed (km/h)"])
st.plotly_chart(fig1)
5️⃣ Power BI Integration
The dashboard embeds Power BI analytics:

python
Copy
Edit
st.markdown(
    f'<iframe width="1000" height="600" src="{POWER_BI_EMBED_URL}" frameborder="0" allowFullScreen="true"></iframe>',
    unsafe_allow_html=True
)
📊 Power BI provides heatmaps, FWI trends, and geospatial insights!

🚀 Deployment
🔹 Deploy on Streamlit Cloud
Push your repository to GitHub
bash
Copy
Edit
git add .
git commit -m "Deploying dashboard"
git push origin main
Go to Streamlit Cloud
Click "New App" → Select your GitHub Repo
Set Main File Path to:
bash
Copy
Edit
app/dashboard.py
Click "Deploy" 🚀
✅ Your dashboard is now live!

🔄 Automate Data Updates (GitHub Actions)
To keep the data updated daily, GitHub Actions runs the fetch_weather.py script every night.

GitHub Actions Workflow (update_data.yml)
yaml
Copy
Edit
name: Update Data Daily
on:
  schedule:
    - cron: '0 0 * * *'  # Runs daily at midnight

jobs:
  update-data:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repository
        uses: actions/checkout@v2
      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.9'
      - name: Install dependencies
        run: pip install -r requirements.txt
      - name: Run Data Fetch Script
        run: python scripts/fetch_weather.py
      - name: Commit and Push Changes
        run: |
          git add data/raw/weather_data.csv
          git commit -m "Auto-update weather data"
          git push
✅ Your dataset now updates daily without manual intervention!

📜 License
This project is open-source under the MIT License.

🤝 Contributing
Want to improve this project? 🚀

✅ Fork this repository
✅ Create a feature branch (git checkout -b feature-new)
✅ Push your changes & submit a PR