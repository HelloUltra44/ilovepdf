# LANG: ARABIC LANG_CODE: ARB                                      >>  copyright ©️ 2021 ajak4405  <<                                           fileName : lang/ARB.py
#                                        Thank: ajak4405                                                   E-mail: ajak4405@gmail.com

from configs.config import settings

# رسالة ترحيب مساءاً (المنزل أ , ب , ج , د ...)
HOME = {
    "HomeA": """مرحبًا [{}](tg://user?id={}) .. !!
سيساعدك هذا الروبوت على القيام بالعديد من الأشياء باستخدام ملفات pdf 🥳

بعض الميزات الرئيسية هي: \n◍ تحويل الصور إلى PDF
◍ `تحويل PDF إلى صور` \n◍` تحويل الملفات إلى pdf` """,
    "HomeACB": {
        "⚙️ الإعدادات ⚙️": "Home|B" , "⚠️ مساعدة ⚠️": "Home|C",
        "📢 القناة 📢": f"{str(settings.OWNED_CHANNEL)}",
        "🌟 كود المصدر 🌟": f"{str(settings.SOURCE_CODE)}",
        "🚶 قريب 🚶": "close|mee"
    } ,
    "HomeAdminCB": {
        "⚙️ الإعدادات ⚙️": "Home|B" , "⚠️ مساعدة ⚠️": "Home|C",
        "📢 القناة 📢": f"{str(settings.OWNED_CHANNEL)}",
        "🌟 كود المصدر 🌟": f"{str(settings.SOURCE_CODE)}",
        "🗽 STATUS 🗽": "status|home", "🚶 قريب 🚶": "close|mee"
    } ,
    "HomeB": """صفحة الإعدادات ⚙️ \n \n اسم المستخدم: {}
معرّف المستخدم: {} \n اسم المستخدم: {} \n تاريخ التسجيل: {} \n
اللغة: {} \n API: {}
الإبهام: {} \n التسمية التوضيحية: {} \n اسم الملف: {} """,
    "HomeBCB": {
        "🌍 LANG 🌍": "set|lang", "📍 THUMB 📍": "set|thumb",
        "📈 NAME 📈": "set|fname", "💩 API 💩": "set|api",
        "📅 CAPTION 📅": "set|capt", "«العودة إلى الصفحة الرئيسية« ": "Home|B2A"
    } ,
    "HomeC": """🪂 ** HELP MESSAGE **:

``` بعض الميزات الرئيسية هي:
 ◍ تحويل الصور إلى PDF \n ◍ Manupultions PDF \n ◍ العديد من برامج الترميز الشائعة إلى pdf
 
تعديل ملف pdf:
 ◍ PDF⥃ الصور [الكل , النطاق , الصفحات] \n ◍ المستندات إلى PDF [png , jpg , jpeg] \n ◍ الصور PDF \n ◍ بيانات PDF الوصفية \n ◍ PDF⥃TEXT \n ◍ TEXT⥃PDF \n ◍ ضغط ملف pdf
 ◍ انقسام PDF [النطاق , الصفحات] \n ◍ دمج PDF \n ◍ إضافة طابع \n ◍ إعادة تسمية PDF \n ◍ تدوير PDF \n ◍ ENCRYPT / DECRYPT PDF \n ◍ PDF FORMATTER \n ◍ PDF⥃JSON / TXT FILE
 ◍ PDF⥃HTML [عرض الويب] \n ◍ URL⥃PDF \n ◍ PDF⥃ZIP / TAR / RAR [الكل , النطاق , الصفحات] \n وأكثر من ذلك بكثير .. """ ,
    "HomeCCB": {"« BACK HOME «": "Home|A", "🛈 INSTRUCTIONS 🛈": "Home|D"},
    "HomeD": """` نظرًا لأن هذه خدمة مجانية , لا يمكنني ضمان المدة التي يمكنني خلالها الحفاظ على هذه الخدمة ..`😝
 
⚠️ تعليمات ⚠️:
🛈 __يرجى عدم محاولة إساءة استخدام إدارة Bot__ 😒
🛈 __لا ترسل بريدًا عشوائيًا هنا , فقد يؤدي ذلك إلى حظر دائم 🎲__.
🛈 __محتويات الاباحيه ايضا ستمنحك حظر دائم 💯__

** أرسل أي صورة لتبدأ: ** 😁 """,
    "HomeDCB": {"⚠️ HELP ⚠️": "Home|C", "» BACK HOME »": "Home|A"}
}

