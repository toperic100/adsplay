from fastapi import APIRouter

router = APIRouter(prefix="/game")

@router.post("/play")
def play_game(user_id: int):
    return {"result": "win", "reward": 10}
