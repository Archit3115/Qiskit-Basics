#!/usr/bin/env python
# coding: utf-8

# In[1]:


import qiskit


# In[2]:


from qiskit import IBMQ


# In[3]:


IBMQ.load_account()


# In[2]:


from qiskit import *
import matplotlib as mpl


# In[3]:


qr = QuantumRegister(2)


# In[4]:


cr = ClassicalRegister(2)


# In[5]:


circuit = QuantumCircuit(qr , cr)

%matplotlib inline
# In[6]:


circuit.draw


# In[7]:


circuit.draw()


# In[8]:


circuit.h(qr[0])


# In[9]:


pip install pylatexenc


# In[10]:


circuit.draw(output='mpl')


# In[11]:


circuit.cx(qr[0], qr[1])


# In[12]:


circuit.draw(output='mpl')


# In[13]:


circuit.measure(qr, cr)


# In[14]:


circuit.draw(output='mpl')


# In[15]:


simulator = Aer.get_backend('qasm_simulator')


# In[16]:


result = execute(circuit, backend = simulator).result()


# In[17]:


from qiskit.tools.visualization import plot_histogram


# In[18]:


plot_histogram(result.get_counts(circuit))


# In[19]:


IBMQ.load_account()


# In[60]:


provider = IBMQ.get_provider('ibm-q')


# In[61]:


qcomp = provider.get_backend('ibmq_16_melbourne')


# In[62]:


job = execute(circuit, backend=qcomp)


# In[63]:


from qiskit.tools.monitor import job_monitor


# In[68]:


job_monitor(job)


# In[69]:


result = job.result()


# In[70]:


plot_histogram(result.get_counts(circuit))


# In[ ]:





# In[ ]:




