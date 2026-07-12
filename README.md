//

#### End To end ML project
This is my first ML project so i will write a step and description of this projrct you can follow them 
and able to create a ML project and  experiance a new project this is common project step

//

--------------Steps to build end to end Ml project-----------------------

1. setup with Github repo this is necessary
    -- Create a new environment For project it kept clean and structured project

        -create new environment
         conda create -p env_name python==version(i used 3.8 You can use new version for ex 3.8) -y

         -To activate new environment 
          conda activate env_name 

         - Follow This Command 
           echo "# Machine-Learning-Project-1" >> README.md
           git init
           git add README.md
           git commit -m "first commit"
           git branch -M main
           git remote add origin https://github.com/AdityaJamdar72/Machine-Learning-Project-1.git
           git push -u origin main

         - Add .gitignore file and choose a file igonrefile for this project we choose python and commit changes

         - pull the all changes for example git pull
          
2. -Add setup.py   file in folder for distributing and installing the Package required for the project 
    In the setup.py file add This in setup()
    name="Machine Learning Project-1",
    version="0.0.1",
    author="Aditya72",
    author_email="jamdaraditya26@gmail.com",
    packages=find_packages(),

    install_requires=get_requirements(file_path) ---------> here get_requirements(file_path) is function and file_path is path of file that contain modeule or library required for project the function is read lines from file_path and use in project make it should contain only module name for example some times it read "\npandas" \n should not  contain for best understanding must read "setup.py" you will  understand setup for project 

   - Add one text file for the lisiting a package and module required for this project for example requirements.txt

3. Add src file and build package 
   - Add one folder for name  is "src" means source why it added when find_package() are running anf try to find package it     going  "src" folder and In the "src" folder have a one file __init__.py it contain package needed to project

   - run this command after proper setup with necessary package and important module
     # pip install -r filename.txt ----------------> for example pip install -r requirements.txt
     if above not working  try this
     # python -m pip install -r filename.txt----------------> for example python -m pip install -r requirements.txt
    
    after package will be created and build one file filename.egg-info


5. --"src" Folder -----------> it contain project logic instead of put all in single python file
        In the src folder create another folder is "components" 

    -components -------------> it contain ML project buildings Blocks 
      > data_ingestion.py -------------> it is used to read data or import a data from database
      > data_transformation.py ------------> it is used to transform a data like cleaning , encoding, etc.
      > __init__.py ------------> it is used to create package 
      > model_trainer.py ---------> used to train model

    -pipeline -------------> it is used to create sequence of step to create train model automatically 
     > __init__.py ------------> it is used to create package 
     > predict_pipeline.py ----------> it is used to create predict pipeline 
     > train_pipeline.py ---------> it is used to create training pipeline
    
    -exception.py ----------> it is used to create custom exception
      create custom exception

    -logger.py -----------> keeps a record of everything happening
      Create alogging file to track a log

4. after all steps happen staged all file and commit and most important push all code to github us this git push -u origin main

