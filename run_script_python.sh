#!/bin/bash
#SBATCH --job-name=traffic-ari
#SBATCH --account=project_2002605
#SBATCH --partition=gpu
#SBATCH --time=24:00:00
#SBATCH --ntasks=1
#SBATCH --mem-per-cpu=64G
#SBATCH --partition=gpu
#SBATCH --gres=gpu:v100:1
##SBATCH --mail-type=BEGIN #uncomment to enable mail


source /projappl/project_2002605/deeplearning/bin/activate
python3 --version
which python3
#module load pytorch/1.10
#module load tensorflow/2.8

srun python3 lstm_pytorch.py
