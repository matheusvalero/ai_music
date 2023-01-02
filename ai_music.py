import random
from MIDIUtil import MIDIFile

notas = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
medidas = 4
time_sig = 4
musica = []

for _ in range(medidas):
    medida = []
    for _ in range(time_sig):
        medida.append(random.choice(notas))
    musica.append(medida)

midi = MIDIFile(1)

track = 0
tempo = 0

midi.addTrackName(track, tempo, "Música Aleatória")
midi.addTempo(track, tempo, 120)

canal = 0
volume = 100

for medida in musica:
    for note in medida:
        tom = notas.index(note) + 60
        duracao = 1
        midi.addNote(track, canal, tom, tempo, duracao, volume)
        tempo += 1

with open("random_music.mid", "wb") as output_file:
    midi.writeFile(output_file)