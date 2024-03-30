"""
  @ Author:   Mr.Hat
  @ Date:     2024/3/30 14:05
  @ Description:
  @ History:
"""

MIN_PROXY_SCORE = 50

# 仅供注册的参数
REGISTER_ACCOUNT_ONLY = True
THREADS = 2

# 小草有人机验证，一下提供可绕过人机验证的大码平台可选
TWO_CAPTCHA_API_KEY = ""
ANTICAPTCHA_API_KEY = ""
CAPMONSTER_API_KEY = ""
CAPSOLVER_API_KEY = ""
CAPTCHAAI_API_KEY = ""

# Captcha 参数
CAPTCHA_PARAMS = {
    "captcha_type": "v2",
    "invisible_captcha": False,
    "sitekey": "6LdyCj0pAAAAAFvvSTRHYOzddUPMPcH232u7a9e0",
    "captcha_url": "https://app.getgrass.io/register"
}


########################################

ACCOUNTS_FILE_PATH = "data/accounts.txt"
PROXIES_FILE_PATH = "data/proxies.txt"
