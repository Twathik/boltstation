from typing import Any, Callable, List


async def inject_data_from_chunk(
    document: List[Any],
    chunk: Any,
    clinicalEventId: str,
    widget_id: str,
    injector: Callable[[List[Any], Any, str], None],
    extracted_data: List[str],
):
    exists = any(item.get("widgetId") == widget_id for item in document)

    document.append(chunk)
    if not exists == True:
        await injector(
            document=document,
            chunk=chunk,
            clinicalEventId=clinicalEventId,
            extracted_data=extracted_data,
        )
