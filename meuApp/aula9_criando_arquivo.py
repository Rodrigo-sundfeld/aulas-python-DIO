arquivo = open('Primeiro arquivo com python.txt', 'w')
arquivo.write('Rodrigo Sundfeld')
arquivo.close()

arquivo = open('Primeiro arquivo com python.txt', 'a')
arquivo.write('\n123456')
arquivo.write('\nBarueri')
arquivo.close()

