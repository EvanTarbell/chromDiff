# bed_entries.py

class BedGraphEntry:
    def __init__(self, chromosome, start, end, score):
        self.chromosome = chromosome
        self.start = start
        self.end = end
        self.score = score

class BedEntry:
    def __init__(self, chromosome, start, end, name, score, strand):
        self.chromosome = chromosome
        self.start = start
        self.end = end
        self.name = name
        self.score = score
        self.strand = strand

class BedEntryHalf:
    def __init__(self, chromosome, start, end):
        self.chromosome = chromosome
        self.start = start
        self.end = end
