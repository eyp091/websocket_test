import socket
import time

def strat_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 5000))
    server_socket.listen(1)
    print("Sunucu başlatıldı. Bekleniyor...")

    client_socket, address = server_socket.accept()
    print(f"Bağlantı kuruldu: {address}")

    try: 
        while True:
            #istemcilye mesaj gönder
            message = "merhaba andorid\n"
            client_socket.sendall(message.encode("utf-8"))
            time.sleep(1)
    except:
        print("Bağlantı kesildi.")
    finally:
        client_socket.close()
        server_socket.close()

strat_server()

# from flask import Flask, request, jsonify
# from PIL import Image
# import io

# app = Flask(__name__)

# @app.route('/send-message', methods=['GET'])
# def send_message():
#     message = "hello android"
#     return jsonify({"status": "success", "message": message})

# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0', port=5000)