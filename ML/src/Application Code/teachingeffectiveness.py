# import cv2
# import numpy as np
# import math
# from mtcnn.mtcnn import MTCNN

# delta = 10
# refresh = 20

# detector = MTCNN()
# cap = cv2.VideoCapture(1)

# if not cap.isOpened():
#     print("Error: Could not open webcam.")
#     exit()

# cv2.namedWindow('frame', cv2.WINDOW_NORMAL)
# cv2.resizeWindow('frame', 600, 400)

# x_end = 1200
# y_end = 700

# START = (900, 160)
# bar_height = 150

# Nose = []
# ideal_matrix = []
# counter = 0

# font = cv2.FONT_HERSHEY_SIMPLEX
# percent_attentive = 0
# percent_notattentive = 0

# # Function to compute Euclidean distance
# def distance(nose, ideal):
#     diff_x = (nose[0] - ideal[0]) ** 2
#     diff_y = (nose[1] - ideal[1]) ** 2
#     return math.sqrt(diff_x + diff_y)

# # Mapping detected nose points to the ideal positions
# def close_program():
#     global cap
#     cap.release()
#     cv2.destroyAllWindows()

# def mapper(noses, ideals):
#     result = [(0, 0)] * len(ideals)
#     for i in range(len(noses)):
#         min_dist = float('inf')
#         k = 0
#         for j in range(len(ideals)):
#             dist = distance(noses[i], ideals[j])
#             if dist < min_dist:
#                 min_dist = dist
#                 k = j
#         result[k] = noses[i]
#     return result

# while True:
#     ret, video_capture = cap.read()
#     if not ret:
#         break

#     result = detector.detect_faces(video_capture)
#     noses = []
#     for i in result:
#         nose = i['keypoints']['nose']
#         noses.append(nose)
#         bounding_box = i['box']
#         cv2.rectangle(video_capture, 
#                       (bounding_box[0], bounding_box[1]), 
#                       (bounding_box[0] + bounding_box[2], bounding_box[1] + bounding_box[3]), 
#                       (255, 255, 255), 2)

#     # Set ideal matrix in the first frame or every refresh cycle
#     if counter == 0 or counter % refresh == 0:
#         ideal_matrix = np.asarray(noses)

#     if len(ideal_matrix) > 0:
#         noses_mapped = np.asarray(mapper(noses, ideal_matrix))
#         diff = noses_mapped - ideal_matrix
#         counter_attentive = 0
#         counter_notattentive = 0

#         for i in range(len(diff)):
#             dist = math.sqrt(diff[i][0] ** 2 + diff[i][1] ** 2)
#             if dist > delta:
#                 counter_notattentive += 1
#                 cv2.circle(video_capture, (noses_mapped[i][0], noses_mapped[i][1]), 25, (0, 0, 255), 2)
#             else:
#                 counter_attentive += 1
#                 cv2.circle(video_capture, (noses_mapped[i][0], noses_mapped[i][1]), 25, (0, 255, 0), 2)

#         total_faces = counter_attentive + counter_notattentive
#         if total_faces > 0:
#             percent_attentive = (counter_attentive / total_faces) * 100
#             percent_notattentive = (counter_notattentive / total_faces) * 100

#     # Alert if attentive percentage drops below 70%
#     if percent_attentive < 70:
#         cv2.putText(video_capture, "ALERT!!", (10, 70), font, 2, (0, 0, 255), 2, cv2.LINE_AA)

#     # Draw bar graph
#     # def draw_bargraph():
#     #     cv2.rectangle(video_capture, (1118, 0), (1278, 235), (255, 255, 255), -1)
#     #     cv2.putText(video_capture, "0_", (START[0] - 40, START[1]), font, 0.5, (0, 0, 0), 1, cv2.LINE_AA)
#     #     cv2.putText(video_capture, "50_", (START[0] - 40, START[1] - 50), font, 0.5, (0, 0, 0), 1, cv2.LINE_AA)
#     #     cv2.putText(video_capture, "100_", (START[0] - 40, START[1] - 100), font, 0.5, (0, 0, 0), 1, cv2.LINE_AA)

