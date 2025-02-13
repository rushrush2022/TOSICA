# Here, export CUDA_VISIBLE_DEVICES=1 is actually disable GPU as the valid value is 0, as there is only 1 GPU whose num starts from 0
# To use GPU, export CUDA_VISIBLE_DEVICES=0
export CUDA_VISIBLE_DEVICES=1
data_type=hPancreas
[ -d zlog/$data_type ] || mkdir -p zlog/$data_type
seed=118
n_epoch=30
learning_rate=0.001
enable_train=1
nohup python run.py \
--data_type $data_type \
--seed $seed \
--n_epoch $n_epoch \
--learning_rate $learning_rate \
--enable_train $enable_train \
--data_seed 0 \
--read_cached_prediction 0 \
--gmt_path human_gobp \
--project hGOBP_demo \
--depth 1 \
--embed_dim 48 \
--num_heads 4 \
--batch_size 32 \
> train$enable_train-$data_type-e$n_epoch-s$seed.log  2>&1 &