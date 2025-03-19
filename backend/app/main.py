from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import api_keys, integrations
from app.db.base import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Low-Code SaaS Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_keys.router, prefix="/api/keys", tags=["API Keys"])
app.include_router(integrations.router, prefix="/api/integrations", tags=["Integrations"])
