# README

## Manager Informations
If you want to use the manager outside the VM (e.g. python script) you should permit the incoming IP-Adress in the Asterisk Server. You can control the permissions over the GUI. After that you have to change the IP-Adress in the Python-Script too. 
Config datas should be manipulated over the Virtual-Box. 

Now we need a script to auto generate SIP.conf and Extension.conf.

Done right now:
* Asterisk call to different numbers
* Parallel calls over python script
* Call is recorded and saved into the shared folder of the Host-Guest-Machine
* A silent playback is called after the called one answered
