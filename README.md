# Neural-recruitment-during-SCS
Source files to model recruitment of cells during SCS. Associated with the following paper: Rogers, Evan R., Hans J. Zander, and Scott F. Lempka. "Neural Recruitment During Conventional, Burst, and 10-kHz Spinal Cord Stimulation for Pain." The journal of pain 23.3 (2022): 434-449.



Included is the template to generate a morphological;y-realistic superficial dorsal horn local cell, as well as useful .mod files to include for biophysical modeling in the NEURON software environment.

Additionally, the file "basic_setup.py" gives an example of how to load the cell to begin a simulation.

Helpful references for the material are as follows:

NEURON simulation environment (https://neuron.yale.edu/neuron/):
  Hines, Michael L., and Nicholas T. Carnevale. "The NEURON simulation environment." Neural computation 9.6 (1997): 1179-1209.
  Carnevale, Nicholas T., and Michael L. Hines. The NEURON book. Cambridge University Press, 2006.

Morphological reconstruction:
  Luz, Liliana L., et al. "Monosynaptic excitatory inputs to spinal lamina I anterolateral‐tract‐projecting neurons from neighbouring lamina I neurons." The Journal 
  of   Physiology 588.22 (2010): 4489-4505.
  Link to reconstruction: https://neuromorpho.org/neuron_info.jsp?neuron_name=L395-LCN
  
Ion channels (experimental & model files):
  Melnick, Igor V., et al. "Ionic basis of tonic firing in spinal substantia gelatinosa neurons of rat." Journal of neurophysiology 91.2 (2004): 646-655.
  (Made available at: https://senselab.med.yale.edu/ModelDB/showmodel.cshtml?model=62285#tabs-1)
  
  Ion channel directory: Zhang, Tianhe C., John J. Janik, and Warren M. Grill. "Modeling effects of spinal cord stimulation on wide-dynamic range dorsal horn neurons: influence of stimulation frequency and GABAergic inhibition." Journal of neurophysiology 112.3 (2014): 552-567.
  (Made available at: https://senselab.med.yale.edu/modeldb/ShowModel?model=168414&file=/ZhangEtAl2014/#tabs-1)
 
 Algorithm for myelinating the model cell:
  Aberra, Aman S., Angel V. Peterchev, and Warren M. Grill. "Biophysically realistic neuron models for simulation of cortical stimulation." Journal of neural     
  engineering 15.6 (2018): 066023.
  
  (Code available at: https://senselab.med.yale.edu/modeldb/ShowModel?model=241165)
  


  
