# INTEGRANTES : DARIO CASTAÑO, ANDRES POLO, FERNANDO PADILLA

from tkinter import *
from tkinter import ttk

import os

import pandas

from matplotlib import pyplot
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from sklearn.model_selection import train_test_split
from sklearn.linear_model import Lasso
from sklearn.linear_model import Ridge
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.metrics import	mean_absolute_error
from sklearn.metrics import r2_score
from sklearn.model_selection import cross_val_score

import numpy

def probarCarga():
	cmd="ab -n "+str(peticiones.get())+" -c "+str(peticiones.get())+" -e reporte.csv "+str(sitio.get())
	r=os.popen(cmd).read()
	print(r)
	
	archivo="reporte.csv"
	cabecera=["%","Tiempo"]
	data=pandas.read_csv(archivo,names=cabecera,delimiter=",", header=0)
	
	array=data.values
	xreg=array[:,0:1]
	yreg=array[:,1:2]
	
	ts=0.3
	seed=7
	xtrain, xtest, ytrain, ytest = train_test_split(xreg,yreg,test_size=ts,random_state=seed)

	if(seleccion.get()==1):
		model=LinearRegression()
		model.fit(xtrain,ytrain)
		if(model.intercept_>=0):
			rl="{model.coef_}x + {model.intercept_}"
		else:
			rl="{model.coef_}x {model.intercept_}"

		Ecuacion.delete(0,"end")
		Ecuacion.insert(0, str(rl))

		f=pyplot.figure(figsize=(4,2))
		pyplot.scatter(xtrain,ytrain)
		pyplot.grid()
		
		xmin=xreg.min()
		ymax=yreg.max()
		xmin=model.coef_*xmin+model.intercept_
		ymax=model.coef_*xmax+model.intercept_
		prediccion=model.predict(xtest)
		kf=KFold(n_splits=5,random_state=7, shuffle=True)
		resultados=cross_val_score(model,xtrain,ytrain,cv=kf, scoring="neg_mean_squared_error")
		MSE=resultados.mean()
		RMSE=numpy.sqrt(float(MSE))
		resultados=cross_val_score(model,xtrain,ytrain,cv=kf, scoring="r2")
		R2=resultados.mean()

		Model_MSE.delete(0,"end")
		Model_MSE.insert(0, str(MSE))

		Model_RMSE.delete(0,"end")
		Model_RMSE.insert(0, str(RMSE))
		
		Model_R2.delete(0,"end")
		Model_R2.insert(0, str(R2))

		pyplot.plot([xmin,xmax],[ymin,ymax],color="r")
		pyplot.show()

		canvas=FigureCanvasTkAgg(f, master=Panel)
		pw=canvas.get_tk_widget()
		pw.place(x=15, y=360)

	elif(seleccion.get()==2):
		model=Ridge()
		model.fit(xtrain,ytrain)
		if(model.intercept_>=0):
			rl="{model.coef_}x + {model.intercept_}"
		else:
			rl="{model.coef_}x {model.intercept_}"
		
		Ecuacion.delete(0,"end")
		Ecuacion.insert(0, str(rl))

		f=pyplot.figure(figsize=(4,2))
		pyplot.scatter(xtrain,ytrain)
		pyplot.grid()
		
		xmin=xreg.min()
		ymax=yreg.max()
		xmin=model.coef_*xmin+model.intercept_
		ymax=model.coef_*xmax+model.intercept_
		prediccion=model.predict(xtest)
		kf=KFold(n_splits=5,random_state=7, shuffle=True)
		resultados=cross_val_score(model,xtrain,ytrain,cv=kf, scoring="neg_mean_squared_error")
		MSE=resultados.mean()
		RMSE=numpy.sqrt(float(MSE))
		resultados=cross_val_score(model,xtrain,ytrain,cv=kf, scoring="r2")
		R2=resultados.mean()

		Model_MSE.delete(0,"end")
		Model_MSE.insert(0, str(MSE))

		Model_RMSE.delete(0,"end")
		Model_RMSE.insert(0, str(RMSE))
		
		Model_R2.delete(0,"end")
		Model_R2.insert(0, str(R2))

		pyplot.plot([xmin,xmax],[ymin,ymax],color="r")
		pyplot.show()

		canvas=FigureCanvasTkAgg(f, master=Panel)
		pw=canvas.get_tk_widget()
		pw.place(x=15, y=360)

	elif(seleccion.get()==3):
		model=Ridge(alpha=1)
		model.fit(xtrain,ytrain)
		if(model.intercept_>=0):
			rl="{model.coef_}x + {model.intercept_}"
		else:
			rl="{model.coef_}x {model.intercept_}"

		Ecuacion.delete(0,"end")
		Ecuacion.insert(0, str(rl))

		f=pyplot.figure(figsize=(4,2))
		pyplot.scatter(xtrain,ytrain)
		pyplot.grid()
		
		xmin=xreg.min()
		ymax=yreg.max()
		xmin=model.coef_*xmin+model.intercept_
		ymax=model.coef_*xmax+model.intercept_
		prediccion=model.predict(xtest)
		kf=KFold(n_splits=5,random_state=7, shuffle=True)
		resultados=cross_val_score(model,xtrain,ytrain,cv=kf, scoring="neg_mean_squared_error")
		MSE=resultados.mean()
		RMSE=numpy.sqrt(float(MSE))
		resultados=cross_val_score(model,xtrain,ytrain,cv=kf, scoring="r2")
		R2=resultados.mean()

		Model_MSE.delete(0,"end")
		Model_MSE.insert(0, str(MSE))

		Model_RMSE.delete(0,"end")
		Model_RMSE.insert(0, str(RMSE))
		
		Model_R2.delete(0,"end")
		Model_R2.insert(0, str(R2))

		pyplot.plot([xmin,xmax],[ymin,ymax],color="r")
		pyplot.show()

		canvas=FigureCanvasTkAgg(f, master=Panel)
		pw=canvas.get_tk_widget()
		pw.place(x=15, y=360)

