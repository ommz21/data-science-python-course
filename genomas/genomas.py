entrada = open("genomas/bacteria.fasta").read()
saida = open("genomas/bacteria.html", "w")
#entrada = open("genomas/human.fasta").read()
#saida = open("genomas/human.html", "w")

cont = {}

for i in ['A', 'T', 'C', 'G']:
    for j in ['A', 'T', 'C', 'G']:
        cont[i+j] = 0

entrada = entrada.replace("\n", "")

for k in range(len(entrada) - 1):
    cont[entrada[k] + entrada[k + 1]] +=1

# html

maximo = max(cont.values())

i = 1
for k in cont:
    transparencia = cont[k] / maximo
    saida.write("<div style = 'width: 100px; border: 1px solid #111; color: #fff; height: 100px; float: left; background-color: rgba(0, 0, 0, "+ str(transparencia) +"')>"+k+"</div>")
    if i % 4 == 0:
        saida.write("<div style = 'clear:both'></div>")
    i += 1

saida.close()

# >R_024570.1 Escherichia coli strain U 5/41 16S ribosomal RA, partial sequence

# >M10098.1 Human 18S rRA gene, complete