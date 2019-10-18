Dead_Ringers_kywords = ['twins','medical','psychological','erotic','thriller','voyeur', 'gynecologist']
Double_Lovers_kywords = ['thriller','gynecologist',"twins","erotica",'pregnancy','voyeur']
for Dead_Ringers_kywords in Double_Lovers_kywords:
    T = 'thriller'
    E = 'eroti%'
    P = 'pregnancy'
    V = 'voyeur'
    M = 'medical'
    TW = 'twins'
    G = 'gynecologist'
    for E in Double_Lovers_kywords:
        print('This title is a match for keyword: EROTIC or EROTICA')
        break
    for TW in Double_Lovers_kywords:
        print('This title is a match for keyword: TWINS')
        break
