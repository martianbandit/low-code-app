from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_integrations():
    return {"message": "Liste des intégrations disponibles"}

@router.post("/webhook")
def create_webhook(url: str):
    # Implémentation future de création de webhook
    return {"message": "Webhook créé", "url": url}