SETTINGS = {
    "default": [" إفتراضي ❌", "✅"], "chgLang": {"SETTING ⚙️» تغيير اللغة 🌐 ":" ajak4405 "},
    "error": "حدث خطأ ما أثناء استرداد البيانات من قاعدة البيانات" , "lang": "الآن , حدد أي لغة .." ,
    "ask": ["الآن , أرسل لي .." , "الآن , أرسل لي .. 😅 \n \n سريع.! ليس لدي المزيد من الوقت لاستعراض النص .. 😏 \n \n / إلغاء: للإلغاء "] ,
    "askApi": "\n \n افتح الرابط أدناه وأرسل لي الرمز السري:", "waitApi": {"فتح الرابط ✅": "https://www.convertapi.com/a/signin"},
    "wait": {"Waiting .. 🥱": "ajak4405"}, "back": {"« BACK TO HOME «": "Home|B2S"}, "errorCB": {"«العودة إلى الصفحة الرئيسية« ": "Home|B2A"} ,
    "result": ["لا يمكن تحديث الإعدادات ❌" , "تم تحديث الإعدادات بنجاح ✅"] , "cant": "لا يمكن استخدام هذه الميزة ❌" ,
    "feedback": "تقييمات من عملاء رائعين مثلك تساعد الآخرين. \n @ ajak4405"
                 "\n \n الإبلاغ عن خطأ في {} اللغة: \n` • تحديد اللغة \n • رسالة الخطأ \n • رسالة جديدة`",
    "feedbtn": {"Report Lang Error": settings.REPORT},
    "thumb" : [
        {"SETTING ⚙️» THUMBNAIL 📷 ":"ajak4405"," ♻ يضيف ♻ ":"set|thumb+"," «BACK TO HOME« ":"Home|B"},
        {"SETTING ⚙️» THUMBNAIL 📷 ":"ajak4405"," ♻ يتغيرون ♻ ":"set|thumb+"," DELETE 🗑 ":"set|thumb-"," ««العودة إلى الصفحة الرئيسية« ":"Home|B2S"}
    ],
    "fname": [
        {"SETTING ⚙️» FNAME 📷 ":"ajak4405"," ♻ يضيف ♻ ":"set|fname+"," «BACK TO HOME« ":"Home|B2S"},
        {"SETTING ⚙️» FNAME 📷 ":"ajak4405"," ♻ يتغيرون ♻ ":"set|fname+"," DELETE 🗑 ":"set|fname-"," «العودة إلى الصفحة الرئيسية« ":"Home|B2S"}
    ] ,
    "api": [
        {"SETTING ⚙️» API 📷 ​​":"ajak4405"," ♻ يضيف ♻ ":"set|api+"," «BACK TO HOME« ":"Home|B2S"},
        {"SETTING ⚙️» API 📷 ​​":"ajak4405"," ♻ يتغيرون ♻ ":"set|api+"," 🗑 DELETE 🗑 ":"set|api-"," «العودة إلى الصفحة الرئيسية« ":"Home|B2S"}
    ] ,
    "capt": [
        {"الإعداد ⚙️» التسمية التوضيحية 📷":"ajak4405"," ♻ يضيف ♻ ":"set|capt+"," «العودة إلى الصفحة الرئيسية« ":"Home|B2S"},
        {"الإعداد ⚙️» التسمية التوضيحية 📷":"ajak4405"," ♻ يتغيرون ♻ ":"set|capt+"," DELETE 🗑 ":"set|capt-","«العودة إلى الصفحة الرئيسية« ":"Home|B2S"}
    ]
}

BOT_COMMAND = {"start": "رسالة ترحيب ..", "txt2pdf": "إنشاء ملف PDF نصي"}

