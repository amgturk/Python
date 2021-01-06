import numpy as np

def WaterTankVolume(lst):
  array= np.array(lst)

  #Create a new empty matrix  --------------
  max_element=max(array)  #it'll be row size
  length_of_array=len(array) # it'll be column size
  volume_array=np.zeros([max_element,length_of_array])
  # --------------------

  # Fill empty areas with ones ( as in graph in question file -> blue areas 0, white areas 1)-----
  for i in range(len(array)): 
      volume_array[0:max_element-array[i],i]=1
  # -----------------------------------  

  # Sum the ones if they're contained with zeros ( these part could easily be shortened but need)
  total=0
  sum_list=[]
  for row in volume_array:
      col=np.array(np.where(row == 0))
      rw,cl=col.shape
      total=0
      if(cl > 1):
          for i in range(cl-1):
              total+=(row[col[0][i]:col[0][i+1]].sum())  
      sum_list.append(total)
  # ------------------------------------    
      
  print("Volume of water tank is: ", sum(sum_list))
  return  sum(sum_list)
    
