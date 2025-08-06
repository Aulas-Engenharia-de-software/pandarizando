import pandas as pd
import numpy as np

print("Iniciando a geração do dataset simulado de episódios...")

animes_info = {
    'Naruto Clássico': {'total_episodios': 220, 'perc_filler': 0.41},
    'Naruto Shippuden': {'total_episodios': 500, 'perc_filler': 0.40},
    'One Piece': {'total_episodios': 1112, 'perc_filler': 0.10},
    'Dragon Ball Z': {'total_episodios': 291, 'perc_filler': 0.13}
}

nota_media_canon = 7.9
desvio_padrao_canon = 0.8

nota_media_filler = 6.2
desvio_padrao_filler = 1.0

lista_episodios = []

for anime, info in animes_info.items():
    num_fillers = int(info['total_episodios'] * info['perc_filler'])
    num_canonicos = info['total_episodios'] - num_fillers

    tipos_episodio = ['Canônico'] * num_canonicos + ['Filler'] * num_fillers
    np.random.shuffle(tipos_episodio)

    for i in range(info['total_episodios']):
        ep_num = i + 1
        ep_tipo = tipos_episodio[i]

        if ep_tipo == 'Canônico':
            nota = np.random.normal(loc=nota_media_canon, scale=desvio_padrao_canon)
        else:
            nota = np.random.normal(loc=nota_media_filler, scale=desvio_padrao_filler)

        nota_final = round(np.clip(nota, 1.0, 10.0), 1)

        lista_episodios.append({
            'anime': anime,
            'numero_episodio': ep_num,
            'tipo_episodio': ep_tipo,
            'nota_simulada': nota_final
        })

df_animes = pd.DataFrame(lista_episodios)
df_animes.to_csv('episodios_animes.csv', index=False, sep=';', encoding='utf-8-sig')

print(f"Arquivo 'episodios_animes.csv' criado com sucesso com {len(df_animes)} registros!")