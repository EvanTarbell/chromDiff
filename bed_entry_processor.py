# bed_entry_processor.py

from bed_entries import BedEntry, BedEntryHalf

def sliding_window_bedentries(bedentry, window_size, step_size):
    new_entries = []
    for i in range(bedentry.start, bedentry.end, step_size):
        new_entries.append(BedEntry(
            bedentry.chromosome, i, i + window_size,
            bedentry.name, bedentry.score, bedentry.strand
        ))
    return new_entries

def extend_entries(entries, window):
    extended_entries = []
    for entry in entries:
        new_start = entry.start - window
        new_end = entry.end + window
        if not entry.name:
            extended_entries.append(BedEntryHalf(entry.chromosome, new_start, new_end))
        else:
            extended_entries.append(BedEntry(entry.chromosome, new_start, new_end, entry.name, entry.score, entry.strand))
    return extended_entries
