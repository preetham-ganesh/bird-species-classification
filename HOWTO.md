# Comparison of Approaches towards Classification of Birds Species

## Installing the package

### Clone the repo

```bash
git clone https://github.com/preetham-ganesh/bird-species-classification.git
cd bird-species-classification
```

## Dataset

### Download

- The dataset used for developing the Neural Network model was downloaded from [[Link]](https://www.kaggle.com/datasets/gpiosenka/100-bird-species).
- Downloaded dataset should be saved at 'dev/data/original'.

### Extraction

```bash
unzip dev/data/original/train.zip -d dev/data/extracted/train
unzip dev/data/original/valid.zip -d dev/data/extracted/validation
unzip dev/data/original/test.zip -d dev/data/extracted/test
```