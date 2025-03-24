from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.lib.get_auth_token import get_auth_token
from src.lib.rabbitMq.connection import RabbitMQManager
from src.routers import (
    audio_transcription,
    export_dicom,
    generate_coronarography,
    generate_pdf,
    parse_gs1,
    pdf_demo,
    document_ai_generator,
    widget_ai_generator,
)
from src.lib.prismaClient import prisma_client
from src.lib.redisClient import redis_client
from src.routers import copilot_audio_transcription
from src.routers import extract_kt_product_infos

rabbitmq_manager = RabbitMQManager()


async def lifespan(app: FastAPI):
    # Setup: Code to run at startup
    print("Starting up...")
    """Verify Redis connection on startup."""
    try:
        await prisma_client.connect()
        redis_client.ping()
        rabbitmq_manager.connect()
        print("Connected to Redis successfully!")
    except Exception as e:
        print(f"Error connecting to Redis: {e}")
        raise e

    yield  # This yields control back to FastAPI, allowing it to run the app
    # Teardown: Code to run at shutdown
    await prisma_client.disconnect()
    rabbitmq_manager.close()

    """Close Redis connection on shutdown."""
    redis_client.close()
    print("Shutting down...")


def get_rabbitmq_manager() -> RabbitMQManager:
    return rabbitmq_manager


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
    document_ai_generator.router,
    prefix="/ai_document",
    tags=["ai_document"],
    dependencies=[Depends(get_rabbitmq_manager)],
)
app.include_router(audio_transcription.router, prefix="/STT", tags=["STT"])
app.include_router(
    copilot_audio_transcription.router,
    prefix="/copilot_STT",
    tags=["copilot_STT"],
    dependencies=[Depends(get_auth_token)],
)
app.include_router(
    widget_ai_generator.router, prefix="/widget_rewrite", tags=["widget_rewrite"]
)
app.include_router(
    extract_kt_product_infos.router, prefix="/kt_product_info", tags=["kt_product_info"]
)

app.include_router(parse_gs1.router, prefix="/gs1_parser", tags=["gs1_parser"])
app.include_router(export_dicom.router, prefix="/export_dicom", tags=["export_dicom"])
app.include_router(
    generate_coronarography.router, prefix="/coronarography", tags=["coronarography"]
)
