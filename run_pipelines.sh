python highpass_filter.py
python lowpass_filter.py
python hat_detection.py
python kick_detection.py
python hat_prep.py
python kick_prep.py

drums_rnn_train --config=one_drum --run_dir=kick_log_dir/run --sequence_example_file=./kick_sequences/training_drum_tracks.tfrecord --hparams="batch_size=64,rnn_layer_sizes=[64,64]" --num_training_steps=20000
drums_rnn_train --config=one_drum --run_dir=hat_log_dir/run --sequence_example_file=./hat_sequences/training_drum_tracks.tfrecord --hparams="batch_size=64,rnn_layer_sizes=[64,64]" --num_training_steps=20000

cp -r kick_log_dir/run track_generator
cp -r hat_log_dir/run track_generator