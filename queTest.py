"""

&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&& NEW RUN &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
loadSavedToDo
^^^^^^ TIME: (3, 2, 539388) ^^^^^
readFromFile
 --- start of readFromFile 150 --- 
{'notCompleted': ['8'], 'completed': ['9', '7', '6', '5', '4', '3', '2', '1', '0'], 'deleted': []}
^^^^^^ TIME: (3, 2, 539406) ^^^^^
Done reading from File 
{'notCompleted': ['8'], 'completed': ['9', '7', '6', '5', '4', '3', '2', '1', '0'], 'deleted': []}
127.0.0.1 - - [14/May/2022 13:03:02] "GET /loadsavedtodo HTTP/1.1" 200 -
Que before append
[]
Que after append
[('notCompleted', '0')]
addTodo
addSingleTodo
^^^^^^ TIME: (3, 5, 606330) ^^^^^
Attempting: Add to notCompleted: 
 Result: Added to notCompleted Successfully 

 @@@@@ DONE?? 
127.0.0.1 - - [14/May/2022 13:03:05] "GET /addtodo/notCompleted/0 HTTP/1.1" 200 -
Que before append
[('notCompleted', '0')]
Que after append
[('notCompleted', '0'), ('removeCompleted', '0')]
addTodo
removeSingleTodo
^^^^^^ TIME: (3, 5, 609676) ^^^^^
['9', '7', '6', '5', '4', '3', '2', '1']
^^^^^^ TIME: (3, 5, 609710) ^^^^^
Attempting: Remove ∆∆ 0 ∆∆ from Completed 
 Result: Removed Successfully #completed 

 @@@@@ DONE?? 
127.0.0.1 - - [14/May/2022 13:03:05] "GET /addtodo/removeCompleted/0 HTTP/1.1" 200 -
save Sleep BEFORE
save Sleep AFTER
saveToFile
^^^^^^ TIME: (3, 5, 613000) ^^^^^
Saving now
combineNCD
^^^^^^ TIME: (3, 5, 613030) ^^^^^
 --- CombineNCD --- 
{'notCompleted': ['0', '8'], 'completed': ['9', '7', '6', '5', '4', '3', '2', '1'], 'deleted': []}
^^^^^^ TIME: (3, 5, 613056) ^^^^^
writeToFile
 --- write to fil 174 --- 
{'notCompleted': ['0', '8'], 'completed': ['9', '7', '6', '5', '4', '3', '2', '1'], 'deleted': []}
^^^^^^ TIME: (3, 5, 613083) ^^^^^
 --- json.dumps alltodo 179 --- 
{"notCompleted": ["0", "8"], "completed": ["9", "7", "6", "5", "4", "3", "2", "1"], "deleted": []}
^^^^^^ TIME: (3, 5, 614045) ^^^^^
Successfully Saved 0
Que after save
[('notCompleted', '0'), ('removeCompleted', '0')]
Que after Pop
[]
127.0.0.1 - - [14/May/2022 13:03:05] "GET /save HTTP/1.1" 200 -
Que before append
[]
Que after append
[('notCompleted', '1')]
addTodo
addSingleTodo
^^^^^^ TIME: (3, 6, 592656) ^^^^^
Attempting: Add to notCompleted: 
 Result: Added to notCompleted Successfully 

 @@@@@ DONE?? 
127.0.0.1 - - [14/May/2022 13:03:06] "GET /addtodo/notCompleted/1 HTTP/1.1" 200 -
Que before append
[('notCompleted', '1')]
Que after append
[('notCompleted', '1'), ('removeCompleted', '1')]
addTodo
removeSingleTodo
^^^^^^ TIME: (3, 6, 594076) ^^^^^
['9', '7', '6', '5', '4', '3', '2']
^^^^^^ TIME: (3, 6, 594093) ^^^^^
Attempting: Remove ∆∆ 1 ∆∆ from Completed 
 Result: Removed Successfully #completed 

 @@@@@ DONE?? 
127.0.0.1 - - [14/May/2022 13:03:06] "GET /addtodo/removeCompleted/1 HTTP/1.1" 200 -
save Sleep BEFORE
save Sleep AFTER
saveToFile
^^^^^^ TIME: (3, 6, 611877) ^^^^^
Saving now
combineNCD
^^^^^^ TIME: (3, 6, 611906) ^^^^^
 --- CombineNCD --- 
{'notCompleted': ['1', '0', '8'], 'completed': ['9', '7', '6', '5', '4', '3', '2'], 'deleted': []}
^^^^^^ TIME: (3, 6, 611926) ^^^^^
writeToFile
 --- write to fil 174 --- 
{'notCompleted': ['1', '0', '8'], 'completed': ['9', '7', '6', '5', '4', '3', '2'], 'deleted': []}
^^^^^^ TIME: (3, 6, 611946) ^^^^^
 --- json.dumps alltodo 179 --- 
{"notCompleted": ["1", "0", "8"], "completed": ["9", "7", "6", "5", "4", "3", "2"], "deleted": []}
^^^^^^ TIME: (3, 6, 612911) ^^^^^
Successfully Saved 1
Que after save
[('notCompleted', '1'), ('removeCompleted', '1')]
Que after Pop
[]
127.0.0.1 - - [14/May/2022 13:03:06] "GET /save HTTP/1.1" 200 -
Que before append
[]
Que after append
[('notCompleted', '2')]
addTodo
addSingleTodo
^^^^^^ TIME: (3, 6, 978282) ^^^^^
Attempting: Add to notCompleted: 
 Result: Added to notCompleted Successfully 

 @@@@@ DONE?? 
127.0.0.1 - - [14/May/2022 13:03:06] "GET /addtodo/notCompleted/2 HTTP/1.1" 200 -
Que before append
[('notCompleted', '2')]
Que after append
[('notCompleted', '2'), ('removeCompleted', '2')]
addTodo
removeSingleTodo
^^^^^^ TIME: (3, 6, 984911) ^^^^^
['9', '7', '6', '5', '4', '3']
^^^^^^ TIME: (3, 6, 984943) ^^^^^
Attempting: Remove ∆∆ 2 ∆∆ from Completed 
 Result: Removed Successfully #completed 

 @@@@@ DONE?? 
127.0.0.1 - - [14/May/2022 13:03:06] "GET /addtodo/removeCompleted/2 HTTP/1.1" 200 -
save Sleep BEFORE
save Sleep AFTER
saveToFile
^^^^^^ TIME: (3, 6, 989118) ^^^^^
Saving now
combineNCD
^^^^^^ TIME: (3, 6, 989167) ^^^^^
 --- CombineNCD --- 
{'notCompleted': ['2', '1', '0', '8'], 'completed': ['9', '7', '6', '5', '4', '3'], 'deleted': []}
^^^^^^ TIME: (3, 6, 989185) ^^^^^
writeToFile
 --- write to fil 174 --- 
{'notCompleted': ['2', '1', '0', '8'], 'completed': ['9', '7', '6', '5', '4', '3'], 'deleted': []}
^^^^^^ TIME: (3, 6, 989198) ^^^^^
 --- json.dumps alltodo 179 --- 
{"notCompleted": ["2", "1", "0", "8"], "completed": ["9", "7", "6", "5", "4", "3"], "deleted": []}
^^^^^^ TIME: (3, 6, 989506) ^^^^^
Successfully Saved 2
Que after save
[('notCompleted', '2'), ('removeCompleted', '2')]
Que after Pop
[]
127.0.0.1 - - [14/May/2022 13:03:06] "GET /save HTTP/1.1" 200 -
Que before append
[]
Que after append
[('notCompleted', '3')]
addTodo
addSingleTodo
^^^^^^ TIME: (3, 7, 357710) ^^^^^
Attempting: Add to notCompleted: 
 Result: Added to notCompleted Successfully 

 @@@@@ DONE?? 
127.0.0.1 - - [14/May/2022 13:03:07] "GET /addtodo/notCompleted/3 HTTP/1.1" 200 -
Que before append
[('notCompleted', '3')]
Que after append
[('notCompleted', '3'), ('removeCompleted', '3')]
addTodo
removeSingleTodo
save Sleep BEFORE
save Sleep AFTER
saveToFile
^^^^^^ TIME: (3, 7, 359897) ^^^^^
Saving now
combineNCD
^^^^^^ TIME: (3, 7, 359909) ^^^^^
 --- CombineNCD --- 
{'notCompleted': ['3', '2', '1', '0', '8'], 'completed': ['9', '7', '6', '5', '4', '3'], 'deleted': []}
^^^^^^ TIME: (3, 7, 359925) ^^^^^
writeToFile
 --- write to fil 174 --- 
{'notCompleted': ['3', '2', '1', '0', '8'], 'completed': ['9', '7', '6', '5', '4', '3'], 'deleted': []}
^^^^^^ TIME: (3, 7, 359940) ^^^^^
^^^^^^ TIME: (3, 7, 359795) ^^^^^
['9', '7', '6', '5', '4']
^^^^^^ TIME: (3, 7, 359998) ^^^^^
Attempting: Remove ∆∆ 3 ∆∆ from Completed 
 Result: Removed Successfully #completed 

 @@@@@ DONE?? 
127.0.0.1 - - [14/May/2022 13:03:07] "GET /addtodo/removeCompleted/3 HTTP/1.1" 200 -
 --- json.dumps alltodo 179 --- 
{"notCompleted": ["3", "2", "1", "0", "8"], "completed": ["9", "7", "6", "5", "4"], "deleted": []}
^^^^^^ TIME: (3, 7, 360999) ^^^^^
Successfully Saved 3
Que after save
[('notCompleted', '3'), ('removeCompleted', '3')]
Que after Pop
[]
127.0.0.1 - - [14/May/2022 13:03:07] "GET /save HTTP/1.1" 200 -
Que before append
[]
Que after append
[('notCompleted', '4')]
addTodo
addSingleTodo
^^^^^^ TIME: (3, 7, 691611) ^^^^^
Attempting: Add to notCompleted: 
 Result: Added to notCompleted Successfully 

 @@@@@ DONE?? 
127.0.0.1 - - [14/May/2022 13:03:07] "GET /addtodo/notCompleted/4 HTTP/1.1" 200 -
Que before append
[('notCompleted', '4')]
Que after append
[('notCompleted', '4'), ('removeCompleted', '4')]
addTodo
removeSingleTodo
^^^^^^ TIME: (3, 7, 693386) ^^^^^
['9', '7', '6', '5']
^^^^^^ TIME: (3, 7, 693402) ^^^^^
Attempting: Remove ∆∆ 4 ∆∆ from Completed 
 Result: Removed Successfully #completed 

 @@@@@ DONE?? 
127.0.0.1 - - [14/May/2022 13:03:07] "GET /addtodo/removeCompleted/4 HTTP/1.1" 200 -
save Sleep BEFORE
save Sleep AFTER
saveToFile
^^^^^^ TIME: (3, 7, 696828) ^^^^^
Saving now
combineNCD
^^^^^^ TIME: (3, 7, 696842) ^^^^^
 --- CombineNCD --- 
{'notCompleted': ['4', '3', '2', '1', '0', '8'], 'completed': ['9', '7', '6', '5'], 'deleted': []}
^^^^^^ TIME: (3, 7, 696849) ^^^^^
writeToFile
 --- write to fil 174 --- 
{'notCompleted': ['4', '3', '2', '1', '0', '8'], 'completed': ['9', '7', '6', '5'], 'deleted': []}
^^^^^^ TIME: (3, 7, 696855) ^^^^^
 --- json.dumps alltodo 179 --- 
{"notCompleted": ["4", "3", "2", "1", "0", "8"], "completed": ["9", "7", "6", "5"], "deleted": []}
^^^^^^ TIME: (3, 7, 697003) ^^^^^
Successfully Saved 4
Que after save
[('notCompleted', '4'), ('removeCompleted', '4')]
Que after Pop
[]
127.0.0.1 - - [14/May/2022 13:03:07] "GET /save HTTP/1.1" 200 -
Que before append
[]
Que after append
[('notCompleted', '5')]
addTodo
addSingleTodo
^^^^^^ TIME: (3, 8, 8834) ^^^^^
Attempting: Add to notCompleted: 
 Result: Added to notCompleted Successfully 

 @@@@@ DONE?? 
127.0.0.1 - - [14/May/2022 13:03:08] "GET /addtodo/notCompleted/5 HTTP/1.1" 200 -
Que before append
[('notCompleted', '5')]
Que after append
[('notCompleted', '5'), ('removeCompleted', '5')]
addTodo
removeSingleTodo
^^^^^^ TIME: (3, 8, 10558) ^^^^^
['9', '7', '6']
^^^^^^ TIME: (3, 8, 10574) ^^^^^
Attempting: Remove ∆∆ 5 ∆∆ from Completed 
 Result: Removed Successfully #completed 

 @@@@@ DONE?? 
127.0.0.1 - - [14/May/2022 13:03:08] "GET /addtodo/removeCompleted/5 HTTP/1.1" 200 -
save Sleep BEFORE
save Sleep AFTER
saveToFile
^^^^^^ TIME: (3, 8, 12525) ^^^^^
Saving now
combineNCD
^^^^^^ TIME: (3, 8, 12551) ^^^^^
 --- CombineNCD --- 
{'notCompleted': ['5', '4', '3', '2', '1', '0', '8'], 'completed': ['9', '7', '6'], 'deleted': []}
^^^^^^ TIME: (3, 8, 12569) ^^^^^
writeToFile
 --- write to fil 174 --- 
{'notCompleted': ['5', '4', '3', '2', '1', '0', '8'], 'completed': ['9', '7', '6'], 'deleted': []}
^^^^^^ TIME: (3, 8, 12584) ^^^^^
 --- json.dumps alltodo 179 --- 
{"notCompleted": ["5", "4", "3", "2", "1", "0", "8"], "completed": ["9", "7", "6"], "deleted": []}
^^^^^^ TIME: (3, 8, 12918) ^^^^^
Successfully Saved 5
Que after save
[('notCompleted', '5'), ('removeCompleted', '5')]
Que after Pop
[]
127.0.0.1 - - [14/May/2022 13:03:08] "GET /save HTTP/1.1" 200 -
        Value: Task1 Result: 




"""