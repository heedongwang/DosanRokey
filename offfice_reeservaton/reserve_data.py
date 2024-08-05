import csv

class reserveData:
    def __init__(self,room, user, start, end):
        self.room = room
        self.user = user
        self.start = start
        self.end = end
    
    #데이터를 딕셔너리로 변경해 반환합니다
    def todic(self):
        return {
            'room': self.room,
            'user': self.user,
            'start': self.start,
            'end': self.end
        }

#예약정보를 csv에서 불러옵니다
def load_Data():
    reservations=[]
    try:
        with open('reserve_list.csv','r',newline='',encoding='utf-8') as load:
            reader=csv.DictReader(load)
            for row in reader:
                reservations.append(reserveData(row['room'], row['user'], row['start'], row['end']))
                
    except FileNotFoundError:
        print("예약 파일을 찾을 수 없습니다.")
    return reservations 


#예약정보를 csv에 저장합니다
def save_Data(reservations):
    with open('reserve_list.csv','w',newline='',encoding='utf-8') as save:
        
        #컬럼명 선언
        fieldnames =['room','user','start','end'] 
        
        writer=csv.DictWriter(save,fieldnames=fieldnames)
        writer.writeheader()
        #reservations에 담겨있는 데이터를 딕셔너리 형식으로 변환하여 저장
        for res in reservations:
            writer.writerow(res.todic())