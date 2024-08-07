from fastapi import APIRouter

date_format = "%d/%m/%Y"
time_format ="%H:%M"

router = APIRouter()

@router.get("/")
def root():
    return "first assignment by MoranSin"

@router.get("/health")
def health_code():
    return 200