# overlap_finder.py

def find_overlaps(entries1, entries2):
    overlaps = []
    for entry1 in entries1:
        for entry2 in entries2:
            condition1 = entry1.start >= entry2.start and entry1.start <= entry2.end
            condition2 = entry1.end >= entry2.start and entry1.end <= entry2.end
            condition3 = entry1.start <= entry2.start and entry1.end >= entry2.end
            contained = condition3
            if condition1 or condition2 or contained:
                overlaps.append((entry1, entry2, contained))
    return overlaps

def clip_entry(entry1, entry2):
    entry2.start = max(entry2.start, entry1.start)
    entry2.end = min(entry2.end, entry1.end)
    return entry2
