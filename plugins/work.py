# fileName : plugins/work.py
# copyright ©️ 2021 ajak4405

import os, shutil
from pyrogram import enums

async def work(message, work="check", mtype=True) -> "str":
    """
    create a new working dir
    mtype: TRUE if message or FALSE if callbackquery
    work: create, check, delete
    """
    if mtype:
        if message.chat.type == enums.ChatType.PRIVATE:
            path = f"work/ajak4405/{message.chat.id}"
        else:
            pat = f"work/ajak4405/{message.chat.id}"
            path = f"work/ajak4405/{message.chat.id}/{message.from_user.id}"
    else:
        if message.message.chat.type == enums.ChatType.PRIVATE:
            path = f"work/ajak4405/{message.message.chat.id}"
        else:
            pat = f"work/ajak4405/{message.message.chat.id}"
            path = f"work/ajak4405/{message.message.chat.id}/{message.message.from_user.id}"
    if work == "create":
        if os.path.exists(path):
            return False    # False if work exists
        os.makedirs(path)
        return path
    elif work == "check":
        return path if os.path.exists(path) else False
    elif work == "delete":
        if mtype and message.chat.type != enums.ChatType.PRIVATE and len(os.listdir(pat)) == 1:
            return shutil.rmtree(pat, ignore_errors=True)
        if not mtype and message.message.chat.type != enums.ChatType.PRIVATE and len(os.listdir(pat)) == 1:
            return shutil.rmtree(pat, ignore_errors=True)
        return shutil.rmtree(path, ignore_errors=True)
