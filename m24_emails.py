import smtplib
import sys
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import getpass

# Server- und Anmeldeinformationen
smtp_server = "mail.upb.de"  # Ersetze durch deinen SMTP-Server
smtp_port = 587  # Typischerweise 587 für TLS oder 465 für SSL
smtp_user = "dwarner"  # Ersetze durch deine E-Mail-Adresse
smtp_password = getpass.getpass("Bitte Passwort eingeben: ", stream=sys.stdin)  # Sichere Passworteingabe

# E-Mail-Inhalte
from_address = "dwarner@upb.de"
to_address = "dwarner@upb.de"
subject = "Betreff der E-Mail"
body = "Dies ist der Text der E-Mail."

# Erstelle die MIME-Nachricht
msg = MIMEMultipart()
msg['From'] = from_address
msg['To'] = to_address
msg['Subject'] = subject

# Füge den E-Mail-Text hinzu
msg.attach(MIMEText(body, 'plain'))

try:
    # Verbindung zum SMTP-Server herstellen
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()  # TLS-Verschlüsselung verwenden
    server.login(smtp_user, smtp_password)  # Anmeldung beim SMTP-Server
    text = msg.as_string()
    server.sendmail(from_address, to_address, text)  # E-Mail senden
    server.quit()  # Verbindung beenden
    print("E-Mail erfolgreich gesendet")
except Exception as e:
    print(f"Fehler beim Senden der E-Mail: {e}")
