#
Berkeley Marina to Lombardie

Citations 

Stirling numbers of the Second Kind (https://en.wikipedia.org/wiki/Stirling_numbers_of_the_second_kind)
Simulated Annealing (http://katrinaeg.com/simulated-annealing.html?fbclid=IwAR3mC2Ggqrl5Jeb3J0GmyEPBeG_D45ZkhQ95kcmq74s9BIW64sZbDxOxmJ0)


Steps for implementation:
1. Download all_inputs from Piazza
2. Create a folder called all_inputs and in this folder make a folder called small, medium, and large Put the inputs for small, medium, and large in their respective folders.
3. Now go back to the head directory and go into the friends_solver folder and open solver.py in any editor.
4. In solver.py go to line 226 and change size_categories = [“<size_of_input>”]. 
5. Edit <size_of_input> to be the small/medium/large input set you would like to create outputs for.
6. On line 15 change path_to_outputs = "../<folder_name>" and change folder_name to be the folder you want to put all your outputs into (The output folder you name will appear in the head directory).
7. On line 255 change processes = (the number of cores in your computer)
8. Now that you are in the friends_solver directory, run the command python3 solver.py (as long as have the most recent version of networkx downloaded). 
9. Outputs will be generated into the output folder you named on step 6. 

