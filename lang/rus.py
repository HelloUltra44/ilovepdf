# LANG: RUSSIAN [RUSSIA] LANG CODE: RUS                          >>  copyright ©️ 2021 nabilanavab  <<                                         fileName : lang/hnd.py
#                                          Thank: nabilanavab                                              E-mail: nabilanavab@gmail.com

from configs.config import settings

# ПРИВЕТСТВЕННОЕ СООБЩЕНИЕ (ДОМ A, B, C, D...)
HOME = {
    "HomeA" : """Эй, [{}](tg://user?id={})..!!
Этот бот поможет вам сделать много вещей с pdf 🥳

Некоторые из ключевых функций:\n◍ `Преобразование изображений в PDF`
◍ `Преобразовать PDF в изображения`\n◍ `Преобразовать файлы в pdf`""",
    "HomeACB": {
        "« ⚙ НАСТРОЙКИ ⚙ »" : "Home|B", "« ⚠ ПОМОЩЬ ⚠ »" : "Home|C",
        "« 📢 КАНАЛ 📢 »" : f"{str(settings.OWNED_CHANNEL)}",
        "« 🌟 ИСХОДНЫЙ КОД 🌟 »" : f"{str(settings.SOURCE_CODE)}",
        "« 🚶 ЗАКРЫТЬ 🚶 »" : "close|mee"
    },
    "HomeAdminCB" : {
        "« ⚙ НАСТРОЙКИ ⚙ »" : "Home|B", "« ⚠️ ПОМОЩЬ ⚠️ »" : "Home|C",
        "« 📢 КАНАЛ 📢 »": f"{str(settings.OWNED_CHANNEL)}",
        "« 🌟 ИСХОДНЫЙ КОД 🌟 »": f"{str(settings.SOURCE_CODE)}",
        "« 🗽 СТАТУС 🗽 »": "status|home", "« 🚶 ЗАКРЫТЬ 🚶 »": "close|mee"
    },
    "HomeB": """СТРАНИЦА НАСТРОЕК ⚙️\n\nИМЯ ПОЛЬЗОВАТЕЛЯ: {}
ID ПОЛЬЗОВАТЕЛЯ: {}\nИМЯ ПОЛЬЗОВАТЕЛЯ: {}\nДАТА ПРИСОЕДИНЕНИЯ: {}\n
ЯЗЫК : {}\nAPI : {}
THUMB: {}\nCAPTION: {}\nИМЯ ФАЙЛА: {}""",
    "HomeBCB": {
        "« 🌍 ЯЗЫК 🌍 »" : "set|lang", "« 📍 THUMB 📍 »" : "set|thumb",
        "« 📈 ИМЯ 📈 »" : "set|fname", "« 💩 API 💩 »" : "set|api",
        "« 📅 ЗАГОЛОВОК 📅 »" : "set|capt", "« НАЗАД НА ДОМОЙ »" : "Home|B2A"
    },
    "HomeC": """   **ПОМОЩНОЕ СООБЩЕНИЕ**   :

```Вот некоторые из основных особенностей:
 ◍ Преобразование изображений в PDF\n ◍ Обработка PDF\n ◍ Многие популярные кодеки в PDF
 
Измените файл PDF:
 ◍ PDF⥃ИЗОБРАЖЕНИЯ [все,диапазон,страницы]\n ◍ DOCS в PDF [png, jpg, jpeg]\n ◍ ИЗОБРАЖЕНИЯ⥃PDF\n ◍ МЕТАДАННЫЕ PDF\n ◍ PDF⥃ТЕКСТ\n ◍ ТЕКСТ⥃PDF\n ◍ Сжать pdf-файл
 ◍ РАЗДЕЛИТЬ PDF [диапазон, страницы]\n ◍ ОБЪЕДИНИТЬ PDF\n ◍ ДОБАВИТЬ ПЕЧАТЬ\n ◍ ПЕРЕИМЕНОВАТЬ PDF\n ◍ ПОВЕРНУТЬ PDF\n ◍ ШИФРОВАТЬ/РАСШИФРОВАТЬ PDF\n ◍ ФОРМАТЕР PDF \n ◍ ФАЙЛ PDF⥃JSON/TXT
 ◍ PDF⥃HTML [просмотр в Интернете]\n ◍ URL⥃PDF\n ◍ PDF⥃ZIP/TAR/RAR [все, диапазон, страницы]\nИ многое другое.. ```""",
    "HomeCCB" : {"« НАЗАД ДОМОЙ «" : "Дом|A", "🛈 ИНСТРУКЦИИ 🛈" : "Дом|D"},
    "HomeD": """`Поскольку это бесплатная услуга, я не могу гарантировать, как долго я смогу поддерживать эту услугу..`😝
 
⚠️ ИНСТРУКЦИЯ ⚠️:
🛈 __Пожалуйста, не пытайтесь оскорблять администраторов ботов__ 😒
🛈 __Не спамить здесь, это может привести к перманентному бану 🎲__.
🛈 __Porn Contents также даст вам ПОСТОЯННЫЙ БАН 💯__

**Отправьте любое изображение для начала:** 😁""",
    "HomeDCB" : {"⚠️ ПОМОЩЬ ⚠️" : "Домой|C", "» НАЗАД ДОМОЙ »" : "Домой|A"}
}

