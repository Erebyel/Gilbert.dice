import pandas as pd
import numpy as np

class Gilbert:

    frase = pd.DataFrame({'artículo': ['La', 'El', 'La', 'La', 'La', 'La', 'El', 'La', 'El', 'La', 'El', 'La', 'El', 'El', 'El', 'El', 'El', 'El', 'La', 'La'], 'sujeto': ['llave', 'polizón', 'hormiga', 'manta', 'casa solariega', 'gabardina', 'impermeable', 'promesa', 'judo', 'brújula', 'whisky', 'inyección', 'sueño', 'utensilio', 'marinero', 'fruto seco', 'bocadillo', 'tulipán', 'piedra', 'vaca'], 'adjetivo masculino': ['naciente', 'sensato', 'juvenil', 'notorio', 'criminal', 'glacial', 'liberal', 'silencioso', 'malicioso', 'coherente', 'pechugón', 'lluvioso', 'envenenado', 'amarillo', 'numeroso', 'geológico', 'caprichoso', 'añejo', 'roto', 'rojo'], 'adjetivo femenino': ['naciente', 'sensata', 'juvenil', 'notoria', 'criminal', 'glacial', 'liberal', 'silenciosa', 'maliciosa', 'coherente', 'pechugona', 'lluviosa', 'envenenada', 'amarilla', 'numerosa', 'geológica', 'caprichosa', 'añeja', 'rota', 'roja'], 'acciones': ['nace', 'se molesta', 'injuria a alguien', 'obtiene', 'contagia', 'gotea', 'jadea', 'se queja', 'llega', 'cercena', 'estudia', 'late', 've algo insólito', 'busca un final feliz', 'oficia', 'golpea', 'bucea', 'se despierta en otra época', 'se hiere', 'se hace derogar']})
    aleatorios = np.random.randint(len(frase['artículo']), size=3)
    retos = {'Retos': ['Este reto es un alivio, te permite la elipsis de 1 palabra que te haya salido como obligatoria para tu texto. Elige sabiamente', 'Qué paradójico sería que tu texto no tuviese una paradoja', 'Era como… la descripción que has hecho. Ex-ac-ta-men-te', 'No es dislexia, es un sinécdoque, ¡que no te enteras!', 'Don Quijote estaría orgulloso de tu aporte al noble arte de las historias de caballería', 'Seguro que, gracias a tu emotiva oda, el protagonista de tu historia será recordado eternamente', 'Este aire suena como una sinestesia, ¿no os parece?"', 'Tiene que parecer un ensayo, no serlo, porque de esto sé que no tienes ni idea', '¿Cuántas líneas tiene ese papel? Bueno, pues como mucho, puedes llenar 30 líneas', 'Alíviate o no te alivies, altérate o no te alteres, pero haz que tu texto sea aliterado']}
    def __init__(self, frase = frase, aleatorios = aleatorios, retos = retos):
        self.frase = frase
        self.aleatorios = aleatorios
        self.retos = retos

    def idea(self):
        '''Genera una frase aleatoria que podrás utilizar como la idea principal del relato.
        El programa no utiliza ninguna lógica ni coherencia para la selección de las columnas,
        por lo que puedes enfrentarte a ideas bastante incoherentes; lo que puede resultar en
        un ejercicio bastante estimulante para la imaginación'''
        if self.frase['artículo'][self.aleatorios[0]] == 'El':
            return ' '.join([self.frase['artículo'][self.aleatorios[0]], self.frase['sujeto'][self.aleatorios[0]], self.frase['adjetivo masculino'][self.aleatorios[1]], self.frase['acciones'][self.aleatorios[2]]])
        else:
            return ' '.join([self.frase['artículo'][self.aleatorios[0]], self.frase['sujeto'][self.aleatorios[0]], self.frase['adjetivo femenino'][self.aleatorios[1]], self.frase['acciones'][self.aleatorios[2]]])

    def palabras(self):
        '''Genera un listado de palabras aleatorio en base a adjetivos que debes utilizar en el
        desarrollo del texto; estas palabras pueden aparecer en todas sus variantes de género y número.'''
        palabras = []
        for n in range(int(np.random.randint(11, size=1))):
            palabras.append(self.frase['adjetivo masculino'][int(np.random.randint(len(self.frase['artículo']), size=1))])
        return palabras

    def reto(self):
        '''Lanza un reto aleatorio de los que existen dentro de la lista, para hacer más complicado
        (o facilitar a veces) la ejecución del relato.'''
        return self.retos['Retos'][int(np.random.randint(len(self.retos['Retos']), size=1))]

    def dice():
        '''¡Devuelve la respuesta que ha generado Gilbert!'''
        print('La idea del relato es:', Gilbert().idea())
        print('El texto debe contener:', Gilbert().palabras())
        print('El reto esta vez es:', Gilbert().reto())

Gilbert.dice()
