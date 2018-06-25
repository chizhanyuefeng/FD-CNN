# AFD-CNN(ADL and Fall Detection Convolutional Neural Networks)

## Net performance
- accuracy = 0.978718

| Class        | Sensitivity    |Specificity  |
| ----- | -----:   | :----: |
| Fall        | 1.000000      |   0.998654    |
| Walk        | 0.969072      |   1.000000    |
| Jog        | 0.983051      |   0.993243    |
| Jump        | 0.948980      |   0.998684    |
| up stair | 0.989474      |   0.997379    |
| down stair|0.967213|0.991848|
| stand to sit|  0.981481      |   0.998667    |
| sit to stand | 0.990476      |   0.997344    |
| Average        | 0.978718      |   0.996977    |

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