HELP_CMD = {
    "userHELP": """[رسائل أوامر المستخدم]: \n
/ البدء: للتحقق مما إذا كان Bot على قيد الحياة \n / إلغاء: إلغاء العمل الحالي
/ delete: مسح الصورة لقائمة انتظار pdf \n / txt2pdf: نص إلى pdf "" ",
    "تعليمات المسؤول": "" "\n \n \n [رسائل أوامر المسؤول]: \n
/ send: للبث , رسالة pm "" ",
    "footerHelp": f "" "\n \n \n رمز المصدر: [i 💜 PDF] ({str (settings.SOURCE_CODE)})
البوت:complete_pdf_bot 💎 \n [قناة الدعم] ({settings.OWNED_CHANNEL}) """,
    "CB": {"⚠️ قريب ⚠️": "close|all"}
}

STATUS_MSG = {
    "HOME": "الآن , حدد أي خيار أدناه للحصول على الحالة الحالية 💱 ..` ",
    "_HOME" : {
        "📊 ↓ SERVER ↓ 📊": "ajak4405", "📶 STORAGE 📶": "status|server",
        "🥥 قاعدة البيانات 🥥": "status|db" , "🌝 ↓ الحصول على قائمة ↓ 🌝": "ajak4405",
        "💎 المشرف 💎": "status|admin", "👤 المستخدمون 👤": "status|users",
        "« رجوع  «": "Home|A"
    } ,
    "DB": """📂 قاعدة البيانات: \n \n ** ◍ مستخدمو قاعدة البيانات: **` {} `📍 \n ** ◍ محادثات قاعدة البيانات: **` {} `📍""" ,
    "SERVER": """** ◍ المساحة الإجمالية: **` {} `
** ◍ المساحة المستخدمة: ** `{} ({}٪)` \n ** ◍ مساحة حرة: ** `{}`
** ◍ استخدام وحدة المعالجة المركزية: ** "{}`٪ \n ** ◍ استخدام ذاكرة الوصول العشوائي: ** `{}`٪
** ◍ العمل الحالي: ** `{}` \n ** ◍ معرف الرسالة: ** `{}""" ,
    "BACK": {"« BACK «": "status|home"}, "ADMIN": "** Total ADMIN: ** __ {} __ \n",
    "USERS": "المستخدمون: \n\n" , "NO_DB": "لم يتم تعيين قاعدة البيانات بعد 💩"
}

feedbackMsg = f"[اكتب تعليقًا 📋]({settings.FEEDBACK})"

# رسالة ترحيب المجموعة
HomeG = {
    "HomeA": """مرحبًا.! 🖐️ \n أنا جديد هنا {message.chat.title} \n
اسمحوا لي أن أقدم نفسي .. \n اسمي هو iLovePDF , ويمكنني مساعدتك في القيام بالكثير
أشياء مع ملفات @ Telegram PDF \n \n شكرًاajak4405 على هذا الروبوت الرائع 😅 """,
    "HomeACB": {
        "🤠 BOT OWNER 🤠": f"https://telegram.dog/{settings.OWNER_USERNAME}",
        "🛡️ UPDATE CHANNEL 🛡️": f"{settings.OWNED_CHANNEL}", "🌟 SOURCE CODE 🌟": f"{settings.SOURCE_CODE}"
    }
}

# واجهة مستخدم محظورة
BAN = {
    "cbNotU": "الرسالة ليست لك .. 😏",
    "banCB": {
        "إنشاء الروبوت الخاص بك": f"{settings.SOURCE_CODE}" , "البرنامج التعليمي": f"{settings.SOURCE_CODE}" ,
        "تحديث القناة": "https://telegram.dog/anumitultrabots"
    } ,
    "UCantUse": """مرحبًا {} \n \n لبعض الأسباب التي تجعلك لا تستطيع استخدام هذا BOT :(""",
    "UCantUseDB": """مرحبًا {} \n \n لبعض الأسباب التي تجعلك لا تستطيع استخدام هذا الروبوت: (\n \n السبب: {}""",
    "GroupCantUse": """{} لا تتوقع أبدًا استجابة جيدة مني \n
منعني المسؤولون من العمل هنا .. 🤭 """,
    "GroupCantUseDB": """{} لا تتوقع أبدًا استجابة جيدة مني \n
منعني المسؤولون من العمل هنا .. 🤭 \n \n السبب: {} """,
    "Force": """انتظر [{}](tg://user?id={}) .. !! \n
نظرًا لحركة المرور الهائلة , يمكن لأعضاء القناة فقط استخدام هذا الروبوت 🚶 \n
هذا يعني أنك بحاجة إلى الانضمام إلى القناة المذكورة أدناه لاستخدامي! \n
اضغط على "♻️retry♻️" `بعد الانضمام .. 😅""" ,
    "ForceCB": {"🌟 JOIN CHANNEL 🌟": "{}", "♻️ Refresh ♻️": "Refresh"},
    "Fool": "لا يمكنك أن تخدعني. 🤭"
}

