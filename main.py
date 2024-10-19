import uvicorn
from fastapi import FastAPI

from product.views import router as product_router


app = FastAPI(title="Shop app")
app.include_router(product_router)


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
