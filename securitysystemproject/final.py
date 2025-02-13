import cv2
from ultralytics import YOLO
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

def send_mail(n, image_path):
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    sender_email = 'aswin0526as@gmail.com'
    sender_password = 'bwcsamqtpbnywotu'
    receiver_email = 'sec23cs156@sairamtap.edu.in'
    subject = 'Attention!!'
    body = f'{n} person detected'
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = subject
    message.attach(MIMEText(body, 'plain'))
    with open(image_path, 'rb') as f:
        img = MIMEImage(f.read())
        img.add_header('Content-Disposition', 'attachment', filename=image_path)
        message.attach(img)
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, message.as_string())
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        server.quit()

model = YOLO('yolov8n.pt')
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    results = model(frame)
    num_persons = 0
    for result in results:
        classes = result.boxes.cls
        num_persons += sum(1 for cls in classes if cls == 0)
    print(f"{num_persons} persons detected")
    if num_persons != 0:
        cv2.imwrite('send_img.jpg', frame)
        send_mail(num_persons, 'send_img.jpg')
    annotated_frame = results[0].plot()
    # cv2.imshow("Camera", annotated_frame)
    

cap.release()
cv2.destroyAllWindows()
