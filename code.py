# random presidential programs text generator

import random

output = open("random.txt", "w")

appealsfile = open("appeals.txt", "r")
introsfile = open("intros.txt", "r")
promintrosfile = open("promintros.txt", "r")
promsfile = open("proms.txt", "r")
endsfile = open("ends.txt", "r")

appealstext = appealsfile.read()
introstext = introsfile.read()
promintrostext = promintrosfile.read()
promstext = promsfile.read()
endstext = endsfile.read()

appeals = appealstext.split("\n")
intros = introstext.split("\n")
promintros = promintrostext.split("\n")
proms = promstext.split("\n")
ends = endstext.split("\n")

appeal = random.choice(appeals)
intro = " ".join(random.sample(set(intros), 5))
promintro = random.choice(promintros)
promises = "\n".join(random.sample(set(proms), 20))
ending = random.choice(ends)

text = "{ap}\n\n{intr}\n\n{promintr}\n\n{promises}\n\n{ending}".format(ap=appeal, intr=intro, promintr=promintro, promises=promises, ending=ending)

output.write(text)
output.close()