#     #     attentive_bar_height = int(percent_attentive)
#     #     not_attentive_bar_height = int(percent_notattentive)

#     #     cv2.rectangle(video_capture, START, (START[0] + 50, START[1] - attentive_bar_height), (0, 255, 0), -1)
#     #     cv2.rectangle(video_capture, (START[0] + 55, START[1]), (START[0] + 100, START[1] - not_attentive_bar_height), (0, 0, 255), -1)
#     def draw_bargraph():
#     # Clear previous bar graph area
#       cv2.rectangle(video_capture, (850, 0), (1050, 200), (255, 255, 255), -1)
      
#       # Draw percentage labels
#       cv2.putText(video_capture, "0_", (START[0] - 40, START[1]), font, 0.5, (0, 0, 0), 1, cv2.LINE_AA)
#       cv2.putText(video_capture, "50_", (START[0] - 40, START[1] - 50), font, 0.5, (0, 0, 0), 1, cv2.LINE_AA)
#       cv2.putText(video_capture, "100_", (START[0] - 40, START[1] - 100), font, 0.5, (0, 0, 0), 1, cv2.LINE_AA)
      
#       # Clamp percentage values between 0 and 100 to prevent overflow or underflow
#       attentive_bar_height = min(max(int(percent_attentive), 0), 100)
#       not_attentive_bar_height = min(max(int(percent_notattentive), 0), 100)
      
#       # Ensure both bars are aligned at the same base (START[1] is the bottom of the graph)
#       # Draw the attentive bar (green) with the correct base alignment
#       cv2.rectangle(video_capture, (START[0], START[1]), 
#                     (START[0] + 50, START[1] - attentive_bar_height), (0, 255, 0), -1)
      
#       # Draw the not-attentive bar (red), placed with proper vertical alignment
#       cv2.rectangle(video_capture, (START[0] + 60, START[1]), 
#                     (START[0] + 110, START[1] - not_attentive_bar_height), (0, 0, 255), -1)

#     draw_bargraph()

#     counter += 1
#     cv2.imshow('frame', video_capture)

#         # Add a button to close the program
#     cv2.createButton('Close Program Window', close_program )
#     # cv2.createButton("Close", close_program, None, cv2.QT_PUSH_BUTTON, 1)
#     # cv2.createButton("Close", close_program)


#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()



# import cv2
# import numpy as np
# import math
# from mtcnn.mtcnn import MTCNN

# delta = 10
# refresh = 20

# detector = MTCNN()
# cap = cv2.VideoCapture(1)

# if not cap.isOpened():
#     print("Error: Could not open webcam.")
#     exit()

# cv2.namedWindow('frame', cv2.WINDOW_NORMAL)
# cv2.resizeWindow('frame', 600, 400)

# x_end = 1200
# y_end = 700

# START = (900, 160)
# bar_height = 150

# Nose = []
# ideal_matrix = []
# counter = 0

# font = cv2.FONT_HERSHEY_SIMPLEX
# percent_attentive = 0
# percent_notattentive = 0

# button_coords = (50, 50, 200, 100)  # (x1, y1, x2, y2)

# # Function to compute Euclidean distance
# def distance(nose, ideal):
#     diff_x = (nose[0] - ideal[0]) ** 2
#     diff_y = (nose[1] - ideal[1]) ** 2
#     return math.sqrt(diff_x + diff_y)

# # Mapping detected nose points to the ideal positions
# def mapper(noses, ideals):
#     result = [(0, 0)] * len(ideals)
#     for i in range(len(noses)):
#         min_dist = float('inf')
#         k = 0
#         for j in range(len(ideals)):
#             dist = distance(noses[i], ideals[j])
#             if dist < min_dist:
#                 min_dist = dist
#                 k = j
#         result[k] = noses[i]
#     return result

# # Function to handle mouse clicks
# def mouse_callback(event, x, y, flags, param):
#     if event == cv2.EVENT_LBUTTONDOWN:
#         # Check if the click is inside the button area
#         x1, y1, x2, y2 = button_coords
#         if x1 <= x <= x2 and y1 <= y <= y2:
#             print("Button clicked! Closing program...")
#             cap.release()
#             cv2.destroyAllWindows()

