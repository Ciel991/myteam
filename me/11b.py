# -*- coding: utf-8 -*-

import ardan
from ardan.lib.curve.ttypes import *
from datetime import datetime
import time,random,sys,json,codecs,threading,glob,requests,urllib

cl = ardan.LINE()
cl.login(token="")
cl.loginResult()

#ki = ardan.LINE()
#ki.login(token="authToken Kamu")
#ki.loginResult()

#ki2 = ardan.LINE()
#ki2.login(token="authToken Kamu")
#ki2.loginResult()

#ki3 = ardan.LINE()
#ki3.login(token="authToken Kamu")
#ki3.loginResult()

#ki4 = ardan.LINE()
#ki4.login(token="authToken Kamu")
#ki4.loginResult()

#ki5 = ardan.LINE()
#ki5.login(token="authToken Kamu")
#ki5.loginResult()

#ki6 = ardan.LINE()
#ki6.login(token="authToken Kamu")
#ki6.loginResult()

#ki7 = ardan.LINE()
#ki7.login(token="authToken Kamu")
#ki7.loginResult()

#ki8 = ardan.LINE()
#ki8.login(token="authToken Kamu")
#ki8.loginResult()

#ki9 = ardan.LINE()
#ki9.login(token="authToken Kamu")
#ki9.loginResult()

#k1 = ardan.LINE()
#k1.login(token="authToken Kamu")
#k1.loginResult()

#k2 = ardan.LINE()
#k2.login(token="authToken Kamu")
#k2.loginResult()

print u"Created by : Ciel"
reload(sys)
sys.setdefaultencoding('utf-8')

helpMessage ="""||=====  F O R   U S E R  =====||
�✒ Mention       - Mention All Member Group
�✒ Lurk          - Set Point Read
�✒ Lurking       - Reading Point
�✒ Ginfo         - Info Grup
||===== F O R   A D M I N =====||
�✒ Glist         - List Group BOT
�✒ Cancel        - Cancel All Pending Grup
�✒ Mid @         - Get MID 
�✒ Invite        - Invite Via Send Contact
�✒ Invite:       - Via MID
�✒ Whitelist @   - Via Tag
�✒ Whitelist:    - Via Mid
�✒ Whitelist     - Via Send Contact
�✒ Blacklist @   - Via Tag
�✒ Blacklist:    - Via Mid
�✒ Blacklist     - Via Send Contact
�✒ Clear ban     - Delete All Blacklist
�✒ Link on       - Open QR
�✒ Link off      - Close QR
�✒ Gurl          - Open QR And Get Link
�✒ Url           - Get QR Link
�✒ Gname         - Change Name Group
�✒ Banlist       - Cek Tersangka Kriminal
�✒ Details grup  - Via Gid
�✒ Inviteme:     - Via Gid
�✒ Info grup
�✒ Clear grup
||===== F O R  K I C K E R =====||
||��✒ Nuke
||��✒ Ratakan
||��✒ Kick @        - Via Tag
||��✒ Kick:         - Via MID
||===== F O R  P L A Y E R =====||
||��✒ Bc:ct 
||��✒ Bc:grup
||��✒ Block @
||��✒ Blocklist
||��✒ Spam on/off
||��✒ Uni
||��✒ Bot:ct        - Broadcast to All Contact BOT
||��✒ Bot:grup      - Broadcast to All Grup Joined BOT
||��✒ Allname:      - Change All Name BOT
||��✒ Allbio:       - Change All Bio BOT
||��✒ Bot sp        - Tes Speed BOT
||��✒ Speed         - Tes Speed
||��✒ Mycopy @      - Copy Profile 
||��✒ Mybackup @    - Backup Profile
||========================||


||===== S E T T I G S =====||          
|| [Like:on/off]     
|| [Add on/off] 	 
|| [Auto join on/off] 	   
|| [Contact on/off] 	
|| [Leave on/off]  
|| [Share on/off]           
|| [Add on/off] 		   
|| [Jam on/off]			   
|| [Jam say:]			   
|| [Com on/off]	
|| [Message set:]	
|| [Comment set:]	
|| [Pesan add:]	
||===== P R O T E C T =====||        
|| [Panick:on/off]      
|| [Protect on]			   
|| [Qrprotect on/off]			   
|| [Inviteprotect on/off]			   
|| [Cancelprotect on/off]		   
|| [Staff add/remove @]	   
||======= FOR ADMIN =======||
 ✯====  https://line.me/ti/p/%40luw8183j====✯
               ✯==== Creator ====✯
	
                  ATTENTION!!!!
  Creator nya sok tau bahasa inggris :V
"""
helo=""

KAC=[cl]
#KAC=[cl]CA=[cl,ki,ki2,ki3,ki4,ki5,ki6,ki7,ki8,ki9,k1]
#DEFF = [cl,ki,ki2,ki3,ki4,ki5,ki6,ki7,ki8,ki9,k1]
mid = cl.getProfile().mid
Bots = [mid,"u1f41296217e740650e0448b96851a3e2"]
admsa = "ub76a0153a283da9a1443dfb043181335"
admin = "ub76a0153a283da9a1443dfb043181335"

wait = {
    'contact':False,
    'autoJoin':True,
    'autoCancel':{"on":False,"members":50},
    'leaveRoom':True,
    'timeline':False,
    'autoAdd':frue,
    'message':"ADD MY CREATOR https://line.me/ti/p/%40luw8183j",
    "lang":"JP",
    "comment":"Auto Like By Ciel",
    "commentOn":False,
    "likeOn":False,
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "clock":False,
    "cNames":"",
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "protect":False,
    "cancelprotect":False,
    "inviteprotect":False,
    "linkprotect":False,
}

wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    "ricoinvite":{},
    'ROM':{},
    }
    
setTime = {}
setTime = wait2['setTime']
blacklistFile='blacklist.txt'
pendinglistFile='pendinglist.txt'

contact = cl.getProfile()
mybackup = cl.getProfile()
mybackup.displayName = contact.displayName
mybackup.statusMessage = contact.statusMessage
mybackup.pictureStatus = contact.pictureStatus

#contact = ki.getProfile()
#backup = ki.getProfile()
#backup.displayName = contact.displayName
#backup.statusMessage = contact.statusMessage
#backup.pictureStatus = contact.pictureStatus

#contact = ki2.getProfile()
#backup = ki2.getProfile()
#backup.displayName = contact.displayName
#backup.statusMessage = contact.statusMessage
#backup.pictureStatus = contact.pictureStatus

#contact = ki3.getProfile()
#backup = ki3.getProfile()
#backup.displayName = contact.displayName
#backup.statusMessage = contact.statusMessage
#backup.pictureStatus = contact.pictureStatus

#contact = ki4.getProfile()
#backup = ki4.getProfile()
#backup.displayName = contact.displayName
#backup.statusMessage = contact.statusMessage
#backup.pictureStatus = contact.pictureStatus

#contact = ki5.getProfile()
#backup = ki5.getProfile()
#backup.displayName = contact.displayName
#backup.statusMessage = contact.statusMessage
#backup.pictureStatus = contact.pictureStatus

#contact = ki6.getProfile()
#backup = ki6.getProfile()
#backup.displayName = contact.displayName
#backup.statusMessage = contact.statusMessage
#backup.pictureStatus = contact.pictureStatus

#contact = ki7.getProfile()
#backup = ki7.getProfile()
#backup.displayName = contact.displayName
#backup.statusMessage = contact.statusMessage
#backup.pictureStatus = contact.pictureStatus

#contact = ki8.getProfile()
#backup = ki8.getProfile()
#backup.displayName = contact.displayName
#backup.statusMessage = contact.statusMessage
#backup.pictureStatus = contact.pictureStatus

#contact = ki9.getProfile()
#backup = ki9.getProfile()
#backup.displayName = contact.displayName
#backup.statusMessage = contact.statusMessage
#backup.pictureStatus = contact.pictureStatus

#contact = k1.getProfile()
#backup = k1.getProfile()
#backup.displayName = contact.displayName
#backup.statusMessage = contact.statusMessage
#backup.pictureStatus = contact.pictureStatus

def cms(string, commands): #/XXX, >XXX, ;XXX, ^XXX, %XXX, $XXX...
    tex = ["+","@","/",">",";","^","%","$","＾","サテラ:","サテラ:","サテラ：","サテラ："]
    for texX in tex:
        for command in commands:
            if string ==command:
                return True
    return False
    
