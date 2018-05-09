# AFD-CNN(ADL and Fall down Detecton Convolutional Neural Networks)

## Net performance
- accuracy = 0.993017

| Class        | Sensitivity    |Specificity  |
| ----- | -----:   | :----: |
| Fall        | 1.0      |   1.0    |
| Walk        | 0.9914529914529915      |   0.998330550918197    |
| Jog        | 0.990990990990991      |   1.0    |
| Jump        | 1.0      |   0.99836867862969    |
| Up&down stair | 0.9827586206896551      |   0.9966666666666667    |
| stand to sit|  0.9887640449438202      |   1.0    |
| sit to stand | 1.0      |   0.9984    |
| Average        | 0.9934238068682083      |   0.998823699459222    |

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

