"""
02. 「パトカー」＋「タクシー」＝「パタトクカシーー」
「パトカー」＋「タクシー」の文字を先頭から交互に連結して文字列「パタトクカシーー」を得よ．
"""

s1 = 'パトカー'
s2 = 'タクシー'
print(''.join(i + j for i, j in zip(s1, s2)))
