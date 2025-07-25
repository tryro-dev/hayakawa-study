import cv2

# パスワードを含むRTSP URL
rtsp_url = 'rtsp://admin:tryro_2000@192.168.40.30:554/cam/realmonitor?channel=1&subtype=0'


# 映像取得
cap = cv2.VideoCapture(rtsp_url)

# 映像サイズ取得（失敗時はデフォルト）
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH) or 640)
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT) or 480)
fps = int(cap.get(cv2.CAP_PROP_FPS) or 20)

# 保存設定
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('output.mp4', fourcc, fps, (width, height))

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("映像の取得に失敗しました。")
        break

    # 映像表示
    cv2.imshow('Live Camera Feed', frame)

    # 動画として保存
    out.write(frame)

    # 終了キー：q
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()
