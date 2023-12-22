from fastapi import FastAPI, HTTPException
from loguru import logger

from app.model import MessageParams
from app.service import get_text_generation

app = FastAPI()


@app.post("/generate", status_code=200)
async def generate_text(message_params: MessageParams):
    print(f"triggered text generator -- model: {message_params.model}, message: {message_params.message}")
    if message_params.model not in ["gpt2", "gpt2-large"]:
        print(f"user tried use wrong model")
        raise HTTPException(
            status_code=405, detail={"error": f"Model name must be `gtp2` or `gtp2-large` not {message_params.model}"}
        )
    try:
        result = get_text_generation(message=message_params.message, model=message_params.model)
        return {"answer": result}
    except Exception as error:
        print(repr(error))
        raise HTTPException(status_code=500, detail={"error": error})
