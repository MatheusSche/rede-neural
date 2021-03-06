import numpy as np
from data import input_neurons, hidden_neurons, output_neurons
from data import get_test_data, get_training_data
from network import Network

network = Network([input_neurons, hidden_neurons, output_neurons])
# uncomment this stretch to start the network with a great test result
# saved_weights = np.load("weights.npy",mmap_mode=None, allow_pickle=True)
# network.weights = saved_weights

training_inputs = get_training_data()
test_inputs     = get_test_data()

network.start_training(training_inputs, 1000,  learning_rate=0.7, test_inputs=test_inputs)

print("\nRESULTADOS:")
for x, single_test in enumerate(test_inputs):
    if x == 0:
        print( "\nSEM RUIDOS:")
    if x == 34:
        print( "\nRUIDO MÍNIMO:")
    if x == 54:
        print( "\nRUIDO MÉDIO:")
    if x == 74:
        print( "\nRUIDO AVANÇADO:")
    if x == 94:
        print( "\nNÃO FAZEM PARTE:")
    network.identify(single_test, log=True)
