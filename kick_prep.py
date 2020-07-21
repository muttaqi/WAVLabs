import os

os.system(
    'convert_dir_to_note_sequences --input_dir=detected_kicks --output_file=kicks.tfrecord --recursive'
)

os.system(
    'drums_rnn_create_dataset --config=\'one_drum\' --input=kicks.tfrecord --output_dir=kick_sequences --eval_ratio=0.10'
)