checkPdf = {
    "pg": "عدد الصفحات: • {} •` 🌟 ",
    "pdf": """` ماذا أفعل بهذا الملف .؟`\n\n اسم الملف: `{}` \n حجم الملف: `{}` """,
    "pdfCB": {
        "⭐ META £ ATA ⭐": "metaData", "PREVIEW 🗳️": "preview",
        "🖼️ الصور 🖼️": "pdf|img", "✏️ TEXT ✏️": "pdf|txt",
        "🔐 ENCRYPT 🔐": "work|encrypt", "🔒 DECRYPT 🔓": "work|decrypt",
        "🗜️ COMPRESS 🗜️": "work|compress", "🤸 تدوير 🤸": "pdf|rotate",
        "✂️ SPLIT ✂️": "pdf|split", "🧬 MERGE 🧬": "merge", "™ ️ STAMP ™ ️": "pdf|stp",
        "✏️ RENAME ✏️": "work|rename", "📝 OCR 📝": "work|ocr",
         "🥷 تنسيق A4": "work|format", "🚫 قريب 🚫": "close|all"
    } ,
    "error": """__ لا أفعل أي شيء بهذا الملف__ 😏 \n \n🐉` خطأ CODEC` 🐉 """,
    "errorCB": {"❌ ERROR IN CODEC ❌": "error", "🔸 قريب 🔸": "close|all"},
    "encrypt": """` FILE IS ENCRYPTED` 🔐 \n \n اسم الملف: `{}` \n حجم الملف: `{}` """,
    "encryptCB": {"🔓 DECRYPT 🔓": "work|decrypt"}
}

PROGRESS = {
    "progress": """** \n تم ✅: ** {0} / {1} \n ** السرعة 🚀: ** {2} / ثانية \n ** الوقت المقدر ⏳: ** {3}""" ,
    "dlImage": " جارٍ تنزيل صورتك ..⏳` ","upFile":" `بدء التحميل ...`📤",
    "dlFile": "` جارٍ تنزيل ملفك ..` 📥 ","upFileCB": {" 📤 .. UPLOADING .. 📤 ":" ajak4405 "},
    "workInP": "العمل قيد التقدم .. 🙇", "refresh": {"♻️ Refresh ♻️": "{}"},
    "takeTime": """`العمل جاري ...` \n` قد يستغرق بعض الوقت ...`""",
    "cbPRO_D": ["📤 DOWNLOAD: {: .2f}٪ 📤", "🎯 CANCEL 🎯"], "cbPRO_U": ["📤 UPLOADED: {: .2f}٪ 📤", "🎯 CANCEL 🎯"]
}

GENERATE = {
    "deleteQueue": "تم حذف قائمة الانتظار بنجاح ..`🤧", "noQueue": "لم يتم تأسيس قائمة انتظار ..`😲",
    "noImages": "لم يتم إنشاء صورة. !! 😒", "getFileNm": "الآن أرسل لي اسم ملف 😒:",
    "geting": "اسم الملف:` {} `\n الصفحات:` {} `", "getingCB": {"📚 GENERATING PDF ..": "ajak4405"},
    "currDL ":" الصور {} التي تم تنزيلها 🥱 "
}

