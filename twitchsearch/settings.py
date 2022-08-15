import os

MIN_TO_NEW_STREAM = 5
MIN_VIEW_COUNT = 5
MAX_STREAM_SEARCH_COUNT = 2000
TWITCH_SPOTLIGHT_APP_ID = os.environ['TWITCH_SPOTLIGHT_APP_ID']
TWITCH_SPOTLIGHT_APP_SECRET = os.environ['TWITCH_SPOTLIGHT_APP_SECRET']
STREAM_LANGUAGE = 'pt'

SUPPORTED_LANGUAGES = {
    "pt":"Português",
    "en":"English",
    "id":"Bahasa Indonesia",
    "ca":"Català",
    "da":"Dansk",
    "de":"Deutsch",
    "es":"Español",
    "fr":"Français",
    "it":"Italiano",
    "hu":"Magyar",
    "nl":"Nederlands",
    "no":"Norsk",
    "pl":"Polski",
    "ro":"Română",
    "sk":"Slovenčina",
    "fi":"Suomi",
    "sv":"Svenska",
    "tl":"Tagalog",
    "vi":"Tiếng Việt",
    "tr":"Türkçe",
    "cs":"Čeština",
    "el":"Ελληνικά",
    "bg":"Български",
    "ru":"Русский",
    "uk":"Українська",
    "ar":"العربية",
    "ms":"بهاس ملايو",
    "hi":"मानक हिन्दी",
    "th":"ภาษาไทย",
    "zh":"中文",
    "ja":"日本語",
    "zh-hk":"粵語",
    "ko":"한국어",
    "asl":"American Sign Language",
    "other":"Outro",
}