# # Set the mouse callback function for the window
# cv2.setMouseCallback('frame', mouse_callback)

# while True:
#     ret, video_capture = cap.read()
#     if not ret:
#         break

#     result = detector.detect_faces(video_capture)
#     noses = []
#     for i in result:
#         nose = i['keypoints']['nose']
#         noses.append(nose)
#         bounding_box = i['box']
#         cv2.rectangle(video_capture, 
#                       (bounding_box[0], bounding_box[1]), 
#                       (bounding_box[0] + bounding_box[2], bounding_box[1] + bounding_box[3]), 
#                       (255, 255, 255), 2)

#     # Draw a button
#     cv2.rectangle(video_capture, (button_coords[0], button_coords[1]), 
#                   (button_coords[2], button_coords[3]), (0, 255, 0), -1)
#     cv2.putText(video_capture, 'Close Program', (button_coords[0] + 10, button_coords[1] + 40), 
#                 font, 0.7, (0, 0, 0), 2, cv2.LINE_AA)

#     if counter == 0 or counter % refresh == 0:
#         ideal_matrix = np.asarray(noses)

#     if len(ideal_matrix) > 0:
#         noses_mapped = np.asarray(mapper(noses, ideal_matrix))
#         diff = noses_mapped - ideal_matrix
#         counter_attentive = 0
#         counter_notattentive = 0

#         for i in range(len(diff)):
#             dist = math.sqrt(diff[i][0] ** 2 + diff[i][1] ** 2)
#             if dist > delta:
#                 counter_notattentive += 1
#                 cv2.circle(video_capture, (noses_mapped[i][0], noses_mapped[i][1]), 25, (0, 0, 255), 2)
#             else:
#                 counter_attentive += 1
#                 cv2.circle(video_capture, (noses_mapped[i][0], noses_mapped[i][1]), 25, (0, 255, 0), 2)

#         total_faces = counter_attentive + counter_notattentive
#         if total_faces > 0:
#             percent_attentive = (counter_attentive / total_faces) * 100
#             percent_notattentive = (counter_notattentive / total_faces) * 100

#     if percent_attentive < 70:
#         cv2.putText(video_capture, "ALERT!!", (10, 70), font, 2, (0, 0, 255), 2, cv2.LINE_AA)

#     counter += 1
#     cv2.imshow('frame', video_capture)

#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()


# 
import cv2
import numpy as np
import math
from mtcnn.mtcnn import MTCNN

delta = 10
refresh = 20

detector = MTCNN()
cap = cv2.VideoCapture(0)  # Changed to 0, which is more common for default webcams

if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

cv2.namedWindow('frame', cv2.WINDOW_NORMAL)
cv2.resizeWindow('frame', 600, 400)
arr = []

x_end = 1200
y_end = 700

START = (900, 160)
bar_height = 150

Nose = []
ideal_matrix = []
counter = 0

font = cv2.FONT_HERSHEY_SIMPLEX
percent_attentive = 0
percent_notattentive = 0

button_width = 30  # Width of the button
button_height = 50  # Height of the button
margin = 50  # Margin from the edges

frame_height = 750  # Assuming frame height of 750

# Updated coordinates for the bottom-left corner
button_coords = (
    margin,  # x1 (left position)
    frame_height - margin - button_height,  # y1 (bottom position - height)
    margin + button_width,  # x2 (x1 + button_width)
    frame_height - margin  # y2 (bottom position)
)


# Function to compute Euclidean distance
def distance(nose, ideal):
    diff_x = (nose[0] - ideal[0]) ** 2
    diff_y = (nose[1] - ideal[1]) ** 2
    return math.sqrt(diff_x + diff_y)


# Mapping detected nose points to the ideal positions
def mapper(noses, ideals):
    result = [(0, 0)] * len(ideals)
    for i in range(len(noses)):
        min_dist = float('inf')
        k = 0
        for j in range(len(ideals)):
            dist = distance(noses[i], ideals[j])
            if dist < min_dist:
                min_dist = dist
                k = j
        result[k] = noses[i]
    return result


