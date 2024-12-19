# Real-Time Privacy-Preserving Student Attention Monitoring System  

This project introduces a novel system to monitor and analyze student attention levels in real-time during classroom sessions. By leveraging Computer Vision techniques, the system ensures both privacy and efficiency in detecting attention and engagement levels.  

## Key Features  

1. *Privacy-Preserving*:  
   - The system obfuscates faces in the video streams to protect student identity and privacy.  

2. *Non-Facial Expression-Based Analysis*:  
   - Attention levels are determined using a grid of points corresponding to the face rather than analyzing facial expressions.  
   - This approach improves processing speed and avoids reliance on subjective emotion-based cues.  

3. *Real-Time Analysis*:  
   - Processes video streams in real time, providing instant feedback on student attention levels.  

4. *Comprehensive Insights*:  
   - Generates heat maps and attention indices to help educators identify areas of improvement in teaching methods.  

## Technologies Used  

- *Frontend*:  
  - HTML  
  - CSS  
  - JavaScript  

- *Backend*:  
  - Python  
  - PHP  

## Project Setup  

1. *Clone the Repository*:  
   ```bash  
   git clone https://github.com/your-username/student-attention-monitor.git  
   cd student-attention-monitor  

	2.	Install Dependencies:
	•	For Python:

pip install -r requirements.txt  


	•	Ensure PHP is installed and configured.

	3.	Run the Application:
	•	Start the backend server:

python app.py  


	•	Serve the frontend files through a web server (e.g., Apache, Nginx).

	4.	Usage:
	•	Connect a camera to capture video streams.
	•	Access the web interface via the server URL to monitor and analyze student attention in real time.

Folder Structure

student-attention-monitor/