SETTINGS = {
    "default": ["ПО УМОЛЧАНИЮ ❌", "НАСТРОЙКА ✅"], "chgLang": {"НАСТРОЙКА ⚙️» ИЗМЕНИТЬ ЯЗЫК 🌐": "nabilanavab"},
    "error" : "Что-то пошло не так при извлечении данных из базы данных", "lang" : "Теперь выберите любой язык..",
    "ask" : ["Сейчас, пришлите мне..", "Сейчас, пришлите мне.. 😅\n\nБыстро.! У меня больше нет времени просматривать текст.. 😏\n\n/cancel: отменить"],
    "askApi" : "\n\nОткройте ссылку ниже и пришлите мне секретный код:", "waitApi" : {"Открыть ссылку ✅" : "https://www.convertapi.com/a/signin"},
    "wait" : {"Жду.. 🥱" : "nabilanavab"}, "back" : {"« НАЗАД ДОМОЙ «" : "Home|B2S"}, "errorCB" : {"« НАЗАД ДОМОЙ »": "Home|B2A"},
    "result": ["Настройки не могут быть обновлены ❌", "Настройки успешно обновлены ✅"], "cant": "Эта функция не может быть использована ❌",
    "feedback": "Отзывы от Потрясающих Клиентов, например, вы помогаете Другим.\n@nabilanavab"
                 "\n\nСообщить об ОШИБКЕ на {} языке:\n`• Укажите язык\n• Сообщение об ошибке\n• Новое сообщение`",
    "feedbtn": {"Сообщить об ошибке языка": settings.REPORT},
    "большой палец" : [
        {"» НАСТРОЙКА ⚙️ » МИНИАТЮР 📷 »" : "nabilanavab", "« ♻ ДОБАВИТЬ ♻ »" : "set|thumb+", "« НАЗАД НА ДОМОЙ «" : "Домой|B"},
        {"» НАСТРОЙКА ⚙️ » МИНИАТЮР 📷 »" : "nabilanavab", "« ♻ ИЗМЕНИТЬ ♻ »" : "set|thumb+", "« 🗑 УДАЛИТЬ 🗑 »" : "set|thumb-", "« НАЗАД НА ДОМОЙ »" : "Home|B2S"}
    ],
    "фамия": [
        {"» SETTING ⚙️ » FNAME 📷 »" : "nabilanavab", "« ♻ ДОБАВИТЬ ♻ »" : "set|fname+", "« НАЗАД НА ДОМОЙ «" : "Home|B2S"},
        {"» НАСТРОЙКА ⚙️ » FNAME 📷 »" : "nabilanavab", "« ♻ ИЗМЕНИТЬ ♻ »" : "set|fname+", "« 🗑 УДАЛИТЬ 🗑 »" : "set|fname-", "« НАЗАД НА ДОМОЙ »" : "Home|B2S"}
    ],
    "апи": [
        {"» НАСТРОЙКА ⚙️ » API 📷 »" : "nabilanavab", "« ♻ ДОБАВИТЬ ♻ »" : "set|api+", "« НАЗАД НА ДОМОЙ «" : "Home|B2S"},
        {"» НАСТРОЙКА ⚙️ » API 📷 »" : "nabilanavab", "« ♻ ИЗМЕНИТЬ ♻ »" : "set|api+", "« 🗑 УДАЛИТЬ 🗑 »" : "set|api-", "« НАЗАД НА ДОМ »" : "Home|B2S"}
    ],
    "капитан": [
        {"» НАСТРОЙКА ⚙️ » ЗАГОЛОВОК 📷 »" : "nabilanavab", "« ♻ ДОБАВИТЬ ♻ »" : "set|capt+", "« НАЗАД НА ДОМОЙ «" : "Home|B2S"},
        {"» НАСТРОЙКА ⚙️ » ЗАГОЛОВОК 📷 »" : "nabilanavab", "« ♻ ИЗМЕНИТЬ ♻ »" : "set|capt+", "« 🗑 УДАЛИТЬ 🗑 »" : "set|capt-", "« НАЗАД НА ДОМОЙ »" : "Home|B2S"}
    ]
}

