import pandas as pd

print("Iniciando a geração do arquivo expandido de derrotas...")

dados_derrotas_expandido = [
    # --- KURIRIN ---
    {'Personagem': 'Kuririn', 'Saga': '22º Torneio', 'Oponente': 'Jackie Chun', 'Tipo_de_Derrota': 'Nocaute', 'Origem_do_Golpe': 'Físico'},
    {'Personagem': 'Kuririn', 'Saga': 'Rei Piccolo', 'Oponente': 'Tambourine', 'Tipo_de_Derrota': 'Morte', 'Origem_do_Golpe': 'Físico'},
    {'Personagem': 'Kuririn', 'Saga': 'Freeza', 'Oponente': 'Freeza', 'Tipo_de_Derrota': 'Morte', 'Origem_do_Golpe': 'Energia (Ki)'},
    {'Personagem': 'Kuririn', 'Saga': 'Cell', 'Oponente': 'Androide 18', 'Tipo_de_Derrota': 'Nocaute', 'Origem_do_Golpe': 'Físico'},
    {'Personagem': 'Kuririn', 'Saga': 'Majin Buu', 'Oponente': 'Daburá', 'Tipo_de_Derrota': 'Neutralizado', 'Origem_do_Golpe': 'Habilidade Especial'},
    {'Personagem': 'Kuririn', 'Saga': 'Majin Buu', 'Oponente': 'Super Buu', 'Tipo_de_Derrota': 'Morte', 'Origem_do_Golpe': 'Habilidade Especial'},
    {'Personagem': 'Kuririn', 'Saga': 'Super', 'Oponente': 'Frost', 'Tipo_de_Derrota': 'Eliminação de Torneio', 'Origem_do_Golpe': 'Energia (Ki)'},

    # --- YAMCHA ---
    {'Personagem': 'Yamcha', 'Saga': '22º Torneio', 'Oponente': 'Tenshinhan', 'Tipo_de_Derrota': 'Nocaute', 'Origem_do_Golpe': 'Físico'},
    {'Personagem': 'Yamcha', 'Saga': 'Saiyan', 'Oponente': 'Saibaman', 'Tipo_de_Derrota': 'Morte', 'Origem_do_Golpe': 'Energia (Ki)'},
    {'Personagem': 'Yamcha', 'Saga': 'Cell', 'Oponente': 'Dr. Gero (Androide 20)', 'Tipo_de_Derrota': 'Neutralizado', 'Origem_do_Golpe': 'Físico'},
    {'Personagem': 'Yamcha', 'Saga': 'Cell', 'Oponente': 'Cell Jr.', 'Tipo_de_Derrota': 'Nocaute', 'Origem_do_Golpe': 'Físico'},
    {'Personagem': 'Yamcha', 'Saga': 'Majin Buu', 'Oponente': 'Super Buu', 'Tipo_de_Derrota': 'Morte', 'Origem_do_Golpe': 'Habilidade Especial'},
    {'Personagem': 'Yamcha', 'Saga': 'Super', 'Oponente': 'Champa', 'Tipo_de_Derrota': 'Nocaute', 'Origem_do_Golpe': 'Físico'},

    # --- TENSHINHAN ---
    {'Personagem': 'Tenshinhan', 'Saga': '22º Torneio', 'Oponente': 'Mestre Tsuru (trapaça)', 'Tipo_de_Derrota': 'Nocaute', 'Origem_do_Golpe': 'Habilidade Especial'},
    {'Personagem': 'Tenshinhan', 'Saga': 'Rei Piccolo', 'Oponente': 'Rei Piccolo', 'Tipo_de_Derrota': 'Nocaute', 'Origem_do_Golpe': 'Energia (Ki)'},
    {'Personagem': 'Tenshinhan', 'Saga': 'Saiyan', 'Oponente': 'Nappa', 'Tipo_de_Derrota': 'Morte', 'Origem_do_Golpe': 'Físico'},
    {'Personagem': 'Tenshinhan', 'Saga': 'Cell', 'Oponente': 'Semi-Perfect Cell', 'Tipo_de_Derrota': 'Nocaute (Exaustão)', 'Origem_do_Golpe': 'Energia (Ki)'},
    {'Personagem': 'Tenshinhan', 'Saga': 'Majin Buu', 'Oponente': 'Super Buu (Gotenks Abs.)', 'Tipo_de_Derrota': 'Nocaute', 'Origem_do_Golpe': 'Energia (Ki)'},

    # --- CHAOS ---
    {'Personagem': 'Chaos', 'Saga': '22º Torneio', 'Oponente': 'Kuririn', 'Tipo_de_Derrota': 'Eliminação de Torneio', 'Origem_do_Golpe': 'Físico'},
    {'Personagem': 'Chaos', 'Saga': 'Rei Piccolo', 'Oponente': 'Rei Piccolo', 'Tipo_de_Derrota': 'Morte', 'Origem_do_Golpe': 'Energia (Ki)'},
    {'Personagem': 'Chaos', 'Saga': 'Saiyan', 'Oponente': 'Nappa', 'Tipo_de_Derrota': 'Morte (Autodestruição)', 'Origem_do_Golpe': 'Energia (Ki)'},
]

df_derrotas_novo = pd.DataFrame(dados_derrotas_expandido)
df_derrotas_novo.to_csv('derrotas_guerreiros_z.csv', index=False, sep=';', encoding='utf-8-sig')

print("Arquivo 'derrotas_guerreiros_z.csv' criado com sucesso!")