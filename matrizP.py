	 
# estados intermedios
estadosI = [x for x in range(0,24)]

# estados finales aprobados
estadosFA = [x for x in range(100,138)] #0:100-36:136

# estados finales error
estadosFE = [x for x in range(200,205)]

#estados finales con asterisco
estadosFCA=[i for i in estadosFA[:3]]+[119,115,117,108,106,107,110]

#estados finales
estadosF=estadosFA+estadosFE

#caracteres permitidos
digitos=[x for x in range(48,58)]
letras=[x for x in range(65,123) if not 90<x<97 and x!=110 and x!=116]
especiales=['|','&','!','/','"','\\','+','-','=','>','<','*','(',')',';',':','[',']',',','.','{','}','$','@','~','_',' ']
especiales=[ord(c) for c in especiales]

simbolos=[digitos,letras]
simbolos+=especiales+[ord('n'),ord('t')]

#matriz de estados finales
matrizEstadosF=[[estadosF[0]	,	"numero entero"								], #100:enteros
				[estadosF[1]	,	"numero decimales"							], #101:decimales
				[estadosF[2]	,	"identificador"  							], #102:identificadores
				[estadosF[3]	,	"||"			 							], #103:operador or
				[estadosF[4]	,	"&&"			 							], #104:operador and 	 
				[estadosF[5]	,	"!~"			 							], #105:negacion
				[estadosF[6]	,	"comentario de una linea"					], #106:comentario de una linea
				[estadosF[7]	,	"comentario multiple linea"					], #107:comentario multiple linea
				[estadosF[8]	,	chr(especiales[3])	   						], #108:signo division /
				[estadosF[9]	,	"texto"			   							], #109:texto
				[estadosF[10]	,	chr(especiales[4])	   						], #110:dobles comillas "
				[estadosF[11]	,	"salto de linea"   							], #111:salto de linea
				[estadosF[12]	,	"tabulador"		   							], #112:tabulador
				[estadosF[13]	,	"\\"	     	   							], #113:diagonal invertida
				[estadosF[14]	,	"++"			   							], #114:incremento
				[estadosF[15]	,	chr(especiales[6])	   						], #115:signo mas + 
				[estadosF[16]	,	"--"			   							], #116:decremento
				[estadosF[17]	,	chr(especiales[7])	   						], #117:signo menos -
				[estadosF[18]	,	"=="										], #118:doble igual
				[estadosF[19]	,	chr(especiales[8])							], #119:signo igual
				[estadosF[20]	,	chr(especiales[9])							], #120:signo mayor >
				[estadosF[21]	,	">="			   							], #121:signo mayor igual >=
				[estadosF[22]	,	chr(especiales[10])	  						], #122:signo menor <
				[estadosF[23]	,	"<="										], #123:signo menor igual <=
				[estadosF[24]	,	chr(especiales[11])  						], #124:multiplicacion
				[estadosF[25]	,	chr(especiales[12])							], #125:abre parentesis (
				[estadosF[26]	,	chr(especiales[13])							], #126:cierra parentesis )
				[estadosF[27]	,	chr(especiales[14])							], #127:punto y coma ;
				[estadosF[28]	,	chr(especiales[15])							], #128:dos puntos :
				[estadosF[29]	,	chr(especiales[16])							], #129:abre corchetes [
				[estadosF[30]	,	chr(especiales[17])							], #130:cierra corchetes ]
				[estadosF[31]	,	chr(especiales[18])							], #131:coma ,
				[estadosF[32]	,	chr(especiales[19])							], #132:punto .
				[estadosF[33]	,	chr(especiales[20])   						], #133:abre llaves {
				[estadosF[34]	,	chr(especiales[21]) 						], #134:cierra llaves }
				[estadosF[35]	,	chr(especiales[22])   						], #135:signo de pesos $
				[estadosF[36]	,	chr(especiales[23])							], #136:arroba @
				[estadosF[37]	,	chr(especiales[25])							], #137:guion bajo 				
				[estadosF[38]	,	"error en numero decimal"					], #200:error en numero decimal
				[estadosF[39]	,	"error en operador"							], #201:error en operador
				[estadosF[40]	,	"error en comentario de una linea"			], #202:error en comentario de una linea
				[estadosF[41]	,	"error en comentario multiple lineas"		], #203:error en comentario multiple lineas
				[estadosF[42]	,	"error en texto"							]] #204:erronr en texto


#PALABRAS RESERVADAS

