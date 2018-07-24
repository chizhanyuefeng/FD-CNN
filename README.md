# AFD-CNN(ADL and Fall Detection Convolutional Neural Networks)

## Net performance
- now we optimize the network and the accuracy is 99.4%

| Class        | Sensitivity    |Specificity  |
| ----- | -----:   | :----: |
| Fall        | 100.0%      |   100.0%    |
| Walk        | 100.0%      |   100.0%    |
| Jog        | 100.0%      |   100.0%    |
| Jump        | 100.0%      |   100.0%    |
| up stair | 99.2%      |   100.0%    |
| down stair|100.0%|99.9%|
| stand to sit|   99.1%     |   99.6%    |
| sit to stand | 97.3%      |   99.9%    |
| Average        | 99.5%      |   99.9%    |

## Requirenments
- python3
- tensorflow 1.4.0
- pandas
- numpy
- matplotlib


## How to train and test
    python ./src/cnn.py

## Dataset
we need two public datasets.

- 1.MobiFall＆MobiAct DataSet
http://www.bmi.teicrete.gr/index.php/research/mobiact

- 2.SisFall http://sistemic.udea.edu.co/en/investigacion/proyectos/english-falls/

