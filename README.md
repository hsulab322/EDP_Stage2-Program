# EDP stage2 experiment instruction
~~You can skip this instruction by downloading the program executables `.exe` on the Google Drive. (recommend)~~

## Requirements
The folder named EDP_stage2-XXXX is where the program is located.
There is a `data` folder, `.py` file and `interface` folder inside a experiment folder.


## Create and activate a psychopy environment

1. open your cmd or terminal (you can open it from the program folder to skip step 2)
2. change directory to the experiment program folders
3. create a virtual environment named EDP_stage2
    ```cmd
    conda create --name EDP_stage2 python=3.7.9
    ```
4. activate the environment
    ```cmd
    conda activate EDP_stage2
    ```
5. Install all the packages we need (make sure the requirements.txt is in the directory)
    ```cmd
    pip install -r requirements.txt
    ```

> You can just install all the required packages in your base environment but creating a new environment is recommended because packages are easy to conflict with each other.


## Run the experiment program
1. activate the environment
    ```cmd
    conda activate EDP_stage2
    ```
2. execute the python script and
   ```cmd
   python EDP_stage2-XXX.py
    ```
