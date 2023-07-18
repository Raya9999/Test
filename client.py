import cv2
from image import similar_video_paths

# Chạy video tương ứng
for video_path in similar_video_paths:
    cap = cv2.VideoCapture(video_path)

    while True:
        ret, frame = cap.read()

        if not ret:
            # Khi video kết thúc, thoát khỏi vòng lặp
            break

        # Hiển thị frame video
        cv2.imshow('Video', frame)

        # Kiểm tra xem người dùng có nhấn phím 'q' để dừng không
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Giải phóng tài nguyên và đóng cửa sổ video
    cap.release()
    cv2.destroyAllWindows()
