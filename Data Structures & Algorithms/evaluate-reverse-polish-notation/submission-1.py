class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        for i in range (len(tokens)):
            if tokens[i].lstrip("-").isdigit() == True :
                st.append(int(tokens[i]))
            else :
                if tokens[i] == "+" :
                    a = st.pop()
                    b = st.pop()
                    res = a + b 
                    st.append(res)
                if tokens[i] == "-" :
                    b = st.pop()
                    a = st.pop()
                    res = a - b 
                    st.append(res)
                if tokens[i] == "*" :
                    a = st.pop()
                    b = st.pop()
                    res = a * b 
                    st.append(res)
                if tokens[i] == "/" :
                    b = st.pop()
                    a = st.pop()
                    res = int(a / b) 
                    st.append(res)

        return st.pop()
                   
                    




        
        
