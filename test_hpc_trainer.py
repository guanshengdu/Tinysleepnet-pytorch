import warnings
warnings.filterwarnings('ignore')
import argparse
import importlib
import os
# import tensorflow as tf

from test_hpc_train import train
# import os
# os.environ['CUDA_VISIBLE_DEVICES'] = '-1'

from types import SimpleNamespace

def run(args, db, gpu, from_fold, to_fold, suffix='', random_seed=42):
    # Set GPU visible

    # Config file
    config_file = os.path.join('./config', f'{db}.py')
    spec = importlib.util.spec_from_file_location("*", config_file)
    config = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(config)

    # Output directory
    output_dir = f'./out_{db}{suffix}'

    assert from_fold <= to_fold
    assert to_fold < config.params['n_folds']

    # Training
    for fold_idx in range(from_fold, to_fold+1):
        train(
            args=args,
            config_file=config_file,
            fold_idx=fold_idx,
            output_dir=os.path.join(output_dir, 'train'),
            log_file=os.path.join(output_dir, f'train_{gpu}.log'),
            restart=True,
            random_seed=random_seed+fold_idx,
        )

        # Reset tensorflow graph
        # tf.reset_default_graph()


if __name__ == '__main__':

    # Save the current working directory
    # cwd = os.getcwd()

    # Set the current working directory
    os.chdir('/cfs/earth/scratch/dugua001/Tinysleepnet-pytorch/')

    # Verify the current working directory
    print(f"Current working directory: {os.getcwd()}")

    """
    parser = argparse.ArgumentParser()
    parser.add_argument("--db", type=str, required=True)
    parser.add_argument("--gpu", type=int, required=True)
    parser.add_argument("--from_fold", type=int, required=True)
    parser.add_argument("--to_fold", type=int, required=True)
    parser.add_argument("--suffix", type=str, default='')
    parser.add_argument("--random_seed", type=int, default=42)
    parser.add_argument("--test_seq_len", type=int, default=20)
    parser.add_argument("--test_batch_size", type=int, default=15)
    parser.add_argument("--n_epochs", type=int, default=200)
    args = parser.parse_args()
    """

    args = SimpleNamespace(
        db="sleepedf",
        gpu=0,
        from_fold=0,
        to_fold=19,
        suffix="",
        random_seed=42,
        test_seq_len=20,
        test_batch_size=15,
        n_epochs=200,
    )

    print(f"args is : {args}")

    run(
        args=args,
        db=args.db,
        gpu=args.gpu,
        from_fold=args.from_fold,
        to_fold=args.to_fold,
        suffix=args.suffix,
        random_seed=args.random_seed,
    )

