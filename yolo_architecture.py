from keras.models import Model
from keras.layers import Input, Conv2D, BatchNormalization, LeakyReLU, MaxPooling2D, GlobalAveragePooling2D, Dense

def create_yolo_model(input_shape, num_classes):
    # Input layer
    input_layer = Input(shape=input_shape)

    # Backbone
    x = yolo_conv_block(input_layer, 32)
    x = MaxPooling2D((2, 2))(x)
    x = yolo_conv_block(x, 64)
    x = MaxPooling2D((2, 2))(x)
    x = yolo_conv_block(x, 128)
    x = MaxPooling2D((2, 2))(x)
    x = yolo_conv_block(x, 256)
    x = MaxPooling2D((2, 2))(x)
    x = yolo_conv_block(x, 512)
    x = MaxPooling2D((2, 2))(x)
    x = yolo_conv_block(x, 1024)
    
    # Detection Head
    x = yolo_detection_block(x, 512)
    x = yolo_detection_block(x, 256)
    x = yolo_detection_block(x, 128)

    # Output layer
    output = Dense(units=num_classes, activation='softmax')(x)

    model = Model(inputs=input_layer, outputs=output)
    return model

def yolo_conv_block(x, filters):
    x = Conv2D(filters, (3, 3), padding='same')(x)
    x = BatchNormalization()(x)
    x = LeakyReLU(alpha=0.1)(x)
    return x

def yolo_detection_block(x, filters):
    x = yolo_conv_block(x, filters)
    x = yolo_conv_block(x, filters // 2)
    x = yolo_conv_block(x, filters)
    x = yolo_conv_block(x, filters // 2)
    x = yolo_conv_block(x, filters)
    return x

# Example usage
input_shape = (416, 416, 3)  # Example input shape (adjust based on your needs)
num_classes = 20  # Example number of classes (adjust based on your needs)
yolo_model = create_yolo_model(input_shape, num_classes)
yolo_model.summary()
