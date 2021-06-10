import ole

context = './hwp_data/'
fname = 'koreatest1'

with ole.open(f'{context+fname}.hwp') as f:
    print(f.list_streams())
    print('=' * 40)
    print(f.get_stream('PrvText').read().decode('utf-16le'))
