
# coding: utf-8

# In[30]:


# Ksenia Lepikhina
# TLEN 5540


# In[31]:


import ntplib
from time import ctime
import random


# In[32]:


c = ntplib.NTPClient()
timeServers = ['time-c.nist.gov','pool.ntp.org',
               'time.google.com', 'tick.usnogps.navy.mil',
              'utcnist.colorado.edu']
server = random.choice(timeServers)
response = c.request(server, version=3)
print(ctime(response.tx_time))

