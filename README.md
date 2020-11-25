# GraphWalker to RobotFramework Offline Converter
Convert GraphWalker models to actual test cases for RobotFramework! In seconds!

# Table of contents
<!--ts-->
   * [Table of contents](#table-of-contents)
   * [Documentation](#documentation)
   * [Installation](#installation)
   * [Prerequisites](#prerequisites)
      * [GraphWalker CLI](#graphwalker-cli)
      * [Model](#model)
      * [Syntax](#syntax)
   * [Usage](#usage)
   * [Output](#output)
      * [Test Case file](#test-case-file)
      * [Keyword file](#keyword-file)
<!--te-->

# Documentation
[GraphWalker](https://github.com/GraphWalker/graphwalker-project/wiki) | 
[RobotFramework](https://robotframework.org/#documentation)

# Installation
There is actually no installation required. All you need is Python to run the program.
All the required modules are already built into Python.

# Prerequisites
* ### GraphWalker CLI
  You need GraphWalker CLI to generate the model steps.
  Download the latest version [here](https://graphwalker.github.io/).
  
* ### Model
  You need to create a model in GraphWalker Studio, which you then download as a json file.
  Download the latest version of GraphWalker Studio [here](https://graphwalker.github.io/)

* ### Syntax
  When creating the model in GraphWalker Studio, it is recommended to use **v** (vertex) or **e** (edge) in the start of the name and _ instead of spaces.
  You just need to match the name of the vertex/edge with the keywords that you will be using.
  
  Example below:
  ```
  v_Home_Page
  e_Go_To_Settings
  ```
  
# Usage
1. Either double click the converter.py file or open it through the terminal to start the program.
```bash
python converter.py
```
2. Name your RobotFramework Test Case in the text field that says "Type test case name here".
3. Click on the "GraphWalker CLI" button, locate and open your graphwalker-cli.4.x.x.jar file.
4. Click on the "JSON model" button, locate and open your model.json file that you want to use.
5. Click the "Go" button to start generating the tests.
6. When the tests are done and the files are created, the Go button turns green. This can take a while, depending on how fast the computer is and how many steps needs to be generated.
7. Click on the "Quit" button to exit the program.

# Output
* ### Test Case file
  The name of the file will be **test_case.robot**, and it will be located in the same directory as the converter program itself.
  You can then fill in with the settings that you want, and all the other things you need to run the test, or you can copy the whole test case to a robot file of choice.
  The syntax will look something like this:
  ```robot
  *** Test Cases ***
  Test Case Name That You Chose In The Program
      [Documentation]
      v_Test_Not_Started
      e_Begin_Web_Test
      v_Home_Page
      e_Go_To_Settings
      v_Settings_Page
      e_Go_Back
      v_Home_Page
      e_Go_To_Settings
  ```
* ### Keyword file
  The other output file will be **keywords.robot**, and it will be in the same location as the test case file.
  
  It will show all the possible keywords that exist in the test case file. You can now start developing the keywords with the desired code.

  Example below:
  ```robot
  *** Keywords ***
  v_Test_Not_Started
  e_Begin_Web_Test
  v_Home_Page
  e_Go_To_Settings
  v_Settings_Page
  e_Go_Back
  ```
  Notice how it does not include duplicates. Only unique keywords in this file.