GUI=Tk()
GUI.title("PRUEBA DE CARGA")
GUI.resizable(True,True)

seleccion=IntVar()
peticiones=StringVar()
sitio=StringVar()

Panel=Frame()
Panel.pack()
Panel.config(width="650", height="650")

T1=Label(Panel, text="NUMERO DE PETICIONES ").place(x=15, y=20)
T2=Label(Panel, text="URL DEL SERVICION WEB: ").place(x=15, y=60)
T3=Label(Panel, text="METODO DE ANALISIS ").place(x=15, y=100)
T4=Label(Panel, text="ECUACION: ").place(x=15, y=160)
T5=Label(Panel, text="MSE: ").place(x=15, y=200)
T6=Label(Panel, text="RMSE: ").place(x=15, y=240)
T7=Label(Panel, text="R2: ").place(x=15, y=280)

P=Entry(Panel, textvariable=peticiones).place(x=250, y=20)
URL=Entry(Panel, width=35,textvariable=sitio).place(x=200, y=60)
Ecuacion=Entry(Panel, width=45, state='disabled').place(x=200,y=160)
Model_MSE=Entry(Panel, width=45, state='disabled').place(x=200,y=200)
Model_RMSE=Entry(Panel, width=45, state='disabled').place(x=200,y=240)
Model_R2=Entry(Panel, width=45, state='disabled').place(x=200,y=280)

Radiobutton(Panel,text="R. L.", variable=seleccion, value=1).place(x=200,y=100)
Radiobutton(Panel,text="Ridge", variable=seleccion, value=2).place(x=260,y=100)
Radiobutton(Panel,text="Lasso", variable=seleccion, value=3).place(x=320,y=100)

Prueba=Button(Panel, text="EJECUTAR", command=probarCarga, width=16).place(x=350, y=20)
ttk.Separator(Panel,orient=HORIZONTAL).place(x=15,y=140,relwidth=1)
ttk.Separator(Panel,orient=HORIZONTAL).place(x=15,y=320,relwidth=1)

GUI.mainloop()
