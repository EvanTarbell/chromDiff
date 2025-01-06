# main.py

import sys
import multiprocessing
from file_readers import readBedGraphFile, readBedFile, read_hmm_matrices
from bed_entry_processor import sliding_window_bedentries
from window_processor import process_window

if __name__ == "__main__":
    bdg1 = sys.argv[1]
    bdg2 = sys.argv[2]
    bed = sys.argv[3]
    model = sys.argv[4]
    win = int(sys.argv[5])
    st = int(sys.argv[6])

    bedGraph1 = readBedGraphFile(bdg1)
    bedGraph2 = readBedGraphFile(bdg2)
    ref = readBedFile(bed)
    mod = read_hmm_matrices(model)

    num_processes = multiprocessing.cpu_count()
    with multiprocessing.Pool(processes=num_processes) as pool:
        results = []
        for temp in ref:
            windows = sliding_window_bedentries(temp, win, st)
            args = [(window, bedGraph1, bedGraph2, mod) for window in windows]
            results.extend(pool.starmap(process_window, args))

        for window, score in results:
            print(f"{window.chromosome}\t{window.start}\t{window.end}\t{score}")
