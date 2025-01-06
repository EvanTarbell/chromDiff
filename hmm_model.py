# hmm_model.py

import numpy as np

def create_new_model(transition_matrix, emission_matrix, state_annotations):
    num_states = transition_matrix.shape[0]
    num_observations = emission_matrix.shape[1]
    new_transitions_matrix = np.zeros((num_states, num_states))
    new_emission_matrix = np.zeros((num_states, num_observations))

    n = len(state_annotations) - 1
    for i in range(n):
        current_state = int(state_annotations[i])
        next_state = int(state_annotations[i + 1])
        new_transitions_matrix[current_state - 1][next_state - 1] += 1
    if n > 0:
        new_transitions_matrix /= n

    return new_transitions_matrix, new_emission_matrix

def compare_models(model1_transition, model1_emission, model2_transition, model2_emission):
    kl_transition = np.sum(
        model1_transition * np.log(np.divide(model1_transition, model2_transition, out=np.zeros_like(model1_transition), where=model2_transition > 0)),
        where=model1_transition > 0
    )
    kl_emission = np.sum(
        model1_emission * np.log(np.divide(model1_emission, model2_emission, out=np.zeros_like(model1_emission), where=model2_emission > 0)),
        where=model1_emission > 0
    )
    return kl_transition + kl_emission
