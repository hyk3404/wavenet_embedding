# wavenet_embedding

* Create feature vector from your dataset using wavenet

## python3.6 Requirments
* If you have a GPU you can install the GPU version of magenta
```
magenta
numpy
librosa
tensorflow
```

## Before the start
* Create a folder named dataset in this project

* You need have wavenet embedding [pretrain model](https://github.com/tensorflow/magenta/tree/master/magenta/models/nsynth)

## run

```
python wavenet_embedding_vector.py
```
## comparison
* If you want to compare the number of mp3 and npy
* This code will output comparison.txt
```
python file_comparison.py
```

