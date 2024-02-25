decleration_text = ("When in the Course of human events, it becomes necessary "
                    "for one people to dissolve the political bands which have "
                    "connected them with another, and to assume among the powers "
                    "of the earth, the separate and equal station to which the "
                    "Laws of Nature and of Nature's God entitle them, a decent "
                    "respect to the opinions of mankind requires that they should "
                    "declare the causes which impel them to the separation."
                    "We hold these truths to be self-evident, that all men are created equal,"
                    "that they are endowed by their Creator with certain unalienable rights," 
                    "that among these are life, liberty and the pursuit of happiness. That to secure" 
                    "these rights, governments are instituted among men, deriving their just" 
                    "powers from the consent of the governed. That whenever any form of" 
                    "government becomes destructive to these ends, it is the right of the people" 
                    "to alter or to abolish it, and to institute new government, laying its" 
                    "foundation on such principles and organizing its powers in such form, as to" 
                    "them shall seem most likely to effect their safety and happiness. Prudence," 
                    "indeed, will dictate that governments long established should not be changed" 
                    "for light and transient causes; and accordingly all experience hath shown" 
                    "that mankind are more disposed to suffer, while evils are sufferable, than" 
                    "to right themselves by abolishing the forms to which they are accustomed.")

ciphers = [4, 93, 52, 12, 41, 23, 9, 1, 34, 2, 11, 111, 6, 13, 24, 99, 100,
30, 10, 26, 16, 29, 155, 32, 37, 61, 15, 42, 3, 27, 70, 77,
45, 55, 43, 35, 108, 103, 56, 159, 166, 7, 8, 174, 36]

### where is the iterator?
def beale_code(text, ciphers):
    text = text.split()
    res = []
    for i in ciphers:
        res.append(list(text[i-1])[0])
    return ''.join(res)

massage = beale_code(decleration_text,ciphers)
print(massage)



