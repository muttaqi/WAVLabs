import os

os.system(
    'convert_dir_to_note_sequences --input_dir=detected_hats --output_file=hats.tfrecord --recursive'
)

os.system(
    'drums_rnn_create_dataset --config=\'one_drum\' --input=hats.tfrecord --output_dir=hats_sequences --eval_ratio=0.10'
)