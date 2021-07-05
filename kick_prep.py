import os

# convert midi files to note sequence files
os.system(
    'convert_dir_to_note_sequences --input_dir=detected_kicks --output_file=kicks.tfrecord --recursive'
)

# create a dataset from the sequence files
os.system(
    'drums_rnn_create_dataset --config=one_drum --input=kicks.tfrecord --output_dir=kick_sequences --eval_ratio=0.10'
)