BOT_COMMAND = {"start" : "Приветствие..", "txt2pdf" : "Создание текстовых PDF-файлов"}

HELP_CMD = {
    "userHELP" : """[СООБЩЕНИЯ КОМАНД ПОЛЬЗОВАТЕЛЯ]:\n
/start: проверить, жив ли бот\n/cancel: отменить текущую работу
/delete: очистить изображение в очередь pdf\n/txt2pdf: текст в pdf""",
    "adminHelp" : """\n\n\n[СООБЩЕНИЯ КОМАНД АДМИНИСТРАТОРА]:\n
/send: для трансляции, сообщение в личку """,
    "footerHelp": f"""\n\n\nИсходный код: [i 💜 PDF]({str(settings.SOURCE_CODE)})
Бот: @complete_pdf_bot 💎\n[Канал поддержки]({settings.OWNED_CHANNEL})""",
    "CB" : {"« ⚠️ ЗАКРЫТЬ ⚠️ »" : "close|all"}
}

STATUS_MSG = {
    "HOME" : "`Теперь выберите любой вариант ниже, чтобы получить текущий статус 💱.. `",
    "_HOME" : {
        "« 📊 ↓ СЕРВЕР ↓ 📊 »" : "nabilanavab", "« 📶 ХРАНИЛИЩЕ 📶 »": "status|server",
        "« 🥥 БАЗА ДАННЫХ 🥥 »": "status|db", "« 🌝 ↓ ПОЛУЧИТЬ СПИСОК ↓ 🌝 »": "nabilanavab",
        "« 💎 АДМИНИСТРАТОР 💎 »": "status|admin", "« 👤 ПОЛЬЗОВАТЕЛИ 👤 »" : "status|users",
        "« НАЗАД »" : "Home|A"
    },
    "DB" : """📂 БАЗА ДАННЫХ :\n\n**◍ Пользователи базы данных :** `{}` 📍\n**◍ Чаты базы данных :** `{}` 📍""",
    "SERVER": """**◍ Общее пространство:** `{}`
**◍ Используемое пространство:** `{}({}%)`\n**◍ Свободное пространство:** `{}`
**◍ Использование ЦП:** `{}`%\n**◍ Использование ОЗУ:** `{}`%
**◍ Текущая работа:** `{}`\n**◍ Идентификатор сообщения:** `{}`""",
    "BACK" : {"« НАЗАД «" : "status|home"}, "ADMIN" : "**Всего АДМИН:** __{}__\n",
    "USERS": "Пользователи, сохраненные в БД:\n\n", "NO_DB": "База данных еще не установлена ​​💩"
}

feedbackMsg = f"[Написать отзыв 📋]({settings.FEEDBACK})"

# ГРУППА ПРИВЕТСТВИЕ
HomeG = {
    "HomeA": """Привет.! 🖐️\nЯ здесь впервые {message.chat.title}\n
Позвольте представиться..\nМеня зовут iLovePDF, и я могу помочь вам во многих
Вещи с PDF-файлами @Telegram\n\nСпасибо @nabilanavab за этого замечательного бота 😅""",
    "HomeACB": {
        "🤠 ВЛАДЕЛЕЦ БОТА 🤠": f"https://telegram.dog/{settings.OWNER_USERNAME}",
        "🛡️ ОБНОВИТЬ КАНАЛ 🛡️": f"{settings.OWNED_CHANNEL}", "🌟 ИСХОДНЫЙ КОД 🌟": f"{settings.SOURCE_CODE}"
    }
}

