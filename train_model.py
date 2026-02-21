import os
from ultralytics.models import YOLO
from dotenv import load_dotenv
import roboflow

if __name__ == "__main__":
    load_dotenv()


    rf = roboflow.Roboflow(api_key=os.environ.get("ROBOFLOW_API_KEY"))
    project = rf.workspace("p0sseid0n").project("poker-cards-cxcvz-n0wl5")
    version = project.version(1)
    dataset = version.download("yolo26")
    model = YOLO("yolo26n.pt")

    model.train(
        data=dataset.location + "/data.yaml", 
        epochs=100, 
        imgsz=640,
        device=0, 
        batch=16,
        workers=0 
    )

