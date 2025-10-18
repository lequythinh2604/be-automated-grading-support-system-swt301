from openai import OpenAI

from app.core.config import settings

client = OpenAI(api_key=settings.OPENAI_API_KEY)

try:
    response = client.chat.completions.create(
        model="ft:gpt-4o-mini-2024-07-18:personal:test1:C4tZqaGq",  # Tên mô hình fine-tuned
        messages=[
            {"role": "system", "content": "Bạn là trợ lý chấm điểm môn Software Testing. Đánh giá câu trả lời và cho điểm từ 0-10."},
            {"role": "user", "content": "White-box testing là gì? Trả lời: Là kiểm thử dựa trên mã nguồn, kiểm tra cấu trúc bên trong của phần mềm."}
        ],
        max_completion_tokens=150
    )
    print(response.choices[0].message.content)
except Exception as e:
    print(f"An error occurred: {e}")
