import mss
import cv2
import dotenv
from PIL import Image
import numpy

from sahi import AutoDetectionModel
from sahi.predict import get_sliced_prediction


dotenv.load_dotenv()

model_path = "runs/detect/train/weights/best.pt"
detection_model = AutoDetectionModel.from_pretrained(
    model_type='ultralytics',
    model_path=model_path,
    confidence_threshold=0.5,
    device="cuda:0"
)

def main():
    with mss.mss() as sct:
        screenshot = sct.grab(sct.monitors[1])

    frame = numpy.array(screenshot)
    frame = numpy.ascontiguousarray(frame[:, :, :3])

    Image.fromarray(frame).save("screenshot.jpg")

    slice_size = 320
    overlap = 0.5
    result = get_sliced_prediction(
        frame,
        detection_model,
        slice_height=slice_size,
        slice_width=slice_size,
        overlap_height_ratio=overlap,
        overlap_width_ratio=overlap
    )

    object_prediction_list = result.object_prediction_list

    annotated_frame = frame.copy()

    for prediction in object_prediction_list:

        bbox = prediction.bbox
        x, y, maxX, maxY = int(bbox.minx), int(bbox.miny), int(bbox.maxx), int(bbox.maxy)

        cv2.rectangle(annotated_frame, (x, y), (maxX, maxY), (0, 255, 0), 2)
        text = f"{prediction.category.name} {prediction.score.value:.2f}"
        cv2.putText(annotated_frame, text, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 2)

    cv2.imwrite('frame.jpg', annotated_frame)

if __name__ == "__main__":
    main()