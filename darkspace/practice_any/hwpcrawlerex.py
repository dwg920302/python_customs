import olefile
from icecream import ic

context = './hwp_data/'
fname = 'koreatest1'

f = olefile.OleFileIO(f'{context+fname}.hwp')

ic(type(f))

ic(f.listdir())

# f.getproperties('PrvText') => dict

# encoded_text = f.openstream('PrvText').read().decode('UTF-16')

# ㅈ대따... BodyText들 전부 암호화 걸려있음;;

encoded2 = f.directory_fp

ic(encoded2)

it = f.getsect(0)

ic(type(it))

g = [f.getsect(i) for i in range(f.nb_sect)]  # 바이너리 데이터 (본문 아님) 인가? 아니면 본문인가?

ic(g)



# encoded_text = f.openstream(f'{context+fname}.hwp/BodyText/Section0').read().decode('UTF-16')

# PrvText(미리보기) 말고 본문을 가져와야 함. PrvText는 자꾸 6번에서 잘림.

# print('=' * 50)
# print(encoded_text)