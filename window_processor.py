# window_processor.py

from bed_entry_processor import extend_entries
from overlap_finder import find_overlaps, clip_entry
from hmm_model import create_new_model, compare_models

def process_window(window, bedGraph1, bedGraph2, mod):
    ext_window = extend_entries(window, window)
    overlaps1 = find_overlaps(ext_window, bedGraph1)
    overlaps2 = find_overlaps(ext_window, bedGraph2)
    temp_list1 = [clip_entry(overlap[0], overlap[1]) if not overlap[2] else overlap[1] for overlap in overlaps1]
    temp_list2 = [clip_entry(overlap[0], overlap[1]) if not overlap[2] else overlap[1] for overlap in overlaps2]
    states1 = make_state_vector(temp_list1)
    states2 = make_state_vector(temp_list2)
    mod1 = create_new_model(mod[0], mod[1], states1)
    mod2 = create_new_model(mod[0], mod[1], states2)
    score = compare_models(mod1[0], mod1[1], mod2[0], mod2[1])
    return window, score

def make_state_vector(bedgraph_entries):
    total_length = sum(entry.end - entry.start for entry in bedgraph_entries)
    state_vector = [0] * total_length
    counter = 0
    for entry in bedgraph_entries:
        for i in range(entry.start, entry.end):
            state_vector[counter] = entry.score
            counter += 1
    return state_vector
