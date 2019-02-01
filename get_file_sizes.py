print("File sizes:")
for f in os.listdir('../input/'):
    if not os.path.isdir('../input/'+f):
        print(f.ljust(30) + str(round(os.path.getsize('../input/'+f)/1000000,2))+' MB')
    else:
        sizes = [os.path.getsize('../input/'+f+'/'+x)/1000000 for x in os.listdir('../input/'+f)]
        print(f.ljust(30)+str(round(sum(sizes),2))+'MB'+ '({} files)'.format(len(sizes)))