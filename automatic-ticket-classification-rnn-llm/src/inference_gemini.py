from google import genai

def generate_reply(api_key, ticket_text, queue):
    client = genai.Client(api_key=api_key)

    prompt = f"""
You are a customer support assistant.

Ticket Queue: {queue}
Customer Issue: {ticket_text}

Write a short, polite, professional acknowledgment message.
Rules:
- Do not promise exact timelines
- Do not request sensitive information
- Keep it empathetic and clear (4–6 lines)
"""

    # Try available models until one works
    last_error = None
    for model in client.models.list():
        try:
            response = client.models.generate_content(
                model=model.name,
                contents=prompt
            )
            return response.text.strip()
        except Exception as e:
            last_error = e
            continue

    # If no model worked
    raise RuntimeError(
        "No available Gemini model could generate content. "
        f"Last error: {last_error}"
    )
