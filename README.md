# 🛡 SafeRoute Chicago — AI-Powered Crime-Aware Safe Route Navigation

A demo-ready web application that uses Machine Learning + real road routing
to suggest the **safest** (not just shortest) driving route across Chicago.

\---

## 📋 Table of Contents

1. [What This App Does](#what-this-app-does)
2. [Project Structure](#project-structure)
3. [Prerequisites](#prerequisites)
4. [Step-by-Step Setup — Windows](#step-by-step-setup--windows)
5. [Step-by-Step Setup — Mac / Linux](#step-by-step-setup--mac--linux)
6. [Running the App](#running-the-app)
7. [Using the App](#using-the-app)
8. [Troubleshooting](#troubleshooting)
9. [Tech Stack](#tech-stack)
10. [API Keys](#api-keys)
11. [Using Real Chicago Crime Data](#using-real-chicago-crime-data-optional)
12. [Making It Public](#making-it-public-sharing-with-others)

\---

## What This App Does

1. You type a **starting location** and **destination** (Chicago neighborhoods)
2. The app converts them to GPS coordinates using OpenStreetMap
3. It fetches **3 different real driving routes** using OpenRouteService API
4. A trained **RandomForest ML model** scores each route for crime risk
5. It picks the **safest route** (lowest risk score)
6. Displays an interactive map with:

   * Crime heatmap overlay
   * All 3 routes (faded alternatives + highlighted safest route)
   * Green start marker, red end marker
   * Risk analysis sidebar

\---

## Project Structure

```
edilproject/
│
├── main.py                ← FastAPI web server (run this)
├── train\_model.py         ← ML model training script (run once)
├── crime\_model.pkl        ← Trained ML model (auto-generated)
├── crime\_data.pkl         ← Heatmap data (auto-generated)
├── requirements.txt       ← Python dependencies
│
├── templates/
│   ├── index.html         ← Home page with input form
│   └── map.html           ← Results page with map
│
├── static/                ← Static files folder (reserved)
├── CODE\_EXPLANATION.txt   ← Full code documentation
└── README.md              ← This file
```

\---

## Prerequisites

Before you start, make sure you have:

### Python 3.10 or higher

Check your version:

```
python --version
```

or on Mac/Linux:

```
python3 --version
```

If not installed, download from: https://www.python.org/downloads/

> ⚠️ During Python installation on Windows, \*\*tick the checkbox\*\*
> "Add Python to PATH" — this is critical or nothing will work.

\---

## Step-by-Step Setup — Windows

### Step 1 — Open Command Prompt

Press `Win + R`, type `cmd`, press Enter.

\---

### Step 2 — Navigate to the project folder

You should see `main.py`, `train\_model.py`, `requirements.txt` listed.

\---

### Step 3 — Create a Virtual Environment

A virtual environment keeps this project's libraries isolated from
your other Python projects. Always use one.

```cmd
python -m venv venv
```
---

This creates a `venv/` folder inside your project directory.

\---

### Step 4 — Activate the Virtual Environment

```cmd
venv\\Scripts\\activate
```

Your prompt should now show `(venv)` at the start:

```
(venv) D:\\edilproject>
```

> ⚠️ IMPORTANT: You must run this activate command EVERY TIME you
> open a new terminal window before running the app. If you close
> the terminal and reopen it, activate again.

\---

### Step 5 — Upgrade pip

```cmd
python -m pip install --upgrade pip
```

\---

### Step 6 — Install All Dependencies

```cmd
pip install -r requirements.txt
```

This downloads and installs all required libraries. Takes 2–5 minutes.

You should see:

```
Successfully installed fastapi-0.111.0 uvicorn-0.29.0 folium-0.16.0 ...
```

\---

### Step 7 — Train the ML Model

Run this ONCE to generate the model files:

```cmd
python train\_model.py
```

Expected output:

```
=======================================================
  SafeRoute AI — Chicago Crime Model Trainer
=======================================================

Generating synthetic Chicago crime data …
  Dataset shape : (10000, 6)

Training RandomForest …
  MAE : 0.0835
  R²  : 0.6669
Saved → crime\_model.pkl
Saved → crime\_data.pkl  (3000 heatmap points)

Sanity predictions:
  Englewood - Saturday night               → risk = 0.986
  Loop area - Tuesday afternoon            → risk = 0.481
  Humboldt - Wednesday morning             → risk = 0.446

Done! Run:  uvicorn main:app --reload
```

\---

### Step 8 — Start the Web Server

```cmd
uvicorn main:app --reload
```

Expected output:

```
INFO:     Started server process \[12345]
INFO:     Waiting for application startup.
✅  crime\_model.pkl loaded
✅  crime\_data.pkl loaded (3000 points)
INFO:     Application startup complete.
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```

\---

### Step 9 — Open the App

Open your browser and visit:

```
http://localhost:8000
```

The SafeRoute Chicago app loads. You are done! 🎉

\---

## Step-by-Step Setup — Mac / Linux

### Step 1 — Open Terminal

Mac: Press `Cmd + Space`, type "Terminal", press Enter.
Linux: Press `Ctrl + Alt + T`.

\---

### Step 2 — Navigate to the project folder

```bash
cd /path/to/edilproject
```

Verify:

```bash
ls
```

You should see `main.py`, `train\_model.py`, `requirements.txt`.

\---

### Step 3 — Create a Virtual Environment

```bash
python3 -m venv venv
```

\---

### Step 4 — Activate the Virtual Environment

```bash
source venv/bin/activate
```

Your prompt shows `(venv)`:

```
(venv) user@machine:\~/edilproject$
```

\---

### Step 5 — Upgrade pip

```bash
pip install --upgrade pip
```

\---

### Step 6 — Install All Dependencies

```bash
pip install -r requirements.txt
```

\---

### Step 7 — Train the ML Model

```bash
python train\_model.py
```

\---

### Step 8 — Start the Web Server

```bash
uvicorn main:app --reload
```

\---

### Step 9 — Open the App

```
http://localhost:8000
```

\---

## Running the App

After the first-time setup, every time you want to use the app:

**Windows:**

```cmd
cd D:\\edilproject
venv\\Scripts\\activate
uvicorn main:app --reload
```

**Mac/Linux:**

```bash
cd /path/to/edilproject
source venv/bin/activate
uvicorn main:app --reload
```

Then open `http://localhost:8000`.

**To stop the server:** Press `Ctrl + C` in the terminal.

**To deactivate the venv when done:** Type `deactivate` and press Enter.

\---

## Using the App

1. Open `http://localhost:8000`
2. Type a **starting location** — examples:

   * `Pilsen`
   * `Loop`
   * `Lincoln Park`
   * `Hyde Park`
   * `Wicker Park`
3. Type a **destination** — examples:

   * `Ashburn`
   * `Englewood`
   * `Rogers Park`
   * `Humboldt Park`
4. Click **"⚡ FIND SAFEST ROUTE"**
5. Wait 3–8 seconds while the system:

   * Geocodes your locations to GPS coordinates
   * Fetches 3 driving routes from ORS API
   * Scores each route with the ML model
   * Renders the interactive map
6. Read the results:

   * **Left sidebar** — Risk %, length, and comparison for all 3 routes
   * **Bright green line** — The safest route
   * **Faded grey lines** — Alternative routes
   * **Heatmap** — Red/orange = high crime areas, dark = lower crime
   * **Hover over a route line** — See its risk % and km length

\---

## Troubleshooting

### ❌ `jinja2.exceptions.TemplateNotFound: index.html`

**Cause:** The `templates/` folder is missing or in the wrong place.

**Fix:** Your folder must look exactly like this:

```
edilproject/
├── main.py
├── train\_model.py
└── templates/           ← must be a subfolder, not a separate location
    ├── index.html
    └── map.html
```

Create the `templates` folder inside `edilproject/` if it doesn't exist,
then move both HTML files into it.

\---

### ❌ `ModuleNotFoundError: No module named 'fastapi'`

**Cause:** Virtual environment is not activated or requirements not installed.

**Fix:**

```cmd
venv\\Scripts\\activate          (Windows)
source venv/bin/activate       (Mac/Linux)
pip install -r requirements.txt
```

\---

### ❌ `crime\_model.pkl NOT found`

**Cause:** The training script hasn't been run yet.

**Fix:**

```cmd
python train\_model.py
```

\---

### ❌ `Could not locate 'X'. Try adding 'Chicago' to the name.`

**Cause:** OpenStreetMap couldn't find that place name.

**Fix:** Be more specific:

* `"downtown"` → try `"The Loop, Chicago, IL"`
* `"north side"` → try `"Lincoln Park, Chicago"`
* Use a full street address: `"600 W Chicago Ave, Chicago"`

\---

### ❌ `ORS API error 429`

**Cause:** Hit the free tier rate limit (2,000 requests/day).

**Fix:** Wait until tomorrow, or get a new free key at https://openrouteservice.org
and replace `ORS\_API\_KEY` in `main.py`.

\---

### ❌ `Routing API error`

**Cause:** ORS couldn't find a driving route (location outside Chicago,
or on non-drivable terrain like a park or lake).

**Fix:** Use different location names clearly within Chicago city limits.

\---

### ❌ Map is blank or all black

**Cause:** Folium map iframe sizing issue.

**Fix:** Hard-refresh with `Ctrl + Shift + R` (Windows/Linux) or
`Cmd + Shift + R` (Mac).

\---

### ❌ `uvicorn: command not found`

**Cause:** Virtual environment not activated.

**Fix:** Run the activate command first, then try again.

```cmd
venv\\Scripts\\activate    (Windows)
source venv/bin/activate (Mac/Linux)
```

\---

### ❌ `Error: Address already in use` / Port 8000 busy

**Cause:** Something else is already running on port 8000.

**Fix:** Use a different port:

```cmd
uvicorn main:app --reload --port 8001
```

Then visit `http://localhost:8001`.

\---

### ❌ `Distance exceeds the 80 km limit`

**Cause:** The two locations are more than 80 km apart (likely different cities).

**Fix:** Use two locations that are both within Chicago.

\---

## Tech Stack

|Component|Technology|Version|
|-|-|-|
|Web Framework|FastAPI|0.111.0|
|ASGI Server|Uvicorn|0.29.0|
|HTML Templates|Jinja2|3.1.4|
|Map Rendering|Folium + Leaflet.js|0.16.0|
|ML Model|Scikit-learn RandomForest|1.4.2|
|HTTP Client|HTTPX (async)|0.27.0|
|Geocoding|Nominatim (OpenStreetMap)|free|
|Routing|OpenRouteService API|free|
|Numerics|NumPy|1.26.4|
|Data Handling|Pandas|2.2.2|
|Model Storage|Joblib|1.4.2|

\---

## API Keys

### OpenRouteService (routing)

Already included in `main.py` as `ORS\_API\_KEY`.

To get your own key:

1. Go to https://openrouteservice.org
2. Sign up for a free account
3. Dashboard → Tokens → Request a token
4. Copy the token, replace `ORS\_API\_KEY` in `main.py`

Free tier limits: **2,000 requests/day**, max 3 alternative routes per request.

### Nominatim (geocoding)

No key needed. The `User-Agent` header in the code satisfies the usage policy.
Rate limit: 1 request/second — more than enough for this app.

\---

## Using Real Chicago Crime Data (Optional)

The app uses synthetic (computer-generated) crime data by default.
To use the real Kaggle dataset for more accurate results:

1. Download from:
https://www.kaggle.com/datasets/georgehanyfouad/crime-prediction-in-chicago-in-2022
2. Save the file as `chicago\_crimes.csv` inside the project folder
3. Open `train\_model.py`, find `generate\_synthetic\_crime\_data()` and
replace the entire function call with:

```python
df = pd.read\_csv("chicago\_crimes.csv")
# Ensure columns: Latitude, Longitude, hour, day, month, risk\_score
```

4. Retrain:

```cmd
python train\_model.py
```

5. Restart server:

```cmd
uvicorn main:app --reload
```

\---

## Making It Public (Sharing With Others)

### Option 1 — Ngrok (fastest, no hosting needed)

While your server is running, open a **second terminal** and:

```cmd
ngrok http 8000
```

Ngrok gives you a public HTTPS URL like `https://abc123.ngrok.io`.
Share it with anyone. Works as long as your computer is on and the
server is running.

Download ngrok: https://ngrok.com/download

\---

### Option 2 — Railway (free permanent cloud hosting)

1. Push your project to GitHub
2. Go to https://railway.app and sign up
3. New Project → Deploy from GitHub repo
4. Add environment variable: none needed
5. Add a `Procfile` in the project root:

```
   web: uvicorn main:app --host 0.0.0.0 --port $PORT
   ```

6. Railway auto-deploys and gives you a permanent public URL

\---

### Option 3 — Render (free cloud hosting)

1. Push to GitHub
2. Go to https://render.com
3. New → Web Service → Connect your repo
4. Build command: `pip install -r requirements.txt \&\& python train\_model.py`
5. Start command: `uvicorn main:app --host 0.0.0.0 --port $PORT`
6. Deploy — free tier available

\---

*SafeRoute AI · Demo System · Chicago Crime Dataset · OpenRouteService*

