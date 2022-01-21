from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from routers import sla

description = """
SLA Calculator 🚀
"""

app = FastAPI(
    title="SLACalculator Swagger UI",
    description=description,
    version="0.0.1",
    contact={
        "name": "99-66",
        "url": "https://github.com/99-66",
    }
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(sla.router, prefix="/sla")


@app.get("/")
async def root():
    return {"message": "It's root"}
