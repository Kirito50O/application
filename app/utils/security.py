import hashlib
import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart 


def verifiaction_api(password):
    sha1_hash = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    prefix = sha1_hash[:5]  
    suffix = sha1_hash[5:]  


    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    response = requests.get(url)

    if response.status_code != 200:
        raise RuntimeError(f"Error: {response.status_code}")

    found = False
    hashes = (line.split(':') for line in response.text.splitlines())
    for returned_suffix, count in hashes:
        if returned_suffix == suffix:
            print(f"Password found! Compromised {count} times.")
            found = True
            return True
    if not found :
        return False
    
def envoyer_notification(destinataire, sujet, message):
    """Envoie un e-mail de notification."""
    # Configuration de l'expéditeur
    expediteur = ""  
    mot_de_passe = ""  

    try:
        # Création de l'objet de l'e-mail
        email = MIMEMultipart()
        email["From"] = expediteur
        email["To"] = destinataire
        email["Subject"] = sujet

        # Contenu du message
        email.attach(MIMEText(message, "plain"))

        # Connexion au serveur SMTP
        with smtplib.SMTP("smtp.gmail.com", 587) as serveur:
            serveur.starttls()  # Démarre le chiffrement TLS
            serveur.login(expediteur, mot_de_passe)
            serveur.send_message(email)

        print(f"Notification envoyée à {destinataire}.")
    except Exception as e:
        print(f"Erreur lors de l'envoi de la notification : {e}")


    

def mail_envoie(passowrd , mail):
    sujet = "Alerte de sécurité : Votre mot de passe est compomis"
        message = (
            f"Bonjour,\n\n"
            f"Votre mot de passe a été détecté comme compromis. "
            f"Nous vous recommandons de le changer immédiatement.\n\n"
            f"Exemple de Règles pour un Mot de Passe Sûr :\n"
            f"Longueur minimale : 12 caractères.\n"
            f"Caractères obligatoires :\n"
            f"- 1 majuscule.\n"
            f"- 1 minuscule.\n"
            f"- 1 chiffre.\n"
            f"- 1 caractère spécial."
        )
        envoyer_notification(utilisateur_email, sujet, message)
