class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:

        res=[]
        line=[]
        linelength=0
        i=0

        while i< len(words):

            if((linelength+len(line)+len(words[i])) > maxWidth):

                extra_spaces=maxWidth-linelength
                spaces= extra_spaces//max(1,len(line)-1)
                reminder=extra_spaces%max(1,len(line)-1)

                for j in range(0, max(1,len(line)-1)):
                    line[j]+= " "*spaces
                    if reminder:
                        line[j]+= " "
                        reminder-=1
                res.append("".join(line))
                line=[]
                linelength=0

            line.append(words[i])
            linelength+=len(words[i])
            i+=1

        lastLine=" ".join(line)
        lastLine+=" "*max(0,maxWidth-len(lastLine))
        res.append(lastLine)

        return res



        