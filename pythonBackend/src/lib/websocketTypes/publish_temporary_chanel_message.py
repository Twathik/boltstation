from typing import Any
from ulid import ULID
from src.lib.websocketTypes.general_classes import MessageDestination, OperationEnum
from src.lib.websocketTypes.temporary_chanel_message_class import (
    TemporaryChanelMessage,
    TemporaryChanelMessagePayload,
    TemporaryChanelMessageType,
    TemporaryMessageDestination,
    TemporaryMessageType,
)
from src.lib.redisClient import notification_chanel, redis_client


def publish_message(
    temporaryChanelId: str,
    content: Any,
    operation: OperationEnum,
    type: TemporaryMessageType,
):
    message = TemporaryChanelMessageType(
        bashPayload=None,
        destination=[],
        globalMessage=False,
        id=ULID(),
        subscriptionIds=[],
        type=MessageDestination.temporaryChanel,
        payload=TemporaryChanelMessagePayload(
            operation=operation,
            message=TemporaryChanelMessage(
                destination=TemporaryMessageDestination.ai_document,
                temporaryChanelId=temporaryChanelId,
                content=content,
                id=ULID(),
                type=type,
            ),
        ),
    )

    redis_client.publish(notification_chanel, message.model_dump_json())
