def filtraurls(index, query):
    
    def filllist(r, w):
        n = {}    
        for url in r:
            for p in  r[url]:
                if url in w and p + 1 in w[url]:
                    if url in n:
                        n[url].append(p + 1)
                    else:
                        n[url] = [p + 1]
        return n
        
    def isvalidurl(l, w):
        x = lookup(l, w)
        if w in ['', ' '] or x == None:
            return None
        return x
            
    _flag = True
    for w in query:
        fw = isvalidurl(index, w)
        if _flag:
            result = fw
            _flag = False
        else:
            result = filllist(result, fw)
                
    return result.keys()
    
    

def multi_lookup(index, query):
    return filtraurls(index, query)
