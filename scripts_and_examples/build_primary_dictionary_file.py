import hmis
import time
import sys

tag = ""
if len(sys.argv)>1:
    tag = "_%s" % (sys.argv[1])

# Location of the 11 files from the HMIS data dump.
hmis_data_location = '../test_data/'
start=time.time()

# Put together a dictionary of all the individuals in the HMIS
# data dump and determine the connections and relationships between
# the different entries in the different files.
print("Reading in and determining relationships in HMIS data...")
print("This might take a while...up to an hour, depending on your machine.")
inds = hmis.create_dictionary_list(directory=hmis_data_location)

# Write this dictionary to a pickled file.
print("Writing pickle file...")
outfilename = "hmis_data%s.pkl" % (tag)
hmis.save_file(inds, outfilename)



print("Done!")
print("Time to generate file: %f seconds" % (time.time()-start))
