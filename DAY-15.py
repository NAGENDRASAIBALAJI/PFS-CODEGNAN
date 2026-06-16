'''
DAY-15
------

DATA ANALYSIS:
--------------
-->THIS IS PROCESS OF INSPECTING, CLEANING,TRANSFROMING, AND MODELING DATA TO DISCOVER USEFUL INSIGHTS...
TYPES OF DA:
------------
1.DESCRIPTIVE ANALYSIS
----------------------
-->SUMMARIZING CAUSES

2.DIAGNOSTIC ANALYSIS:
----------------------
-->UNDERSTANDING CAUSES

3.PREDICTIVE ANALYSIS:
----------------------
-->FORECASTING FUTURE OUTCOMES
4.PRESCRIPTIVE ANALYSIS:
------------------------
-->SUGGESTING ACTINS BASED ON DATA

WHY DA:
-------
-->TO IMPROVE DECISION MAKING
-->DETECTS TRENDS & PATTERNS

NUMPY (NUMERICAL PYTHON):
-------------------------
-->THIS PYTHON LIBERARY FOR NUMERICAL COMPUTING .IT PROVIDES SUPPORT FOR
MULTI-DIMENSINAL ARRAYS, AND LINEAR ALGEBRA OPERATION AMKING IT ESSENTIAL FOR DATA ANALYSIS

USING NUMPY IN DA:
------------------
-->IMPROVED PERFROMANCE
-->SIMPLIFIES COMPLEX OPERATIONS
-->EASY DATA MANIPILATION....

import numpy as np
arr_1 = np.array([10,20,30,40,50])
print(arr_1)

---------------------
import numpy as np
arr_1 = np.array([[10,20,30], [30,40,50]])
print(arr_1)
print(arr_1.shape)
reshaped = arr_1.reshape(3,2)
print(reshaped)
-----------------------
import numpy as np
arr_1 = np.array([10,20,30])
nrm_copy = arr_1.view()
arr_1[0] = 100
print(nrm_copy)
print(arr_1)
----------------------------
copy_dee = arr_1.copy()
arr_1[1] = 200
print(copy_dee)
print(arr_1)


PANDAS:
-------
-->THE PANDAS IS A POWERFUL DATA MANIPULATION AND ANALYSIS LIBRARY..
-->WHERE IT PROVIDES DATA STRUCTURE LIKE SERIES AND DATAFRAME FOR EFFICIENCE
DATA HANDLING...

'''
import pandas as pd
any_ = pd.Series(['12999','52996','4999','69999'],
                 index = ['earbuds','watch','smartphone','laptop'])
print(any_)































