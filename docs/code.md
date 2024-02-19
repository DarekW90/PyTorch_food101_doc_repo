# Code and experiments

## For full code see ➡ [GitHub](https://github.com/DarekW90/PyTorch_food101_doc_repo/blob/main/foodvision-bootcamp.ipynb)

## Experiments completed with this model:
Both experiments are done on ViT_B_16 pretrained model<br/>
![vit_b_16_params](https://github.com/DarekW90/PyTorch_food101_doc_repo/blob/main/Images/model.png?raw=true)

### Experiment_1: Train on 20% of total data 

![20_percent_data](https://github.com/DarekW90/PyTorch_food101_doc_repo/blob/main/Images/20_percent_for_testing.png?raw=true)
![20_percent_data_training](https://github.com/DarekW90/PyTorch_food101_doc_repo/blob/main/Images/20_percent_data_training.png?raw=true)
![curves_20_percent_data](https://github.com/DarekW90/PyTorch_food101_doc_repo/blob/main/Images/curves_20_percent_data.png?raw=true)

### Experiment_2: Train on 100% of total data

![100_percent_training_data](https://github.com/DarekW90/PyTorch_food101_doc_repo/blob/main/Images/100_percent_for_testing.png?raw=true)
![curves_100_percent_data](https://github.com/DarekW90/PyTorch_food101_doc_repo/blob/main/Images/curves_100_percent_data.png?raw=true)


### Summary:
![most_wrong](https://github.com/DarekW90/PyTorch_food101_doc_repo/blob/main/Images/most_wrong.png?raw=true)

As can bee see most wrongs predictions for photos are these food which almost looks the same.

#### Note:
    For this setup its not worth to run such big dataset on that little ammount of epochs, 
    probably when learning will go for longer (more epochs) 
    time then Loss could be lower and Accuracy higher.

    As can be seen Loss curve still going down so probably if I could do 10 or 15 epochs more,
    then curves could be realy close, also Accuracy curve keeps going up.

Unfortunetly I am unable to do longer test becouse of long learning time limited compute times in GoogleColab / Kaggle<br/>
I don't want to waste more compute time for this project, in my opinion it is better if I keep them for other practices.
