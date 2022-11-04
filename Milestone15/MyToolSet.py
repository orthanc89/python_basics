
# bitte die E-Book PDF- Seiten (pdf-seite) 198-225 bearbeiten
# verwende paramiko und urllib um ein tool zu schreiben, das folgende aufgaben erfüllt
# erstelle für die cli und für die Gui folgende Views:
# ssh command-eingabe
# ssh rückgabe in dictionary-liste speichern (für spätere Analysen)
# ssh rückgaben auflisten
# url aufruf und check der rückgabe ob der Server eine HTML-Seite zurückliefert
# url status der aufrufe in eine Liste speichern
# url statis in dicht/liste anzeigen lassen
# Auswahl ob dies über cli oder gui passieren soll.
# advanced:
# frage per ssh z.B. die Bash_history aus und suche nach schlüsselworten in den ausgabezeilen

# benötigte funktonen:
import urllib
import sys
import getpass


# frame und co initialisieren Alex
##initGui Alex
def initgui():
    global root
    root = tk.Tk()
    global frame
    frame = tk.Frame(root)


# variablen, dics{}, lits() Ben
##initAll()
global saveSCRSdic
saveSCRSdic = {}

global savePara
savePara = {}

global saveSCRSitems
saveSCRSitems = {'Status', 'Command', 'Rückgabe', 'Status'}

global serverlist
serverlist = []


# basis menü (cli oder gui) Ben
##userchooseGuiCli
y = True
def userchooseGuiCli():
    print('\n')

    while y:
        userchoose = int(input('Bitte wähle aus: \n [1] CLI \n [2] Gui \n [3] Exit '))
        if userchoose == 1:
            cliHauptprogramm()

        elif userchoose == 2:
            guiHauptprogramm()

        elif userchoose == 3:
            x = False
            sys.exit()

        else:
            x = False
            print(' Bitte wähle was aus!')

# paramiko als ssh_command starten
# eingabemaske für paramiko (einzelabfrage auf einen server)
##CliInputForm()
##GuiInputForm()

def ssh_command(serveritem):

    import paramiko
    x = False
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try: #probiere, wenn nicht funktionuckelt, mache except
        client.connect(serveritem['ip'], port=serveritem['port'], username=serveritem['user'], password=serveritem['password'])
        _, stdout, stderr = client.exec_command(serveritem['cmd'])
        output = stdout.readlines() + stderr.readlines()
        if output:
            print('--- Output ---')
            for line in output:
                print(line.strip())
        return output

    except Exception as fehler:   #fehlermeldung erwarten
        print('Wir haben einen Connection error' + fehler)





def CliInputForm():

    # user = getpass.getuser ()
    serveritem = {'ip': '', 'port': '', 'user': '', 'password': '', 'cmd': ''}

    serveritem['user'] = input('Username: ')
    serveritem['password'] = input('Password:')

    serveritem['ip'] = input('Enter server IP: ') or '192.168.1.203"'
    serveritem['port'] = input('Enter port or <CR>: ') or 2222
    serveritem['cmd'] = input('Enter command or <CR>: ') or 'id'
    # ssh_command(ip, port, user, password, cmd)
    return serveritem



def urllibprog():
    from urllib import request

    putput = input("Geb hier bitte ine webside zum scannen ein: ")
    rueckgabewert = request.urlopen(putput)
    print(type(rueckgabewert))

    rueckgabewert = request.urlopen(putput)
    print(rueckgabewert.code)
    print("Dateigröße in Bytes: ", rueckgabewert.length)
    print("Anfang des Inhalts:", rueckgabewert.peek())
    inhalt = rueckgabewert.read()
    print(type(inhalt))
    # hier ggf. harte fehlerbehandlung einbauen für den fall das eine webside einen codeerror aufruft
    # decodex = re.findall("charset=")

    inhalt_text = inhalt.decode("UTF-8")
    print(type(inhalt_text))
    inhalt_text = inhalt.decode("UTF-8")
    print(inhalt_text)


# eingabemask für das erstellen einer serverliste
##CliServeroutForm()
##GuiServerInputForm()
def CliServeroutForm(serveritem):
    x = False

    with open('serverliste.txt', 'w') as temp_file:
        for item in serveritem:
            temp_file.write("%s\n" % item)
    file = open('serverliste.txt', 'r')
    print(file.read())




# cli hauptprogramm
##cliHauptprogramm()
def cliHauptprogramm():
    x = False
    global serverlist
    userchoose = 0
    userchoose = int(input('Bitte wähle aus: \n [1] Paramiko \n [2] UrlLibs \n [3] Exit '))

    if userchoose == 1:

        print('Paramiko wird gestartet! \n')
        serveritem = CliInputForm()
        cmdout = ssh_command(serveritem)
        serverlist.append(serveritem)


        userchoose2 = input('Möchtest du dir die Serverliste ausgeben lassen ? [y/n]')
        if userchoose2 == 'y':
            listserver(serverlist)


    if userchoose == 2:

        print('URLLibs wird gestartet! \n')
        urllibprog()

    elif userchoose == 3:
        x = False
        sys.exit()

    else:
        x = False
        print(' Bitte wähle was aus!')

def listserver(serverlist):

    counter = 0
    for serveritem in serverlist:
        print (counter.__str__() +" "+ serveritem["ip"] + " " +  serveritem['user'] + " " + serveritem['password'] + " " + serveritem["port"] + " " + serveritem['cmd'])
        counter += 1
# gui Hauptprogramm
## guiHauptprogramm


# hauptmenü für die auswahl von urllib oder paramiko
##chooseUserUrlPara()

# eingabemasken sowohl im cli und gui (einzelabfrage auf einen server)


# check auf den status der abfrage
##Check unabhängig von GUI/CLI
###CheckSshDict()
###savePara{}

# check ist das commando ausgeführt worden (ja/nein/errormsg)
##Check unabhängig von GUI/CLI
###CheckCmdDict()

# speicherfunktion in eine liste (server, commando, rückgabe, status) in ein dict {} speichern
##SaveSCRS()
###saveSCRSitems = {'Status', 'Command', 'Rückgabe', 'Status'}

# funktion zum anzeigen der liste(n)
##showlists()

# eingabemaske für urllibs (einzelabfrage auf einen server)
##aksUrl()

# eingabemask für das erstellen einer serverliste
##makeUrlList()

# check auf den status der abfrage
##checkStatus()

# def showWebsite():
# print("Anfang des Inhalts:", rueckgabewert.peek())
# urls =[]
# urls.append('http://www.google.com/')
# urls.append('http://www.example.com/')
# urls.append('http://www.heise.com/')
# urls.append('http://www.golem.de/')
# urls.append('http://www.heise.de/')
# for url in urls:
     #   rueckgabewert = request.urlopen(url)
      #  if rueckgabewert.code == 200:
       #     print("webseite konnte geladen werden")
        #    print(url)
        #    showWebsite()
# elif rueckgabewert.code == 400:
         #   print("fehlerhafte URL",url)
# elif rueckgabewert.code ==403:
        #    print("Zugriff nicht erlaubt",url)
# elif rueckgabewert == 404:
        #    print("URL konnte nicht gefunden werden",url)
# else:
         #   print("Unbekannter Fehler",url)

# check ist das commando ausgeführt worden (ja/nein/errormsg)
##checkCmd()

# speicherfunktion in eine liste
##saveList()

# speicherfunktion in eine liste (url, rückgabe(webside), status) = in ein dict {}
##saveListUrl()

# funktion zum anzeigen der liste(n)
##showList()

# Hauptmenu
##hauptmenu()

userchooseGuiCli()




