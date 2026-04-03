================================================================================
🛡️ SafeRoute Chicago — AI-Powered Navigation with SOS Alerting
================================================================================

SafeRoute AI is a specialized navigation engine for Chicago that uses 
Machine Learning to calculate the safest driving path. It features an 
integrated Twilio SOS Emergency System to provide real-time location 
sharing during travel.

---
📋 TABLE OF CONTENTS
---
1. New Feature: SOS Emergency Alerting
2. What This App Does
3. Project Structure
4. Step-by-Step Setup
5. Twilio Configuration
6. Tech Stack
7. Troubleshooting

---
🚨 1. NEW FEATURE: SOS EMERGENCY ALERTING
---
The system now includes a critical safety layer for drivers:
- Real-time GPS Tracking: Uses the browser's Geolocation API.
- One-Touch SMS: Sends an automated emergency message via Twilio API.
- Smart Context: SMS includes current location, destination, and Maps link.
- Visual & Audio Feedback: Pulsing SOS button and audio alert confirmation.

---
🔍 2. WHAT THIS APP DOES
---
- Geocoding: Converts names (e.g., "Pilsen") into GPS coordinates.
- Multi-Route Analysis: Fetches 3 driving routes via OpenRouteService.
- Risk Scoring: RandomForest ML Model analyzes 30+ points along every route.
- Interactive Results:
    * Green Path: The AI-recommended safest route.
    * Crime Heatmap: Visual overlay of high-risk zones.
    * Risk Legend: Safety percentage breakdown for every path.

---
📂 3. PROJECT STRUCTURE
---
edilproject/
│
├── main.py                <-- FastAPI server (with Twilio SOS logic)
├── train_model.py         <-- ML training script (run once)
├── crime_model.pkl        <-- Generated ML Model
├── crime_data.pkl         <-- Generated Heatmap data
├── requirements.txt       <-- Python Dependencies
│
├── templates/
│   ├── index.html         <-- Home input form
│   └── map.html           <-- Interactive map + SOS Dashboard
│
└── static/                <-- CSS/JS assets

---
💻 4. STEP-BY-STEP SETUP (WINDOWS)
---
1. Navigate to project folder: cd path/to/edilproject
2. Create Environment: python -m venv venv
3. Activate Environment: venv\Scripts\activate
4. Install Libraries: pip install -r requirements.txt
5. Train Model: python train_model.py
6. Start App: uvicorn main:app --reload

---
📲 5. TWILIO CONFIGURATION (REQUIRED)
---
Configure your credentials in main.py:

TWILIO_SID    = "your_sid_here"
TWILIO_TOKEN  = "your_token_here"
TWILIO_FROM   = "+1234567890"   # Your Twilio Number
SOS_CONTACT   = "+91XXXXXXXXXX"  # Your Emergency Contact

Note: Trial accounts must verify the SOS_CONTACT number in the Twilio Console.

---
🛠 6. TECH STACK
---
- Backend: FastAPI (Python)
- Emergency API: Twilio SMS API
- Mapping: Folium / Leaflet.js
- Routing: OpenRouteService API
- ML Engine: Scikit-Learn (Random Forest)
- Frontend: Jinja2, Rajdhani & Space Mono Fonts

---
⚠️ 7. TROUBLESHOOTING
---
- "Fetching Location..." hangs: Grant Location Permissions in your browser.
- SMS Not Received: Check Twilio logs; ensure contact is a "Verified Caller ID".
- Coordinates Invalid: Access requires 'localhost' or a secure 'https' connection.

================================================================================
SafeRoute AI · Demo System · Chicago Crime Dataset · OpenRouteService
================================================================================
