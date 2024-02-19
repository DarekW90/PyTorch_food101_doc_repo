# Demo 🤗

For full interactive demo site see ➡ [HuggingFace](https://huggingface.co/spaces/DarekW90/foodvision_demo)

Hey! Glad to see you here this is only image of my demo site, please feel free and see how it works at HuggingFace 🤗

![hugging_face_portal](https://github.com/DarekW90/PyTorch_food101_doc_repo/blob/main/Images/demo_site_image.png?raw=true)

## Known issues:

* This model is working only with food images that has been trained on (food101)
  * That's mean if you put anything else than food this model is going to predict what is this according to it knowledge (don't be surprised when a photo of a car is uploaded and the model says it's a steak)
    * **HOW TO FIX**: double checking models first model classify binary food or no food, and another one classify type of food. (In this moment I am going to implement this but need some time to practice)
  <br/><br/>
  * If someone uploads a photo but our model doesn't have the capacity to classify that certain class:
    *  **HOW TO FIX** :
    1. Get more data for unknown classes (upgrade the model).
    2. Ask someone if the prediction is right/wrong, if it's wrong, track it to a database and update later (active learning).
    <br/><br/>
  * The image quality is poor (food in other place than center)
    *  **HOW TO FIX**: Add guidelines to the camera app to hint at taking a photo.
  <br/><br/>
  * Multiple foods in one shot
    *  **HOW TO FIX** :
    1. Return multiple classification results (e.g. the top 5 classification prediction probabilities)
    2. Object detection (detect each different food in an image and individually classify them)


