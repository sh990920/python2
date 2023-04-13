import csv
with open('차량관리.csv', 'w', newline='', encoding='UTF-8') as file:
    csv_maker = csv.writer(file, delimiter=',', quotechar='"')
    csv_maker.writerow([1, '08러1234', '2020-10-18.14:00'])
    csv_maker.writerow([2, '25다4567', '2020-10-21.14:50'])
    csv_maker.writerow([3, '28하8932', '2020-10-23.14:00'])
print('차량관리.csv 파일이 생성되었습니다.')