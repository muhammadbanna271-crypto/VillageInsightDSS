import anthropic
from django.conf import settings

from apps.chatbot.services.prompts import SYSTEM_PROMPT
from apps.chatbot.tools import TOOLS_SCHEMA, execute_tool


class ClaudeChatService:
    """
    Engine "Claude" -- dikunci password, dipakai lewat Anthropic API
    dengan format tool-use bawaan Anthropic.
    """

    MAX_TOOL_ITERATIONS = 5

    @classmethod
    def ask(cls, message, history=None):
        """
        message: teks pertanyaan warga (str)
        history: list pesan sebelumnya, format Anthropic messages
                 (biasanya disimpan di session Django)

        Return: (reply_text, updated_history)
        """

        if not settings.ANTHROPIC_API_KEY:

            return (
                (
                    "Maaf, mesin Claude belum dikonfigurasi oleh "
                    "admin (API key belum diatur)."
                ),
                history or [],
            )

        client = anthropic.Anthropic(
            api_key=settings.ANTHROPIC_API_KEY,
        )

        messages = list(history or [])

        messages.append(
            {"role": "user", "content": message}
        )

        for _ in range(cls.MAX_TOOL_ITERATIONS):

            response = client.messages.create(
                model=settings.CHATBOT_MODEL,
                max_tokens=1024,
                system=SYSTEM_PROMPT,
                tools=TOOLS_SCHEMA,
                messages=messages,
            )

            messages.append(
                {
                    "role": "assistant",
                    "content": [
                        block.model_dump()
                        for block in response.content
                    ],
                }
            )

            if response.stop_reason != "tool_use":

                final_text = "".join(

                    block.text

                    for block in response.content

                    if block.type == "text"

                )

                return final_text, messages

            tool_results = []

            for block in response.content:

                if block.type == "tool_use":

                    result = execute_tool(
                        block.name,
                        block.input,
                    )

                    tool_results.append(
                        {
                            "type": "tool_result",
                            "tool_use_id": block.id,
                            "content": str(result),
                        }
                    )

            messages.append(
                {
                    "role": "user",
                    "content": tool_results,
                }
            )

        return (
            (
                "Maaf, pertanyaan ini terlalu kompleks untuk saya "
                "proses saat ini. Coba tanyakan dengan lebih spesifik."
            ),
            messages,
        )
