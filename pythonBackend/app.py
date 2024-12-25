from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routers import generate_pdf, pdf_demo, document_ai_generator
from src.lib.prismaClient import prisma_client
from src.lib.redisClient import redis_client


async def lifespan(app: FastAPI):
    # Setup: Code to run at startup
    print("Starting up...")
    """Verify Redis connection on startup."""
    try:
        await prisma_client.connect()
        redis_client.ping()
        print("Connected to Redis successfully!")
    except Exception as e:
        print(f"Error connecting to Redis: {e}")
        raise e

    yield  # This yields control back to FastAPI, allowing it to run the app
    # Teardown: Code to run at shutdown
    await prisma_client.disconnect()

    """Close Redis connection on shutdown."""
    redis_client.close()
    print("Shutting down...")


# Create the FastAPI app
app = FastAPI(lifespan=lifespan)  # type: ignore

origins = [
    "http://localhost:3000",  # React/Next.js running locally
    "http://app.bolt.local",  # Your production frontend domain
]

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Allow these origins
    allow_credentials=True,  # Allow cookies/auth headers
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)


@app.get("/")
def index():
    return {"message": "Welcome to BoltPyBack reloaded"}


app.include_router(generate_pdf.router, prefix="/pdf", tags=["pdf"])
app.include_router(pdf_demo.router, prefix="/pdf_demo", tags=["pdf_demo"])
app.include_router(
    document_ai_generator.router, prefix="/ai_document", tags=["ai_document"]
)
