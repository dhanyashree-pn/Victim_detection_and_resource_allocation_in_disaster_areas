# Victim_detection_and_resource_allocation_in_disaster_areas

In the wake of disasters and emergencies, the ability to efficiently manage and control crowds is a vital component of effective disaster response.
Crowd management in disaster areas is a multidisciplinary approach that involves planning, coordination, and execution to prevent chaos and minimize the risks associated with large gatherings of individuals during such events. 
The monitoring provides critical insights into crowd dynamics, allowing for optimized resource allocation and anomaly detection. 
By capitalizing on physiological responses related to changes in skin temperature, the project aims to provide a proactive solution that enhances the speed and precision of emergency response efforts.

## Our main objectives are:
*To optimize resource allocation: Utilize deep learning algorithms and systems to efficiently distribute resources to areas with the greatest need, ensuring critical resources are allocated effectively.

*To minimize risks and response times: Build accurate crowd-tracking mechanisms that provide real-time data on individual positions and velocities during disaster events.

*To Design and build: a unified system that seamlessly integrates crowd monitoring capabilities and automated detection of injured individuals using thermal imaging technology. 

## Existing Systems:
The current victim detection models are trained are usually on RGB images. But when there are any disasters say earthquake, or landslides etc.. the victims or persons in that disaster areas will be covered with dust or grey color. So some of the models fail to detect the victims since there is no much difference between the background and their skin colour. This is one of the major problem in the current scenario. Also some of the victims may loose their critical or golden time to get treated and may have life threatining situations. 

## Proposed System:
The proposed system introduces a model that is built on thermal datasets. So basically this tackles the problem of the victims not being detected due to no much change in the background and skin colour. Also we have implemented a mechanism that allocates the resources to the victims based on the count of the victims detected. We have introduced another feature that classifies the victims into not severly injured and severely injured based on the temperature of their body. This helps in prioritizing the victims who need urgent treatment. 
