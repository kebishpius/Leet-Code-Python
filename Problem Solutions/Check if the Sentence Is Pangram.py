y= ['q', 'w', 'e' , 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f','g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm', ]
        for i in range(26):
            if sentence.find(y[i]) == -1:
                return False
        return True
