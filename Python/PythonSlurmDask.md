## Python SLURM job control via DASK

These notes adapted from official documentation at https://jobqueue.dask.org/en/latest/

#### Benefits and Limitations (pros and cons)

DASK makes it very easy for you to write portable code, that you can run and debug locally in your laptop with pycharm or whatever, and scale up your execution to whatever cluster you happen to have available when you want to scale up. Their compatibility list today (2019) includes: OAR, PBS, SGE, SLURM, MOAB, and LSF.

They do a great job following well-known code patterns of pandas, numpy, scikit, and so on, so your learning curve should be very easy, and mutually beneficial to these other libraries.

There is one downside: One controller job starts, and then launches all the other jobs. Only when they all start, does anything begin. A more efficient use of the cluster would be allowing the cluster to manage which jobs run when; suppose you have a cluster with 100 nodes in it, and you have 999 computations you need to do. If you request `cluster.scale(999)` your job will never run. So maybe you request 100, but suppose other people are also using the cluster at the same time as you, and one of them has a long-running job. You never know exactly how many jobs you can run in parallel; you just want to `sbatch` an array of 999 jobs, and let the cluster schedule them whenever and wherever it can. You make your 999 batch jobs all store their results in a shared directory. You also submit a summary job to process the results from the shared direcotry, using the `sbatch --dependency=` option to make the summary job dependent on all 999 array jobs completion. This way, the cluster will run all of your jobs as fast as it can, on whatever resources it has available and you don't need to think about it or care.

If you want optimal performance as described above, you need to submit jobs using `sbatch` and parse the output to get the jobid; or you could use `pyslurm` if only it were compatible. Our version of slurm (May 2019) is 17.02.11, whereas the minimum version for `pyslurm` compatibility is 17.11.10. So until we upgrade our slurm installation, `sbatch` is the only available option for optimal performance, whereas DASK provides maximum portability.

#### Installation

* If using pip:

        pip install dask_jobqueue

* If using conda:

        conda install dask-jobqueue -c conda-forge
    

#### Configuration

* In your local development environment (laptop pycharm etc) no configuration necessary - skip ahead to  "Example Usage." You can write portable code that works on both your local environment and the distributed environment. The only caveat is that when run on the cluster, the following configuration steps are needed:

* Only do these steps on the cluster, not on your local laptop:

* Manually load the module once. It will automatically create `~/.config/dask` with example yaml files.

               echo "import dask_jobqueue" | python3

* Edit `~/.config/dask/dask.yaml`:

           temporary-directory: /scratch

* Edit `~/.config/dask/distributed.yaml`
  
     * no changes

* Edit `~/.config/dask/jobqueue.yaml`
  
     * un-comment jobqueue and the slurm section. (Delete everything else)
     
     * Intelligently edit your queue settings
       
       * Set `local-directory` to `/scratch`
       * If you have conda loaded, and the right environment activated, automatically in your `.bash_profile` and `.bashrc`, you can probably skip this step: If you need to add extra options to your slurm `job_script`, edit `env-extra`. For example, you might need something like this: `env-extra: ['source /cluster/home/username/example_env_extra.sh']` and you might need to create `/cluster/home/username/example_env_extra.sh` like this [example env extra.sh](files/example_env_extra.sh). For more info, see [In dask_jobqueue, how to add extra lines to job_script](https://stackoverflow.com/questions/56148498/in-dask-jobqueue-how-to-add-extra-lines-to-job-script)
       
       * Here is my initial example: [jobqueue.yaml](files/jobqueue.yaml)
       

#### Example Usage

* On your laptop, try some of the basic examples from https://docs.dask.org/en/latest/#familiar-user-interface

     * Here is one complete example that I did: [funwithdask.py](files/funwithdask.py)

* On the cluster, be sure to complete the "Configuration" section above, then try this. If you have problems, or want to know how it works, see [How this works](https://jobqueue.dask.org/en/latest/howitworks.html). After doing this, normal dask commands like you did on a single system automagically use the cluster. Simply repeat the basic examples you did above.

         from dask_jobqueue import SLURMCluster
         
         cluster = SLURMCluster()    # could use class constructor to override settings from yaml
         cluster.scale(100)          # Start 100 workers in 100 jobs
         
         from distributed import Client
         client = Client(cluster)
         
         # repeat whatever basic examples you did before... now they're distributed...