from struct import unpack
import datetime
def day_to_csv():
    with open('sh999999.day','rb') as read_stream:
        with open('sh999999.csv','w+') as write_stream:
            while True:
                stock_date = read_stream.read(4)
                open_price = read_stream.read(4)
                high_price = read_stream.read(4)
                low_price = read_stream.read(4)
                close_price = read_stream.read(4)
                amount = read_stream.read(4)
                vol = read_stream.read(4)
                reservation = read_stream.read(4)
                if not stock_date:
                    break
                stock_date = unpack('l',stock_date)
                open_price = unpack('l',open_price)
                high_price = unpack('l',high_price)
                low_price = unpack('l',low_price)
                close_price = unpack('l',close_price)
                amount = unpack('f',amount)
                vol = unpack('l',vol)
                reservation = unpack('l',reservation)
                date_format = datetime.datetime.strptime(str(stock_date[0]),'%Y%M%d')
                data_list = date_format.strftime('%Y-%M-%d')+\
                                  ','+str(open_price[0]/100)+\
                                  ','+str(high_price[0]/100.0)+\
                                  ','+str(low_price[0]/100.0)+\
                                  ','+str(close_price[0]/100.0)+\
                                  ','+str(amount[0])+\
                                  ','+str(vol[0])+'\r'
                write_stream.writelines(data_list)


day_to_csv()