# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
__conda_setup="$('/cluster/tufts/SOMELAB/anaconda3/bin/conda' 'shell.bash' 'hook' 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
    if [ -f "/cluster/tufts/SOMELAB/anaconda3/etc/profile.d/conda.sh" ]; then
        . "/cluster/tufts/SOMELAB/anaconda3/etc/profile.d/conda.sh"
    else
        export PATH="/cluster/tufts/SOMELAB/anaconda3/bin:$PATH"
    fi
fi
unset __conda_setup
# <<< conda initialize <<<


conda activate fooenv

