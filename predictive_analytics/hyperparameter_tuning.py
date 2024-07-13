from hyperopt import fmin, tpe, hp, Trials
import tensorflow as tf

def objective(params, X_train, y_train, X_test, y_test):
    model = tf.keras.Sequential([
        tf.keras.layers.Dense(params['units'], activation='relu', input_shape=(X_train.shape[1],)),
        tf.keras.layers.Dense(1, activation='sigmoid')
    ])
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    history = model.fit(X_train, y_train, epochs=10, validation_data=(X_test, y_test), verbose=0)
    return -max(history.history['val_accuracy'])

space = {
    'units': hp.choice('units', [32, 64, 128])
}

best = fmin(objective, space, algo=tpe.suggest, max_evals=100, trials=Trials())
print(best)
