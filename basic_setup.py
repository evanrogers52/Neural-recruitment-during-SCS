from neuron import h, gui
h.load_file('LocalCell.hoc')   ## Load the file with the cell template (includes spatial info & connections)
LocalCell = h.LocalCell()      ## Generate a local cell from the template

###### Sections in the local cell ######
### Soma --- To access, use LocalCell.soma
h.psection(sec = LocalCell.soma) ## Example of psection of the soma

### AIS --- Axon initial segment --- to access, use LocalCell.ais
h.psection(sec = LocalCell.ais) ## Example of psection of the soma

### dendrites -- The dendrites -- to access, use LocalCell.dend[i], where i is the index of the section
h.psection(sec = LocalCell.dend[42]) ## Example of psection of the soma

### axon -- The rest of the axon (a list of all sections) -- to access, use LocalCell.axon[i], where i is the index of the section
h.psection(sec = LocalCell.axon[12]) ## Example of psection of the soma


### nodes -- The nodes of Ranvier, as well as axon terminations -- to access, use LocalCell.node[i], where i is the index of the section
h.psection(sec = LocalCell.node[400]) ## Example of psection of the soma
#########################################

## Note: This provides a template to make performing simulations easier/efficient. 
##       Before using, make sure sections are appropriately discretized (e.g., nseg) 

## Note: The dendrites, axon, and nodes are in lists.
##       To access all sections of a given type conveniently, you can
##       loop through the list.


## Note: This template does not differentiate between myelinated and unmyelinated axon. 
##       Therefore, the easiest way to do this when assigning biophysical properties 
##       is to check the diameter --- unmyelinated axon will be of diameter < 0.2 um.

## Note: the list of nodes of Ranvier are registered to all bifurcations and terminals. 
##       One can check whether the node is attached to unmyelinated axon to be more precise
##       and assign properties of unmyelinated axons

