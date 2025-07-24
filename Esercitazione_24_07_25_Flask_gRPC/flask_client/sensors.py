from flask_client.SensorThread import SensorThread

N_TH=5
BASE_URL="http://localhost:5000"

if __name__=="__main__":
    
    
    th=[]
    for i in range(N_TH):
        t=SensorThread("SensorThread", i+1, BASE_URL)
        th.append(t)
        t.start()
        
    for t in th:
        t.join()