import olefile

context = './hwp_data/'
fname = 'koreatest1'

f = olefile.OleFileIO(f'{context+fname}.hwp')

print(f)

encoded_text = f.openstream('PrvText').read().decode('UTF-16')

# encoded_text = f.openstream(f'{context+fname}.hwp/BodyText/Section0').read().decode('UTF-16')

# PrvText(미리보기) 말고 본문을 가져와야 함. PrvText는 자꾸 6번에서 잘림.

print('=' * 50)
print(encoded_text)

encoded_text = f.openstream('FileHeader').read().decode('UTF-16')

print('=' * 50)
print(encoded_text)
