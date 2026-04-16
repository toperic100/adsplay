from fastapi import APIRouter

router = APIRouter(prefix="/ad")

@router.post("/watch")
def watch_ad(user_id: int, ad_id: int):
    return {"msg": "ad watched", "reward": 5}