document = {
    "refresh": PROGRESS['refresh'] , "inWork": PROGRESS['workInP'] , "reply": checkPdf['pdf'] ,
    "replyCB": checkPdf['pdfCB'], "download": PROGRESS['dlFile'], "process": "⚙️ يعالج..",
    "takeTime": PROGRESS['takeTime'], "upFile": PROGRESS['upFile'], "dlImage": PROGRESS['dlImage'],
    "big": """بسبب الحمل الزائد , حدود المالك {} ميغابايت لملفات pdf 🙇
\n` ارجوك ارسل لي ملف اقل من {} ميغا بايت الحجم` 🙃 """,
    "bigCB": {"💎 إنشاء بوت دعم 2 جيجا بايت 💎": "https://github.com/ajak4405/ilovepdf"},
    "imageAdded": """تمت إضافة {} صفحة / صفحة إلى ملف pdf الخاص بك ..`🤓 \n \n اسم الملف:` {} .pdf` """,
    "setHdImg": """الآن صورة إلى PDF في وضع HD""",
    "setDefault": {"« رجوع إلى الجودة الافتراضية «": "close|hd"},
    "error": """حدث خطأ ما .. 🐉 \n\n الخطأ:` {} """,
    "noAPI": "` الرجاء إضافة تحويل API .. 💩 \n\n ابدأ »الإعدادات» api »add / change`",
    "useDOCKER": " الملف غير مدعوم , انشر الروبوت باستخدام docker` ",
    "fromFile": "` تم التحويل: {} إلى {} `", "unsupport": "` ملف غير مدعوم..🙄` ",
    "generateRN": {"إنشاء 📚": "generate" , "إعادة تسمية ✍️": "generateREN"} ,
    "generate": {"إنشاء 📚": "generate"} , "cancelCB": {"⟨قريب⟩": "close|me"}
}

noHelp = "`لن يساعدك أحد` 😏 "

split = {
    "inWork": PROGRESS['workInP'], "cancelCB": document['cancelCB'] ,
    "download": PROGRESS['dlFile'], "exit": "` Process Canceled..` 😏 ",
    "button" : {
        "⚙️ PDF» SPLIT ↓ ":" ajak4405 "," مع في النطاق 🦞 ":"split|R",
        "صفحة واحدة 🐛": "split|S", "« BACK «": "pdf"
    } ,
    "work": ["النطاق" , "واحد"] , "أكثر من": " 5 محاولة .. تم إلغاء العملية ..`😏 ",
    "pyromodASK_1": """ __Pdf انقسام »حسب النطاق \n الآن , أدخل النطاق (البداية: النهاية): __
\n /exit __لإلغاء__ """,
    "completed": "اكتمل التنزيل ..` ✅",
    "error_1": "خطأ في بناء الجملة: justNeedStartAndEnd` ",
    "error_2": "خطأ في بناء الجملة: errorInEndingPageNumber` ",
    "error_3": "خطأ في بناء الجملة: errorInStartingPageNumber` ",
    "error_4": "خطأ في بناء الجملة: pageNumberMustBeADigit` 🧠",
    "error_5": "خطأ في بناء الجملة: noEndingPageNumber Or notADigit` 🚶",
    "error_6": " تعذر العثور على أي رقم ..`😏 ",
    "error_7": "حدث خطأ ما ..`😅", "error_8": "أدخل أرقامًا أقل من {} ..` 😏 ",
    "error_9": " التحقق الأول من عدد الصفحات` 😏 ","upload":" ⚙️ `بدء التحميل ...` 📤"
}

