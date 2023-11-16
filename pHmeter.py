"Acquisition du pH"

from Phidget22.Phidget import *
from Phidget22.Devices.VoltageInput import *
from Phidget22.Devices.PHSensor import *
#from controlPannel import ControlPannel
import math
import numpy as np
from configparser import ConfigParser
import os
from pathlib import Path
import re

path = Path(__file__)
ROOT_DIR = path.parent.absolute()
cal_data_path = os.path.join(ROOT_DIR, "config\cal_data.ini")

def volt2pH(a,b,U): #m: pente, c: ordonnée à l'origine
	#U=a*pH+b
	if a!=0:
		pH=(U-b)/a
	else:
		pH=1000
	return pH

class PHMeter:

	def __init__(self):
		self.state='closed'

	def connect(self):
		#pHmètre
		U_pH = VoltageInput() #pH-mètre
		U_pH.setDeviceSerialNumber(432846)
		U_pH.setChannel(0)
		try:
			U_pH.openWaitForAttachment(1000)
			if U_pH.getIsOpen():
				U_pH.setDataRate(3)
				U_pH.setVoltageChangeTrigger(0.00001) #seuill de déclenchement (Volt)
				self.getCalData()
				self.currentVoltage=U_pH.getVoltage()
				self.currentPH=volt2pH(self.a,self.b,self.currentVoltage)
				self.state='open'
				print("pH mètre connecté")
			else:
				self.state='closed'
				print("pH-mètre non connecté")
		except:
			self.state='closed'
			print("pH-mètre non connecté")
		self.voltagechannel=U_pH
	
	def getCalData(self):
		#print("passage dans get cal data")
		parser = ConfigParser()
		parser.read(cal_data_path)
		self.CALdate=parser.get('data', 'date')
		self.CALtemperature=float(parser.get('data', 'temperature'))
		self.CALtype=parser.get('data', 'calib_type')
		self.U1=float(parser.get('data', 'U1'))
		self.U2=float(parser.get('data', 'U2'))
		self.U3=float(parser.get('data', 'U3'))
		self.a = float(parser.get('data', 'a'))
		self.b = float(parser.get('data', 'b'))

	def doOnVoltageChange(self,ch,voltage): 
		#les arguments de cette fonctions ne peuvent pas être changés
		#self:PHMeter,ch:VoltageInput,voltage:float 
		self.currentVoltage=voltage #self.voltagechannel.getVoltage()
		#print("current voltage=",self.currentVoltage)
		self.current_PH=volt2pH(self.a,self.b,self.currentVoltage)  
		#return(self.currentVoltage,self.current_PH)
	
	def activatePHmeter(self):
		#si le voltagechangetrigger est à zéro, l'évènement se produit périodiquement
		self.voltagechannel.setOnVoltageChangeHandler(self.doOnVoltageChange)
	
	def onCalibrationChange(self):
		parser = ConfigParser()
		parser.read(cal_data_path)
		self.CALdate=parser.get('data', 'date')
		self.CALtemperature=float(parser.get('data', 'temperature'))
		#c'est un string : à convertir en set puis à ordonner
		l=re.findall('\d+',parser.get('data', 'calib_type'))
		ll=[int(x) for x in l]
		self.CALtype=sorted(ll) 
		#print(l,ll)
		#print("pHmeter.onCalibrationCHange",self.CALtype)
		self.U1=float(parser.get('data', 'U1'))
		self.U2=float(parser.get('data', 'U2'))
		self.U3=float(parser.get('data', 'U3'))
		self.a = float(parser.get('data', 'a'))
		self.b = float(parser.get('data', 'b'))
		print(self.CALdate, "calibration change on ph meter")
	
	def saveCalData(self,date,temperature,caltype,u_cal,coeffs):
		parser = ConfigParser()
		parser.read(cal_data_path)
		
		parser.set('data', 'date', str(date)) 
		parser.set('data', 'temperature', str(temperature))
		#print("caltype ",caltype)
		#print("str(caltype) ",str(caltype))
		parser.set('data', 'calib_type', str(caltype))
		#print(u_cal)
		try:
			parser.set('data', 'U1', str(float(u_cal[0])))
			parser.set('data', 'U2', str(float(u_cal[1])))
			parser.set('data', 'U3', str(float(u_cal[2])))
		except:
			pass
		#print(coeffs)
		parser.set('data', 'a', str(float(coeffs[0])))
		parser.set('data', 'b', str(float(coeffs[1])))
		
		file = open(cal_data_path,'w')	#qu'est-ce qu'apporte r+ ou lieu de w
		parser.write(file) 
		file.close()

		#sauvegarde de toutes les calibration
		oldCal = open("config/CALlog.txt", "a")
		oldCal.write(str(date)+"\n"+str(temperature)+"°C \nType de calibration: "+str(caltype)+"\nVoltages calib:\n"+str(u_cal)+"\nCoefficients U=a*pH+b\n(a,b)="+str(coeffs)+"\n\n")
		oldCal.close()

	def computeCalCoefs(self,u_cal,pH_buffers):
		if pH_buffers == [4]:
			b=u_cal[0]-4*self.a	#dernière calibration
		if pH_buffers == [4,7]:
			pH = np.array([4,7])
			u = np.array([u_cal[0:2]]).T #seulement pH4 et 7
			#print("pH : ",pH," tensions de calib: ", u)
			a=(u_cal[1]-u_cal[0])/3;b=u_cal[0]-4*a
		if pH_buffers == [4,7,10]:
			pH = np.array([4,7,10])
			u = np.array([u_cal[0:3]]).T #pH 4, 7 et 10
			#print("pH : ",pH," tensions de calib: ", u)
			A = np.vstack([pH.T, np.ones(len(pH)).T]).T
			x = np.linalg.lstsq(A, u, rcond=None)[0]		#a: pente, b: ord à l'origine
			a=float(x[0].item());b=float(x[1].item())	#U=a*pH+b
		self.a=a
		self.b=b
		return a, b
		
	def close(self):
		self.voltagechannel.close()
		self.state='closed'

if __name__ == "__main__":
    #création d'un canal pour la tension d'entrée
	ch = VoltageInput()
	ch.setDeviceSerialNumber(432846)
	ch.setChannel(0)
	ch.openWaitForAttachment(1000)
	ch.setOnVoltageChangeHandler(PHMeter.DoOnVoltageChange)
	
	phm = PHMeter(ch)
	phm.configure_pHmeter()

	#ch.setOnVoltageChangeHandler(PHMeter.DoOnVoltageChange)
	
	#ch.setDataRate(1)
	#ch.setVoltageChangeTrigger(0.0001) #précision de 10mV

	# pH_set = (4,7)
	# CALcoefs=phm.Two_point_calibration(pH_set)

	# ch.setSensorType(VoltageSensorType.SENSOR_TYPE_1130_PH)
	# sensorValue = ch.getSensorValue() #pour comparer aux valeurs calculées avec calibration
	# print("SensorValue: pH = " + str(sensorValue))

	ch.close()