# ЗАБАНИРОВАННЫЙ ПОЛЬЗОВАТЕЛЬСКИЙ ИНТЕРФЕЙС
BAN = {
    "cbNotU": "Сообщение не для вас.. 😏",
    "banCB" : {
        "« Создай своего бота »": f"{settings.SOURCE_CODE}", "« Учебник »": f"{settings.SOURCE_CODE}",
        "« Обновить канал »": "https://telegram.dog/anumitultrabots"
    },
    "UCantUse" : """Привет {}\n\nПО КАКИМ-ТО ПРИЧИНАМ ВЫ НЕ МОЖЕТЕ ИСПОЛЬЗОВАТЬ ЭТОГО БОТА :(""",
    "UCantUseDB" : """Привет {}\n\nПО НЕКОТОРОЙ ПРИЧИНЕ ВЫ НЕ МОЖЕТЕ ИСПОЛЬЗОВАТЬ ЭТОГО БОТА :(\n\nПРИЧИНА: {}""",
    "GroupCantUse" : """{} НИКОГДА НЕ ЖДУ ОТ МЕНЯ ХОРОШЕГО ОТВЕТА\n
АДМИНИСТРАЦИЯ ОГРАНИЧИЛА МЕНЯ ЗДЕСЬ РАБОТАТЬ.. 🤭""",
    "GroupCantUseDB" : """{} НИКОГДА НЕ ЖДУ ОТ МЕНЯ ХОРОШЕГО ОТВЕТА\n
АДМИНИСТРАЦИЯ ОГРАНИЧИЛА МЕНЯ ЗДЕСЬ РАБОТАТЬ.. 🤭\n\nПРИЧИНА: {}""",
    "Force" : """Подождите [{}](tg://user?id={})..!!\n
Из-за огромного трафика только участники канала могут использовать этого бота 🚶\n
Это означает, что вам нужно присоединиться к указанному ниже каналу, чтобы использовать меня!\n
Нажмите `"♻️повторить♻️"` после присоединения.. 😅""",
    "ForceCB" : {"« 🌟 ПРИСОЕДИНЯЙТЕСЬ К КАНАЛУ 🌟 »" : "{}", "« ♻️ Обновить ♻️ »" : "обновить"},
    "Fool": "Не пытайтесь обмануть.. 🤭"
}

checkPdf = {
    "pg": "`Количество страниц: •{}•` 🌟",
    "pdf" : """`Что мне делать с этим файлом?`\n\nИмя файла: `{}`\nРазмер файла: `{}`""",
    "pdfCB": {
        "« ⭐ META£ATA ⭐ »": "metaData", "« 🗳 ПРЕДВАРИТЕЛЬНЫЙ ПРОСМОТР 🗳 »": "preview",
        "« 🖼️ ИЗОБРАЖЕНИЯ 🖼️ »" : "pdf|img", "« ✏️ ТЕКСТ ✏️ »" : "pdf|txt",
        "« 🔐 ЗАШИФРОВАТЬ 🔐 »" : "work|encrypt", "« 🔒 РАСШИФРОВАТЬ 🔓 »" : "work|decrypt",
        "« 🗜 СЖАТИЕ 🗜️ »" : "work|compress", "« 🤸 ПОВОРОТ 🤸 »" : "pdf|rotate",
        "« ✂️ РАЗДЕЛИТЬ ✂️" : "pdf|split", "« ОБЪЕДИНИТЬ " : "merge", "« ™️ ПЕЧАТЬ ™️" : "pdf|stp",
        "« ✏ ПЕРЕИМЕНОВАТЬ ✏️ »" : "work|rename", "« 📝 OCR 📝 »" : "work|ocr",
        "« A4 FORMAT »" : "work|format", "« 🚫 ЗАКРЫТЬ 🚫 »" : "close|all"
    },
    "error": """__Я ничего не делаю с этим файлом__ 😏\n\n🐉 `CODEC ERROR` 🐉""",
    "errorCB" : {"❌ ОШИБКА В КОДЕКЕ ❌" : "error", "🔸 ЗАКРЫТЬ 🔸" : "close|all"},
    "encrypt": """`ФАЙЛ ЗАШИФРОВАН` 🔐\n\nИмя файла: `{}`\nРазмер файла: `{}`""",
    "encryptCB" : {"« 🔓 РАСШИФРОВАТЬ 🔓 »" : "work|decrypt"}
}

PROGRESS = {
    "progress" : """**\nГотово ✅ : **{0}/{1}\n**Скорость 🚀:** {2}/с\n**Расчетное время ⏳:** {3}""",
    "dlImage": "`Изображение загружается..⏳`", "upFile": "Началась загрузка..`📤",
    "dlFile": "`Скачивание вашего файла..` 📥", "upFileCB" : {"📤 .. ЗАГРУЗКА.. 📤" : "nabilanavab"},
    "workInP": "РАБОТА В ПРОГРЕССЕ.. 🙇", "refresh" : {"« ♻️ Обновить ♻️ »" : "{}"},
    "takeTime": """```⚙ Работа в процессе..`\n`Это может занять некоторое время..```💛""",
    "cbPRO_D" : ["📤 ЗАГРУЗИТЬ: {:.2f}% 📤", "🎯 ОТМЕНИТЬ 🎯"], "cbPRO_U" : ["📤 ЗАГРУЖЕНО: {:.2f}% 📤", "🎯 ОТМЕНИТЬ 🎯"]
}