pdf2IMG = {
    "inWork": PROGRESS['workInP'], "process": document['process'],
    "download": PROGRESS['dlFile'], "uploadfile": split["upload"],
    "toImage": {
        "⚙️ PDF» صور ↓ ":"ajak4405"," 🖼 IMG 🖼 ":"pdf|img|img",
        "📂 DOC 📂": "pdf|img|doc", "🤐 ZIP 🤐": "pdf|img|zip" ,
        "🎯 TAR 🎯": "pdf|img|tar", "« BACK «": "pdf"
    } ,
    "imgRange": {
        "⚙️ PDF» صور »{} ↓": "ajak4405", "🙄 ALL 🙄": "p2img|{}A",
        "🤧 RANGE 🤧": "p2img|{}R", "🌝 PAGES 🌝": "p2img|{}S", "« BACK «": "pdf|img"
    } ,
    "over": " 5 محاولات .. تم إلغاء العملية ..`😏 ",
    "pyromodASK_1": """ __Pdf - Img ›Doc» الصفحات: \n الآن , أدخل النطاق (البداية: النهاية): __
\n / خروج __لإلغاء__ """,
    "pyromodASK_2": """ __Pdf - Img ›Doc» الصفحات: \n الآن , أدخل أرقام الصفحات مفصولة بـ__ (,):
\n / خروج __لإلغاء__ """,
    "exit": "إلغاء العملية ..` 😏",
    "error_1": "خطأ في بناء الجملة: justNeedStartAndEnd` ",
    "error_2": "خطأ في بناء الجملة: errorInEndingPageNumber` ",
    "error_3": "خطأ في بناء الجملة: errorInStartingPageNumber` ",
    "error_4": "خطأ في بناء الجملة: pageNumberMustBeADigit` 🧠",
    "error_5": "خطأ في بناء الجملة: noEndingPageNumber Or notADigit` 🚶",
    "error_6": " تعذر العثور على أي رقم ..`😏 "," error_7 ":" `حدث خطأ ما ..`😅",
    "error_8": "يحتوي` PDF فقط على {} صفحات` 💩 "," error_9 ":" التحقق الأول من عدد الصفحات` 😏 ",
    "error_10": "__بسبب بعض القيود يرسل البوت 50 صفحة فقط على هيئة ZIP ..__ 😅",
    "total": "` إجمالي الصفحات: {} .. ⏳` ","upload":" `تحميل: {} / {} صفحات .. 🐬`",
    "current": "` تم تحويلها: {} / {} صفحات .. 🤞` ","complete":" اكتمل التحميل .. `🏌️",
    "cancelledAT": "` تم الإلغاء عند {} / {} من الصفحات..` 🙄 ","cbAns":" ⚙️ Okeyda, Canceling .. ",
    "cancelCB": {"💤 CANCEL 💤": "close|P2I"}, # EDITABLE: ❌
    "canceledCB": {"🍄 CANCELED 🍄": "close|P2IDONE"},
    "completed": {"😎 COMPLETED 😎": "close|P2ICOMP"}
}

merge = {
    "inWork": PROGRESS['workInP'] , "process": document['process'] , "upload": PROGRESS['upFile'] ,
    "load": "__بسبب التحميل الزائد , يمكنك فقط دمج 5 ملفات PDF في وقت واحد__" ,
    "sizeLoad": "بسبب التحميل الزائد للبوت فقط دعم٪ sMb pdfs .." , # إزالة٪ s عرض خطأ
    "pyromodASK": """__MERGE pdfs» إجمالي ملفات PDF في قائمة الانتظار: {} __

/exit __لإلغاء__
/merge __لدمج__ """,
    "exit": "إلغاء العملية..` 😏", "total": "إجمالي ملفات PDF: {} 💡",
    "current": "__Started Downloading Pdf: {} 📥__", "cancel": "إلغاء عملية الدمج .. 😏`",
    "started": "__ بدأ الدمج .. __ 🪄", "caption": "` pdf مدمج 🙂` ",
    "error": "قد يكون ملف مشفر ...` \n \n السبب: {}"
}

metaData = {
    "inWork": PROGRESS ['workInP'], "process": document['process'], "download": PROGRESS['dlFile'], # [❌]
    "read": "الرجاء قراءة هذه الرسالة مرة أخرى .. 🥴"
}

المعاينة = {
    "inWork": PROGRESS ['workInP'] , "process": document['process'] , "error": document['error'] ,
    "download": PROGRESS ['dlFile'], "_": "يحتوي ملف PDF على {} صفحات فقط 🤓 \n \n",
    "__": "صفحات PDF: {} \n \n", "total": "إجمالي الصفحات: {} ..` 🤌 ",
    "album": "تحضير ألبوم ..` 🤹", "upload": f"` تحميل: معاينة الصفحات .. 🐬` "
}