# Function to handle mouse clicks
def mouse_callback(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        # Check if the click is inside the button area
        x1, y1, x2, y2 = button_coords
        if x1 <= x <= x2 and y1 <= y <= y2:
            print("Button clicked! Closing program...")
            cap.release()
            cv2.destroyAllWindows()


# Set the mouse callback function for the window
cv2.setMouseCallback('frame', mouse_callback)

while True:
    ret, video_capture = cap.read()
    if not ret:
        break

    result = detector.detect_faces(video_capture)
    noses = []
    for i in result:
        nose = i['keypoints']['nose']
        noses.append(nose)
        bounding_box = i['box']
        cv2.rectangle(video_capture,
                      (bounding_box[0], bounding_box[1]),
                      (bounding_box[0] + bounding_box[2], bounding_box[1] + bounding_box[3]),
                      (255, 255, 255), 2)

    # Draw a button
    cv2.rectangle(video_capture, (button_coords[0], button_coords[1]),
                  (button_coords[2], button_coords[3]), (255, 255, 255), -1)
    cv2.putText(video_capture, 'X', (button_coords[0] + 10, button_coords[1] + 40),
                font, 0.7, (0, 0, 0), 2, cv2.LINE_AA)

    if counter == 0 or counter % refresh == 0:
        ideal_matrix = np.asarray(noses)

    if len(ideal_matrix) > 0:
        noses_mapped = np.asarray(mapper(noses, ideal_matrix))
        diff = noses_mapped - ideal_matrix
        counter_attentive = 0
        counter_notattentive = 0

        for i in range(len(diff)):
            dist = math.sqrt(diff[i][0] ** 2 + diff[i][1] ** 2)
            if dist > delta:
                counter_notattentive += 1
                cv2.circle(video_capture, (noses_mapped[i][0], noses_mapped[i][1]), 25, (0, 0, 255), 2)
            else:
                counter_attentive += 1
                cv2.circle(video_capture, (noses_mapped[i][0], noses_mapped[i][1]), 25, (0, 255, 0), 2)

        total_faces = counter_attentive + counter_notattentive
        if total_faces > 0:
            percent_attentive = (counter_attentive / total_faces) * 100
            percent_notattentive = (counter_notattentive / total_faces) * 100

    # Alert if attentive percentage drops below 70%
    if percent_attentive < 70:
        cv2.putText(video_capture, "ALERT!!", (10, 70), font, 2, (0, 0, 255), 2, cv2.LINE_AA)

    # Draw bar graph
    def draw_bargraph():
        # Clear previous bar graph area
        cv2.rectangle(video_capture, (850, 0), (1050, 200), (255, 255, 255), -1)

        # Draw percentage labels
        cv2.putText(video_capture, "0_", (START[0] - 40, START[1]), font, 0.5, (0, 0, 0), 1, cv2.LINE_AA)
        cv2.putText(video_capture, "50_", (START[0] - 40, START[1] - 50), font, 0.5, (0, 0, 0), 1, cv2.LINE_AA)
        cv2.putText(video_capture, "100_", (START[0] - 40, START[1] - 100), font, 0.5, (0, 0, 0), 1, cv2.LINE_AA)

        # Clamp percentage values between 0 and 100 to prevent overflow or underflow
        attentive_bar_height = min(max(int(percent_attentive), 0), 100)
        not_attentive_bar_height = min(max(int(percent_notattentive), 0), 100)

        # Draw the attentive bar (green) with the correct base alignment
        cv2.rectangle(video_capture, (START[0], START[1]),
                      (START[0] + 50, START[1] - attentive_bar_height), (0, 255, 0), -1)

        # Draw the not-attentive bar (red), placed with proper vertical alignment
        cv2.rectangle(video_capture, (START[0] + 60, START[1]),
                      (START[0] + 110, START[1] - not_attentive_bar_height), (0, 0, 255), -1)

    draw_bargraph()

    if percent_attentive or percent_notattentive:
        arr.append({'Percent Attentive': percent_attentive, 'Percent Not Attentive': percent_notattentive})

    counter += 1
    cv2.imshow('frame', video_capture)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

print(arr)