def bot(op):
    try:
        if op.type == 0:
            return
        if op.type == 13:
            if mid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            cl.rejectGroupInvitation(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        cl.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param1, matched_list)
        if op.type == 19:
            if mid in op.param3:
                wait["blacklist"][op.param2] = True
        if op.type == 22:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 24:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 26:
            msg = op.message
            if msg.toType == 0:
                msg.to = msg.from_
                if msg.from_ == "u83c0edf4fcac8f4baf169d3d69edff71":
                    if "join:" in msg.text:
                        list_ = msg.text.split(":")
                        try:
                            cl.acceptGroupInvitationByTicket(list_[1],list_[2])
                            G = cl.getGroup(list_[1])
                            G.preventJoinByTicket = True
                            cl.updateGroup(G)
                        except:
                            cl.sendText(msg.to,"error")
            if msg.toType == 1:
                if wait["leaveRoom"] == True:
                    cl.leaveRoom(msg.to)
            if msg.contentType == 16:
                url = msg.contentMetadata["postEndUrl"]
                cl.like(url[25:58], url[66:], likeType=1001)
        if op.type == 26:
            msg = op.message
            if msg.contentType == 13:
            	if wait["ricoinvite"] == True:
                     if msg.from_ in admin:
                         _name = msg.contentMetadata["displayName"]
                         invite = msg.contentMetadata["mid"]
                         groups = cl.getGroup(msg.to)
                         pending = groups.invitee
                         targets = []
                         for s in groups.members:
                             if _name in s.displayName:
                                 ki.sendText(msg.to,"-> " + _name + " was here")
                                 break
                             elif invite in wait["blacklist"]:
                                 cl.sendText(msg.to,"Sorry, " + _name + " On Blacklist")
                                 cl.sendText(msg.to,"Call ciel to use command !, \n➡Unban: " + invite)
                                 break                             
                             else:
                                 targets.append(invite)
                         if targets == []:
                             pass
                         else:
                             for target in targets:
                                 try:
                                     ki.findAndAddContactsByMid(target)
                                     ki.inviteIntoGroup(msg.to,[target])
                                     random.choice(KAC).sendText(msg.to,"Invited this nigga💋: \n➡" + _name)
                                     wait2["ricoinvite"] = False
                                     break                              
                                 except:             
                                          cl.sendText(msg.to,"Negative, Err0r Detected")
                                          wait2["ricoinvite"] = False
                                          break
            if msg.contentType == 13:
                if wait["wblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        cl.sendText(msg.to,"sudah masuk daftar hitam👈")
                        wait["wblack"] = False
                    else:
                        wait["commentBlack"][msg.contentMetadata["mid"]] = True
                        wait["wblack"] = False
                        cl.sendText(msg.to,"Itu tidak berkomentar👈")
                elif wait["dblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        del wait["commentBlack"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"Done")
                        wait["dblack"] = False
                    else:
                        wait["dblack"] = False
                        cl.sendText(msg.to,"Tidak ada dalam daftar hitam👈")
                elif wait["wblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        cl.sendText(msg.to,"sudah masuk daftar hitam")
                        wait["wblacklist"] = False
                    else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = False
                        cl.sendText(msg.to,"Done👈")
                elif wait["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"Done👈")
                        wait["dblacklist"] = False
                    else:
                        wait["dblacklist"] = False
                        cl.sendText(msg.to,"Done👈")
                elif wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendText(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
                    else:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + contact.displayName + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
            elif msg.contentType == 16:
                if wait["timeline"] == False:
                    msg.contentType = 0
                    if wait["lang"] == "JP":
                        msg.text = "menempatkan URL\n" + msg.contentMetadata["postEndUrl"]
                    else:
                        msg.text = "URLâ†’\n" + msg.contentMetadata["postEndUrl"]
                    cl.sendText(msg.to,msg.text)
            elif msg.text is None:
                return
            elif msg.text.lower()  == 'help':
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,helpMessage)
                else:
                    cl.sendText(msg.to,helpMessage)
            elif "Mybot" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': kimid}
                ki.sendMessage(msg) 
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki2mid}
                ki2.sendMessage(msg) 
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki3mid}
                ki3.sendMessage(msg) 
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki4mid}
                ki4.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki5mid}
                ki5.sendMessage(msg) 
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki6mid}
                ki6.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki7mid}
                ki7.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki8mid}
                ki8.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki9mid}
                ki9.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': k1mid}
                k1.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': k2mid}
                k2.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': k3mid}
                k3.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': k4mid}
                k4.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': k5mid}
                k5.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': k6mid}
                k6.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': k7mid}
                k7.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': k8mid}
                k8.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': k9mid}
                k9.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': w1mid}
                w1.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': w2mid}
                w2.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': w3mid}
                w3.sendMessage(msg) 
                msg.contentType = 13
                msg.contentMetadata = {'mid': w4mid}
                w4.sendMessage(msg) 
                msg.contentType = 13
                msg.contentMetadata = {'mid': w5mid}
                w5.sendMessage(msg) 
                msg.contentType = 13
                msg.contentMetadata = {'mid': w6mid}
                w6.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': w7mid}
                w7.sendMessage(msg) 
                msg.contentType = 13
                msg.contentMetadata = {'mid': w8mid}
                w8.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': w9mid}
                w9.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': l1mid}
                l1.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': l2mid}
                l2.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': l3mid}
                l3.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': l4mid}
                l4.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': l5mid}
                l5.sendMessage(msg)
            elif "Pro1" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': kimid}
                ki.sendMessage(msg)
            elif "Pro2" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki2mid}
                ki2.sendMessage(msg)
            elif "Pro3" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki3mid}
                ki3.sendMessage(msg)
            elif "Pro4" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki4mid}
                ki4.sendMessage(msg)
            elif "Pro5" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki5mid}
                ki5.sendMessage(msg)
            elif "Pro6" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki6mid}
                ki6.sendMessage(msg)
            elif "Pro7" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki7mid}
                ki7.sendMessage(msg)
            elif "Pro8" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki8mid}
                ki8.sendMessage(msg)
            elif "Pro9" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki9mid}
                ki9.sendMessage(msg)
            elif "Pro10" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': k1mid}
                k1.sendMessage(msg)
            elif "Pro11" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': k2mid}
                k2.sendMessage(msg)
            elif "Pro12" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': k3mid}
                k3.sendMessage(msg)
            elif "Pro13" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': k4mid}
                k4.sendMessage(msg)
            elif "Pro14" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': k5mid}
                k5.sendMessage(msg)
            elif "Pro15" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': k6mid}
                k6.sendMessage(msg)
            elif "Pro16" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': k7mid}
                k7.sendMessage(msg)
            elif "Pro17" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': k8mid}
                k8.sendMessage(msg)
            elif "Pro18" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': k9mid}
                k9.sendMessage(msg)
            elif "Pro19" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': w1mid}
                w1.sendMessage(msg)
            elif "Pro20" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': w2mid}
                w2.sendMessage(msg)
            elif "Pro21" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': w3mid}
                w3.sendMessage(msg) 
            elif "Pro22" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': w4mid}
                w4.sendMessage(msg) 
            elif "Pro23" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': w5mid}
                w5.sendMessage(msg) 
            elif "Pro24" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': w6mid}
                w6.sendMessage(msg)
            elif "Pro25" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': w7mid}
                w7.sendMessage(msg) 
            elif "Pro26" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': w8mid}
                w8.sendMessage(msg)
            elif "Pro27" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': w9mid}
                w9.sendMessage(msg)
            elif "Pro28" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': l1mid}
                l1.sendMessage(msg)
            elif "Pro29" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': l2mid}
                l2.sendMessage(msg)
            elif "Pro30" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': l3mid}
                l3.sendMessage(msg)
            elif "Pro31" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': l4mid}
                l4.sendMessage(msg)
            elif "Pro32" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': l5mid}
                l5.sendMessage(msg)
            elif msg.text in ["Bot1 Gift","Bot1 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '2'}
                msg.text = None
                ki.sendMessage(msg)
            elif msg.text in ["Gift","gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '3'}
                msg.text = None
                cl.sendMessage(msg)

            elif msg.text in ["Bot2 Gift","Bot2 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '3'}
                msg.text = None
                ki2.sendMessage(msg)

            elif msg.text in ["Bot3 Gift","Bot3 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '4'}
                msg.text = None
                ki3.sendMessage(msg)
            elif msg.text in ["Bot4 Gift","Bot4 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '5'}
                msg.text = None
                ki4.sendMessage(msg)

            elif msg.text in ["Cancel","cancel"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    if group.invitee is not None:
                        gInviMids = [contact.mid for contact in group.invitee]
                        cl.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"No invites👈")
                        else:
                            cl.sendText(msg.to,"Invite people inside not👈")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Tidak ada undangan👈")
                    else:
                        cl.sendText(msg.to,"invitan tidak ada")
            elif "Contact" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': msg.to}
                cl.sendMessage(msg)
            elif "Pro1 mid" == msg.text:
                ki.sendText(msg.to,kimid)
            elif "Pro2 mid" == msg.text:
                ki2.sendText(msg.to,ki2mid)
            elif "Pro3 mid" == msg.text:
                ki3.sendText(msg.to,ki3mid)
            elif "Pro4 mid" == msg.text:
                ki4.sendText(msg.to,ki4mid)
            elif "Pro5 mid" == msg.text:
                ki5.sendText(msg.to,ki5mid)
            elif "Pro6 mid" == msg.text:
                ki6.sendText(msg.to,ki6mid)
            elif "Pro7 mid" == msg.text:
                ki7.sendText(msg.to,ki7mid)
            elif "Pro8 mid" == msg.text:
                ki8.sendText(msg.to,ki8mid)
            elif "Pro9 mid" == msg.text:
                ki9.sendText(msg.to,ki9mid)
            elif "Pro10 mid" == msg.text:
                k1.sendText(msg.to,k1mid)
            elif "Pro11 mid" == msg.text:
                k2.sendText(msg.to,k2mid)
            elif "Pro12 mid" == msg.text:
                k3.sendText(msg.to,k3mid)
            elif "Pro13 mid" == msg.text:
                k4.sendText(msg.to,k4mid)
            elif "Pro14 mid" == msg.text:
                k5.sendText(msg.to,k5mid)
            elif "Pro15 mid" == msg.text:
                k6.sendText(msg.to,k6mid)
            elif "Pro16 mid" == msg.text:
                k7.sendText(msg.to,k7mid)
            elif "Pro17 mid" == msg.text:
                k8.sendText(msg.to,k8mid)
            elif "Pro18 mid" == msg.text:
                k9.sendText(msg.to,k9mid)
            elif "Pro19 mid" == msg.text:
                w1.sendText(msg.to,w1mid)
            elif "Pro20 mid" == msg.text:
                w2.sendText(msg.to,w2mid)
            elif "Pro21 mid" == msg.text:
                w3.sendText(msg.to,w3mid)
            elif "Pro22 mid" == msg.text:
                w4.sendText(msg.to,w4mid)
            elif "Pro23 mid" == msg.text:
                w5.sendText(msg.to,w5mid)
            elif "Pro24 mid" == msg.text:
                w6.sendText(msg.to,w6mid)
            elif "Pro25 mid" == msg.text:
                w7.sendText(msg.to,w7mid)
            elif "Pro26 mid" == msg.text:
                w8.sendText(msg.to,w8mid)
            elif "Pro27 mid" == msg.text:
                w9.sendText(msg.to,w9mid)
            elif "Pro28 mid" == msg.text:
                l1.sendText(msg.to,l1mid)
            elif "Pro29 mid" == msg.text:
                l2.sendText(msg.to,l2mid)
            elif "Pro30 mid" == msg.text:
                l3.sendText(msg.to,l3mid)
            elif "Pro31 mid" == msg.text:
                l4.sendText(msg.to,l4mid)
            elif "Pro32 mid" == msg.text:
                l5.sendText(msg.to,l5mid)
            elif "All mid" == msg.text:
                ki.sendText(msg.to,kimid)
                ki2.sendText(msg.to,ki2mid)
                ki3.sendText(msg.to,ki3mid)
                ki4.sendText(msg.to,ki4mid)
                ki5.sendText(msg.to,ki5mid)
                ki6.sendText(msg.to,ki6mid)
                ki7.sendText(msg.to,ki7mid)
                ki8.sendText(msg.to,ki8mid)
                ki9.sendText(msg.to,ki9mid)
                k1.sendText(msg.to,k1mid)
                k2.sendText(msg.to,k2mid)
                k3.sendText(msg.to,k3mid)
                k4.sendText(msg.to,k4mid)
                k5.sendText(msg.to,k5mid)
                k6.sendText(msg.to,k6mid)
                k7.sendText(msg.to,k7mid)
                k8.sendText(msg.to,k8mid)
                k9.sendText(msg.to,k9mid)
                w1.sendText(msg.to,w1mid)
                w2.sendText(msg.to,w2mid)
                w3.sendText(msg.to,w3mid)
                w4.sendText(msg.to,w4mid)
                w5.sendText(msg.to,w5mid)
                w6.sendText(msg.to,w6mid)
                w7.sendText(msg.to,w7mid)
                w8.sendText(msg.to,w8mid)
                w9.sendText(msg.to,w9mid)
                l1.sendText(msg.to,l1mid)
                l2.sendText(msg.to,l2mid)
                l3.sendText(msg.to,l3mid)
                l4.sendText(msg.to,l4mid)
                l5.sendText(msg.to,l5mid)
            elif "Timeline: " in msg.text:
                tl_text = msg.text.replace("Timeline: ","")
                cl.sendText(msg.to,"line://home/post?userMid="+mid+"&postId="+cl.new_post(tl_text)["result"]["post"]["postInfo"]["postId"])
            elif "Allname: " in msg.text:
                string = msg.text.replace("Allname: ","")
                if len(string.decode('utf-8')) <= 1000000000000:
                    profile = ki.getProfile()
                    profile.displayName = string
                    ki.updateProfile(profile)
                if len(string.decode('utf-8')) <= 1000000000000:
                    profile = ki2.getProfile()
                    profile.displayName = string
                    ki2.updateProfile(profile)
                if len(string.decode('utf-8')) <= 1000000000000:
                    profile = ki3.getProfile()
                    profile.displayName = string
                    ki3.updateProfile(profile)
                if len(string.decode('utf-8')) <= 1000000000000:
                    profile = ki4.getProfile()
                    profile.displayName = string
                    ki4.updateProfile(profile)
                if len(string.decode('utf-8')) <= 1000000000000:
                    profile = ki5.getProfile()
                    profile.displayName = string
                    ki5.updateProfile(profile)
                if len(string.decode('utf-8')) <= 1000000000000:
                    profile = ki6.getProfile()
                    profile.displayName = string
                    ki6.updateProfile(profile)
                if len(string.decode('utf-8')) <= 1000000000000:
                    profile = ki7.getProfile()
                    profile.displayName = string
                    ki7.updateProfile(profile)
                if len(string.decode('utf-8')) <= 1000000000000:
                    profile = ki8.getProfile()
                    profile.displayName = string
                    ki8.updateProfile(profile)
                if len(string.decode('utf-8')) <= 1000000000000:
                    profile = ki9.getProfile()
                    profile.displayName = string
                    ki9.updateProfile(profile)
                if len(string.decode('utf-8')) <= 1000000000000:
                    profile = k1.getProfile()
                    profile.displayName = string
                    k1.updateProfile(profile)
                if len(string.decode('utf-8')) <= 1000000000000:
                    profile = k2.getProfile()
                    profile.displayName = string
                    k2.updateProfile(profile)
                if len(string.decode('utf-8')) <= 1000000000000:
                    profile = k3.getProfile()
                    profile.displayName = string
                    k3.updateProfile(profile)
                if len(string.decode('utf-8')) <= 1000000000000:
                    profile = k4.getProfile()
                    profile.displayName = string
                    k4.updateProfile(profile)
                if len(string.decode('utf-8')) <= 1000000000000:
                    profile = k5.getProfile()
                    profile.displayName = string
                    k5.updateProfile(profile)
                if len(string.decode('utf-8')) <= 1000000000000:
                    profile = k6.getProfile()
                    profile.displayName = string
                    k6.updateProfile(profile)
                if len(string.decode('utf-8')) <= 1000000000000:
                    profile = k7.getProfile()
                    profile.displayName = string
                    k7.updateProfile(profile)
                if len(string.decode('utf-8')) <= 1000000000000:
                    profile = k8.getProfile()
                    profile.displayName = string
                    k8.updateProfile(profile)
                if len(string.decode('utf-8')) <= 1000000000000:
                    profile = k9.getProfile()
                    profile.displayName = string
                    k9.updateProfile(profile)
                if len(string.decode('utf-8')) <= 1000000000000:
                    profile = w1.getProfile()
                    profile.displayName = string
                    w1.updateProfile(profile)
                if len(string.decode('utf-8')) <= 1000000000000:
                    profile = w2.getProfile()
                    profile.displayName = string
                    w2.updateProfile(profile)
                if len(string.decode('utf-8')) <= 1000000000000:
                    profile = w3.getProfile()
                    profile.displayName = string
                    w3.updateProfile(profile)
                if len(string.decode('utf-8')) <= 1000000000000:
                    profile = w4.getProfile()
                    profile.displayName = string
                    w4.updateProfile(profile)
                if len(string.decode('utf-8')) <= 1000000000000:
                    profile = w5.getProfile()
                    profile.displayName = string
                    w5.updateProfile(profile)
                if len(string.decode('utf-8')) <= 1000000000000:
                    profile = w6.getProfile()
                    profile.displayName = string
                    w6.updateProfile(profile)
                if len(string.decode('utf-8')) <= 1000000000000:
                    profile = w7.getProfile()
                    profile.displayName = string
                    w7.updateProfile(profile)
                if len(string.decode('utf-8')) <= 1000000000000:
                    profile = w8.getProfile()
                    profile.displayName = string
                    w8.updateProfile(profile)
                if len(string.decode('utf-8')) <= 1000000000000:
                    profile = w9.getProfile()
                    profile.displayName = string
                    w9.updateProfile(profile)
                if len(string.decode('utf-8')) <= 1000000000000:
                    profile = l1.getProfile()
                    profile.displayName = string
                    l1.updateProfile(profile)
                if len(string.decode('utf-8')) <= 1000000000000:
                    profile = l2.getProfile()
                    profile.displayName = string
                    l2.updateProfile(profile)
                if len(string.decode('utf-8')) <= 1000000000000:
                    profile = l3.getProfile()
                    profile.displayName = string
                    l3.updateProfile(profile)
                if len(string.decode('utf-8')) <= 1000000000000:
                    profile = l4.getProfile()
                    profile.displayName = string
                    l4.updateProfile(profile)
                if len(string.decode('utf-8')) <= 1000000000000:
                    profile = l5.getProfile()
                    profile.displayName = string
                    l5.updateProfile(profile)
            elif "Allbio: " in msg.text:
                string = msg.text.replace("Allbio: ","")
                if len(string.decode('utf-8')) <= 1000000000000:
                    profile = ki.getProfile()
                    profile.statusMessage = string
                    ki.updateProfile(profile)
                if len(string.decode('utf-8')) <= 1000000000000:
                    profile = ki2.getProfile()
                    profile.statusMessage = string
                    ki2.updateProfile(profile)
                if len(string.decode('utf-8')) <= 1000000000000:
                    profile = ki3.getProfile()
                    profile.statusMessage = string
                    ki3.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki4.getProfile()
                    profile.statusMessage = string
                    ki4.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki5.getProfile()
                    profile.statusMessage = string
                    ki5.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki6.getProfile()
                    profile.statusMessage = string
                    ki6.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki7.getProfile()
                    profile.statusMessage = string
                    ki7.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki8.getProfile()
                    profile.statusMessage = string
                    ki8.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki9.getProfile()
                    profile.statusMessage = string
                    ki9.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = k1.getProfile()
                    profile.statusMessage = string
                    k1.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = k2.getProfile()
                    profile.statusMessage = string
                    k2.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = k3.getProfile()
                    profile.statusMessage = string
                    k3.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = k4.getProfile()
                    profile.statusMessage = string
                    k4.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = k5.getProfile()
                    profile.statusMessage = string
                    k5.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = k6.getProfile()
                    profile.statusMessage = string
                    k6.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = k7.getProfile()
                    profile.statusMessage = string
                    k7.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = k8.getProfile()
                    profile.statusMessage = string
                    k8.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = k9.getProfile()
                    profile.statusMessage = string
                    k9.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = w1.getProfile()
                    profile.statusMessage = string
                    w1.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = w2.getProfile()
                    profile.statusMessage = string
                    w2.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = w3.getProfile()
                    profile.statusMessage = string
                    w3.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = w4.getProfile()
                    profile.statusMessage = string
                    w4.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = w5.getProfile()
                    profile.statusMessage = string
                    w5.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = w6.getProfile()
                    profile.statusMessage = string
                    w6.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = w7.getProfile()
                    profile.statusMessage = string
                    w7.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = w8.getProfile()
                    profile.statusMessage = string
                    w8.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = w9.getProfile()
                    profile.statusMessage = string
                    w9.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = l1.getProfile()
                    profile.statusMessage = string
                    l1.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = l2.getProfile()
                    profile.statusMessage = string
                    l2.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = l3.getProfile()
                    profile.statusMessage = string
                    l3.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = l4.getProfile()
                    profile.statusMessage = string
                    l4.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = l5.getProfile()
                    profile.statusMessage = string
                    l5.updateProfile(profile)

#---------------------------------------------------------
            elif "1team: " in msg.text:
                string = msg.text.replace("1team: ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki.getProfile()
                    profile.displayName = string
                    ki.updateProfile(profile)
                    ki.sendText(msg.to,"􀜁􀇔􏿿Update Names👉" + string + "👈")
#--------------------------------------------------------
            elif "2team: " in msg.text:
                string = msg.text.replace("2team: ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki2.getProfile()
                    profile.displayName = string
                    ki2.updateProfile(profile)
                    ki2.sendText(msg.to,"􀜁􀇔􏿿Update Names👉" + string + "👈")
#--------------------------------------------------------
            elif "3team: " in msg.text:
                string = msg.text.replace("3team: ","")
                if len(string.decode('utf-8')) <= 1000000000000000000000:
                    profile = ki3.getProfile()
                    profile.displayName = string
                    ki3.updateProfile(profile)
                    ki3.sendText(msg.to,"􀜁􀇔􏿿Update Names👉" + string + "👈")
#--------------------------------------------------------
            elif "4team: " in msg.text:
                string = msg.text.replace("4team: ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki4.getProfile()
                    profile.displayName = string
                    ki4.updateProfile(profile)
                    ki4.sendText(msg.to,"􀜁􀇔􏿿Update Names👉" + string + "👈")
#--------------------------------------------------------
            elif "5team: " in msg.text:
                string = msg.text.replace("5pro: ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki5.getProfile()
                    profile.displayName = string
                    ki5.updateProfile(profile)
                    ki5.sendText(msg.to,"􀜁􀇔􏿿Update Names👉" + string + "👈")
#--------------------------------------------------------
            elif "6team: " in msg.text:
                string = msg.text.replace("6team: ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki6.getProfile()
                    profile.displayName = string
                    ki6.updateProfile(profile)
                    ki6.sendText(msg.to,"􀜁􀇔􏿿Update Names👉" + string + "👈")
#--------------------------------------------------------
            elif "7team: " in msg.text:
                string = msg.text.replace("7pro: ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki7.getProfile()
                    profile.displayName = string
                    ki7.updateProfile(profile)
                    ki7.sendText(msg.to,"􀜁􀇔􏿿Update Names👉" + string + "👈")
#--------------------------------------------------------
            elif "8team: " in msg.text:
                string = msg.text.replace("8team: ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki8.getProfile()
                    profile.displayName = string
                    ki8.updateProfile(profile)
                    ki8.sendText(msg.to,"􀜁􀇔􏿿Update Names👉" + string + "👈")
#--------------------------------------------------------
            elif "9team: " in msg.text:
                string = msg.text.replace("9team: ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki9.getProfile()
                    profile.displayName = string
                    ki9.updateProfile(profile)
                    ki9.sendText(msg.to,"􀜁􀇔􏿿Update Names👉" + string + "👈")
#--------------------------------------------------------
            elif "11team: " in msg.text:
                string = msg.text.replace("11team: ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = k1.getProfile()
                    profile.displayName = string
                    k1.updateProfile(profile)
                    k1.sendText(msg.to,"􀜁􀇔􏿿Update Names👉" + string + "👈")
#--------------------------------------------------------
            elif "11team: " in msg.text:
                string = msg.text.replace("11team: ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = k2.getProfile()
                    profile.displayName = string
                    k2.updateProfile(profile)
                    k2.sendText(msg.to,"􀜁􀇔􏿿Update Names👉" + string + "👈")
#--------------------------------------------------------
            elif "12team: " in msg.text:
                string = msg.text.replace("12team: ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = k3.getProfile()
                    profile.displayName = string
                    k3.updateProfile(profile)
                    k3.sendText(msg.to,"􀜁􀇔􏿿Update Names👉" + string + "👈")
#--------------------------------------------------------
            elif "13team: " in msg.text:
                string = msg.text.replace("13team: ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = k4.getProfile()
                    profile.displayName = string
                    k4.updateProfile(profile)
                    k4.sendText(msg.to,"􀜁􀇔􏿿Update Names👉" + string + "👈")
#--------------------------------------------------------
            elif "14team: " in msg.text:
                string = msg.text.replace("14team: ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = k5.getProfile()
                    profile.displayName = string
                    k5.updateProfile(profile)
                    k5.sendText(msg.to,"􀜁􀇔􏿿Update Names👉" + string + "👈")
#--------------------------------------------------------
            elif "15team: " in msg.text:
                string = msg.text.replace("15team: ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = k6.getProfile()
                    profile.displayName = string
                    k6.updateProfile(profile)
                    k6.sendText(msg.to,"􀜁􀇔􏿿Update Names👉" + string + "👈")
#--------------------------------------------------------
            elif "16team: " in msg.text:
                string = msg.text.replace("16team: ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = k7.getProfile()
                    profile.displayName = string
                    k7.updateProfile(profile)
                    k7.sendText(msg.to,"􀜁􀇔􏿿Update Names👉" + string + "👈")
#--------------------------------------------------------
            elif "17team: " in msg.text:
                string = msg.text.replace("17team: ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = k8.getProfile()
                    profile.displayName = string
                    k8.updateProfile(profile)
                    k8.sendText(msg.to,"􀜁􀇔􏿿Update Names👉" + string + "👈")
#--------------------------------------------------------
            elif "18team: " in msg.text:
                string = msg.text.replace("18team: ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = k9.getProfile()
                    profile.displayName = string
                    k9.updateProfile(profile)
                    k9.sendText(msg.to,"􀜁􀇔􏿿Update Names👉" + string + "👈")
#--------------------------------------------------------
            elif "19team: " in msg.text:
                string = msg.text.replace("19team: ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = w1.getProfile()
                    profile.displayName = string
                    w1.updateProfile(profile)
                    w1.sendText(msg.to,"􀜁􀇔􏿿Update Names👉" + string + "👈")
#--------------------------------------------------------
            elif "20team: " in msg.text:
                string = msg.text.replace("20pro: ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = w2.getProfile()
                    profile.displayName = string
                    w2.updateProfile(profile)
                    w2.sendText(msg.to,"􀜁􀇔􏿿Update Names👉" + string + "👈")
#--------------------------------------------------------
            elif "Mid: " in msg.text:
                mmid = msg.text.replace("Mid: ","")
                msg.contentType = 13
                msg.contentMetadata = {"mid":mmid}
                cl.sendMessage(msg)
            elif msg.text.lower() == 'contact on':
                if wait["contact"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Sudah On")
                    else:
                        cl.sendText(msg.to,"It is already open")
                else:
                    wait["contact"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already open 👈")
                    else:
                        cl.sendText(msg.to,"It is already open 􀜁􀇔􏿿")
            elif msg.text.lower() == 'contact off':
                if wait["contact"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"sudah off ô€œô€„‰👈")
                    else:
                        cl.sendText(msg.to,"It is already off ô€œ��ô€„‰👈")
                else:
                    wait["contact"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"off ô€œô€„‰already")
                    else:
                        cl.sendText(msg.to,"already Close ô€œô€„‰👈")
            elif msg.text.lower() == 'protect on':
                if wait["protect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Ini sudah on 􀜁􀇔􏿿👈")
                    else:
                        cl.sendText(msg.to,"Hal ini sudah terbuka ô€¨👈")
                else:
                    wait["protect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already ON􀜁􀇔􏿿")
                    else:
                        cl.sendText(msg.to,"It is already On ô€¨")
            elif msg.text.lower() == 'qrprotect on':
                if wait["linkprotect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Ini sudah on 􀜁􀇔��👈")
                    else:
                        cl.sendText(msg.to,"Hal ini sudah terbuka ô€¨👈")
                else:
                    wait["linkprotect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already ON􀜁􀇔􏿿")
                    else:
                        cl.sendText(msg.to,"It is already On ô€¨")
            elif msg.text.lower() == 'inviteprotect on':
                if wait["inviteprotect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Ini sudah on 􀜁􀇔􏿿👈")
                    else:
                        cl.sendText(msg.to,"Hal ini sudah terbuka ô€¨����👈")
                else:
                    wait["inviteprotect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already ON􀜁􀇔􏿿")
                    else:
                        cl.sendText(msg.to,"It is already On ô€¨")
            elif msg.text.lower() == 'cancelprotect on':
                if wait["cancelprotect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Ini sudah on 􀜁􀇔􏿿👈")
                    else:
                        cl.sendText(msg.to,"Hal ini sudah terbuka ô€¨👈")
                else:
                    wait["cancelprotect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already ON􀜁􀇔􏿿")
                    else:
                        cl.sendText(msg.to,"It is already On ô€¨")
            elif msg.text.lower() == 'auto join on':
                if wait["autoJoin"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Ini sudah off 􀜁􀇔􏿿👈")
                    else:
                        cl.sendText(msg.to,"Hal ini sudah terbuka ô€¨👈")
                else:
                    wait["autoJoin"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already ON􀜁􀇔􏿿")
                    else:
                        cl.sendText(msg.to,"It is already On ô€¨")
            elif msg.text in ["Allprotect on","Panick:on"]:
              if msg.from_ in admin:
                if wait["inviteprotect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Ini sudah on 􀜁􀇔􏿿👈")
                    else:
                        cl.sendText(msg.to,"Already on")
                else:
                    wait["inviteprotect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect invite on 􀜁􀇔􏿿")
                if wait["cancelprotect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Ini sudah on 􀜁􀇔􏿿👈")
                    else:
                        cl.sendText(msg.to,"Already on")
                else:
                    wait["cancelprotect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect cancel on 􀜁􀇔􏿿")
                if wait["protect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Ini sudah on 􀜁􀇔􏿿👈")
                    else:
                        cl.sendText(msg.to,"Already on")
                else:
                    wait["protect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect on 􀜁􀇔􏿿")
                    else:
                        cl.sendText(msg.to,"Already on")
                if wait["linkprotect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Ini sudah on 􀜁􀇔􏿿👈")
                    else:
                        cl.sendText(msg.to,"Already on")
                else:
                    wait["linkprotect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect QR on 􀜁􀇔􏿿")
                    else:
                        cl.sendText(msg.to,"Already on")
            elif msg.text in ["Allprotect off","Panick:off"]:
              if msg.from_ in admin:
                if wait["inviteprotect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Ini sudah off 􀜁􀇔􏿿👈")
                    else:
                        cl.sendText(msg.to,"Already off")
                else:
                    wait["inviteprotect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect invite off 􀜁􀇔􏿿")
                if wait["cancelprotect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Ini sudah off 􀜁􀇔􏿿👈")
                    else:
                        cl.sendText(msg.to,"Already off")
                else:
                    wait["cancelprotect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect cancel off 􀜁􀇔􏿿")
                if wait["protect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Ini sudah off 􀜁􀇔􏿿👈")
                    else:
                        cl.sendText(msg.to,"Already off")
                else:
                    wait["protect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect off 􀜁􀇔􏿿")
                    else:
                        cl.sendText(msg.to,"Already off")
                if wait["linkprotect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Ini sudah off 􀜁􀇔􏿿👈")
                    else:
                        cl.sendText(msg.to,"Already off")
                else:
                    wait["linkprotect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect QR off 􀜁􀇔􏿿")
                    else:
                        cl.sendText(msg.to,"Already off")
            elif msg.text.lower() == 'auto join off':
                if wait["autoJoin"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto Join Already Off")
                    else:
                        cl.sendText(msg.to,"Auto Join set off")
                else:
                    wait["autoJoin"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already close")
                    else:
                        cl.sendText(msg.to,"It is already open ô€œ👈")
            elif msg.text in ["Protect off"]:
                if wait["protect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"hall ini sudah off ô€œ👈")
                    else:
                        cl.sendText(msg.to,"sudah dimatikan ô€œô€„‰👈")
                else:
                    wait["protect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already close")
                    else:
                        cl.sendText(msg.to,"It is already open ô€œ👈")
            elif msg.text in ["Qrprotect off","qrprotect off"]:
                if wait["linkprotect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"hall ini sudah off ô€œ👈")
                    else:
                        cl.sendText(msg.to,"sudah dimatikan ô€œô€„‰👈")
                else:
                    wait["linkprotect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already close")
                    else:
                        cl.sendText(msg.to,"It is already open ô€œ👈")
            elif msg.text in ["Inviteprotect off"]:
                if wait["inviteprotect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"hall ini sudah off ô€œ👈")
                    else:
                        cl.sendText(msg.to,"sudah dimatikan ô€œô€„‰👈")
                else:
                    wait["inviteprotect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already close")
                    else:
                        cl.sendText(msg.to,"It is already open ô€œ👈")
            elif msg.text in ["Cancelprotect off"]:
                if wait["cancelprotect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"hall ini sudah off ô€œ👈")
                    else:
                        cl.sendText(msg.to,"sudah dimatikan ô€œô€„‰👈")
                else:
                    wait["cancelprotect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already close")
                    else:
                        cl.sendText(msg.to,"It is already open ô€œ👈")
            elif "Group cancel: " in msg.text:
                try:
                    strnum = msg.text.replace("Group cancel: ","")
                    if strnum == "off":
                        wait["autoCancel"]["on"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Itu off undangan ditolak👈\nSilakan kirim dengan menentukan jumlah orang ketika Anda menghidupkan👈")
                        else:
                            cl.sendText(msg.to,"Off undangan ditolak👈Sebutkan jumlah terbuka ketika Anda ingin mengirim")
                    else:
                        num =  int(strnum)
                        wait["autoCancel"]["on"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,strnum + "Kelompok berikut yang diundang akan ditolak secara otomatis👈")
                        else:
                            cl.sendText(msg.to,strnum + "The team declined to create the following automatic invitation")
                except:
                    if wait["lang"] == "JP":
                        kk.sendText(msg.to,"Nilai tidak benar👈")
                    else:
                        cl.sendText(msg.to,"Weird value🛡")
            elif msg.text in ["Leave on","Auto leave: on"]:
                if wait["leaveRoom"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"on👈􀜁􀇔􏿿")
                    else:
                        cl.sendText(msg.to,"Sudah terbuka 􀜁􀇔􏿿")
                else:
                    wait["leaveRoom"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done👈􀜁􀇔􏿿")
                    else:
                        cl.sendText(msg.to,"Is already open👈􀜁􀇔􏿿")
            elif msg.text in ["Leave off","Auto leave: off"]:
                if wait["leaveRoom"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"on👈􀜁􀇔􏿿")
                    else:
                        cl.sendText(msg.to,"Sudah off👈􀜁􀇔􏿿")
                else:
                    wait["leaveRoom"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done👈􀜁􀇔􏿿")
                    else:
                        cl.sendText(msg.to,"Is already close👈􀜁􀇔􏿿")
            elif msg.text in ["Share on","share on"]:
                if wait["timeline"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done 􀜁􀇔􏿿")
                    else:
                        cl.sendText(msg.to,"Hal ini sudah terbuka👈")
                else:
                    wait["timeline"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"on👈")
                    else:
                        cl.sendText(msg.to,"on👈")
            elif msg.text in ["Share off","share off"]:
                if wait["timeline"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done👈􀜁􀇔􏿿")
                    else:
                        cl.sendText(msg.to,"It is already turned off 􀜁􀇔􏿿👈")
                else:
                    wait["timeline"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Off👈")
                    else:
                        cl.sendText(msg.to,"Off👈")
            elif msg.text.lower() == 'Settings':
                md = ""
                if wait["contact"] == True: md+="☞ Contact → ✔\n"
                else: md+="☞ Contact → ❌\n"
                if wait["autoJoin"] == True: md+="☞ Auto Join → ✔\n"
                else: md+="☞ Auto Join → ❌\n"
                if wait["autoCancel"]["on"] == True:md+="☞ Auto cancel: " + str(wait["autoCancel"]["members"]) + " → ✔\n"
                else: md+="☞ Group cancel → ❌\n"
                if wait["leaveRoom"] == True: md+="☞ Auto leave → ✔\n"
                else: md+="☞ Auto leave → ❌\n"
                if wait["timeline"] == True: md+="☞ share → ✔\n"
                else:md+="☞ Share → ❌\n"
                if wait["autoAdd"] == True: md+="☞ Auto add → ✔\n"
                else:md+="☞ Auto add → ❌\n"
                if wait["commentOn"] == True: md+="☞ Auto komentar → ✔\n"
                else:md+="☞ Auto komentar → ❌\n"
                if wait["protect"] == True: md+="☞ Protect → ✔\n"
                else:md+="☞ Protect → ❌\n"
                if wait["linkprotect"] == True: md+="☞ Link Protect → ✔\n"
                else:md+="☞ Link Protect → ❌\n"
                if wait["inviteprotect"] == True: md+="☞ Invitation Protect → ✔\n"
                else:md+="☞ Invitation Protect → ❌\n"
                if wait["cancelprotect"] == True: md+="☞ Cancel Protect → ✔\n"
                else:md+="☞ Cancel Protect → ❌\n"
                if wait["likeOn"] == True: md+="☞ Auto like → ✔\n"
                else:md+="☞ Auto like → ❌\n" 
                cl.sendText(msg.to,md)
                msg.contentType = 13
                msg.contentMetadata = {'mid': 'u63b477a73bc4dc8f08dd9a2ae572ad14'}
                cl.sendMessage(msg)
            
            elif msg.text in ["Like:on"]:
                if wait["likeOn"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done。")
                else:
                    wait["likeOn"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already。")
            elif msg.text in ["いいね:オフ","Like:off"]:
                if wait["likeOn"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done。")
                else:
                    wait["likeOn"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already。")
                        
            elif msg.text in ["Add on","Add auto on"]:
                if wait["autoAdd"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already On")
                    else:
                        cl.sendText(msg.to,"Already On👈")
                else:
                    wait["autoAdd"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already On👈")
                    else:
                        cl.sendText(msg.to,"Already On👈")
            elif msg.text in ["Add off","Add auto off"]:
                if wait["autoAdd"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Hal ini sudah off👈")
                    else:
                        cl.sendText(msg.to,"Hal ini sudah dimatikan👈")
                else:
                    wait["autoAdd"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already Off👈")
                    else:
                        cl.sendText(msg.to,"Untuk mengaktifkan-off👈")
            elif "Message set: " in msg.text:
                wait["message"] = msg.text.replace("Message set: ","")
                cl.sendText(msg.to,"We changed the message👈")
            elif "Help set: " in msg.text:
                wait["help"] = msg.text.replace("Help set: ","")
                cl.sendText(msg.to,"We changed the Help👈")
            elif "Pesan add: " in msg.text:
                wait["message"] = msg.text.replace("Pesan add: ","")
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"Kami mengubah pesan🛡")
                else:
                    cl.sendText(msg.to,"Change information")
            elif msg.text in ["Pesan add cek","Message Confirmation"]:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"Additional information is automatically set to the following \n\n" + wait["message"])
                else:
                    cl.sendText(msg.to,"Pesan tambahan otomatis telah ditetapkan sebagai berikut \n\n" + wait["message"])
            elif msg.text in ["Change","change"]:
                if wait["lang"] =="JP":
                    wait["lang"] = "TW"
                    cl.sendText(msg.to,"I changed the language to engglis👈")
                else:
                    wait["lang"] = "JP"
                    cl.sendText(msg.to,"I changed the language to indonesia👈")
            elif "Message set: " in msg.text:
                c = msg.text.replace("Message set: ","")
                if c in [""," ","\n",None]:
                    cl.sendText(msg.to,"Is a string that can not be changed👈")
                else:
                    wait["comment"] = c
                    cl.sendText(msg.to,"This has been changed👈\n\n" + c)
            elif "Comment set: " in msg.text:
                c = msg.text.replace("Comment set: ","")
                if c in [""," ","\n",None]:
                    cl.sendText(msg.to,"Merupakan string yang tidak bisa diubah👈")
                else:
                    wait["comment"] = c
                    cl.sendText(msg.to,"Ini telah diubah👈\n\n" + c)
            elif msg.text in ["Com on","Com:on","Comment on"]:
                if wait["commentOn"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Aku berada di👈")
                    else:
                        cl.sendText(msg.to,"To open👈")
                else:
                    wait["commentOn"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ã‚ªãƒ³ã«ã—ã¾ã—ãŸ👈")
                    else:
                        cl.sendText(msg.to,"è¦äº†å¼€👈")
            elif msg.text in ["Com off"]:
                if wait["commentOn"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Hal ini sudah off")
                    else:
                        cl.sendText(msg.to,"It is already turned off")
                else:
                    wait["commentOn"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Off👈")
                    else:
                        cl.sendText(msg.to,"To turn off")
            elif msg.text in ["Com","Comment"]:
                cl.sendText(msg.to,"Auto komentar saat ini telah ditetapkan sebagai berikut:👈\n\n" + str(wait["comment"]))
            elif msg.text in ["Com Bl"]:
                wait["wblack"] = True
                cl.sendText(msg.to,"Please send contacts from the person you want to add to the blacklistô€œô€…”👈")
            elif msg.text in ["Com hapus Bl"]:
                wait["dblack"] = True
                cl.sendText(msg.to,"Please send contacts from the person you want to add from the blacklistô€œô€…”👈")
            elif msg.text in ["Com Bl cek"]:
                if wait["commentBlack"] == {}:
                    cl.sendText(msg.to,"Nothing in the blacklistô€œ🛡")
                else:
                    cl.sendText(msg.to,"The following is a blacklistô€œ👈")
                    mc = ""
                    for mi_d in wait["commentBlack"]:
                        mc += "ãƒ»" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
            elif msg.text.lower() == 'jam on':
                if wait["clock"] == True:
                    cl.sendText(msg.to,"Sudah On")
                else:
                    wait["clock"] = True
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"(%H:%M)")
                    profile = cl.getProfile()
                    profile.displayName = wait["cName"] + nowT
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"👉Jam on👈")
            elif msg.text.lower() == 'jam off':
                if wait["clock"] == False:
                    cl.sendText(msg.to,"Hal ini sudah off🛡")
                else:
                    wait["clock"] = False
                    cl.sendText(msg.to,"Adalah Off")
            elif "Jam say: " in msg.text:
                n = msg.text.replace("Jam say: ","")
                if len(n.decode("utf-8")) > 30:
                    cl.sendText(msg.to,"terlalu lama")
                else:
                    wait["cName"] = n
                    cl.sendText(msg.to,"Ini telah diubah🛡\n\n" + n)
            elif msg.text.lower() == 'update':
                if wait["clock"] == True:
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"(%H:%M)")
                    profile = cl.getProfile()
                    profile.displayName = wait["cName"] + nowT
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"Diperbarui👈")
                else:
                    cl.sendText(msg.to,"Silahkan Aktifkan Nama")

            elif msg.text == "Lurk":
                if msg.toType == 2:
                    cl.sendText(msg.to, "Set reading point:" + datetime.now().strftime('\n%Y/%m/%d %H:%M:%S'))
                    try:
                        del wait2['readPoint'][msg.to]
                        del wait2['readMember'][msg.to]
                    except:
                        pass
                        wait2['readPoint'][msg.to] = msg.id
                        wait2['readMember'][msg.to] = ""
                        wait2['setTime'][msg.to] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                        wait2['ROM'][msg.to] = {}
                        print wait2
                        
            elif msg.text == "Lurking":
                if msg.toType == 2:
                    if msg.to in wait2['readPoint']:
                        if wait2["ROM"][msg.to].items() == []:
                            chiya = ""
                        else:
                            chiya = ""
                            for rom in wait2["ROM"][msg.to].items():
                                print rom
                                chiya += rom[1] + "\n"

                        cl.sendText(msg.to, "==============================\nActive readers:%s\n\n\n\nPassive readers:\n%s\n\n==============================\nIn the last seen point:\n[%s]\n==============================\n [☸]➦Powered By: Alin々•┅─────" % (wait2['readMember'][msg.to],chiya,setTime[msg.to]))
                        print "ReadPoint Set..."
                        try:
                            del wait2['readPoint'][msg.to]
                            del wait2['readMember'][msg.to]
                        except:
                            pass
                        wait2['readPoint'][msg.to] = msg.id
                        wait2['readMember'][msg.to] = ""
                        wait2['setTime'][msg.to] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                        wait2['ROM'][msg.to] = {}
                        print wait
                        cl.sendText(msg.to, "Auto set reading point in:" + datetime.now().strftime('\n%Y-%m-%d %H:%M:%S'))
                    else:
                        cl.sendText(msg.to, "Reading point has not been set.")

#-----------------------[Add Staff Section]------------------------
            elif "Add staff @" in msg.text:
                if msg.from_ in admin:
                    print "[Command]Staff add executing"
                    _name = msg.text.replace("Add staff @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                staff.append(target)
                                cl.sendText(msg.to,"Added to the staff list")
                            except:
                                pass
                    print "[Command]Staff add executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Admin permission required.")

            elif "Remove staff @" in msg.text:
                if msg.from_ in admin:
                    print "[Command]Staff remove executing"
                    _name = msg.text.replace("Remove staff @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                staff.remove(target)
                                cl.sendText(msg.to,"Removed to the staff list")
                            except:
                                pass
                    print "[Command]Staff remove executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Admin permission required.")

            elif msg.text in ["Stafflist","stafflist"]:
                if staff == []:
                    cl.sendText(msg.to,"The stafflist is empty")
                else:
                    cl.sendText(msg.to,"Staff list: ")
                    mc = ""
                    for mi_d in staff:
                        mc += "->" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
                    print "[Command]Stafflist executed"								
#-----------------------------------------------------------

#----------------------------------------------------------------
            
#-----------------------------------------------------------
#-----------------------------------------------------------)
#----------------------ADMIN COMMAND------------------------------#

            elif ("Kick " in msg.text):
                if msg.from_ in admin:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            cl.kickoutFromGroup(msg.to,[target])
                        except:
                            cl.sendText(msg.to,"Error")
                    
            elif "Mention" in msg.text:
                group = cl.getGroup(msg.to)
                k = len(group.members)//100
                for j in xrange(k+1):
                    msg = Message(to=msg.to)
                    txt = u''
                    s=0
                    d=[]
                    for i in group.members[j*100 : (j+1)*100]:
                        d.append({"S":str(s), "E" :str(s+8), "M":i.mid})
                        s += 9
                        txt += u'@Krampus\n'
                    msg.text = txt
                    msg.contentMetadata = {u'MENTION':json.dumps({"MENTIONEES":d})}
                    cl.sendMessage(msg) 

            elif "Ratakan" in msg.text:
                  if msg.from_ in admin:
                       nk0 = msg.text.replace("Ratakan","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("all","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for g in gs.members:
                           if _name in g.displayName:
                              targets.append(g.mid)
                       if targets == []:
                           cl.sendText(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:                            
                             if not target in Bots:
                                if not target in admin:
                                  try:
                                      klist=[cl,ki,ki2,ki3,ki4,ki5,ki6,ki7,ki8,ki9,w1,w2,w3,w4,w5]
                                      kicker=random.choice(klist)
                                      kicker.kickoutFromGroup(msg.to,[target])
                                      print (msg.to,[g.mid])
                                  except:
                                      cl.sendText(msg.to,"Sukses Bosqu")
                                      cl.sendText(msg.to,"masih mauko sundala")

            elif msg.text in ["List grup"]:
                if msg.from_ in admin:
                    gid = cl.getGroupIdsJoined()
                    h = "===[List Groups]==="
                    total = str(len(gid))
                    for i in gid:
                        if i is not None:
                            try:
                                groups = cl.getGroup(i)
                                if groups.members is not None:
                                    members = str(len(groups.members))
                                else:
                                    members = "0"
                                if groups.invitee is not None:
                                    pendings = str(len(groups.invitee))
                                else:
                                    pendings = "0"
                                h += "\n[" + groups.name + "] ->(" + members +")\n -+GroupID : " + i
                            except:
                                break
                        else:
                            break
                    if gid is not None:
                        cl.sendText(msg.to,h + "\n|[Total Groups]| : " + str(total))
                    else:
                        cl.sendText(msg.to,"Tidak ada grup saat ini")
                    ginv = cl.getGroupIdsInvited()
                    j = "===[List Groups Invited]==="
                    totals = str(len(ginv))
                    for z in ginv:
                        if z is not None:
                            try:
                                groups = cl.getGroup(z)
                                if groups.members is not None:
                                    members = str(len(groups.members))
                                else:
                                    members = "0"
                                if groups.invitee is not None:
                                    pendings = str(len(groups.invitee))
                                else:
                                    pendings = "0"
                                j += "\n[" + groups.name + "] ->(" + members + ")\n -+GroupID : " + i
                            except:
                                break
                        else:
                            break
                    if ginv is not None:
                        cl.sendText(msg.to,j + "\n|[Total Groups Invited]| : " + str(totals))
                    else:
                        cl.sendText(msg.to,"Tidak ada grup tertunda saat ini")

            elif msg.text in ["Info grup"]:
                if msg.from_ in admin:
                    gid = cl.getGroupIdsJoined()
                    cl.sendText(msg.to,"===[List Details Group]===")
                    total = str(len(gid))
                    for i in gid:
                        if i is not None:
                            try:
                                groups = ki.getGroup(i)
                                if groups.members is not None:
                                    members = str(len(groups.members))
                                else:
                                    members = "0"
                                if groups.invitee is not None:
                                    pendings = str(len(groups.invitee))
                                else:
                                    pendings = "0"
                                h = "[" + groups.name + "]\n -+GroupID : " + i + "\n -+Members : " + members + "\n -+MembersPending : " + pendings + "\n -+Creator : " + groups.creator.displayName
                            except:
                                break
                        else:
                            break
                    if gid is not None:
                        cl.sendText(msg.to,h)
                        cl.sendText(msg.to,"|[Total Groups]| : " + str(total))
                    else:
                        cl.sendText(msg.to,"Tidak ada grup saat ini")
                    ginv = cl.getGroupIdsInvited()
                    cl.sendText(msg.to,"===[List Details Groups Invited]===")
                    totals = str(len(ginv))
                    for z in ginv:
                        if z is not None:
                            try:
                                groups = cl.getGroup(z)
                                if groups.members is not None:
                                    members = str(len(groups.members))
                                else:
                                    members = "0"
                                if groups.invitee is not None:
                                    pendings = str(len(groups.invitee))
                                else:
                                    pendings = "0"
                                j = "[" + groups.name + "]\n -+GroupID : " + i + "\n -+Members : " + members + "\n -+MembersPending : " + pendings + "\n -+Creator : " + groups.creator.displayName
                            except:
                                break
                        else:
                            break
                    if ginv is not None:
                        cl.sendText(msg.to,j)
                        cl.sendText(msg.to,"|[Total Groups Invited]| : " + str(totals))
                    else:
                        cl.sendText(msg.to,"Tidak ada grup tertunda saat ini")

            elif "Details grup: " in msg.text:
                if msg.from_ in admin:
                    gid = msg.text.replace("/DetailsGroup: ","")
                    if gid in [""," "]:
                        cl.sendText(msg.to,"Grup id tidak valid")
                    else:
                        try:
                            groups = cl.getGroup(gid)
                            if groups.members is not None:
                                members = str(len(groups.members))
                            else:
                                members = "0"
                            if groups.invitee is not None:
                                pendings = str(len(groups.invitee))
                            else:
                                pendings = "0"
                            h = "[" + groups.name + "]\n -+GroupID : " + gid + "\n -+Members : " + members + "\n -+MembersPending : " + pendings + "\n -+Creator : " + groups.creator.displayName + "\n -+GroupPicture : http://dl.profile.line.naver.jp/" + groups.pictureStatus
                            cl.sendText(msg.to,h)
                        except Exception as error:
                            cl.sendText(msg.to,(error))
            
            elif "Cancel invite: " in msg.text:
                if msg.from_ in admin:
                    gids = msg.text.replace("Cancel invite: ","")
                    gid = cl.getGroup(gids)
                    for i in gid:
                        if i is not None:
                            try:
                                cl.rejectGroupInvitation(i)
                            except:
                                cl.sendText(msg.to,"Error!")
                                break
                        else:
                            break
                    if gid is not None:
                        cl.sendText(msg.to,"Berhasil tolak undangan dari grup " + gid.name)
                    else:
                        cl.sendText(msg.to,"Grup tidak ditemukan")
            
            elif msg.text in ["Accept invite"]:
                if msg.from_ in admin:
                    gid = cl.getGroupIdsInvited()
                    _list = ""
                    for i in gid:
                        if i is not None:
                            gids = cl.getGroup(i)
                            _list += gids.name
                            cl.acceptGroupInvitation(i)
                        else:
                            break
                    if gid is not None:
                        cl.sendText(msg.to,"Berhasil terima semua undangan dari grup :\n" + _list)
                    else:
                        cl.sendText(msg.to,"Tidak ada grup yang tertunda saat ini")
            
            elif "Myname: " in msg.text:
                string = msg.text.replace("Myname: ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = cl.getProfile()
                    profile.displayName = string
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"Update Bio" + string)

            elif "Mybio: " in msg.text:
                string = msg.text.replace("Mybio: ","")
                if len(string.decode('utf-8')) <= 500:
                    profile = cl.getProfile()
                    profile.statusMessage = string
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"Update Bio" + string)
            
            elif ("Gname: " in msg.text):
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    group.name = msg.text.replace("Gname: ","")
                    cl.updateGroup(group)
                else:
                    cl.sendText(msg.to,"Tidak Dapat Mengubah Nama Grup")

            elif "Kick: " in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("Kick: ","")
                cl.kickoutFromGroup(msg.to,[midd])
            elif "Invite: " in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("Invite: ","")
                cl.findAndAddContactsByMid(midd)
                cl.inviteIntoGroup(msg.to,[midd])

            elif "Mysteal @" in msg.text:            
                print "[Command]dp executing"
                _name = msg.text.replace("Mysteal @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    cl.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = cl.getContact(target)
                            path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                            cl.sendImageWithURL(msg.to, path)
                        except:
                            pass
                print "[Command]dp executed"

            elif "Mycopy @" in msg.text:
                if msg.toType == 2:
                    if msg.from_ in admin:
                        print "[COPY] Ok"
                        _name = msg.text.replace("Mycopy @","")
                        _nametarget = _name.rstrip('  ')
                        gs = cl.getGroup(msg.to)
                        targets = []
                        for g in gs.members:
                            if _nametarget == g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            cl.sendText(msg.to, "Not Found...")
                        else:
                            for target in targets:
                                try:
                                    cl.cloneContactProfile(target)
                                    cl.sendText(msg.to, "Sukses Copy Profile")
                                except Exception as e:
                                    print e
                                    
            elif "Copy @" in msg.text:
                if msg.toType == 2:
                    if msg.from_ in admin:
                        print "[COPY] Ok"
                        _name = msg.text.replace("Copy @","")
                        _nametarget = _name.rstrip('  ')
                        gs = cl.getGroup(msg.to)
                        targets = []
                        for g in gs.members:
                            if _nametarget == g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            cl.sendText(msg.to, "Tidak Ada Target Copy")
                        else:
                            for target in targets:
                                try:
                                    ki.cloneContactProfile(target)
                                    ki2.cloneContactProfile(target)
                                    ki3.cloneContactProfile(target)
                                    ki4.cloneContactProfile(target)
                                    ki5.cloneContactProfile(target)
                                    ki6.cloneContactProfile(target)
                                    ki7.cloneContactProfile(target)
                                    ki8.cloneContactProfile(target)
                                    ki9.cloneContactProfile(target)
                                    k1.cloneContactProfile(target)
                                    k2.cloneContactProfile(target)
                                    k3.cloneContactProfile(target)
                                    k4.cloneContactProfile(target)
                                    k5.cloneContactProfile(target)
                                    k6.cloneContactProfile(target)
                                    k7.cloneContactProfile(target)
                                    k8.cloneContactProfile(target)
                                    k9.cloneContactProfile(target)
                                    w1.cloneContactProfile(target)
                                    w2.cloneContactProfile(target)
                                    w3.cloneContactProfile(target)
                                    w4.cloneContactProfile(target)
                                    w5.cloneContactProfile(target)
                                    w6.cloneContactProfile(target)
                                    w7.cloneContactProfile(target)
                                    w8.cloneContactProfile(target)
                                    w9.cloneContactProfile(target)
                                    l1.cloneContactProfile(target)
                                    l2.cloneContactProfile(target)
                                    l3.cloneContactProfile(target)
                                    l4.cloneContactProfile(target)
                                    k5.cloneContactProfile(target)
                                    cl.sendText(msg.to, "Sukses Copy Profile")
                                except Exception as e:
                                    print e
                                    
            elif msg.text in ["Mybackup"]:
                try:
                    cl.updateDisplayPicture(mybackup.pictureStatus)
                    cl.updateProfile(mybackup)
                    cl.sendText(msg.to, "Backup Sukses Bosqu")
                except Exception as e:
                    cl.sendText(msg.to, str (e))
                    
            elif msg.text in ["Backup"]:
                try:
                    ki.updateDisplayPicture(backup.pictureStatus)
                    ki.updateProfile(backup)
                    ki2.updateDisplayPicture(backup.pictureStatus)
                    ki2.updateProfile(backup)
                    ki3.updateDisplayPicture(backup.pictureStatus)
                    ki3.updateProfile(backup)
                    ki4.updateDisplayPicture(backup.pictureStatus)
                    ki4.updateProfile(backup)
                    ki5.updateDisplayPicture(backup.pictureStatus)
                    ki5.updateProfile(backup)
                    ki6.updateDisplayPicture(backup.pictureStatus)
                    ki6.updateProfile(backup)
                    ki7.updateDisplayPicture(backup.pictureStatus)
                    ki7.updateProfile(backup)
                    ki8.updateDisplayPicture(backup.pictureStatus)
                    ki8.updateProfile(backup)
                    ki9.updateDisplayPicture(backup.pictureStatus)
                    ki9.updateProfile(backup)
                    k1.updateDisplayPicture(backup.pictureStatus)
                    k1.updateProfile(backup)
                    k2.updateDisplayPicture(backup.pictureStatus)
                    k2.updateProfile(backup)
                    k3.updateDisplayPicture(backup.pictureStatus)
                    k3.updateProfile(backup)
                    k4.updateDisplayPicture(backup.pictureStatus)
                    k4.updateProfile(backup)
                    k5.updateDisplayPicture(backup.pictureStatus)
                    k5.updateProfile(backup)
                    k6.updateDisplayPicture(backup.pictureStatus)
                    k6.updateProfile(backup)
                    k7.updateDisplayPicture(backup.pictureStatus)
                    k7.updateProfile(backup)
                    k8.updateDisplayPicture(backup.pictureStatus)
                    k8.updateProfile(backup)
                    k9.updateDisplayPicture(backup.pictureStatus)
                    k9.updateProfile(backup)
                    w1.updateDisplayPicture(backup.pictureStatus)
                    w1.updateProfile(backup)
                    w2.updateDisplayPicture(backup.pictureStatus)
                    w2.updateProfile(backup)
                    w3.updateDisplayPicture(backup.pictureStatus)
                    w3.updateProfile(backup)
                    w4.updateDisplayPicture(backup.pictureStatus)
                    w4.updateProfile(backup)
                    w5.updateDisplayPicture(backup.pictureStatus)
                    w5.updateProfile(backup)
                    w6.updateDisplayPicture(backup.pictureStatus)
                    w6.updateProfile(backup)
                    w7.updateDisplayPicture(backup.pictureStatus)
                    w7.updateProfile(backup)
                    w8.updateDisplayPicture(backup.pictureStatus)
                    w8.updateProfile(backup)
                    w9.updateDisplayPicture(backup.pictureStatus)
                    w9.updateProfile(backup)
                    l1.updateDisplayPicture(backup.pictureStatus)
                    l1.updateProfile(backup)
                    l2.updateDisplayPicture(backup.pictureStatus)
                    l2.updateProfile(backup)
                    l3.updateDisplayPicture(backup.pictureStatus)
                    l3.updateProfile(backup)
                    l4.updateDisplayPicture(backup.pictureStatus)
                    l4.updateProfile(backup)
                    l5.updateDisplayPicture(backup.pictureStatus)
                    l5.updateProfile(backup)
                    cl.sendText(msg.to, "Backup Sukses Bosqu")
                except Exception as e:
                    cl.sendText(msg.to, str (e))

            elif "Bc:ct " in msg.text:
                bctxt = msg.text.replace("Bc:ct ", "")
                a = cl.getAllContactIds()
                for manusia in a:
                    cl.sendText(manusia, (bctxt))

            elif "Bot:ct " in msg.text:
              if msg.from_ in admin:
                bctxt = msg.text.replace("Bot:ct ", "")
                b = ki.getAllContactIds()
                for manusia in b:
                    ki.sendText(manusia, (bctxt))
                c = ki2.getAllContactIds()
                for manusia in c:
                    ki2.sendText(manusia, (bctxt))
                d = ki3.getAllContactIds()
                for manusia in d:
                    ki3.sendText(manusia, (bctxt))
                e = ki4.getAllContactIds()
                for manusia in e:
                    ki4.sendText(manusia, (bctxt))
                f = ki5.getAllContactIds()
                for manusia in f:
                    ki5.sendText(manusia, (bctxt))
                g = ki6.getAllContactIds()
                for manusia in g:
                    ki6.sendText(manusia, (bctxt))
                h = ki7.getAllContactIds()
                for manusia in h:
                    ki7.sendText(manusia, (bctxt))
                i = ki8.getAllContactIds()
                for manusia in i:
                    ki8.sendText(manusia, (bctxt))
                j = ki9.getAllContactIds()
                for manusia in j:
                    ki9.sendText(manusia, (bctxt))
                k = k1.getAllContactIds()
                for manusia in k:
                    k1.sendText(manusia, (bctxt))
                l = k2.getAllContactIds()
                for manusia in l:
                    k2.sendText(manusia, (bctxt))
                m = k3.getAllContactIds()
                for manusia in m:
                    k3.sendText(manusia, (bctxt))
                n = k4.getAllContactIds()
                for manusia in n:
                    k4.sendText(manusia, (bctxt))
                o = k5.getAllContactIds()
                for manusia in o:
                    k5.sendText(manusia, (bctxt))
                p = k6.getAllContactIds()
                for manusia in p:
                    k6.sendText(manusia, (bctxt))
                q = k7.getAllContactIds()
                for manusia in q:
                    k7.sendText(manusia, (bctxt))
                r = k8.getAllContactIds()
                for manusia in r:
                    k8.sendText(manusia, (bctxt))
                s = k9.getAllContactIds()
                for manusia in s:
                    k9.sendText(manusia, (bctxt))
                t = w1.getAllContactIds()
                for manusia in t:
                    w1.sendText(manusia, (bctxt))
                u = w2.getAllContactIds()
                for manusia in u:
                    w2.sendText(manusia, (bctxt))
                
            elif "Bc:grup " in msg.text:
                bctxt = msg.text.replace("Bc:grup ", "")
                a = cl.getGroupIdsJoined()
                for manusia in a:
                    cl.sendText(manusia, (bctxt))
            
            elif "Bot:grup " in msg.text:
              if msg.from_ in admin:
                bctxt = msg.text.replace("Bot:grup ", "")
                b = ki.getGroupIdsJoined()
                for manusia in b:
                    ki.sendText(manusia, (bctxt))
                c = ki2.getGroupIdsJoined()
                for manusia in c:
                    ki2.sendText(manusia, (bctxt))
                d = ki3.getGroupIdsJoined()
                for manusia in d:
                    ki3.sendText(manusia, (bctxt))
                e = ki4.getGroupIdsJoined()
                for manusia in e:
                    ki4.sendText(manusia, (bctxt))
                f = ki5.getGroupIdsJoined()
                for manusia in f:
                    ki5.sendText(manusia, (bctxt))
                g = ki6.getGroupIdsJoined()
                for manusia in g:
                    ki6.sendText(manusia, (bctxt))
                h = ki7.getGroupIdsJoined()
                for manusia in h:
                    ki7.sendText(manusia, (bctxt))
                i = ki8.getGroupIdsJoined()
                for manusia in i:
                    ki8.sendText(manusia, (bctxt))
                j = ki9.getGroupIdsJoined()
                for manusia in j:
                    ki9.sendText(manusia, (bctxt))
                k = k1.getGroupIdsJoined()
                for manusia in k:
                    k1.sendText(manusia, (bctxt))
                l = k2.getGroupIdsJoined()
                for manusia in l:
                    k2.sendText(manusia, (bctxt))
                m = k3.getGroupIdsJoined()
                for manusia in m:
                    k3.sendText(manusia, (bctxt))
                n = k4.getGroupIdsJoined()
                for manusia in n:
                    k4.sendText(manusia, (bctxt))
                o = k5.getGroupIdsJoined()
                for manusia in o:
                    k5.sendText(manusia, (bctxt))
                p = k6.getGroupIdsJoined()
                for manusia in p:
                    k6.sendText(manusia, (bctxt))
                q = k7.getGroupIdsJoined()
                for manusia in q:
                    k7.sendText(manusia, (bctxt))
                r = k8.getGroupIdsJoined()
                for manusia in r:
                    k8.sendText(manusia, (bctxt))
                s = k9.getGroupIdsJoined()
                for manusia in s:
                    k9.sendText(manusia, (bctxt))
                t = w1.getGroupIdsJoined()
                for manusia in t:
                    w1.sendText(manusia, (bctxt))
                u = w2.getGroupIdsJoined()
                for manusia in u:
                    w2.sendText(manusia, (bctxt))

            elif "Spam " in msg.text:
                txt = msg.text.split(" ")
                jmlh = int(txt[2])
                teks = msg.text.replace("Spam "+str(txt[1])+" "+str(jmlh)+" ","")
                tulisan = jmlh * (teks+"\n")
                if txt[1] == "on":
                    if jmlh <= 100000:
                       for x in range(jmlh):
                           cl.sendText(msg.to, teks)
                    else:
                       cl.sendText(msg.to, "Out of Range!")
                elif txt[1] == "off":
                    if jmlh <= 100000:
                        cl.sendText(msg.to, tulisan)
                    else:
                        cl.sendText(msg.to, "Out Of Range!")

            elif msg.text in ["Sp","Speed","speed"]:
                start = time.time()
                cl.sendText(msg.to, "Wait....")
                elapsed_time = time.time() - start
                cl.sendText(msg.to, "%sseconds" % (elapsed_time))

            elif msg.text.lower() == 'me':
                msg.contentType = 13
                msg.contentMetadata = {'mid': mid}
                cl.sendMessage(msg)

            elif cms(msg.text,["creator","Creator"]):
                msg.contentType = 13
                msg.contentMetadata = {'mid': 'u63b477a73bc4dc8f08dd9a2ae572ad14'}
                cl.sendText(msg.to,"􀜁􀇔􏿿 My Creator 􀜁􀇔􏿿 ")
                cl.sendMessage(msg)
                cl.sendText(msg.to,"􀜁􀇔􏿿 Dont Kick out From group 􀜁􀇔􏿿 ")
            
            elif "Inviteme: " in msg.text:
              if msg.from_ in admin:
                gid = msg.text.replace("Inviteme: ","")
                if gid == "":
                    cl.sendText(msg.to,"Invalid group id")
                else:
                    try:
                        cl.findAndAddContactsByMid(msg.from_)
                        cl.inviteIntoGroup(gid,[msg.from_])
                    except:
                        cl.sendText(msg.to,"Mungkin saya tidak di dalaam grup itu")

            elif msg.text in ["Clear grup"]:
              if msg.from_ in admin:
                gid = cl.getGroupIdsJoined()
                gid = ki.getGroupIdsJoined()
                gid = ki2.getGroupIdsJoined()
                gid = ki3.getGroupIdsJoined()
                gid = ki4.getGroupIdsJoined()
                gid = ki5.getGroupIdsJoined()
                gid = ki6.getGroupIdsJoined()
                gid = ki7.getGroupIdsJoined()
                gid = ki8.getGroupIdsJoined()
                gid = ki9.getGroupIdsJoined()
                gid = k1.getGroupIdsJoined()
                gid = k2.getGroupIdsJoined()
                gid = k3.getGroupIdsJoined()
                gid = k4.getGroupIdsJoined()
                gid = k5.getGroupIdsJoined()
                gid = k6.getGroupIdsJoined()
                gid = k7.getGroupIdsJoined()
                gid = k8.getGroupIdsJoined()
                gid = k9.getGroupIdsJoined()
                gid = w1.getGroupIdsJoined()
                gid = w2.getGroupIdsJoined()
                gid = w3.getGroupIdsJoined()
                gid = w4.getGroupIdsJoined()
                gid = w5.getGroupIdsJoined()
                gid = w6.getGroupIdsJoined()
                gid = w7.getGroupIdsJoined()
                gid = w8.getGroupIdsJoined()
                gid = w9.getGroupIdsJoined()
                gid = l1.getGroupIdsJoined()
                gid = l2.getGroupIdsJoined()
                gid = l3.getGroupIdsJoined()
                gid = l4.getGroupIdsJoined()
                gid = l5.getGroupIdsJoined()
                for i in gid:
                    ki.leaveGroup(i)
                    ki2.leaveGroup(i)
                    ki3.leaveGroup(i)
                    ki4.leaveGroup(i)
                    ki5.leaveGroup(i)
                    ki6.leaveGroup(i)
                    ki7.leaveGroup(i)
                    ki8.leaveGroup(i)
                    ki9.leaveGroup(i)
                    k1.leaveGroup(i)
                    k2.leaveGroup(i)
                    k3.leaveGroup(i)
                    k4.leaveGroup(i)
                    k5.leaveGroup(i)
                    k6.leaveGroup(i)
                    k7.leaveGroup(i)
                    k8.leaveGroup(i)
                    k9.leaveGroup(i)
                    w1.leaveGroup(i)
                    w2.leaveGroup(i)
                    w3.leaveGroup(i)
                    w4.leaveGroup(i)
                    w5.leaveGroup(i)
                    w6.leaveGroup(i)
                    w7.leaveGroup(i)
                    w8.leaveGroup(i)
                    w9.leaveGroup(i)
                    l1.leaveGroup(i)
                    l2.leaveGroup(i)
                    l3.leaveGroup(i)
                    l4.leaveGroup(i)
                    l5.leaveGroup(i)
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"Bot Sudah Keluar Di semua grup")
                else:
                    cl.sendText(msg.to,"He declined all invitations")

            elif msg.text == "Ginfo":
                    group = cl.getGroup(msg.to)
                    try:
                        gCreator = group.creator.displayName
                    except:
                        gCreator = "Error"
                    md = "[Nama Grup : ]\n" + group.name + "\n\n[Id Grup : ]\n" + group.id + "\n\n[Pembuat Grup :]\n" + gCreator + "\n\n[Gambar Grup : ]\nhttp://dl.profile.line-cdn.net/" + group.pictureStatus
                    if group.preventJoinByTicket is False: md += "\n\nKode Url : Diizinkan"
                    else: md += "\n\nKode Url : Diblokir"
                    if group.invitee is None: md += "\nJumlah Member : " + str(len(group.members)) + " Orang" + "\nUndangan Yang Belum Diterima : 0 Orang"
                    else: md += "\nJumlah Member : " + str(len(group.members)) + " Orang" + "\nUndangan Yang Belum Diterima : " + str(len(group.invitee)) + " Orang"
                    cl.sendText(msg.to,md)
            
            elif msg.text == "Uni":
	            cl.sendText(msg.to,"Hai Perkenalkan.....\nNama saya siapa ya?\n\n1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1\n\nMakasih Sudah Dilihat :)\nJangan Dikick ampun mzz :v")
            
            elif "Music " in msg.text.lower():
	            songname = msg.text.lower().replace("Music ","")
	            params = {"songname":" songname"}
	            r = requests.get('https://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
	            data = r.text
	            data = json.loads(data)
	            for song in data:
		            cl.sendMessage(msg.to, song[4])
            
            elif "Youtube " in msg.text:
                 query = msg.text.replace("Youtube ","")
                 with requests.session() as s:
                     s.headers['user-agent'] = 'Mozilla/5.0'
                     url    = 'http://www.youtube.com/results'
                     params = {'search_query': query}
                     r    = s.get(url, params=params)
                     soup = BeautifulSoup(r.content, 'html5lib')
                     for a in soup.select('.yt-lockup-title > a[title]'):
                         if '&List' not in a['href']:
                               cl.sendText(msg.to,'http://www.youtube.com' + a['href'] + a['title'])
            
            elif "Block @" in msg.text:
                if msg.toType == 2:
                    print "[block] OK"
                    _name = msg.text.replace("Block @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                           targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to, "Not Found...")
                    else:
                        for target in targets:
                            try:
                               cl.blockContact(target)
                               cl.sendText(msg.to, "Success block contact~")
                            except Exception as e:
                               print e

            elif msg.text.lower() == 'blocklist':
                blockedlist = cl.getBlockedContactIds()
                cl.sendText(msg.to, "Please wait...")
                kontak = cl.getContacts(blockedlist)
                num=1
                msgs="User Blocked List\n"
                for ids in kontak:
                    msgs+="\n%i. %s" % (num, ids.displayName)
                    num=(num+1)
                msgs+="\n\nTotal %i blocked user(s)" % len(kontak)
                cl.sendText(msg.to, msgs)
            
            elif msg.text in ["Glist"]:
                gid = cl.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "[★] %s\n" % (cl.getGroup(i).name +"→["+str(len(cl.getGroup(i).members))+"]")
                cl.sendText(msg.to,"▒▒▓█[List Group]█▓▒▒\n"+ h +"Total Group =" +"["+str(len(gid))+"]")

            elif msg.text in ["Invite"]:
              if msg.from_ in admin:
                wait["ricoinvite"] = True
                random.choice(KAC).sendText(msg.to,"send contact 😉")
                
            elif ("Cek " in msg.text):
                   key = eval(msg.contentMetadata["MENTION"])
                   key1 = key["MENTIONEES"][0]["M"]
                   mi = cl.getContact(key1)
                   cl.sendText(msg.to,"Mid:" +  key1)

            elif "Mid @" in msg.text:
              if msg.from_ in admin:  
                _name = msg.text.replace("Mid @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                        ki.sendText(msg.to, g.mid)
                    else:
                        pass

            elif "Mymid" == msg.text:
                cl.sendText(msg.to,mid)

            elif msg.text in ["Link on"]:
              if msg.from_ in admin:  
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    group.preventJoinByTicket = False
                    cl.updateGroup(group)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"URL open")
                    else:
                        cl.sendText(msg.to,"URL open")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"It can not be used outside the group ô€œô€„‰👈")
                    else:
                        cl.sendText(msg.to,"Can not be used for groups other than ô€œô€„‰")
            
            elif msg.text in ["Link off"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    group.preventJoinByTicket = True
                    cl.updateGroup(group)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"URL close👈")
                    else:
                        cl.sendText(msg.to,"URL close👈")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"It can not be used outside the group  👈")
                    else:
                        cl.sendText(msg.to,"Can not be used for groups other than ô€œ")

            elif msg.text in ["url","Url"]:
                if msg.toType == 2:
                    g = cl.getGroup(msg.to)
                    if g.preventJoinByTicket == True:
                        g.preventJoinByTicket = False
                        cl.updateGroup(g)
                    gurl = cl.reissueGroupTicket(msg.to)
                    cl.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Hal ini tidak dapat digunakan di luar kelompok")
                    else:
                        cl.sendText(msg.to,"Tidak dapat digunakan untuk kelompok selain")

            elif msg.text in ["Gurl"]:
                if msg.toType == 2:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        cl.updateGroup(x)
                    gurl = cl.reissueGroupTicket(msg.to)
                    cl.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can't be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")

            elif msg.text in ["S1glist"]:
                gs = ki.getGroupIdsJoined()
                L = "☫『 Groups List 』☫\n"
                for i in gs:
                    L += "[⭐] %s \n" % (ki.getGroup(i).name + " | [ " + str(len (ki.getGroup(i).members)) + " ]")
                ki.sendText(msg.to, L + "\nTotal Group : [ " + str(len(gs)) +" ]")
            elif msg.text in ["S2glist"]:
                gs = ki2.getGroupIdsJoined()
                L = "☫『 Groups List 』☫\n"
                for i in gs:
                    L += "[⭐] %s \n" % (ki2.getGroup(i).name + " | [ " + str(len (ki2.getGroup(i).members)) + " ]")
                ki2.sendText(msg.to, L + "\nTotal Group : [ " + str(len(gs)) +" ]")
            elif msg.text in ["S3glist"]:
                gs = ki3.getGroupIdsJoined()
                L = "☫『 Groups List 』☫\n"
                for i in gs:
                    L += "[⭐] %s \n" % (ki3.getGroup(i).name + " | [ " + str(len (ki3.getGroup(i).members)) + " ]")
                ki3.sendText(msg.to, L + "\nTotal Group : [ " + str(len(gs)) +" ]")
            elif msg.text in ["S4glist"]:
                gs = ki4.getGroupIdsJoined()
                L = "☫『 Groups List 』☫\n"
                for i in gs:
                    L += "[⭐] %s \n" % (ki4.getGroup(i).name + " | [ " + str(len (ki4.getGroup(i).members)) + " ]")
                ki4.sendText(msg.to, L + "\nTotal Group : [ " + str(len(gs)) +" ]")
            elif msg.text in ["S5glist"]:
                gs = ki5.getGroupIdsJoined()
                L = "☫『 Groups List 』☫\n"
                for i in gs:
                    L += "[⭐] %s \n" % (ki5.getGroup(i).name + " | [ " + str(len (ki5.getGroup(i).members)) + " ]")
                ki5.sendText(msg.to, L + "\nTotal Group : [ " + str(len(gs)) +" ]")
            elif msg.text in ["S6glist"]:
                gs = ki6.getGroupIdsJoined()
                L = "☫『 Groups List 』☫\n"
                for i in gs:
                    L += "[⭐] %s \n" % (ki6.getGroup(i).name + " | [ " + str(len (ki6.getGroup(i).members)) + " ]")
                ki6.sendText(msg.to, L + "\nTotal Group : [ " + str(len(gs)) +" ]")
            elif msg.text in ["S7glist"]:
                gs = ki7.getGroupIdsJoined()
                L = "☫『 Groups List 』☫\n"
                for i in gs:
                    L += "[⭐] %s \n" % (ki7.getGroup(i).name + " | [ " + str(len (ki7.getGroup(i).members)) + " ]")
                ki7.sendText(msg.to, L + "\nTotal Group : [ " + str(len(gs)) +" ]")
            elif msg.text in ["S8glist"]:
                gs = ki8.getGroupIdsJoined()
                L = "☫『 Groups List 』☫\n"
                for i in gs:
                    L += "[⭐] %s \n" % (ki8.getGroup(i).name + " | [ " + str(len (ki8.getGroup(i).members)) + " ]")
                ki8.sendText(msg.to, L + "\nTotal Group : [ " + str(len(gs)) +" ]")
            elif msg.text in ["S9glist"]:
                gs = ki9.getGroupIdsJoined()
                L = "☫『 Groups List 』☫\n"
                for i in gs:
                    L += "[⭐] %s \n" % (ki9.getGroup(i).name + " | [ " + str(len (ki9.getGroup(i).members)) + " ]")
                ki9.sendText(msg.to, L + "\nTotal Group : [ " + str(len(gs)) +" ]")
            elif msg.text in ["S10glist"]:
                gs = k1.getGroupIdsJoined()
                L = "☫『 Groups List 』☫\n"
                for i in gs:
                    L += "[⭐] %s \n" % (k1.getGroup(i).name + " | [ " + str(len (k1.getGroup(i).members)) + " ]")
                k1.sendText(msg.to, L + "\nTotal Group : [ " + str(len(gs)) +" ]")
            elif msg.text in ["S11glist"]:
                gs = k2.getGroupIdsJoined()
                L = "☫『 Groups List 』☫\n"
                for i in gs:
                    L += "[⭐] %s \n" % (k2.getGroup(i).name + " | [ " + str(len (k2.getGroup(i).members)) + " ]")
                k2.sendText(msg.to, L + "\nTotal Group : [ " + str(len(gs)) +" ]")
            elif msg.text in ["S12glist"]:
                gs = k3.getGroupIdsJoined()
                L = "☫『 Groups List 』☫\n"
                for i in gs:
                    L += "[⭐] %s \n" % (k3.getGroup(i).name + " | [ " + str(len (k3.getGroup(i).members)) + " ]")
                k3.sendText(msg.to, L + "\nTotal Group : [ " + str(len(gs)) +" ]")
            elif msg.text in ["S13glist"]:
                gs = k4.getGroupIdsJoined()
                L = "☫『 Groups List 』☫\n"
                for i in gs:
                    L += "[⭐] %s \n" % (k4.getGroup(i).name + " | [ " + str(len (k4.getGroup(i).members)) + " ]")
                k4.sendText(msg.to, L + "\nTotal Group : [ " + str(len(gs)) +" ]")
            elif msg.text in ["S14glist"]:
                gs = k5.getGroupIdsJoined()
                L = "☫『 Groups List 』☫\n"
                for i in gs:
                    L += "[⭐] %s \n" % (k5.getGroup(i).name + " | [ " + str(len (k5.getGroup(i).members)) + " ]")
                k5.sendText(msg.to, L + "\nTotal Group : [ " + str(len(gs)) +" ]")
            elif msg.text in ["S15glist"]:
                gs = k6.getGroupIdsJoined()
                L = "☫『 Groups List 』☫\n"
                for i in gs:
                    L += "[⭐] %s \n" % (k6.getGroup(i).name + " | [ " + str(len (k6.getGroup(i).members)) + " ]")
                k6.sendText(msg.to, L + "\nTotal Group : [ " + str(len(gs)) +" ]")
            elif msg.text in ["S16glist"]:
                gs = k7.getGroupIdsJoined()
                L = "☫『 Groups List 』☫\n"
                for i in gs:
                    L += "[⭐] %s \n" % (k7.getGroup(i).name + " | [ " + str(len (k7.getGroup(i).members)) + " ]")
                k7.sendText(msg.to, L + "\nTotal Group : [ " + str(len(gs)) +" ]")
            elif msg.text in ["S17glist"]:
                gs = k8.getGroupIdsJoined()
                L = "☫『 Groups List 』☫\n"
                for i in gs:
                    L += "[⭐] %s \n" % (k8.getGroup(i).name + " | [ " + str(len (k8.getGroup(i).members)) + " ]")
                k8.sendText(msg.to, L + "\nTotal Group : [ " + str(len(gs)) +" ]")
            elif msg.text in ["S18glist"]:
                gs = k9.getGroupIdsJoined()
                L = "☫『 Groups List 』☫\n"
                for i in gs:
                    L += "[⭐] %s \n" % (k9.getGroup(i).name + " | [ " + str(len (k9.getGroup(i).members)) + " ]")
                k9.sendText(msg.to, L + "\nTotal Group : [ " + str(len(gs)) +" ]")
            elif msg.text in ["S19glist"]:
                gs = w1.getGroupIdsJoined()
                L = "☫『 Groups List 』☫\n"
                for i in gs:
                    L += "[⭐] %s \n" % (w1.getGroup(i).name + " | [ " + str(len (w1.getGroup(i).members)) + " ]")
                w1.sendText(msg.to, L + "\nTotal Group : [ " + str(len(gs)) +" ]")
            elif msg.text in ["S20glist"]:
                gs = w2.getGroupIdsJoined()
                L = "☫『 Groups List 』☫\n"
                for i in gs:
                    L += "[⭐] %s \n" % (w2.getGroup(i).name + " | [ " + str(len (w2.getGroup(i).members)) + " ]")
                w2.sendText(msg.to, L + "\nTotal Group : [ " + str(len(gs)) +" ]")
                    
#-----------------------------------------------------------
            elif "#leave" in msg.text:
                try:
                    import sys
                    sys.exit()
                except:
                    pass
#-----------------------------------------------------------
            elif msg.text in ["Bot sp","Bot speed"]:
                start = time.time()
                ki.sendText(msg.to, "My speed....")
                elapsed_time = time.time() - start
            
            elif msg.text.lower() == 'responsname':
                profile = ki.getProfile()
                text = profile.displayName
                ki.sendText(msg.to, text)
                profile = ki2.getProfile()
                text = profile.displayName
                ki2.sendText(msg.to, text)
                profile = ki3.getProfile()
                text = profile.displayName
                ki3.sendText(msg.to, text)
                profile = ki4.getProfile()
                text = profile.displayName
                ki4.sendText(msg.to, text)

#------------------------------------------------------------------	
            elif "Steal home @" in msg.text:            
                print "[Command]dp executing"
                _name = msg.text.replace("Steal home @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    ki.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = cl.getContact(target)
                            cu = cl.channel.getCover(target)
                            path = str(cu)
                            cl.sendImageWithURL(msg.to, path)
                        except:
                            pass
                print "[Command]dp executed"			
 #------------------------------------------------------------------
            elif "Blacklist @" in msg.text:
              if msg.from_ in admin:
                if msg.toType == 2:
                    print "[BL]ok"
                    _name = msg.text.replace("Blacklist @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Not found.")
                    else:
                        for target in targets:
                            try:
                                wait["blacklist"][target] = True
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                cl.sendText(msg.to,"Success Boss")
                            except:
                                cl.sendText(msg.to,"Error")
                                
            elif "Blacklist all" in msg.text:
              if msg.from_ in admin:
                  if msg.toType == 2:
                       print "ok"
                       _name = msg.text.replace("Blacklist all","")
                       gs = cl.getGroup(msg.to)
                       cl.sendText(msg.to,"Semua Telah Di Hapus")
                       targets = []
                       for g in gs.members:
                           if _name in g.displayName:
                                targets.append(g.mid)
                       if targets == []:
                            cl.sendText(msg.to,"Maaf")
                       else:
                           for target in targets:
                               if not target in Bots:
                                   try:
                                       wait["blacklist"][target] = True
                                       f=codecs.open('st2__b.json','w','utf-8')
                                       json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                       cl.sendText(msg.to,"Success Boss")
                                   except:
                                       cl.sentText(msg.to,"Berhasil Dihapus")
            
            elif "Whitelist @" in msg.text:
              if msg.from_ in admin:
                if msg.toType == 2:
                    print "[WL]ok"
                    _name = msg.text.replace("Whitelist @","")
                    _nametarget = _name.rstrip('  ')
                    gs = ki.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Not found.")
                    else:
                        for target in targets:
                            try:
                                del wait["blacklist"][target]
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                cl.sendText(msg.to,"Success Boss")
                            except:
                                cl.sendText(msg.to,"There was no blacklist user")

            elif "Blacklist: " in msg.text:       
             if msg.from_ in admin:           
                       nk0 = msg.text.replace("Blacklist: ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    wait["blacklist"][target] = True
                                    f=codecs.open('st2__b.json','w','utf-8')
                                    json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                    cl.sendText(msg.to,"Target Locked")
                                except:
                                    cl.sendText(msg.to,"Error")

            elif "Whitelist: " in msg.text:             
              if msg.from_ in admin:     
                       nk0 = msg.text.replace("Whitelist: ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    del wait["blacklist"][target]
                                    f=codecs.open('st2__b.json','w','utf-8')
                                    json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                    cl.sendText(msg.to,"Target Unlocked")
                                except:
                                    cl.sendText(msg.to,"Error")

            elif msg.text in ["Clear ban"]:
              if msg.from_ in admin:
                wait["blacklist"] = {}
                cl.sendText(msg.to,"clear")
            elif msg.text in ["Whitelist"]:
              if msg.from_ in admin:
                wait["wblacklist"] = True
                cl.sendText(msg.to,"send contact to ban")
            
            elif msg.text in ["Blacklist"]:
              if msg.from_ in admin:
                wait["dblacklist"] = True
                cl.sendText(msg.to,"send contact to ban")
            
            elif msg.text in ["Banlist"]:
              if msg.from_ in admin:
                if wait["blacklist"] == {}:
                    cl.sendText(msg.to,"Nothing 􀨁􀄻double thumbs up􏿿")
                else:
                    cl.sendText(msg.to,"Daftar Banlist􏿿")
                    mc = "[⎈]Blacklist [⎈]\n"
                    for mi_d in wait["blacklist"]:
                        mc += "[✗] " + cl.getContact(mi_d).displayName + " \n"
                    cl.sendText(msg.to, mc + "")
            elif msg.text in ["Ban cek","Cekban"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    cocoa = "[⎈]Mid Blacklist [⎈]"
                    for mm in matched_list:
                        cocoa += "\n" + mm + "\n"
                    cl.sendText(msg.to,cocoa + "")
            elif msg.text.lower() == 'kill':
              if msg.from_ in admin:
                if msg.toType == 2:
                    group = ki.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        ki.sendText(msg.to,"Tidak ada Daftar Blacklist")
                        return
                    for jj in matched_list:
                        try:
                            cl.kickoutFromGroup(msg.to,[jj])
                            ki.kickoutFromGroup(msg.to,[jj])
                            ki2.kickoutFromGroup(msg.to,[jj])
                            ki3.kickoutFromGroup(msg.to,[jj])
                            ki4.kickoutFromGroup(msg.to,[jj])
                            ki5.kickoutFromGroup(msg.to,[jj])
                            ki6.kickoutFromGroup(msg.to,[jj])
                            ki7.kickoutFromGroup(msg.to,[jj])
                            ki8.kickoutFromGroup(msg.to,[jj])
                            ki9.kickoutFromGroup(msg.to,[jj])
                            k1.kickoutFromGroup(msg.to,[jj])
                            k2.kickoutFromGroup(msg.to,[jj])
                            k3.kickoutFromGroup(msg.to,[jj])
                            k4.kickoutFromGroup(msg.to,[jj])
                            k5.kickoutFromGroup(msg.to,[jj])
                            print (msg.to,[jj])
                        except:
                            pass
            elif "Nuke" in msg.text:
              if msg.from_ in admin:
                if msg.toType == 2:
                    print "ok"
                    _name = msg.text.replace("Nuke","")
                    gs = ki.getGroup(msg.to)
                    gs = ki2.getGroup(msg.to)
                    gs = ki3.getGroup(msg.to)
                    gs = ki4.getGroup(msg.to)
                    gs = ki5.getGroup(msg.to)
                    gs = ki6.getGroup(msg.to)
                    gs = ki7.getGroup(msg.to)
                    gs = ki8.getGroup(msg.to)
                    gs = ki9.getGroup(msg.to)
                    gs = w1.getGroup(msg.to)
                    gs = w2etGroup(msg.to)
                    gs = w3.getGroup(msg.to)
                    gs = w4.getGroup(msg.to)
                    gs = w5.getGroup(msg.to)
                    cl.sendText(msg.to,"Masih Mauko Sundala")
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Tidak ada Member")
                        ki2.sendText(msg.to,"Nothing Bosqu")
                    else:
                        for target in targets:
                          if not target in Bots:
                            try:
                                klist=[cl,ki,ki2,ki3,ki4,ki5,ki6,ki7,ki8,ki9,w1,w2,w3,w4,w5]
                                kicker=random.choice(klist)
                                kicker.kickoutFromGroup(msg.to,[target])
                                print (msg.to,[g.mid])
                            except:
                                ki.sendText(msg,to,"Hahaha")
                                ki2.sendText(msg,to,"Fakyu Sundala")

#-----------------------------------------------

#-----------------------------------------------
            elif msg.text.lower() == ["1"]:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki2.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki3.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki4.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki5.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki6.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki7.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki8.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki9.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        k1.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        k2.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        k3.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        k4.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        k5.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        k6.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        k7.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        k8.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        k9.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        w1.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        w2.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        random.choice(KAC).updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        random.choice(KAC).updateGroup(G)
                       
#-----------------------------------------------
            elif msg.text in ["Sayang","Kuy","All join","Minna"]:
                if msg.from_ in admsa:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)
                        ki2.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)
                        ki3.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)
                        ki4.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)
                        ki5.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)
                        ki6.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)
                        ki7.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)
                        ki8.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)
                        ki9.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)
                        k1.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)
                        k2.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)
                        k3.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)
                        k4.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)
                        k5.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)
                        k6.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        k7.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        k8.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        k9.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        w1.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        w2.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        w3.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        w4.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        w5.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        w6.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        w7.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        w8.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        w9.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        l1.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        l2.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        l3.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        l4.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        l5.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        G = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki.updateGroup(G)

            elif msg.text.lower() == 'Hello':
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki2.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki3.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki4.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki5.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki6.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki7.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki8.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki9.acceptGroupInvitationByTicket(msg.to,Ticket)
                        k1.acceptGroupInvitationByTicket(msg.to,Ticket)
                        k2.acceptGroupInvitationByTicket(msg.to,Ticket)
                        k3.acceptGroupInvitationByTicket(msg.to,Ticket)
                        k4.acceptGroupInvitationByTicket(msg.to,Ticket)
                        k5.acceptGroupInvitationByTicket(msg.to,Ticket)
                        k6.acceptGroupInvitationByTicket(msg.to,Ticket)
                        k7.acceptGroupInvitationByTicket(msg.to,Ticket)
                        k8.acceptGroupInvitationByTicket(msg.to,Ticket)
                        k9.acceptGroupInvitationByTicket(msg.to,Ticket)
                        w1.acceptGroupInvitationByTicket(msg.to,Ticket)
                        w2.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki.updateGroup(G)
#-----------------------------------------------
            elif "Ciel1 in" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki.updateGroup(G)
#-----------------------------------------------
            elif "Ciel2 in" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki2.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki2.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki2.updateGroup(G)
#-----------------------------------------------
            elif "Ciel3 in" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki3.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki2.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki2.updateGroup(G)
#-----------------------------------------------
            elif "Ciel4 in" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki4.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki3.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki3.updateGroup(G)
#-----------------------------------------------
            elif "Ciel5 in" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki5.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki5.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki5.updateGroup(G)
#-----------------------------------------------
            elif "Ciel6 in" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki6.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki6.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki6.updateGroup(G)
#-----------------------------------------------
            elif "Ciel7 in" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki7.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki7.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki7.updateGroup(G)
#-----------------------------------------------
            elif "Ciel8 in" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki8.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki8.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki8.updateGroup(G)
#-----------------------------------------------
            elif "Ciel9 in" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki9.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki9.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki9.updateGroup(G)
#-----------------------------------------------
            elif "Ciel10 in" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        k1.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        k1.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        k1.updateGroup(G)
#-----------------------------------------------
            elif "Ciel in" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        k2.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        k2.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        k2.updateGroup(G)
#-----------------------------------------------
            elif "Ciel in" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        k3.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        k3.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        k3.updateGroup(G)
#-----------------------------------------------
            elif "Ciel13 in" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        k4.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        k4.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        k4.updateGroup(G)
#-----------------------------------------------
            elif "Ciel14 in" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        k5.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        k5.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        k5.updateGroup(G)
#-----------------------------------------------
            elif "Ciel15 in" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        k6.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        k6.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        k6.updateGroup(G)
#-----------------------------------------------
            elif "Ciel16 in" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.gtGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        k7.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        k7.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        k7.updateGroup(G)
#-----------------------------------------------
            elif "Ciel17 in" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        k8.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        k8.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        k8.updateGroup(G)
#-----------------------------------------------
            elif "Ciel18 in" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        k9.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        k9.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        k9.updateGroup(G)
#-----------------------------------------------
            elif "Ciel19 in" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        w1.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        w1.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        w1.updateGroup(G)
#-----------------------------------------------
            elif "Ciel20 in" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        w2.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        w2.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        w2.updateGroup(G)
#-----------------------------------------------
            elif msg.text in ["Bye minna",",","Good bye","Sayonara"]:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        cl.sendText(msg.to,"Bye Bye minna😘 "  +  str(ginfo.name)  + "")
                        ki.leaveGroup(msg.to)
                        ki2.leaveGroup(msg.to)
                        ki3.leaveGroup(msg.to)
                        ki4.leaveGroup(msg.to)
                        ki5.leaveGroup(msg.to)
                        ki6.leaveGroup(msg.to)
                        ki7.leaveGroup(msg.to)
                        ki8.leaveGroup(msg.to)
                        ki9.leaveGroup(msg.to)
                        k1.leaveGroup(msg.to)
                        k2.leaveGroup(msg.to)
                        k3.leaveGroup(msg.to)
                        k4.leaveGroup(msg.to)
                        k5.leaveGroup(msg.to)
                        k6.leaveGroup(msg.to)
                        k7.leaveGroup(msg.to)
                        k8.leaveGroup(msg.to)
                        k9.leaveGroup(msg.to)
                        w1.leaveGroup(msg.to)
                        w2.leaveGroup(msg.to)
                        w3.leaveGroup(msg.to)
                        w4.leaveGroup(msg.to)
                        w5.leaveGroup(msg.to)
                        w6.leaveGroup(msg.to)
                        w7.leaveGroup(msg.to)
                        w8.leaveGroup(msg.to)
                        w9.leaveGroup(msg.to)
                        l1.leaveGroup(msg.to)
                        l2.leaveGroup(msg.to)
                        l3.leaveGroup(msg.to)
                        l4.leaveGroup(msg.to)
                        l5.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "Ciel1 bye" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "Ciel2 bye" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki2.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "Ciel3 bye" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki3.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "Ciel4 bye" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki4.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "Ciel5 bye" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki5.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "Ciel6 bye" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki6.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "Ciel7 bye" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki7.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "Ciel8 bye" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki8.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "Ciel9 bye" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki9.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "Ciel0 bye" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        k1.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "Ciel11 bye" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        k2.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "CielCiel12 bye" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        k3.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "Ciel13 bye" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        k4.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "Ciel14 bye" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        k5.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "Ciel15 bye" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        k6.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "Ciel16 bye" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        k7.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "Ciel17 bye" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        k8.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "Ciel18 bye" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        k9.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "Ciel19 bye" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        w1.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "Ciel20 bye" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        w2.leaveGroup(msg.to)
                    except:
                        pass

            elif msg.text in ["Welcome","wc","welcome","Wc"]:
                ginfo = cl.getGroup(msg.to)
                cl.sendText(msg.to,"Selamat Datang Di Grup " + str(ginfo.name))
                cl.sendText(msg.to,"Owner Grup " + str(ginfo.name) + " :\n" + ginfo.creator.displayName )
#----------------------------------------------- 
#-----------------------------------------------
        if op.type == 19:
            try:
                if op.param3 in mid:
                    if op.param2 in kimid:
                        G = ki.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                    else:
                        G = ki.getGroup(op.param1)
                        
                        ki.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                        ki.updateGroup(G)
                        wait["blacklist"][op.param2] = True

                       
                        
                elif op.param3 in kimid:
                    if op.param2 in ki2mid:
                        G = ki2.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki2.updateGroup(G)
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki2.updateGroup(G)
                    else:
                        G = ki2.getGroup(op.param1)

                        ki2.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki2.updateGroup(G)
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)


                elif op.param3 in ki3mid:
                    if op.param2 in ki2mid:
                        G = ki2.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki2.updateGroup(G)
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki2.updateGroup(G)
                    else:
                        G = cl.getGroup(op.param1)

                        
                        ki2.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki2.updateGroup(G)
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki2.updateGroup(G)
                        
                elif op.param3 in ki2mid:
                    if op.param2 in ki3mid:
                        G = ki3.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki3.updateGroup(G)
                        Ticket = ki3.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki3.updateGroup(G)
                    else:
                        G = cl.getGroup(op.param1)

                        
                        ki3.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki3.updateGroup(G)
                        Ticket = ki3.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki3.updateGroup(G)
                        
                elif op.param3 in ki4mid:
                    if op.param2 in ki5mid:
                        G = ki5.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki5.updateGroup(G)
                        Ticket = ki5.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                    else:
                        G = ki5.getGroup(op.param1)

                        
                        ki5.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki5.updateGroup(G)
                        Ticket = ki5.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki5.updateGroup(G)

                elif op.param3 in ki5mid:
                    if op.param2 in ki4mid:
                        G = ki4.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki4.updateGroup(G)
                        Ticket = ki4.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki4.updateGroup(G)
                    else:
                        G = ki4.getGroup(op.param1)

                        
                        ki4.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki4.updateGroup(G)
                        Ticket = ki4.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki4.updateGroup(G)

                elif op.param3 in ki6mid:
                    if op.param2 in ki5mid:
                        G = ki5.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki5.updateGroup(G)
                        Ticket = ki5.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki5.updateGroup(G)
                    else:
                        G = ki5.getGroup(op.param1)

                        
                        ki5.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki5.updateGroup(G)
                        Ticket = ki5.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki5.updateGroup(G)

                elif op.param3 in ki7mid:
                    if op.param2 in ki6mid:
                        G = ki6.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki6.updateGroup(G)
                        Ticket = ki6.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki6.updateGroup(G)
                    else:
                        G = ki6.getGroup(op.param1)

                        
                        ki6.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki6.updateGroup(G)
                        Ticket = ki6.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki6.updateGroup(G)

                elif op.param3 in ki6mid:
                    if op.param2 in ki7mid:
                        G = ki7.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki7.updateGroup(G)
                        Ticket = ki7.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki7.updateGroup(G)
                    else:
                        G = ki7.getGroup(op.param1)

                        
                        ki7.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki7.updateGroup(G)
                        Ticket = ki7.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki7.updateGroup(G)

            	elif op.param3 in ki8mid:
                    if op.param2 in ki7mid:
                        G = ki7.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki7.updateGroup(G)
                        Ticket = ki7.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki7.updateGroup(G)
                    else:
                        G = ki7.getGroup(op.param1)

                        
                        ki7.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki7.updateGroup(G)
                        Ticket = ki7.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki7.updateGroup(G)

                elif op.param3 in ki7mid:
                    if op.param2 in ki8mid:
                        G = ki8.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki8.updateGroup(G)
                        Ticket = ki8.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki8.updateGroup(G)
                    else:
                        G = ki8.getGroup(op.param1)

                        
                        ki8.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki8.updateGroup(G)
                        Ticket = ki8.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki8.updateGroup(G)

                elif op.param3 in ki9mid:
                    if op.param2 in ki8mid:
                        G = ki8.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki8.updateGroup(G)
                        Ticket = ki8.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki8.updateGroup(G)
                    else:
                        G = ki8.getGroup(op.param1)

                        
                        ki8.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki8.updateGroup(G)
                        Ticket = ki8.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki8.updateGroup(G)

                elif op.param3 in ki8mid:
                    if op.param2 in ki9mid:
                        G = ki9.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki9.updateGroup(G)
                        Ticket = ki9.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki9.updateGroup(G)
                    else:
                        G = ki9.getGroup(op.param1)

                        
                        ki9.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki9.updateGroup(G)
                        Ticket = ki9.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki9.updateGroup(G)

                elif op.param3 in k1mid:
                    if op.param2 in ki9mid:
                        G = ki9.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki9.updateGroup(G)
                        Ticket = ki9.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki9.updateGroup(G)
                    else:
                        G = ki9.getGroup(op.param1)

                        
                        ki9.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki9.updateGroup(G)
                        Ticket = ki9.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki9.updateGroup(G)

                elif op.param3 in ki9mid:
                    if op.param2 in k1mid:
                        G = k1.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        k1.updateGroup(G)
                        Ticket = k1.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        k1.updateGroup(G)
                    else:
                        G = k1.getGroup(op.param1)

                        
                        k1.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        k1.updateGroup(G)
                        Ticket = k1.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        k1.updateGroup(G)

                elif op.param3 in k1mid:
                    if op.param2 in k2mid:
                        G = k2.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        k2.updateGroup(G)
                        Ticket = k2.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        k2.updateGroup(G)
                    else:
                        G = k2.getGroup(op.param1)

                        
                        k2.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        k2.updateGroup(G)
                        Ticket = k2.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        k2.updateGroup(G)

                elif op.param3 in k3mid:
                    if op.param2 in k2mid:
                        G = k2.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        k2.updateGroup(G)
                        Ticket = k2.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        k2.updateGroup(G)
                    else:
                        G = k2.getGroup(op.param1)

                        
                        k2.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        k2.updateGroup(G)
                        Ticket = k2.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        k2.updateGroup(G)

                elif op.param3 in k4mid:
                    if op.param2 in k3mid:
                        G = k3.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        k3.updateGroup(G)
                        Ticket = k3.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        k3.updateGroup(G)
                    else:
                        G = k3.getGroup(op.param1)

                        
                        k3.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        k3.updateGroup(G)
                        Ticket = k3.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        k3.updateGroup(G)

                elif op.param3 in k3mid:
                    if op.param2 in k4mid:
                        G = k4.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        k4.updateGroup(G)
                        Ticket = k4.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        k4.updateGroup(G)
                    else:
                        G = k4.getGroup(op.param1)

                        
                        k4.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        k4.updateGroup(G)
                        Ticket = k4.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        k4.updateGroup(G)

                elif op.param3 in k5mid:
                    if op.param2 in k4mid:
                        G = k4.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        k4.updateGroup(G)
                        Ticket = k4.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        k4.updateGroup(G)
                    else:
                        G = k4.getGroup(op.param1)

                        
                        k4.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        k4.updateGroup(G)
                        Ticket = k4.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        k4.updateGroup(G)

                elif op.param3 in k4mid:
                    if op.param2 in k5mid:
                        G = k5.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        k5.updateGroup(G)
                        Ticket = k5.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        k5.updateGroup(G)
                    else:
                        G = k5.getGroup(op.param1)

                        
                        k5.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        k5.updateGroup(G)
                        Ticket = k5.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        k5.updateGroup(G)

                elif op.param3 in k5mid:
                    if op.param2 in k6mid:
                        G = k6.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        k6.updateGroup(G)
                        Ticket = k6.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        k6.updateGroup(G)
                    else:
                        G = k6.getGroup(op.param1)

                        
                        k6.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        k6.updateGroup(G)
                        Ticket = k6.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        k6.updateGroup(G)

                elif op.param3 in k6mid:
                    if op.param2 in k7mid:
                        G = k7.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        k7.updateGroup(G)
                        Ticket = k7.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        k7.updateGroup(G)
                    else:
                        G = k7.getGroup(op.param1)

                        
                        k7.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        k7.updateGroup(G)
                        Ticket = k7.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        k7.updateGroup(G)

                elif op.param3 in k7mid:
                    if op.param2 in k8mid:
                        G = k8.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        k8.updateGroup(G)
                        Ticket = k8.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        k8.updateGroup(G)
                    else:
                        G = k8.getGroup(op.param1)

                        
                        k8.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        k8.updateGroup(G)
                        Ticket = k8.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        k8.updateGroup(G)

                elif op.param3 in k8mid:
                    if op.param2 in k9mid:
                        G = k9.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        k9.updateGroup(G)
                        Ticket = k9.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        k9.updateGroup(G)
                    else:
                        G = k9.getGroup(op.param1)

                        
                        k9.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        k9.updateGroup(G)
                        Ticket = k9.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        k9.updateGroup(G)

                elif op.param3 in k9mid:
                    if op.param2 in w1mid:
                        G = w1.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        w1.updateGroup(G)
                        Ticket = w1.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        w1.updateGroup(G)
                    else:
                        G = w1.getGroup(op.param1)

                        
                        w1.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        w1.updateGroup(G)
                        Ticket = w1.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        w1.updateGroup(G)

                elif op.param3 in w1mid:
                    if op.param2 in w2mid:
                        G = w2.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        w2.updateGroup(G)
                        Ticket = w2.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        w2.updateGroup(G)
                    else:
                        G = w2.getGroup(op.param1)

                        
                        w2.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        w2.updateGroup(G)
                        Ticket = w2.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        w2.updateGroup(G)
                        
                elif op.param3 in w2mid:
                    if op.param2 in w3mid:
                        G = w3.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        w3.updateGroup(G)
                        Ticket = w3.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        w3.updateGroup(G)
                    else:
                        G = w3.getGroup(op.param1)

                        
                        w3.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        w3.updateGroup(G)
                        Ticket = w3.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        w3.updateGroup(G)
                        
                elif op.param3 in w3mid:
                    if op.param2 in w4mid:
                        G = w4.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        w4.updateGroup(G)
                        Ticket = w4.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        w4.updateGroup(G)
                    else:
                        G = w4.getGroup(op.param1)

                        
                        w4.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        w4.updateGroup(G)
                        Ticket = w4.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        w4.updateGroup(G)
                        
                elif op.param3 in w4mid:
                    if op.param2 in w5mid:
                        G = w5.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        w5.updateGroup(G)
                        Ticket = w5.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        w5.updateGroup(G)
                    else:
                        G = w5.getGroup(op.param1)

                        
                        w5.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        w5.updateGroup(G)
                        Ticket = w5.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        w5.updateGroup(G)
                        
                elif op.param3 in w5mid:
                    if op.param2 in w6mid:
                        G = w6.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        w6.updateGroup(G)
                        Ticket = w6.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        w6.updateGroup(G)
                    else:
                        G = w6.getGroup(op.param1)

                        
                        w6.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        w6.updateGroup(G)
                        Ticket = w6.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        w6.updateGroup(G)
                        
                elif op.param3 in w6mid:
                    if op.param2 in w7mid:
                        G = w7.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        w7.updateGroup(G)
                        Ticket = w7.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        w7.updateGroup(G)
                    else:
                        G = w7.getGroup(op.param1)

                        
                        w7.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        w7.updateGroup(G)
                        Ticket = w7.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        w7.updateGroup(G)
                        
                elif op.param3 in w7mid:
                    if op.param2 in w8mid:
                        G = w8.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        w8.updateGroup(G)
                        Ticket = w8.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        w8.updateGroup(G)
                    else:
                        G = w8.getGroup(op.param1)

                        
                        w8.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        w8.updateGroup(G)
                        Ticket = w8.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        w8.updateGroup(G)
                        
                elif op.param3 in w8mid:
                    if op.param2 in w9mid:
                        G = w9.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        w9.updateGroup(G)
                        Ticket = w9.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        w9.updateGroup(G)
                    else:
                        G = w9.getGroup(op.param1)

                        
                        w9.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        w9.updateGroup(G)
                        Ticket = w9.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        w9.updateGroup(G)
                        
                elif op.param3 in w9mid:
                    if op.param2 in l1mid:
                        G = l1.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        l1.updateGroup(G)
                        Ticket = l1.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        l1.updateGroup(G)
                    else:
                        G = l1.getGroup(op.param1)

                        
                        l1.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        l1.updateGroup(G)
                        Ticket = l1.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        l1.updateGroup(G)
                        
                elif op.param3 in l1mid:
                    if op.param2 in l2mid:
                        G = l2.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        l2.updateGroup(G)
                        Ticket = l2.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        l2.updateGroup(G)
                    else:
                        G = l2.getGroup(op.param1)

                        
                        l2.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        l2.updateGroup(G)
                        Ticket = l2.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        l2.updateGroup(G)
                        
                elif op.param3 in l2mid:
                    if op.param2 in l3mid:
                        G = l3.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        l3.updateGroup(G)
                        Ticket = l3.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        l3.updateGroup(G)
                    else:
                        G = l3.getGroup(op.param1)

                        
                        l3.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        l3.updateGroup(G)
                        Ticket = l3.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        l3.updateGroup(G)
                        
                elif op.param3 in l3mid:
                    if op.param2 in l4mid:
                        G = l4.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        l4.updateGroup(G)
                        Ticket = l4.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        l4.updateGroup(G)
                    else:
                        G = l4.getGroup(op.param1)

                        
                        l4.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        l4.updateGroup(G)
                        Ticket = l4.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        l4.updateGroup(G)
                        
                elif op.param3 in l4mid:
                    if op.param2 in l5mid:
                        G = l5.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        l5.updateGroup(G)
                        Ticket = l5.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        l5.updateGroup(G)
                    else:
                        G = l5.getGroup(op.param1)

                        
                        l5.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        l5.updateGroup(G)
                        Ticket = l5.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        l5.updateGroup(G)
            except:
                pass

	if op.type == 17:
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
	    if wait["protect"] == True:
		if wait["blacklist"][op.param2] == True:
		   try:
			random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
			G = random.choice(KAC).getGroup(op.param1)
			G.preventJoinByTicket = True
			ki4.updateGroup(G)
#			random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
		   except:
#			pass
			try:
			    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
			    G = random.choice(KAC).getGroup(op.param1)
			    G.preventJoinByTicket = True
			    random.choice(KAC).updateGroup(G)
#			    random.choice(KAK).kickoutFromGroup(op.param1,[op.param2])
			except:
			    pass
		elif op.param2 not in admin + Bots:
		    random.choice(KAC).sendText(op.param1,"Welcome. Don't Play Bots. I can kick you!")
	    else:
		pass
	if op.type == 19:
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
		elif wait["protect"] == True:
		    wait ["blacklist"][op.param2] = True
		    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
		else:
		    cl.sendText(op.param1,"")
	    else:
		cl.sendText(op.param1,"")
	if op.type == 13:
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
		elif wait["inviteprotect"] == True:
		    wait ["blacklist"][op.param2] = True
		    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
		else:
		    cl.sendText(op.param1,"")
	    else:
		cl.sendText(op.param1,"")
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
		elif wait["inviteprotect"] == True:
		    wait ["blacklist"][op.param2] = True
		    cl.cancelGroupInvitation(op.param1,[op.param3])
		else:
		    cl.sendText(op.param1,"")
	    else:
		cl.sendText(op.param1,"")
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
		elif wait["cancelprotect"] == True:
		    wait ["blacklist"][op.param2] = True
		    cl.cancelGroupInvitation(op.param1,[op.param3])
		else:
		    cl.sendText(op.param1,"")
	    else:
		cl.sendText(op.param1,"")
	if op.type == 11:
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
		elif wait["linkprotect"] == True:
		    wait ["blacklist"][op.param2] = True
		    G = ki.getGroup(op.param1)
		    G.preventJoinByTicket = True
		    ki.updateGroup(G)
		    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
		else:
		    cl.sendText(op.param1,"")
	    else:
		cl.sendText(op.param1,"")
        if op.type == 5:
            if wait["autoAdd"] == True:
                if (wait["message"] in [""," ","\n",None]):
                    pass
                else:
                    cl.sendText(op.param1,str(wait["message"]))
                    
#------Open QR Kick start------#
        if op.type == 11:
            if wait["linkprotect"] == True:
                if op.param2 not in Bots:
                    G = random.choice(KAC).getGroup(op.param1)
                    G.preventJoinByTicket = True
                    random.choice(KAC).kickoutFromGroup(op.param1,[op.param3])
                    random.choice(KAC).updateGroup(G)
        #------Open QR Kick finish-----#
#------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------
        if op.type == 55:
            print "[NOTIFIED_READ_MESSAGE]"
            try:
                if op.param1 in wait2['readPoint']:
                    Nama = cl.getContact(op.param2).displayName
                    if Nama in wait2['readMember'][op.param1]:
                        pass
                    else:
                        wait2['readMember'][op.param1] += "\n|| " + Nama
                        wait2['ROM'][op.param1][op.param2] = "|| " + Nama
                        wait2['setTime'][msg.to] = datetime.strftime(now2,"%H:%M")
                else:
                    cl.sendText
            except:
                pass

        if op.type == 59:
            print op


    except Exception as error:
        print error


def a2():
    now2 = datetime.now()
    nowT = datetime.strftime(now2,"%M")
    if nowT[14:] in ["10","20","30","40","50","00"]:
        return False
    else:
        return True
def nameUpdate():
    while True:
        try:
        #while a2():
            #pass
            if wait["clock"] == True:
                now2 = datetime.now()
                nowT = datetime.strftime(now2,"(%H:%M)")
                profile = cl.getProfile()
                profile.displayName = wait["cName"] + nowT
                cl.updateProfile(profile)
            time.sleep(600)
        except:
            pass
thread2 = threading.Thread(target=nameUpdate)
thread2.daemon = True
thread2.start()

def autolike():
    count = 1
    while True:
        try:
           for posts in cl.activity(1)["result"]["posts"]:
             if posts["postInfo"]["liked"] is False:
                if wait["likeOn"] == True:
                   cl.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   ki.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   ki2.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   ki3.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   ki4.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   ki5.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   ki6.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   ki7.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   ki8.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   ki9.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   k1.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   k2.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   k3.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   k4.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   k5.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   k6.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   k7.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   k8.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   k9.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   w1.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   w2.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   print "Like"
                   if wait["commentOn"] == True:
                      if posts["userInfo"]["writerMid"] in wait["commentBlack"]:
                         pass
                      else:
                          cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"])
                          ki.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"])
                          ki2.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"])
                          ki3.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"])
                          ki4.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"])
                          ki5.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"])
                          ki6.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"])
                          ki7.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"])
                          ki8.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"])
                          ki9.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"])
                          k1.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"])
                          k2.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"])
                          k3.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"])
                          k4.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"])
                          k5.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"])
                          k6.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"])
                          k7.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"])
                          k8.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"])
                          k9.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"])
                          w1.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"])
                          w2.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"])
        except:
            count += 1
            if(count == 50):
                sys.exit(0)
            else:
                pass
thread2 = threading.Thread(target=autolike)
thread2.daemon = True
thread2.start()

#def autolike():
#     for zx in range(0,50):
#        hasil = cl.activity(limit=1000)
#        if hasil['result']['posts'][zx]['postInfo']['liked'] == False:
#          try:    
#            ki.like(hasil['result']['posts'][z")
#            ki2.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
#            ki2.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like by MuhMursalinD\n\nHttp://line.me/ti/p/~muhmursalind")
#            ki3.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
#            ki3.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like by MuhMursalinD\n\nHttp://line.me/ti/p/~muhmursalind")
#            ki4.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
#            ki4.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like by MuhMursalinD\n\nHttp://line.me/ti/p/~muhmursalind")
#            ki5.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
#            ki5.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like by MuhMursalinD\n\nHttp://line.me/ti/p/~muhmursalind")
#            ki6.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
#            ki6.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like by MuhMursalinD\n\nHttp://line.me/ti/p/~muhmursalind")
#            print "Like"
#            print "Like"
#            print "Like"
#          except:
#            pass
#        else:
#            print "Already Liked"
#     time.sleep(600)
#thread2 = threading.Thread(target=autolike)
#thread2.daemon = True
#thread2.start()

while True:
    try:
        Ops = cl.fetchOps(cl.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(cl.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            cl.Poll.rev = max(cl.Poll.rev, Op.revision)
            bot(Op)
