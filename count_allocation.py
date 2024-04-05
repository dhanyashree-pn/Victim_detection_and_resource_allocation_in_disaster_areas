from roboflow import Roboflow
import supervision as sv
import cv2
import pandas as pd
import  matplotlib.pyplot as plt

rf = Roboflow(api_key="jNOBuOEl1QrhUQpP8jvj")
project = rf.workspace().project("flir-data-set")
model = project.version(22).model

def heatmap(annotated_image):
    image=cv2.cvtColor(annotated_image, cv2.COLOR_BGR2GRAY)
    #image=cv2.imread(annotated_image, cv2.IMREAD_GRAYSCALE)
    #image = cv2.imread(image_path)
    if image is not None:
        # Threshold the image to create a binary mask
        _, binary_image = cv2.threshold(image, 128, 255, cv2.THRESH_BINARY)
        # Find contours in the binary image
        contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        # Initialize list to store bounding boxes
        boxes = []
        # Loop over contours to collect bounding boxes
        for contour in contours:
            # Filter contours based on area to exclude noise
            area = cv2.contourArea(contour)
            if area > 100:  # Adjust this threshold as needed
                x, y, w, h = cv2.boundingRect(contour)
                boxes.append((x, y, w, h))
        # Create a color-coded heatmap
        heatmap_output = cv2.applyColorMap(image, cv2.COLORMAP_JET)
        #cv2.imshow(heatmap)
        return heatmap_output


def count_people(image_path):
    image=cv2.imread(image_path)
    result = model.predict(image_path, confidence=40, overlap=30).json()
    labels = [item["class"] for item in result["predictions"]]
    detections = sv.Detections.from_roboflow(result)
    label_annotator = sv.LabelAnnotator()
    bounding_box_annotator = sv.BoxAnnotator()
    annotated_image = bounding_box_annotator.annotate(
        scene=image, detections=detections)
    annotated_image = label_annotator.annotate(scene=annotated_image, detections=detections, labels=labels)
    heatmap_output=heatmap(annotated_image)
    count=len(detections)
    resource_allocation(count)
    sv.plot_image(image=annotated_image, size=(16, 16))
    return count,annotated_image,heatmap_output


def resource_allocation(count):
    affectedpopulation = count
    #print('here')
    if affectedpopulation != 0:
        #print('NON-FOOD RELIEF ITEMS')
        rounded_population = round(1 * affectedpopulation)
        ClothingandBedding = rounded_population
        Mattress = rounded_population
        BathingSoap = rounded_population
        LaundrySoap = rounded_population
        Toothbrush = rounded_population
        Toothpaste = rounded_population
        Shampoo = rounded_population
        water = 2.7 * affectedpopulation
        rice = 420 * affectedpopulation
        lentils = 50 * affectedpopulation
        meat = 20 * affectedpopulation
        oil = 25 * affectedpopulation
        sugar = 20 * affectedpopulation
        salt = 5 * affectedpopulation
        biscuits = 125 * affectedpopulation
        milk = 10 * affectedpopulation
        nonfoodData = {
            'Clothing/Bedding': ClothingandBedding,
            'Mattresses/Mats': Mattress,
            'Bathing Soap': BathingSoap,
            'Laundry Soap': LaundrySoap,
            'Toothbrush': Toothbrush,
            'Toothpaste': Toothpaste,
            'Shampoo': Shampoo
        }
        df = pd.DataFrame(list(nonfoodData.items()), index=['1', '2', '3', '4', '5', '6', '7'],
                          columns=['Non Food Items', 'Total Quantity based on per person'])
        #print(df, 600, 300)
        #print('FOOD RELIEF ITEMS')
        foodData = {
            'Clean Drinking Water(in litres)': water,
            'Cereals(Wheat,Rice,Maize in grams)': rice,
            'Legumes(Beans,Lentils in grams)': lentils,
            'Meta/Fish(in grams)': meat,
            'Cooking oil(in grams)': oil,
            'Sugar(in grams)': sugar,
            'Salt(in grams)': salt,
            'High-Energy Biscuits(in grams)': biscuits,
            'Milk Powder(in grams)': milk
        }
        df1 = pd.DataFrame(list(foodData.items()), index=['1', '2', '3', '4', '5', '6', '7', '8', '9'],
                           columns=['Food Items', 'Quantity based on person per day'])
        #print(df1, 600, 300)
        return df,df1


def detect_victims(image):
    count,detected_image,heatmap_output=count_people(image)
    non_food_relief,food_relief=resource_allocation(count)
    return count,detected_image,heatmap_output,non_food_relief,food_relief

