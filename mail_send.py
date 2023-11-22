import os
import pandas as pd
# Python library for reading and manipulating PDF files.
import PyPDF2
# Python library that provides a simple client-side implementation of the
# Simple Mail Transfer Protocol (SMTP)
import smtplib
# MIMEText class is used to create a plain text message object,
# and the text content is passed as a parameter to the constructor.
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


# Create a gmail authentication
def send_mail(to_email, subject, message):
    smtp_server = 'smtp.gmail.com' # smtp server address
    smtp_port = 587 # smtp port address
    smtp_username = 'tejasf4@gmail.com' # email address
    smtp_password = 'add-your-app password' # app password

    # create the email message
    # MIMEMultipart is used to create a multipart message
    msg = MIMEMultipart()
    # The sender, recipient, and subject are set using the message headers
    msg['From'] = smtp_username
    msg['to'] = to_email
    msg['subject'] = subject
    # We can add another attachment
    msg.attach(MIMEText(message, 'plain'))

    # Connect to the SMTP server and send email
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.sendmail(smtp_username, to_email, msg.as_string())


# get pdf same name as Excel file's "name" column
def extract_email_from_pdf(pdf_path):
    # get "pdf_path" from main()
    with open(pdf_path, 'rb') as file:
        # PdfReader -->we can do operation extracting text, merging or splitting pages and more
        pdf_reader = PyPDF2.PdfReader(file)
        text = ''
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text


def main():
    folder_path = 'E:\\Start Python\\A-To-Z-Python\\demo'
    excel_path = 'E:\\Start Python\\A-To-Z-Python\\demo\\Book1.xlsx'

    # read the Excel file
    df = pd.read_excel(excel_path)

    # iterate through row in the DataFrame
    for index, row in df.iterrows():
        name = row['name']
        email = row['email']

        # Construct the PDF file path
        pdf_path = os.path.join(folder_path, f'{name}.pdf')

        # Check if the pdf is existing
        if os.path.exists(pdf_path):
            # extract email content from the PDF
            email_content = extract_email_from_pdf(pdf_path)

            # send mail to a specific address
            send_mail(email, 'subject of the email', email_content)
            print(f"Email send to {email} for {name}.")
        else:
            print(f"PDF file not found for {name}.")


if __name__ == "__main__":
    main()
