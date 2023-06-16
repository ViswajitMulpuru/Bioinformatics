#!/bin/bash
#PBS -N Viswajit
#PBS -q gpu
#PBS -l select=1:ncpus=40:ngpus=2
#PBS -o out.log
#PBS -e error.log

cd /home/nidhi/rec
source /apps/gromacs/gpu/bin/GMXRC
source /apps/intel/parallel_studio_xe_2018_update3_cluster_edition/bin/compilervars.sh intel64

export LD_LIBRARY_PATH=/usr/local/cuda/lib64:$LD_LIBRARY_PATH
cat $PBS_NODEFILE | uniq > nodes
nvidia-smi | tee nv.log

cd PBS_O_WORKDIR
mpirun -np 2 /apps/gromacs/gpu/bin/gmx_mpi mdrun -ntomp 20 -pin on -cpi -deffnm md
