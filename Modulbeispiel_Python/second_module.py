import first_module	

#wenn von dieser Datei aus gestartet wird, wird name nie zu main und deswegen wird die main Methode im first_module nie ausgeführt.


# eine andere Möglichkeit ist: 
# first_module.main()
# dies führt dann aber auch die main Methode aus, falls gewünscht. Der Import muß aber vorhanden sein.



print ("Second Module's Name: {}".format(__name__))