stamp = {
    "stamp": {
        "⚙️ PDF» STAMP ↓ ":"ajak4405",
        "ليس للنشر العام 🤧": "pdf|stp|10",
        "للإصدار العام 🥱": "pdf|stp|8",
        "سري 🤫": "pdf|stp|2", "Departmental 🤝": "pdf|stp|3",
        "التجريبية 🔬": "pdf|stp|4", "انتهاء الصلاحية 🐀": "pdf|stp|5",
        "نهائي 🔧": "pdf|stp|6", "للتعليق 🗯️": "pdf|stp|7",
        "غير معتمد 😒": "pdf|stp|9", "موافق عليه 🥳": "pdf|stp|0",
        "تم البيع ✊": "pdf|stp|11", "سري للغاية 😷": "pdf|stp|12",
        "مسودة 👀": "pdf|stp|13", "AsIs 🤏": "pdf|stp|1",
        "« رجوع «": "pdf"
    } ,
    "stampA": {
        "⚙️ PDF» STAMP »COLOR ↓": "ajak4405" ,
        "أحمر ❤️": "spP|{}|r", "أزرق 💙": "spP|{}|b" ,
        "أخضر 💚": "spP|{}|g", "Yellow 💛": "spP|{}|c1",
        "الوردي 💜": "spP|{}|c2" , "Hue 💚": "spP|{}|c3" ,
        "أبيض 🤍": "spP|{}|c4", "أسود 🖤": "spP|{}|c5" ,
        "« رجوع «": "pdf|stp"
    } ,
    "inWork": PROGRESS['workInP'], "process": document['process'],
    "download": PROGRESS['dlFile'] , "upload": PROGRESS['upFile'] ,
    "stamping": "بدء ختم..` 💠", "caption": """pdf مختوم \n اللون:` {} `\n لا:` {} `"""
}

work = {
    "inWork": PROGRESS['workInP'], "process": document['process'],
    "download": PROGRESS['dlFile'], "takeTime": PROGRESS ['takeTime'],
    "upload": PROGRESS['upFile'], "button": document['cancelCB'] ,
    "rot360": "لديك مشكلة كبيرة ..🙂" , "ocrError": "مالك مقيد 😎🤏" ,
    "largeNo": "أرسل ملف pdf أقل من 5 صفحات .. 🙄",
    "pyromodASK_1": """ __PDF {} »\n الآن , الرجاء إدخال كلمة المرور: __ \n \n / exit __ لإلغاء__""",
    "pyromodASK_2": """ __إعادة تسمية PDF »\n الآن , الرجاء إدخال الاسم الجديد: __ \n \n / خروج __ لإلغاء__""" ,
    "exit": "إلغاء العملية .. 😏 ","ren_caption":" __الاسم الجديد: __ `{}` ",
    "notENCRYPTED": "` الملف غير مشفر ..` 👀 ",
    "compress": "` بدأ الضغط .. 🌡️ \n قد يستغرق بعض الوقت ..`💛 ",
    "decrypt": "⚙️` بدأ فك التشفير .. 🔓 \n قد يستغرق بعض الوقت ..`💛 ",
    "encrypt": "⚙️` بدأ التشفير .. 🔐 \n قد يستغرق بعض الوقت ..`💛 ",
    "ocr": "⚙️` Adding OCR Layer .. ✍️ \n قد يستغرق بعض الوقت ..`💛 ",
    "format": "⚙️` بدء التنسيق .. 🤘 \n قد يستغرق بعض الوقت ..`💛 ",
    "rename": "⚙️` إعادة تسمية PDf .. ✏️ \n قد يستغرق بعض الوقت ..`💛 ",
    "rot": "⚙️` تدوير PDf .. 🤸 \n قد يستغرق بعض الوقت ..`💛 ",
    "pdfTxt": "⚙️` استخراج النص .. 🐾 \n قد يستغرق بعض الوقت ..`💛 ",
    "fileNm": "اسم الملف القديم: {} \n اسم الملف الجديد: {}",
    "rotate" : {
        "⚙️ PDF» ROTETE ↓ ":"ajak4405"," 90 ° ":"work|rot90"," 180 ° ":"work|rot180",
        " 270 ° ": "work|rot270", "360 °": "work|rot360", "« BACK «": "pdf"
    } ,
    "txt" : {
        "⚙️ PDF» TXT ↓ ":"ajak4405"," 📜 MESSAGE 📜 ":"work|M"," 🧾 TXT FIL 🧾 ":"work|T",
        "🌐 HTML 🌐": "work|H", "🎀 JSON 🎀": "work|J", "« BACK «": "pdf"
    }
}

