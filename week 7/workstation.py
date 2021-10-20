import itertools



class Car:
        def __init__(self, license, brand, color):
            # c = Car('AA1234', 'Honda',  'White')
            # มีตัวแปร reportเก็บประวัติ
            self.license = license
            self.brand = brand
            self.color = color
            self.report = []

        def __str__(self):
            #return string of car exemple 'AA1234 - White Honda'
                return f'{self.license} - {self.brand} {self.color}'

        def __lt__(self, rhs):
                #sort number of car by string
                return self.license > rhs.license
        
        def add_report(self, new_report):
                # เพิ่มประวัติซ่อมบำรุงโดยไม่ต้องคืนค่า
                # new_report เก็บ tuple ('Date','Discription','price')
                # exemple(('25 May 2017', 'change tires' , '1500'))
                # c1.add_report(('25 May 2017', 'change tires' , 1500))

                self.new_report = ()
                self.report.append(list(new_report))
                self.new_report = tuple(self.report)
                
                #print(self.report)
                
            
                

        def total_payment(self):
                # return all pass maintenance price

                total = 0
                for i in self.new_report:
                        total += i[2]
                return f'All pass maintenance price is {total}'
                

        def max_payment(self):
                #return all maintenance record (Date, discription, price) that have maximun price
                #in case there is no maintenance record return empty list.
                
                if len(self.new_report) != 0:
                        for i in range(len(self.new_report)):
                                print(self.new_report[i+1][2])
                                        
                                                



                pass

c1 = Car('AB1234', 'Honda',  'White')
c2 = Car('AA1234', 'Toyota', 'Black')

print(c1)
print(c2)

c1.add_report(('25 May 2017', 'change tires' , 1500))
c1.add_report(('25 May 2017', 'change Break' , 2000))

#print(c1.total_payment())
print(c1.max_payment())

