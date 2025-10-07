import random


def word_guess():
    word_list = ['kuća', 'knjiga', 'rijeka', 'grad', 'planina', 'more', 'automobil', 'škola', 'drvo', 'cvijet', 'zrakoplov',
     'telefon', 'ulica', 'mjesečina', 'sunce', 'dijamant', 'jednorog', 'tigar', 'igračka', 'kamera', 'balon', 'olovka',
      'sanke', 'kompjuter', 'ptica', 'kometa', 'kišobran', 'soba', 'kafa', 'riba', 'pas', 'čaj', 'lampa', 'stolica', 'jastuk',
       'televizor', 'sat', 'zvijezda', 'planeta', 'kamen', 'piće', 'ljeto', 'zima', 'proljeće', 'jesen', 'voda', 'mlijeko',
        'sir', 'hljeb', 'povrće', 'voće', 'čokolada', 'kolač', 'torta', 'baglama', 'klavir', 'harmonika', 'gitara', 'saksofon',
         'truba', 'bubanj', 'orkestar', 'džep', 'torba', 'jakna', 'majica', 'hlače', 'čarape', 'cipele', 'šal', 'kaput', 'kapa',
          'ruža', 'orhideja', 'ljubičica', 'maslina', 'kesten', 'orah', 'snijeg', 'ormar', 'led', 'vjetar', 'bura', 'duga',
           'oblaci', 'kiša', 'snješko', 'cijev', 'boja', 'crvena', 'plava', 'zelena', 'žuta', 'narandžasta', 'bijela', 'crna',
            'siva', 'smeđa', 'roza', 'ljubičasta', 'indigo', 'lubenica', 'jagoda', 'borovnica', 'grožđe', 'šljiva']

    word = random.choice(word_list)
    counter = 0
    answer = input(f"Ovo je riječ od {len(word)} slova, a prvo slovo je '{word[counter]}'. Šta misliš koja je riječ? > ").lower()

    while counter < 3:
        if answer != word and counter < 2:
            counter += 1
            answer = input(f"Ne, ne baš. Iduće slovo je '{word[counter]}'. Možeš li sada pogoditi? > ")
        elif answer != word and counter == 2:
            print(f"Ne, riječ je {word}. Više sreće drugi put!")
            restart = input("Želiš li ponovo pokušati? (d/n): ").lower()
            if restart == 'd':
                word_list.remove(word)
                word_guess()
            else:
                print("Zatvaram program...")
            break
        else:
            print("Tačno!")
            restart = input("Želiš li ponovo pokušati? (d/n): ").lower()
            if restart == 'd':
                word_list.remove(word)
                word_guess()
            else:
                print("Zatvaram program...")
            break


word_guess()
