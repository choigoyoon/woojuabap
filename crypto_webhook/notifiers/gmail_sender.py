import os
import smtplib
import logging
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from typing import Optional
from dotenv import load_dotenv

load_dotenv()
logger = logging.getLogger(__name__)

class GmailSender:
    def __init__(self):
        self.email = os.getenv('GMAIL_USER')
        self.password = os.getenv('GMAIL_APP_PASSWORD')
        
        if not self.email or not self.password:
            raise ValueError("Gmail 설정이 없습니다. (.env 파일을 확인하세요)")

    async def send_email(self,
                        subject: str,
                        body: str,
                        to_email: Optional[str] = None) -> bool:
        """
        Gmail을 통해 이메일 전송
        """
        try:
            if not to_email:
                to_email = self.email

            # 이메일 주소 검증
            if not '@' in to_email or not '.' in to_email:
                raise ValueError(f"잘못된 이메일 주소: {to_email}")

            msg = MIMEMultipart()
            msg['From'] = self.email
            msg['To'] = to_email
            msg['Subject'] = subject

            msg.attach(MIMEText(body, 'plain'))

            with smtplib.SMTP('smtp.gmail.com', 587) as server:
                server.starttls()
                server.login(self.email, self.password)
                server.send_message(msg)

            logger.info(f"이메일 전송 성공: {subject}")
            return True

        except Exception as e:
            logger.error(f"이메일 전송 실패: {str(e)}")
            return False
