echo "activating conda environment"
dire=`pwd`
echo $dire
eval "$($(which conda) 'shell.bash' 'hook')"
conda env create --file=viral.yml
conda activate viral
script="$dire/variantcalling.sh"
bash "$script"
