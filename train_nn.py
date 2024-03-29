"""Conv Nets training script."""
import click
import numpy as np
np.random.seed(9)

import data
import util
from nn import create_net


@click.command()
@click.option('--cnf', default='configs/c_512_4x4_32.py', show_default=True,
              help='Path or name of configuration module.')
@click.option('--weights_from', default=None, show_default=True,
              help='Path to initial weights file.')
def main(cnf, weights_from):

    config = util.load_module(cnf).config
    # print(config)
    if weights_from is None:
        weights_from = config.weights_file
    else:
        weights_from = str(weights_from)
    print(config.get('train_dir'))
    files = data.get_image_files(config.get('train_dir'))
    names = data.get_names(files)
    labels = data.get_labels(names).astype(np.float32)
    print("Checkpoint 5")
    net = create_net(config)
    print("Checkpoint 6")
    print(weights_from)
    # print(net.load_params_from())
    try:
        print("Checkpoint 7")
        net.load_params_from(weights_from)
        print("Checkpoint 8")
        print("loaded weights from {}".format(weights_from))
    except IOError:
        print("couldn't load weights starting from scratch")

    print("fitting ...")
    print(files)
    print(labels)
    net.fit(files, labels)

if __name__ == '__main__':
    main()

