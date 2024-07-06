# Glaucoma-Detection

As per the National Eye Institute;
“The only way to find out if you have glaucoma is to get a comprehensive
dilated eye exam. If cup to disc ratio size is more than >0.5 mm then this is glaucoma. If cup to
disc ratio size < 0.5 mm then its normal eye condition”

This dilation can affect the optic cup and change the cup-disc ratio. A model can be trained to
make this observation, calculate the ratio, and make a diagnosis.

Methodology:
1. First we separate the masks in the given dataset to extract the cups and discs
2. Next we split the dataset in train and test sets
3. We train the model to segment the images based on the retracted cups and discs
4. We test and evaluate the model to assess performance
5. We process the results to obtain the cup-disc ratio

Network Architecture Details

Layers:

Contracting Path (Encoder):
Enc1: Two convolutional layers (64 filters, 3x3 kernel size) followed by ReLU activation and
batch normalization.
Enc2: Max pooling (2x2), followed by two convolutional layers (128 filters, 3x3 kernel size)
with ReLU and batch normalization.
Enc3: Max pooling (2x2), followed by two convolutional layers (256 filters, 3x3 kernel size)
with ReLU and batch normalization.
Enc4: Max pooling (2x2), followed by two convolutional layers (512 filters, 3x3 kernel size)
with ReLU and batch normalization.
Enc5: Max pooling (2x2), followed by two convolutional layers (1024 filters, 3x3 kernel size)
with ReLU and batch normalization.

Expanding Path (Decoder):
Dec4: Up-convolution (512 filters, 2x2 kernel size), concatenation with Enc4, followed by two
convolutional layers (512 filters, 3x3 kernel size) with ReLU and batch normalization.
Dec3: Up-convolution (256 filters, 2x2 kernel size), concatenation with Enc3, followed by two
convolutional layers (256 filters, 3x3 kernel size) with ReLU and batch normalization.
Dec2: Up-convolution (128 filters, 2x2 kernel size), concatenation with Enc2, followed by two
convolutional layers (128 filters, 3x3 kernel size) with ReLU and batch normalization.
Dec1: Up-convolution (64 filters, 2x2 kernel size), concatenation with Enc1, followed by two
convolutional layers (64 filters, 3x3 kernel size) with ReLU and batch normalization.

Output Layer: Convolutional layer (1 filter, 1x1 kernel size) to produce the final segmentation
mask.

Activation Functions:
ReLU: Used after each convolutional layer to introduce non-linearity.
Sigmoid: Applied to the output layer for binary segmentation tasks.

Training Process Details

Data Augmentation Techniques:
● Random Horizontal Flip
● Random Vertical Flip
● Random Rotation (up to 30 degrees)
● Color Jitter (brightness, contrast, saturation, hue adjustments)
● Random Resized Crop

Optimizer Choice:
Adam Optimizer: Chosen for its adaptive learning rate capabilities.

Learning Rate Schedule:
StepLR: Reduces the learning rate by a factor of 0.1 every 10 epochs to help the model converge
more effectively.

Pre-Processing:
After obtaining the results from the model, we simply calculate the number of white pixels in
both masks corresponding to an input image, and obtain the ratio.

