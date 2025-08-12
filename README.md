# AutoJHA — AI-Powered Job Hazard Analysis Generator

AutoJHA is a web application that generates professional **Job Hazard Analyses (JHAs)** using real-time weather data, geolocation, and an AI language model.  
It streamlines safety documentation by combining **site-specific job info** with **live environmental conditions** to produce a detailed hazard report in Markdown format.

---

## Features

- **Interactive Streamlit Frontend**  
  User-friendly form to input job details, tasks, and site conditions.

- **FastAPI Backend**  
  Validates input, orchestrates API calls, and communicates with the AI model.

- **Real-Time Weather & Alerts**  
  Integrates with [NWS API](https://www.weather.gov/documentation/services-web-api) for location-specific forecasts and active hazard alerts.

- **Geocoding Support**  
  Converts job site addresses into latitude/longitude for weather lookups.

- **AI-Generated JHAs**  
  Uses [Gemini API](https://ai.google.dev/) to create Markdown-formatted hazard analyses tailored to each job.

- **Modular Design**  
  External API clients, schema validation, and prompt templates are cleanly separated.

---

## Project Structure

```
autojha/
├── backend/
│   ├── core/             # Config & settings
│   ├── external/         # API integrations (Gemini, Geocode, NWS)
│   ├── routers/          # FastAPI route handlers
│   ├── schemas/          # Pydantic models for request/response validation
│   ├── utils/            # Prompt templates & helper functions
│   └── main.py           # FastAPI application entrypoint
├── frontend/
│   ├── app.py           # Streamlit landing page
│   └── generate_jha.py   # JHA creation UI
├── .env.example          # Example environment variables
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```

---

## Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/evan-caswell/autojha.git
cd autojha
```

### 2. Create and activate a virtual environment
```bash
python -m venv .venv
source .venv/bin/activate   # macOS/Linux
.venv\Scripts\activate      # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure environment variables
Copy `.env.example` to `.env` and fill in the required values:
```bash
cp .env.example .env
```
**Required keys:**
- `GEMINI_API_KEY` — API key for Gemini
- `GEOCODE_API_KEY` — API key for your geocoding provider

### 5. Run the backend (FastAPI)
```bash
uvicorn backend.main:app --reload --port 8000
```

### 6. Run the frontend (Streamlit)
Open a new terminal in the project root:
```bash
streamlit run app.py --server.port 8501
```

The app will be available at:
- **Frontend:** http://localhost:8501  
- **Backend API Docs:** http://localhost:8000/docs

---

## Usage

1. Open the Streamlit frontend.
2. Enter job information, tasks, and site conditions.
3. Provide a job location (validated via geocoding).
4. Click **Generate JHA**.
5. Review the AI-generated Markdown output.

---

## Safety & Data Notes

- Weather data is fetched from the **National Weather Service API**.
- Location lookups use the configured geocoding provider.
- AI-generated content should always be reviewed by a safety professional before field use.

---

## Technology Stack

- **Frontend:** [Streamlit](https://streamlit.io/)
- **Backend:** [FastAPI](https://fastapi.tiangolo.com/)
- **AI Model:** [Google Gemini API](https://ai.google.dev/)
- **Weather Data:** [NWS API](https://www.weather.gov/documentation/services-web-api)
- **Geocoding:** [Geocode.xyz](https://geocode.xyz/)
- **Validation:** [Pydantic](https://docs.pydantic.dev/)

---

## Roadmap

- [ ] Replace `geocode.xyz` with a more reliable provider (e.g., Nominatim or Google Geocoding API)
- [ ] Implement caching for geocode & weather data
- [ ] Add PDF export for generated JHAs
- [ ] Persist & view saved JHAs in a database
- [X] Improve prompt structure for more consistent AI output

---

## Contributing

Pull requests are welcome!  
For major changes, please open an issue first to discuss your ideas.

---

## License

This project is licensed under the MIT License.  