PROCESS = {
    "ocr": "OCR added", "decryptError": "__Cannot فك تشفير الملف بـ__` {} `🕸️",
    "decrypted": "__ملف مشفر__" , "encrypted": "__رقم الصفحة__: {} \n__ المفتاح__ 🔐: || {} ||",
    "compressed": """الحجم الأصلي: {} \n الحجم المضغوط: {} \n \n النسبة: {: .2f}٪""" ,
    "cantCompress": "لا يمكن ضغط الملف أكثر ..🤐",
    "pgNoError": "" "__لسبب ما يدعم تنسيق A4 لملفات pdf التي تحتوي على أقل من 5 صفحات __ \n \n إجمالي الصفحات: {} ⭐" "",
    "ocrError": "لديك طبقة نص بالفعل ..` 😏 ",
    "90": "__تدوير 90 درجة __" , "180": "__تدوير 180 درجة __" , "270": "__تدوير 270 درجة __" ,
    "formatted": "A4 Formatted File" , "M": "♻ مستخرج {} الصفحات ♻" ,
    "H": "ملف HTML" , "T": "ملف TXT" , "J": "ملف JSON"
}

pdf2TXT = {
    "upload": PROGRESS["upFile"] , "exit": split['exit'] , "nothing": "لا شيء لإنشاء .. 😏" ,
    "TEXT": "` إنشاء ملف PDF من الرسائل النصية »` ","start":" بدأ تحويل النص إلى ملف PDF..🎉 ",
    "font_btn": {
        "TXT @ PDF» SET FONT":"ajak4405"," Times ":"pdf|font|t"," Courier ":"pdf|font|c"," Helvetica (افتراضي) ":"pdf|font|h",
        "Symbol": "pdf|font|s", "Zapfdingbats": "pdf|font|z", "🚫 قريب 🚫": "close|me"
    } ,
    "size_btn": {"TXT @ PDF» {} »SET SCALE": "ajak4405", "Portarate": "t2p|{}|p", "Landscape": "t2p|{}|l", "« رجوع «": "pdf|T2P"},
    "askT": "__TEXT TO PDF» الآن , الرجاء إدخال العنوان: __ \n \n / خروج __ لإلغاء __ \n / تخطي __للتخطي__ ",
    "askC": "__TEXT TO PDF» الآن , الرجاء إدخال فقرة {}: __ \n \n / خروج __ لإلغاء __ \n / إنشاء __لإنشاء _ "
}

URL = {
    "get": {"🧭 Get PDF File 🧭": "getFile"}, "close": HELP_CMD ['CB'], "notPDF": "ليس ملف PDF" ,
    "error": "🐉 حدث خطأ ما \n \n الخطأ:` {} `\n \nNB: في المجموعات , لا يمكن للبرامج الآلية جلب المستندات إلا بعد الانضمام إلى المجموعة =)",
    "done": "` `انتهى تقريبًا .. ✅ \n الآن , بدأ التحميل .. 📤 `" , "_error_": "أرسل لي أي عنوان url أو روابط pdf مباشرة برقية" ,
    "openCB": {"Open In Browser": "{}"}, "_error": "` Some Thing Went Wrong = (`\n \n` {}` ",
    "_get": "[فتح الدردشة] ({}) \n \n ** حول الدردشة ↓ ** \n نوع الدردشة: {} \n اسم الدردشة: {} \n الدردشة Usr: @ {} \n"
             "معرف الدردشة: {} \n التاريخ: {} \n \n ** حول الوسائط ↓ ** \n الوسائط: {} \n اسم الملف: {} \n حجم الملف: {} \n \n نوع الملف: {}"
}

getFILE = {
    "inWork": PROGRESS ['workInP'], "big": "أرسل pdf url أقل من {} ميغابايت", "انتظر": "انتظر .. دعني .. 😜",
    "dl": {"📥 .. تنزيل .. 📥": "ajak4405"}, "up": {"📤 ..UPLOADING .. 📤": "ajak4405"},
    "complete": {"😎 مكتمل 😎": f"{str(settings.SOURCE_CODE)}"}
}

cbAns = [
    "هذه الميزة قيد التطوير ⛷️" , "Error annenn paranjille .. ثم ماذا .. 😏" ,
    "تم إلغاء العملية .. 😏" , "الملف غير مشفر .. 👀" , "لا شيء رسمي بخصوصه .. 😅" , "🎉 مكتمل .. 🏃"
]

inline_query = {
    "TOP": {"Now, Select Language ➟": "ajak4405"}, "capt": "SET LANGUAGE ⚙️", "des": "By:ajak4405 ❤"
}

# ===================================================================================================================================[NABIL A NAVAB -> TG: ajak4405]
