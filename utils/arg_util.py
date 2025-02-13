import argparse, os
from datetime import datetime
import logging


logger = logging.getLogger()
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(filename)s %(lineno)d: %(message)s',
                    datefmt='%m-%d %H:%M:%S')
DATE_TIME = "%y_%m_%d %H:%M:%S"


class ArgparseUtil(object):
    """
    参数解析工具类
    """
    def __init__(self):
        """ Basic args """
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument("--seed", default=1, type=int)
        self.parser.add_argument('--gpu_device_id', default=0, type=int, 
                                 help='the GPU NO. Use int because compare with gpu total count')
        self.parser.add_argument("--data_type", default=None, type=str)
        self.parser.add_argument("--label_name", default='Celltype', type=str)
        self.parser.add_argument("--project", default='hGOBP_demo', type=str)
        self.parser.add_argument("--gmt_path", default='human_gobp', type=str)
        self.parser.add_argument("--save_model_per_epoch", type=int, default=1, help="0 is false, 1 is true")
        # self.parser.add_argument("--ignore_gpu", type=int, default=0, help="0 is false, 1 is true")

    def train_classifier(self):
        """ task args """
        self.parser.add_argument("--enable_train", type=int, default=1, help="0 is false, 1 is true")
        self.parser.add_argument("--data_seed", type=int, default=0, help="seed used to create mock data or split data")
        self.parser.add_argument("--val_data_ratio", type=float, default=0.2, help="split train data as train and val")
        self.parser.add_argument("--read_cached_prediction", type=int, default=1, help="0 is false, overwite; 1 true")
        self.parser.add_argument("--n_epoch", type=int, default=30, help="")
        self.parser.add_argument("--learning_rate", type=float, default=0.001, help="")
        self.parser.add_argument("--depth", type=int, default=1, help="")
        self.parser.add_argument("--embed_dim", type=int, default=48, help="")
        self.parser.add_argument("--num_heads", type=int, default=4, help="")
        self.parser.add_argument("--batch_size", type=int, default=8, help="")
        args = self.parser.parse_args()
        return args


def save_args(args, output_dir='.', with_time_at_filename=False):
    os.makedirs(output_dir, exist_ok=True)

    t0 = datetime.now().strftime(DATE_TIME)
    if with_time_at_filename:
        out_file = os.path.join(output_dir, f"args-{t0}.txt")
    else:
        out_file = os.path.join(output_dir, f"args.txt")
    with open(out_file, "w", encoding='utf-8') as f:
        f.write(f'{t0}\n')
        for arg, value in vars(args).items():
            f.write(f"{arg}: {value}\n")


def log_args(args, logger):
    for arg, value in vars(args).items():
        logger.info(f"{arg}: {value}")
