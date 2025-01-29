from apscheduler.schedulers.asyncio import AsyncIOScheduler
from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from twilio.rest import Client
from decouple import config
from db.connection import Session as SessionLocal
from db.models import RetornosModel, PacienteModel

class NotificationScheduler:
    def __init__(self):
        self.scheduler = AsyncIOScheduler()

    def send_whatsapp_message(self, to, message):
        account_sid = config('TWILIO_ACCOUNT_SID')
        auth_token = config('TWILIO_AUTH_TOKEN')
        from_whatsapp_number = 'whatsapp:' + config('TWILIO_WHATSAPP_FROM')
        to_whatsapp_number = 'whatsapp:' + to

        client = Client(account_sid, auth_token)
        client.messages.create(body=message, from_=from_whatsapp_number, to=to_whatsapp_number)

    def check_upcoming_appointments(self):
        db: Session = SessionLocal()
        try:
            next_week = datetime.now() + timedelta(days=7)
            appointments = db.query(RetornosModel).filter(RetornosModel.data == next_week.date()).all()
            for appointment in appointments:
                patient = db.query(PacienteModel).filter(PacienteModel.numeroSUS == appointment.FkPaciente).first()
                if patient and patient.telefone:
                    message = f"Olá {patient.nome}, você tem um retorno marcado para {next_week.date()}."
                    self.send_whatsapp_message(patient.telefone, message)
        finally:
            db.close()

    def start(self):
        self.scheduler.add_job(self.check_upcoming_appointments, 'interval', days=1)
        self.scheduler.start()
