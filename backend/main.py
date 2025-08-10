from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.routers import jha_router

app = FastAPI()

origins = ["http://localhost:8501"]

# Add middleware to allow the backend to receive request from the frontend since they
# have different origins.
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(jha_router.router)
