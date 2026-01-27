# 国际化与多语言支持（gettext示例）
import gettext
import os

LOCALE_DIR = os.path.join(os.path.dirname(__file__), 'locale')
LANG = os.getenv('LANG', 'zh_CN')
trans = gettext.translation('messages', LOCALE_DIR, languages=[LANG], fallback=True)
_ = trans.gettext
