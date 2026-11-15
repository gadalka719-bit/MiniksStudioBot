import os
from google import genai
from google.genai import types

# Инициализация клиента Google GenAI (ключ подтянется из переменных окружения)
client = genai.Client()

async def generate_edit_concept(prompt_text: str) -> str:
    """Генерирует детальный концепт и тайминги для эдита по запросу пользователя"""
    try:
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=f"Создай крутой, детальный концепт для TikTok/Reels эдита на тему: {prompt_text}. "
                     f"Укажи: 1) Рекомендуемый стиль музыки (например, phonk, drift), "
                     f"2) Точки ударов (биты) и тайминги для смены кадров, "
                     f"3) Визуальные эффекты (вспышки, шейк, цветокоррекция), "
                     f"4) Цепляющий хук на первые секунды.",
            config=types.GenerateContentConfig(
                temperature=0.7,
            )
        )
        return response.text
    except Exception as e:
        return f"Ошибка при генерации концепта: {str(e)}"