GENERATE = {
    "deleteQueue" : "`Очередь успешно удалена..`🤧", "noQueue" : "`Очередь не создана..`😲",
    "noImages": "Изображение не найдено.!! 😒", "getFileNm": "Теперь пришлите мне имя файла 😒: ",
    "geting" : "Имя файла: `{}`\nСтраницы: `{}`", "getingCB" : {"📚 GENERATING PDF.." : "nabilanavab"},
    "currDL": "Загружено {} изображений   "
}

document = {
    "refresh" : PROGRESS['refresh'], "inWork": PROGRESS['workInP'], "reply": checkPdf['pdf'],
    "replyCB" : checkPdf['pdfCB'], "download": PROGRESS['dlFile'], "process": "⚙️ Обработка..",
    "takeTime" : PROGRESS['takeTime'], "upFile": PROGRESS['upFile'], "dlImage": PROGRESS['dlImage'],
    "big": """Из-за перегрузки владелец ограничивает {} МБ для файлов PDF 🙇
\n`Пожалуйста, пришлите мне файл меньше {}mb Size` 🙃""",
    "bigCB" : {"💎 Создать бота поддержки 2Gb 💎" : "https://github.com/nabilanavab/ilovepdf"},
    "imageAdded": """`Добавлено {} страниц в ваш pdf..`🤓\n\nfileName: `{}.pdf`""",
    "setHdImg": """Теперь изображение в PDF находится в режиме HD 😈""",
    "setDefault": {"« Вернуться к качеству по умолчанию  »" : "close|hd"},
    "error": """ЧТО-ТО пошло НЕ ТАК.. 🐉\n\nОШИБКА: `{}`""",
    "noAPI": "`Пожалуйста, добавьте конвертировать API.. 💩\n\nПуск »Настройки »API »добавить/изменить`",
    "useDOCKER": "`Файл не поддерживается, разверните бота с помощью докера`",
    "fromFile": "`Преобразовано: {} в {}`", "unsupport" : "`неподдерживаемый файл..🙄`",
    "generateRN": {"GENERATE 📚" : "generate", "RENAME ✍️" : "generateREN"},
    "generate" : {"СОЗДАТЬ 📚" : "generate"}, "cancelCB" : {"⟨ Отменить ⟩" : "close|me"}
}

noHelp = f"`никто тебе не поможет` 😏"

split = {
    "inWork": PROGRESS['workInP'], "cancelCB": document['cancelCB'],
    "download": PROGRESS['dlFile'], "exit": "`Процесс отменен..` 😏",
    "кнопка" : {
        "« ⚙️ PDF » РАЗДЕЛИТЬ ↓ »" : "nabilanavab", "« 🦞 With In Range 🦞 »" : "split|R",
        "« 🐛 Одна страница 🐛 »" : "split|S", "« НАЗАД »" : "pdf"
    },
    "work" : ["Range", "Single"], "over" : "`5 попытка завершена.. Процесс отменен..`😏",
    "pyromodASK_1" : """__Pdf Split » По диапазону\nТеперь введите диапазон (начало:конец) :__
\n/exit __для отмены__""",
    "completed": "`Загрузка завершена..` ✅",
    "error_1": "Синтаксическая ошибка: justNeedStartAndEnd `🚶",
    "error_2": "Синтаксическая ошибка: errorInEndingPageNumber `🚶",
    "error_3": "Синтаксическая ошибка: errorInStartingPageNumber `🚶",
    "error_4": "Синтаксическая ошибка: pageNumberMustBeADigit` 🧠",
    "error_5": "Синтаксическая ошибка: noEndingPageNumber Or notADigit` 🚶",
    "error_6": "`Не могу найти ни одного номера..`😏",
    "error_7": "Что-то пошло не так..`😅", "error_8": "Введите числа меньше {}..`😏",
    "error_9": "`1st Check Number of pages` 😏", "upload" : "⚙️ `Началась загрузка..` 📤"
}

