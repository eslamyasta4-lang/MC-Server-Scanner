import mcipc.query
from mcipc.query import Client

def check_server(ip, port=25565):
    print(f"🔍 Scanning: {ip}:{port}...")
    try:
        with Client(ip, port) as client:
            basic_stats = client.basic_stats
            print(f"✅ Server Online!")
            print(f"🎮 Version: {basic_stats.version}")
            print(f"👥 Players: {basic_stats.num_players}/{basic_stats.max_players}")
            print(f"📝 MOTD: {basic_stats.motd}")
    except Exception as e:
        print(f"❌ Error: Could not connect to server. (Check IP/Port)")

# جرب السيرفر اللي أنت عايزه هنا
target_ip = input("Enter MC Server IP: ")
check_server(target_ip)
