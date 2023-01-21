# fileName : lang/__init__.py
# copyright ©️ 2021 ajak4405

from configs.config import settings

langList = {
        "eng" : ["🅴🅽🅶🅻🅸🆂🅷", "English"]
    }

# Display Lang in a Beutiful Way
async def disLang(lang):
    if lang in langList:
        return langList[lang][0]
    else:
        return langList[settings.DEFAULT_LANG][0]

# ===================================================================================================================================[NABIL A NAVAB -> TG: ajak4405]
