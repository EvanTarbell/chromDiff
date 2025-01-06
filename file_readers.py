# file_readers.py

import numpy as np
from bed_entries import BedGraphEntry, BedEntry

def readBedGraphFile(filename):
    entries = []
    with open(filename, 'r') as f:
        for line in f:
            fields = line.strip().split('\t')
            chromosome = fields[0]
            start = int(fields[1])
            end = int(fields[2])
            score = fields[3]
            if isinstance(score, str):
                score = score.strip().split('_')[0]
            entries.append(BedGraphEntry(chromosome, start, end, score))
    return entries

def readBedFile(filename):
    entries = []
    with open(filename, 'r') as f:
        for line in f:
            fields = line.strip().split('\t')
            chromosome = fields[0]
            start = int(fields[1])
            end = int(fields[2])
            name = fields[3] if len(fields) >= 4 else ""
            score = int(fields[4]) if len(fields) >= 6 else 0
            strand = fields[5] if len(fields) >= 6 else ""
            entries.append(BedEntry(chromosome, start, end, name, score, strand))
    return entries

def read_hmm_matrices(filename):
    transition_matrix = []
    emission_matrix = []
    with open(filename, "r") as f:
        line = f.readline().strip()
        if line == "$TRANS":
            line = f.readline().strip()
            while line != "$EM":
                transition_matrix.append([float(x) for x in line.split()])
                line = f.readline().strip()
        if line == "$EM":
            line = f.readline().strip()
            while line:
                emission_matrix.append([float(x) for x in line.split()])
                line = f.readline().strip()
    return np.array(transition_matrix), np.array(emission_matrix)
