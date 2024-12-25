from langchain_ollama import OllamaLLM
from langchain.schema import SystemMessage, HumanMessage
from pprintpp import pprint
from lib.prismaClient import prisma_client


async def summarize_medicalDocument(document_id: str):

    try:
        await prisma_client.connect()
        model = OllamaLLM(
            model="gemma2:latest",
            keep_alive="10m",
            temperature=0.2,
        )

        try:
            document = await prisma_client.documentstore.find_first_or_raise(
                where={"id": document_id}
            )

            system_prompt = SystemMessage(
                content="""
**Please summarize the following medical document according to the guidelines below:**

- Include all key points from the original document.
- Write the summary exclusively in **French**.
- Maintain a **professional and formal tone**, similar to that of a **physician's report**.
- Include all relevant medical information such as symptoms, diagnoses, treatments, tests, and results.
- Ensure the summary is clear, concise, and accurately reflects the original content.
- Present each distinct piece of information as bullet points for better readability.
- Do not include titles or headings from the original document.
- Strictly limit your response to the medical information described in the document.
- Omit any unrelated details or additional explanations.
- Avoid adding commentary or contextual notes beyond the requested information.
- Do not infer or include negative findings for observations not listed in the medical document.
- If multiple observations are described in the medical document, organize your response into an unordered list for clarity.
- **Format your answer in Markdown format.**

## **Medical Document:**


            """
            )
            # pprint(document.mdContent, depth=4)
            user_prompt = HumanMessage(content=document.mdContent)

            chat_prompt = [system_prompt, user_prompt]

            results = model.invoke(chat_prompt)

            await prisma_client.documentstore.update(
                where={"id": document_id}, data={"summarizedMdContent": results}
            )
            await prisma_client.disconnect()
            print("operation finished with success")
            pass
        except Exception as e:
            await prisma_client.disconnect()
            raise e
        pass
    except Exception as e:
        raise e
