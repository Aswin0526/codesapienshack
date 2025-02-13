import cv2
from ultralytics import YOLO
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart


def send_mail(n,image_path):
  # Email configuration
  smtp_server = 'smtp.gmail.com'
  smtp_port = 587  # Use 465 for SSL
  sender_email = 'aswin0526as@gmail.com'
  sender_password = 'bwcsamqtpbnywotu'
  receiver_email = 'sec23cs156@sairamtap.edu.in'

  # Create the email content
  subject = 'Attention!!'
  body = f'{n} person detected'

  # Create a multipart message and set headers
  message = MIMEMultipart()
  message['From'] = sender_email
  message['To'] = receiver_email
  message['Subject'] = subject

  # Attach the body with the msg instance
  message.attach(MIMEText(body, 'plain'))

  with open(image_path, 'rb') as f:
        # Attach the image
        img = MIMEImage(f.read())
        img.add_header('Content-Disposition', 'attachment', filename=image_path)
        message.attach(img)

  try:
      # Connect to the server and log in
      server = smtplib.SMTP(smtp_server, smtp_port)
      server.starttls()  # Secure the connection
      server.login(sender_email, sender_password)

      # Send the email
      server.sendmail(sender_email, receiver_email, message.as_string())
      print("Email sent successfully!")

  except Exception as e:
      print(f"Error: {e}")

  finally:
      # Terminate the SMTP session and close the connection
      server.quit()

# Initialize the YOLO model (YOLOv8n model)
model = YOLO('yolov8n.pt')

# Initialize the camera
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

while cap.isOpened():
    ret, frame = cap.read()

    if not ret:
        break

    # Run YOLOv8 inference
    results = model(frame)
    
    # Count the number of persons detected
    num_persons = 0
    for result in results:
        classes = result.boxes.cls  # Extract class IDs
        num_persons += sum(1 for cls in classes if cls == 0)  # Count 'person' class (ID 0)

    

    
    
    # Print the number of persons detected
    print(f"{num_persons} persons detected")

    if(num_persons!=0):
      cv2.imwrite('send_img.jpg',frame)
      send_mail(num_persons,'send_img.jpg')
    else:
        pass

    
    # Display the resulting frame
    annotated_frame = results[0].plot()
    cv2.imshow("Camera", annotated_frame)

    if cv2.waitKey(1) == ord('q'):
        break
  
    

cap.release()
cv2.destroyAllWindows()
