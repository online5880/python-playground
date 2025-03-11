import asyncio
from email.message import EmailMessage
import aiosmtplib
import os
from dotenv import load_dotenv

load_dotenv()  # .env 파일 로드

username = os.getenv("EMAIL_USER")
password = os.getenv("EMAIL_PASSWORD")

async def send_email(subject: str, msg: str):
    # 이메일 메시지 구성
    message = EmailMessage()
    message["From"] = os.getenv("EMAIL_USER")  # 발신자 이메일
    message["To"] = "gjtjqkr5880@gmail.com"
    message["Subject"] = f"{subject}"
    message.set_content(f"{msg}")

    # SMTP 서버 정보
    smtp_host = "smtp.naver.com"
    smtp_port = 465
    
    await aiosmtplib.send(
        message,
        hostname="smtp.naver.com",
        port=465,
        use_tls=True,  # SSL/TLS를 초기부터 사용
        username=username,
        password=password,
    )
    print("이메일 전송 완료")

asyncio.run(send_email("제목","내용"))