pdf2IMG = {
    "inWork" : PROGRESS['workInP'], "cancelCB" : document['process'],
    "download" : PROGRESS['dlFile'], "exit" : split["upload"],
    "toImage" : {
        "» ⚙ PDF » ИЗОБРАЖЕНИЯ ↓ »" : "nabilanavab", "« 🖼 IMG 🖼 »" : "pdf|img|img",
        "« 📂 DOC 📂": "pdf|img|doc", "« 🤐 ZIP 🤐 »" : "pdf|img|zip",
        "« 🎯 TAR 🎯 »" : "pdf|img|tar", "« НАЗАД »" : "pdf"
    },
    "диапазон изображений": {
        "» ⚙️ PDF » ИЗОБРАЖЕНИЯ » {} ↓" : "nabilanavab", "🙄 ВСЕ 🙄" : "p2img|{}A",
        "« 🤧 ДИАПАЗОН 🤧 »" : "p2img|{}R", "« 🌝 СТРАНИЦЫ 🌝 »" : "p2img|{}S", "« НАЗАД »" : "pdf|img"
    },
    "over" : "`5 попытка завершена.. Процесс отменен..`😏",
    "pyromodASK_1" : """__Pdf - Img›Doc » Страницы:\nТеперь введите диапазон (начало:конец) :__
\n/exit __для отмены__""",
    "pyromodASK_2" : """"__Pdf - Img›Doc » Страницы:\nТеперь введите номера страниц, разделенные __ (,) :
\n/exit __для отмены__""",
    "exit": "`Процесс отменен..` 😏",
    "error_1": "Синтаксическая ошибка: justNeedStartAndEnd `🚶",
    "error_2": "Синтаксическая ошибка: errorInEndingPageNumber `🚶",
    "error_3": "Синтаксическая ошибка: errorInStartingPageNumber `🚶",
    "error_4": "Синтаксическая ошибка: pageNumberMustBeADigit` 🧠",
    "error_5": "Синтаксическая ошибка: noEndingPageNumber Or notADigit` 🚶",
    "error_6": "`Не могу найти номер..`😏", "error_7" : "Что-то пошло не так..`😅",
    "error_8": "`PDF содержит только {} страниц` 💩", "error_9" : "`1st Check Number of pages` 😏",
    "error_10": "__Из-за некоторых ограничений бот отправляет только 50 страниц в ZIP-архиве..__😅",
    "total": "`Всего страниц: {}..⏳`", "upload": "`Загружается: {}/{} страниц.. 🐬`",
    "current": "`Преобразовано: {}/{} страниц.. 🤞`", "complete" : "`Загрузка завершена.. `🏌️",
    "canceledAT" : "`Отменено на {}/{} страниц..` 🙄", "cbAns" : "⚙️ Окейда, Отмена.. ",
    "cancelCB" : {"💤 ОТМЕНА 💤" : "close|P2I"}, # РЕДАКТИРОВАНИЕ: ❌
    "canceledCB" : {"🍄 ОТМЕНЕНО 🍄" : "close|P2IDONE"},
    "completed" : {"😎 COMPLETED 😎" : "close|P2ICOMP"}
}

merge = {
    "inWork" : PROGRESS['workInP'], "process" : document['process'], "upload": PROGRESS['upFile'],
    "load" : "__Из-за перегрузки вы можете объединить только 5 PDF-файлов за раз__",
    "sizeLoad" : "`Из-за перегрузки бот поддерживает только %sMb pdf..", # удаление %s показывает ошибку
    "pyromodASK" : """__MERGE pdf » Всего pdf в очереди: {}__

/exit __для отмены__
/merge __to merge__""",
    "exit": "Процесс отменен..` 😏", "total" : "Все PDF-файлы: {} 💡",
    "current": "__Началась загрузка Pdf: {} 📥__", "cancel" : "`Процесс слияния отменен.. 😏`",
    "started" : "__Merging Started.. __   ", "caption" : "`слияние pdf 🙂`",
    "error": "`Файл может быть зашифрован..`\n\nПричина: {}"
}

metaData = {
    "inWork": PROGRESS['workInP'], "process": document['process'], "download": PROGRESS['dlFile'], # [❌]
    "read" : "Пожалуйста, прочитайте это сообщение еще раз..   "
}

preview = {
    "inWork": PROGRESS['workInP'], "process": document['process'], "error": document['error'],
    "download": PROGRESS['dlFile'], "_": "PDF содержит только {} страниц 🤓\n\n",
    "__": "Страниц PDF: {}\n\n", "total" : "`Всего страниц: {}..`   ",
    "album": "`Подготовка альбома..` 🤹", "upload" : f"`Загрузка: страницы предварительного просмотра.. 🐬`"
}

