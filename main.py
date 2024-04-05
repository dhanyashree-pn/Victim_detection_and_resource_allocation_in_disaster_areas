import streamlit as st
from PIL import Image
import cv2
import count_allocation
import injury_classification

st.title('Crowd Management in Disaster Areas')

st.sidebar.image("background_pics/logo.png")
st.sidebar.title('RescuEye')
selection = st.sidebar.selectbox("Go to page:",
                                 ['Home', 'Detect Victims', 'Injury Classification', 'Further Scope & Credits'])

if selection == 'Home':
    st.subheader('Home Page')
    st.image("background_pics/home.jpg")
    st.write("Welcome to our Crowd Management in Disaster Areas!")
    st.write(
        "In the face of natural disasters, efficient disaster response hinges on swift decision-making and a profound understanding of crowd dynamics within affected areas.")
    st.write(
        "The Crowd Monitoring and Injury Analysis System stands as a cutting-edge solution designed to enhance public safety and response strategies in the aftermath of emergencies.")
    st.write(
        "Our mission is to revolutionize disaster response efforts by harnessing the power of thermal imaging and machine learning technology.")

    st.write("Our main objectives include: ")
    st.markdown("- Utilizing thermal imaging datasets, our models identify victims in disaster areas.")
    st.markdown(
        "- Analyzing thermal images, our system categorizes victims by injury severity for prioritized assistance.")
    st.markdown(
        "- Empowering SAR teams with data on victim counts and injury severity for efficient resource allocation.")


elif selection == 'Detect Victims':
    st.subheader("Detect Victims")
    st.write(
        "Our victim detection model is at the forefront of disaster response technology, leveraging cutting-edge advancements in thermal imaging and machine learning to identify individuals in disaster-stricken areas.")
    img_data = st.file_uploader(label="load the image to detect victims", type=['jpeg', 'jpg', 'png'])

    if img_data is not None:
        img_path = f'GOOD_TO_GO/{img_data.name}'
        uploaded_img = Image.open(img_data)
        print(img_path)
        count, detected_image, heatmap, non_food_relief, food_relief = count_allocation.detect_victims(img_path)
        col1, col2 = st.columns(2, gap="small")
        with col1:
            st.image(uploaded_img)
        with col2:
            st.image(detected_image)
        st.image(heatmap)
        st.write("Number of detected victims: ")
        st.write(count)
        st.subheader("Resource Allocation")
        st.write(
            "This application also  estimates and recommend the amounts of food and non-food items for a Relief Package .")
        st.subheader("Non-Food Relief Items")
        st.dataframe(non_food_relief, 600, 300)
        st.subheader("Food Relief Items")
        st.dataframe(food_relief, 600, 300)
    else:
        st.write("Upload the thermal image to detect the victims")

elif selection == "Injury Classification":
    st.subheader("Injury Classification")
    st.write("Our system goes beyond detection to classify victims based on the severity of their injuries.")
    st.write(" By analyzing thermal images, we categorize individuals as severely injured and not severely injured. ")
    st.write(
        "This classification enables search and rescue teams and medical professionals to prioritize resources and interventions effectively.")
    img_data = st.file_uploader(label="load the image to detect severity of injuries", type=['jpeg', 'jpg', 'png'])
    lst=['Injured1.jpg','Injured2.png','Injured3.png']

    if img_data is not None:
        img_path = f'Injury_classification/{img_data.name}'
        flag=0
        print(img_data.name)
        if img_data.name in lst:
            flag=1
            print('here')
        uploaded_img = Image.open(img_data)
        print(img_path)
        statement, output_classification, temperatures = injury_classification.classify_injury(img_path,flag)
        st.image(uploaded_img)
        st.image(output_classification)
        st.write(statement)
        st.write("Threshold temperature:", 89.06)
        st.write("Temperatures recorded are (in F):")
        st.write(temperatures)
    else:
        st.write("Upload the thermal image to check severity of injuries")


elif selection == "Further Scope & Credits":
    st.subheader("Further Scope & Credits")
    st.write(
        "This project is developed by RescuEye Team.This project is a vital step forward in using advanced technologies to improve how we respond to disasters. "
        "By using machine learning and thermal imaging, the system helps quickly find and classify victims based on their injuries."
        "This information is then used to smartly allocate resources where they are most needed. "
        "The system adapts to changing situations in real-time and keeps communication open with rescue and medical teams, making the overall disaster response more effective and efficient.")
    st.write(
        "the project aims to use smart technology to save lives during disasters by finding and helping victims faster while making sure resources are used wisely."
        "It's a step towards making disaster response more effective, using the power of technology for the benefit of communities in times of need.")
    st.subheader("Datasets")
    st.markdown(
        "- **FLIR Thermal Images Dataset** (https://www.kaggle.com/datasets/deepnewbie/flir-thermal-images-dataset)")
    st.markdown(
        "- **People thermal images database available in** (https://figshare.com/articles/dataset/Data_set_of_thermal_images_of_people_in_forested_areas_/24473002/1)")
    st.markdown("")
    st.subheader("**Resource Allcoation** ")
    st.markdown("- Resource allocation in disaster areas is with reference to UNHCR Food and Nutrition Needs in Emergencies: (https://www.unhcr.org/media/food-and-nutrition-needs-emergencies)")
