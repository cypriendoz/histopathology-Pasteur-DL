"""
More precise than BasicNN, instead of a collection of networks, one chose himself characteristics of his network
"""

from keras.models import Sequential
from keras.layers import Convolution2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense


def basic(model,nb1,nb2,nb3,nb_conv,nb_pool,input_shape):

    model.add(Convolution2D(nb1, (nb_conv,nb_conv), input_shape=input_shape))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(nb_pool,nb_pool)))

    model.add(Convolution2D(nb2, (nb_conv,nb_conv)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(nb_pool,nb_pool)))

    model.add(Convolution2D(nb3,(nb_conv,nb_conv)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(nb_pool,nb_pool)))

    model.add(Flatten())
    model.add(Dense(64))
    model.add(Activation('relu'))
    model.add(Dropout(0.5))
    model.add(Dense(1))
    model.add(Activation('sigmoid'))

    model.compile(loss='binary_crossentropy',
                optimizer='rmsprop',
                metrics=['accuracy'])