stamp = {
    "stamp" : {
        "« ⚙ PDF » ПЕЧАТЬ ↓ »" : "nabilanavab",
        "« Не для публичной публикации 🤧 »": "pdf|stp|10",
        "« Для публичного выпуска 🥱 »": "pdf|stp|8",
        "« Конфиденциально 🤫 »" : "pdf|stp|2", "« Ведомственный 🤝 »" : "pdf|stp|3",
        "« Экспериментальный 🔬 »" : "pdf|stp|4", "« Просрочено 🐀 »" : "pdf|stp|5",
        "« Окончательный 🔧 »" : "pdf|stp|6", "« Для комментария 🗯️ »" : "pdf|stp|7",
        "« Не утверждено 😒 »" : "pdf|stp|9", "« Утверждено 🥳 »" : "pdf|stp|0",
        "« Продано ✊ »": "pdf|stp|11", "« Совершенно секретно 😷 »": "pdf|stp|12",
        "« Черновик 👀 »" : "pdf|stp|13", "« как есть 🤏 »" : "pdf|stp|1",
        "« НАЗАД »" : "pdf"
    },
    "stampA" : {
        "« ⚙ PDF » ПЕЧАТЬ » ЦВЕТ ↓»" : "nabilanavab",
        "« Красный ❤️ »" : "spP|{}|r", "« Синий 💙 »" : "spP|{}|b",
        "« Зеленый 💚 »" : "spP|{}|g", "« Желтый 💛 »" : "spP|{}|c1",
        "« Розовый 💜 »" : "spP|{}|c2", "« Оттенок 💚 »" : "spP|{}|c3",
        "« Белые 🤍 »" : "spP|{}|c4", "« Черные 🖤 »" : "spP|{}|c5",
        "« Назад »" : "pdf|stp"
    },
    "inWork": PROGRESS ['workInP'], "document" : document ['process'],
    "download": PROGRESS ['dlFile'], "upload": PROGRESS ['upFile'],
    "stamping": "`Начато штампование..` 💠", "caption": """stamped pdf\ncolor: `{}`\nannot: `{}`"""
}

work = {
    "inWork": PROGRESS['workInP'], "document" : document['process'],
    "download": PROGRESS ['dlFile'], "takeTime": PROGRESS ['takeTime'],
    "upload": PROGRESS['upFile'], "button": document['cancelCB'],
    "rot360": "У вас большая проблема..🙂", "ocrError": "Владелец ограничен 😎  ",
    "largeNo" : "отправить pdf файл менее 5 страниц.. 🙄",
    "pyromodASK_1" : """__PDF {} »\nТеперь введите пароль :__\n\n/exit __для отмены__""",
    "pyromodASK_2" : """__Переименовать PDF »\nТеперь введите новое имя:__\n\n/exit __для отмены__""",
    "exit" : "процесс отменен.. `😏", "ren_caption" : "__Новое имя: __ `{}`",
    "notENCRYPTED": "`Файл не зашифрован..` 👀",
    "compress": "⚙️ `Начало сжатие.. 🌡️\nЭто может занять некоторое время..`💛",
    "decrypt": "⚙️ `Началась расшифровка.. 🔓\nЭто может занять некоторое время..`💛",
    "encrypt": "⚙️ `Шифрование началось.. 🔐\nЭто может занять некоторое время..`💛",
    "ocr": "⚙️ `Добавление слоя OCR.. ✍️\nЭто может занять некоторое время..`💛",
    "format": "⚙️ `Началось форматирование.. 🤘\nЭто может занять некоторое время..`💛",
    "rename" : "⚙️ `Переименование PDf.. ✏️\nЭто может занять некоторое время..`💛",
    "rot" : "⚙️ `Поворот PDf.. 🤸\nЭто может занять некоторое время..`💛",
    "pdfTxt": "⚙️ `Извлечение текста.. 🐾\nЭто может занять некоторое время..`💛",
    "fileNm": "Старое имя файла: {}\nНовое имя файла: {}",
    "rotate" : {
        "» ⚙️ PDF » ROTETE ↓ »" : "nabilanavab", "« 90° »" : "work|rot90", "« 180° »" : "work|rot180",
        "« 270° »" : "work|rot270", "« 360° »": "work|rot360", "« НАЗАД »" : "pdf"
    },
    "txt" : {
        "» ⚙️ PDF » TXT ↓ »" : "nabilanavab", "« 📜 СООБЩЕНИЕ 📜 »" : "work|M", "« 🧾 TXT FIL 🧾 »" : "work|T",
        "« 🌐 HTML 🌐 »" : "work|H", "« 🎀 JSON 🎀 »" : "work|J", "« НАЗАД »" : "pdf"
    }
}

