################ PROTECCION DE ARCHIVOS ################
import sys, os, subprocess, time, pyfiglet
from colorama import init, Fore, Style
import ctypes
init(autoreset=True)
rutpass='C:\\Windows\\passx00.txt'
e='               '
banner=pyfiglet.figlet_format(f"{e}SECFILES")
carpeta_protegida='PROTEGER'
user=os.getlogin()
if len(sys.argv) > 2 and sys.argv[1] == "-c":
 nueva_clave = sys.argv[2]
 with open(rutpass, 'w') as f:
  f.write(nueva_clave)
 print(f"\n\t{Fore.GREEN}{Style.BRIGHT}NUEVA CLAVE GUARDADA EXITOSAMENTE")
 time.sleep(2)
 sys.exit()

if not os.path.exists(carpeta_protegida):
 os.makedirs(carpeta_protegida)

x=f'{Fore.GREEN}{Style.BRIGHT}============================================================{Style.RESET_ALL}'
print(f"\n{banner}\n\t{x}\n\tPOR FAVOR MUEVA LOS ARCHIVOS QUE DESEA\n\tAPLICAR SEGURIDAD A LA CARPETA {Fore.GREEN}{Style.BRIGHT}{carpeta_protegida}\n\t{x}")
atributos = ctypes.windll.kernel32.GetFileAttributesW(carpeta_protegida)
if atributos == 22:
 if os.path.exists(rutpass):
  clv=input("\n\tIntroduzca su clave para desbloquear carpeta -> ")
  with open(rutpass, "r") as f:
   ver=f.read()
   if ver == clv:
    cmdd=f'icacls {carpeta_protegida} /grant "{user}:(R)"'
    subprocess.run(cmdd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    command=f'attrib -h -s {carpeta_protegida}'
    subprocess.run(command, shell=True)
    os.chdir(carpeta_protegida)
    cmd2='cipher /d'
    subprocess.run(cmd2, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print(F"\n\t{Fore.GREEN}{Style.BRIGHT}CARPETA DESBLOQUEADA CON EXITO")
   else:
    print(f"\n\t{Fore.RED}{Style.BRIGHT}CLAVE INVALIDA, INTENTALO NUEVAMENTE...")
   time.sleep(3)
   sys.exit()

def seguridad():
 print(F"\n\t{Fore.GREEN}{Style.BRIGHT}SEGURIDAD APLICADA EXITOSAMENTE")
 command=f'attrib +h +s {carpeta_protegida}'
 subprocess.run(command, shell=True)
 os.chdir(carpeta_protegida)
 cmd2=f'cipher /e'
 subprocess.run(cmd2, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
 os.chdir('..')
 cmd3=f'icacls {carpeta_protegida} /deny "{user}:(R)"'
 subprocess.run(cmd3, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
mostrar=os.listdir(carpeta_protegida)
cantidad=len(mostrar)
if int(cantidad) == 0 :
 pass
else:
 if not os.path.exists(rutpass):
  clave=input('\n\tIntroduzca la clave para proteger la carpeta ---> ')
  with open(rutpass, 'w') as f:
   f.write(clave)
   f.close()
   seguridad()
 else:
  seguridad()
input()


