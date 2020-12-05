class students:
    def __init__(self,uin,first,colg_id):
        self.uin=uin
        self.first=first
        self.colg_id=colg_id

class  rooms:
    def __init__(self,room_id,room_name,colg_id):
        self.room_id=room_id
        self.room_name=room_name
        self.colg_id=colg_id

class teachers:
    def __init__(self,teacher_id,teacher_first,branch,max_duty,colg_id):
        self.teacher_id=teacher_id
        self.teacher_first=teacher_first
        self.branch=branch
        self.max_duty=max_duty
        self.colg_id=colg_id
class datesheet:
    def __init__(self,date,session,room_no):
        self.date=date
        self.session=session
        self.room_no=room_no

        


