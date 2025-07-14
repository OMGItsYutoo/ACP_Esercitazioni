from flask_client.SensorThread import SensorThread

SERVER_BASE_URL="http://localhost:5000"

if __name__=="__main__":
    
    ths=[]
    for i in range(5):
        th=SensorThread(f"[SensorThread-{i+1}]", i+1, SERVER_BASE_URL)
        ths.append(th)
        th.start()
        
    for _ in range(5):
        th.join()
