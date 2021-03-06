# hyperparameters
D_STEPS = 5
G_STEPS = 2
NB_EPOCH = 50
IMAGES_TO_GENERATE = 5
MODEL_COMPLEXITY = 1

LATENT_DIMENSION = 100
G_INPUTS = LATENT_DIMENSION

IMAGE_X = 128
IMAGE_Y = 128

MINIBATCH_SIZE = 16
# TRAIN_SIZE = 1 # ???

LR = 0.0002
LEAK  = 0.2
BETA1  = 0.5
BETA2 = 0.999
MEAN = 0.0
STD = 0.02

COLOR = 0

if COLOR:
    NB_CHANNELS = 3
else:
    NB_CHANNELS = 1

save = True


CAN_USE_PLT = 1

DATASET = "impressionism"

SAVE = True
CHECKPOINT = 3
packing = 4

SAVE_PATH = "results/"

LOAD_MODELS = True

D_LOAD_NAME = "epoch2_D_model.pt"
G_LOAD_NAME = "epoch2_G_model.pt"