PROCESS = {
    "ocr" : "Добавлено OCR", "decryptError" : "__Не удается расшифровать файл с помощью __ `{}` 🕸️",
    "decrypted": "__Расшифрованный файл__", "encrypted": "__Номер страницы__: {}\n__key__ 🔐: ||{}||",
    "compressed": """`Исходный размер: {}\nСжатый размер: {}\n\nСоотношение: {:.2f} %`""",
    "cantCompress": "Файл не может быть сжат сильнее..🤐",
    "pgNoError" : """__По какой-то причине ФОРМАТИРОВАНИЕ A4 Поддерживает PDF-файлы с менее чем 5 страницами__\n\nВсего страниц: {} ⭐""",
    "ocrError": "`Уже есть текстовый слой.. `😏",
    "90": "__Поворот на 90°__", "180": "__Поворот на 180°__", "270": "__Поворот на 270°__",
    "formatted": "Файл в формате A4", "M": "♻ Извлечено {} страниц ♻",
    "H": "HTML-файл", "T": "TXT-файл", "J": "JSON-файл"
}

pdf2TXT = {
    "upload": PROGRESS["upFile"], "exit" : split['exit'], "nothing" : "Нечего создавать.. 😏",
    "TEXT" : "`Создать PDF из текстовых сообщений »`", "start" : "Начато преобразование txt в Pdf..🎉",
    "font_btn": {
        "TXT@PDF » SET FONT »" : "nabilanavab", "« Times »" : "pdf|font|t", "« Courier »" : "pdf|font|c", "« Helvetica (по умолчанию) »" : "pdf|font|h",
        "« Symbol »": "pdf|font|s", "« Zapfdingbats »": "pdf|font|z", "« 🚫 CLOSE 🚫 »": "close|me"
    },
    "size_btn" : { "TXT@PDF » {} » SET SCALE »" : "nabilanavab", "« Portarate »" : "t2p|{}|p", "« Landscape »" : "t2p|{}|l", "« Назад «": "pdf|T2P"},
    "askT" : "__ТЕКСТ В PDF » Теперь введите НАЗВАНИЕ: __\n\n/exit __для отмены__\n/skip __для пропуска__",
    "askC" : "__ТЕКСТ В PDF» Теперь введите абзац {}:__\n\n/exit __для отмены__\n/create __для создания__"
}

URL = {
    "get" : {"   Получить файл PDF   " : "getFile"}, "close" : HELP_CMD['CB'], "notPDF" : "`Не файл PDF",
    "error" : "🐉 ЧТО-ТО ПОШЛО НЕ ТАК 🐉\n\nОШИБКА: `{}`\n\nNB: в группах боты могут получать документы только после присоединения к группе =)",
    "done" : "```Почти готово.. ✅\nТеперь началась загрузка.. 📤```", "_error_" : "отправьте мне любой URL-адрес или прямую ссылку на телеграмму в формате pdf",
    "openCB" : {"Открыть в браузере" : "{}"}, "_error" : "`Что-то пошло не так =(`\n\n`{}`",
    "_get" : "[Открыть чат]({})\n\n**О ЧАТЕ ↓**\nТип чата: {}\nИмя чата: {}\nПользователь чата: @{}\n"
             "Идентификатор чата: {}\nДата: {}\n\n**О МЕДИА ↓**\nМедиа: {}\nИмя файла: {}\nРазмер файла: {}\n\nТип файла: {}"
}

getFILE = {
    "inWork" : PROGRESS['workInP'], "big" : "send pdf url less than {}mb", "wait" : "Wait.. Let me.. 😜",
    "dl" : {"📥 ..DOWNLOADING.. 📥" : "nabilanavab"}, "up" : {"📤 ..UPLOADING..  📤" : "nabilanavab"},
    "complete" : {"😎 COMPLETED 😎" : f"{str(settings.SOURCE_CODE)}"}
}

cbAns = [
    "This feature is Under Development ⛷️", "Error annenn paranjille.. then what.. 😏",
    "Process Canceled.. 😏", "File Not Encrypted.. 👀", "Nothing Official About it.. 😅", "🎉 Completed.. 🏃"
]

inline_query = {
    "TOP" : { "Now, Select Language ➟" : "nabilanavab" }, "capt" : "SET LANGUAGE ⚙️", "des" : "By: @nabilanavab ❤"
}

# ===================================================================================================================================[NABIL A NAVAB -> TG: nabilanavab]
