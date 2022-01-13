with open('C:\\New folder\\demo.txt','w') as fh:
    for i in range(10):
        fh.write("this is line no %d\n" % (i+1))
