params = {
    """
    Configuration parameters for training and prediction using Tinysleepnet-pytorch on the SleepEDF dataset.

    Attributes:
        params (dict): General configuration parameters.
            n_epochs (int): Number of training epochs.
            learning_rate (float): Learning rate for the optimizer.
            adam_beta_1 (float): Beta 1 parameter for the Adam optimizer.
            adam_beta_2 (float): Beta 2 parameter for the Adam optimizer.
            adam_epsilon (float): Epsilon parameter for the Adam optimizer.
            clip_grad_value (float): Gradient clipping value.
            evaluate_span (int): Number of epochs between evaluations.
            checkpoint_span (int): Number of epochs between checkpoints.
            no_improve_epochs (int): Number of epochs with no improvement for early stopping.
            model (str): Model identifier.
            n_rnn_layers (int): Number of RNN layers.
            n_rnn_units (int): Number of RNN units.
            sampling_rate (float): Sampling rate of the input data.
            input_size (int): Size of the input data.
            n_classes (int): Number of output classes.
            l2_weight_decay (float): L2 weight decay for regularization.
            dataset (str): Dataset identifier.
            data_dir (str): Directory path to the dataset.
            n_folds (int): Number of folds for cross-validation.
            n_subjects (int): Number of subjects in the dataset.
            augment_seq (bool): Whether to augment sequences.
            augment_signal_full (bool): Whether to augment the full signal.
            weighted_cross_ent (bool): Whether to use weighted cross-entropy loss.

        train (dict): Configuration parameters for training.
            Inherits all attributes from `params` and adds:
            seq_length (int): Sequence length for training.
            batch_size (int): Batch size for training.

        predict (dict): Configuration parameters for prediction.
            Inherits all attributes from `params` and adds:
            batch_size (int): Batch size for prediction.
            seq_length (int): Sequence length for prediction.
    """
    # Train
    "n_epochs": 200,
    "learning_rate": 1e-4,
    "adam_beta_1": 0.9,
    "adam_beta_2": 0.999,
    "adam_epsilon": 1e-8,
    "clip_grad_value": 5.0,
    "evaluate_span": 50,
    "checkpoint_span": 50,

    # Early-stopping
    "no_improve_epochs": 50,

    # Model
    "model": "model-mod-8",
    "n_rnn_layers": 1,
    "n_rnn_units": 128,
    "sampling_rate": 100.0,
    "input_size": 3000,
    "n_classes": 5,
    "l2_weight_decay": 1e-3,

    # Dataset
    "dataset": "sleepedf",
    "data_dir": "./data/sleepedf/sleep-cassette/eeg_fpz_cz",
    # "data_dir": "../tinysleepnet/data/sleepedf/sleep-cassette/eeg_fpz_cz",
    "n_folds": 20,
    "n_subjects": 20,

    # Data Augmentation
    "augment_seq": True,
    "augment_signal_full": True,
    "weighted_cross_ent": True,
}

train = params.copy()
train.update({
    "seq_length": 20,
    "batch_size": 15,
})

predict = params.copy()
predict.update({
    "batch_size": 1,
    "seq_length": 1,
})
