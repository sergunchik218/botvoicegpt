from typing import List, Dict



def chat_gpt_response_to_text(response: List[Dict[str, str]]) -> str:
    result = []
    for iten in response:
        response_text = iten.get("text")
        clear_message = response_text.strip("\n")
        result.append(clear_message)
    return " ".join(result)