resesrvadas=["if","for","While","Repeat","cases","to","down","begin","end","integer","real","string","case","main"]

#LECTURA Y RECORRIDO DE ARCHIVO



def createMatriz(fileMatriz):
	file=open(fileMatriz,'r')
	lineas=[l.split('\t') for l in file.read().split('\n')]
	file.close()
	return lineas

def getColumna(caracter):
	if caracter in digitos:
		return 0
	if caracter in letras:
		return 1
	return (simbolos.index(caracter) if caracter in simbolos else None)

def leerArchivo(nombre):
	lineas=[]
	f=open(nombre)
	for linea in f:
		lineas.append(repr(linea)[1:-1])
	f.close()
	return lineas

def recorrerLinea(linea):
	simbolos=[]
	for l in linea:
		simbolos.append(ord(l))
	return simbolos

def recorrerLineas(lineas):
	lineasR=[]
	for linea in lineas:
		chars=recorrerLinea(linea)
		lineasR.append(chars)
	return lineasR

def automata(cadena,estado):

	apuntador=0
	resultado=""
	identificador=""
	while (apuntador<len(cadena)):
		
		cod=cadena[apuntador]
		apuntador=apuntador+1
		value=str(cod).ljust(5)+chr(cod).ljust(5)
		print_info("[!]","Token:",value,5,8)

		columna=getColumna(cod)
		estado=int(matrizEstados[estado][columna])	
		# print_info("[!]","Estado:",estado,5,8)

		if estado in estadosF:
			idE=estadosF.index(estado)
			if estado in estadosFE:
				print_info('[E]',estado,matrizEstadosF[idE][1],5,8)
				return -1
			print_info('[+]',"Read:",matrizEstadosF[idE][1],5,8)
			if estado in estadosFCA:
				# print("{cod1 %s, col %i, estado %i, apuntador %i }"%(cod,columna,estado,apuntador))
				if estado == 102:
					print_info("[I]","Id:",identificador,5,8)
					if identificador in resesrvadas:
						print_info("[R]","Reservada:",identificador,5,8)						

				estado=0
				apuntador=apuntador-1
				identificador=""
			else:
				identificador=""
				estado=0
				resultado+=chr(cod)
		elif estado in estadosI:
			resultado+=chr(cod)
			if estado != 0:
				identificador+=chr(cod)
		else:
			print("Hay algun problema muchacho")
	print_info("[=]","Res:",resultado,5,8)
	return estado	

def compilador(archivo):
	i=0
	estado=0
	lineas=leerArchivo(archivo) #devuelve un arreglo de lineas
	lineasR=recorrerLineas(lineas) #devuelve un arreglo de arreglos de los simbolos en ascii
	while(i < len(lineasR) and estado!=-1):
		codes= ["[%s:%s]"%(lineasR[i][x],lineas[i][x]) for x in range(len(lineasR[i]))]
		# codes=[(lineasR[i][x],lineas[i][x]) for x in range(len(lineasR[i]))]
		print_info("\n[*]","Linea:",i+1,6,8)
		print_info("[!]","Texto:",lineas[i],5,8)
		print_info("[!]","Ascii:",codes,5,8)
		estado=automata(lineasR[i],estado)
		i=i+1


def print_info(type,context,value,a,b):
		info=str(type).ljust(a)
		info+=str(context).ljust(b)
		info+=str(value)
		print(info)

def print_matriz(mE,eI,mN):		
	print('%s:\n'%(mN))
	[print(str(eI[i]).ljust(3) ,mE[i]) for i in range(len(mE))]
	print("")

def print_all():
	print("estadosI:\t",estadosI,"\n")
	print("estadosFA:\t",estadosFA,"\n")
	print("estadosFE:\t",estadosFE,"\n")
	print("estadosFCA:\t",estadosFCA,"\n")
	print("estadosF:\t",estadosF,"\n")
	print("digitos:\t",digitos,"\n")
	print("letras:\t",letras,"\n")
	print("especiales:\t",especiales,"\n")
	print("simbolos:\t",simbolos,"\n")
	print_matriz([[str(i).rjust(3) for i in estado] for estado in matrizEstados ],estadosI,"MATRIZ ESTADOS")
	print_matriz([str(estado[1]).rjust(50) for estado in matrizEstadosF],estadosF,"ESTADOS FINALES")

#matriz de estados intermedios
matrizEstados=createMatriz("matriz.txt")
# print_all()

compilador("file.txt")
