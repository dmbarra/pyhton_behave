# Python with BDD project

<br>


**All scenarios for features are:**<br>
_'features/\*.features'_

**Automation test:**<br>
_I wrote automation in python, using selenium, behave and verify.<br>_
_I configured project to use local selenium, so in this project you need to start selenium in your machine.<br>_
_I use PageObject to register page components_ <br>
_I wrote basic scenarios of tests, without edge test cases or validation for components limits._<br>
_I automated just three test cases Create new task, manage tasks and create new subtask. The idea was to show how to implement project and tests cases following good practices of automation tests._<br>
_I create file to configure the framework of BDD, behave.ini_<br>
_In root of the project there is file -project_config.json- where is configured the user. Should be here all configuration related with environment to be tested_<br>
_All scenarios with tag @not_implemented means I did wrote steps for this scenarios_<br>

**Test case will fail:**<br>
_One of the scenarios is falling because one of Acceptance criteria is not respected_<br>

**Things I should have done differently:**<br>
_I wrote project_driver module, the propose is in future create flexible driver, using remote driver and another browsers_<br>
_I use a json file to load config, in this case I prefer to create proper file using another format to store configs_<br>
_The steps I split in given, when and then, but I know after time project very complex, will be terrible to manage that, 
so in this case is necessary create new layer on interaction with components and create module for each feature_<br>


**Install dependencies:**<br>
_pip install -r requirements.txt_<br>

**Run automation:**<br>
_behave_<br>